package databaseASM;
import edu.yu.cs.dataStructures.fall2016.SimpleSQLParser.*;
import edu.yu.cs.dataStructures.fall2016.SimpleSQLParser.SelectQuery.FunctionInstance;
import net.sf.jsqlparser.JSQLParserException;

import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileWriter;
import java.io.IOException;
import java.io.PrintWriter;
import java.sql.Timestamp;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashSet;
import java.util.LinkedList;
import java.util.Map;
import java.util.Scanner;

public class DataBase implements CanExecute
{
	private File querylog;
	private File lastbackup;
	private File createqueries;
	
	private int numRowsAffected = 0;
	
	private static Table success;
	
	public static void main(String[] args) throws JSQLParserException, IOException
	{
		//clear all of the logs to make fresh files with new input
		//	got the printwriter code from http://stackoverflow.com/questions/6994518/how-to-delete-the-content-of-text-file-without-deleting-itself
		
		
		//READ ME: The method wipeFiles is to make it easier to test input queries without having to worry about 
		//	making new names for my tables. This method deletes all of the data in the database. I have two text
		//	files that I use for queries. input.txt has all of my tests, including all of the create queries.
		//	After executing that you will have some tables already made, so if you want you can comment out 
		// 	the wipeFiles method and change the input file below to input2.txt. You can then put new queries 
		//	into there and work with the tables from the previous input file.
		
		
		DataBase.wipeFiles();
		DataBase db = new DataBase();
		
		File inputFile = new File(System.getProperty("user.dir") + "\\input.txt");
		try (Scanner scanner = new Scanner(inputFile)) {
			while (scanner.hasNextLine()) {
				try {
				String line = scanner.nextLine();
				System.out.println("#" + line);
				if (!line.startsWith("/")) System.out.println(db.execute(line));
				} catch(IllegalArgumentException e) {
					System.err.println(e.getMessage());
					if (e.getMessage().equals("TableName is null")) {
						throw e;
					}
				}
			}
		}
	}
	
	public DataBase() throws IOException, JSQLParserException
	{
		Table.setDB(this);
		//got the System.getProperty("user.dir") + "\\createqueries.txt" thing from stackexchange
		//	after fumbling around for a while trying to make a file in the current directory
		this.createqueries = new File(System.getProperty("user.dir") + "\\createqueries.txt");
		this.createqueries.createNewFile();
		this.querylog = new File(System.getProperty("user.dir") + "\\querylog.txt");
		this.querylog.createNewFile();
		this.lastbackup = new File(System.getProperty("user.dir") + "\\lastbackup.txt");
		this.lastbackup.createNewFile();
		
		this.initialize();
	}
	
	private void initialize() throws JSQLParserException, IOException
	{
		Scanner scanner = new Scanner(this.lastbackup);
		//if the file isn't empty. Assuming that it's either empty or has a valid structure
		if (scanner.hasNextLine()) {
			//get rid of the timestamp
			scanner.nextLine();
			//execute the queries
			SQLParser parser = new SQLParser();
			while(scanner.hasNextLine()) {
				String line = scanner.nextLine();
				if (line.equals("endQueries")) {
					break;
				}
				SQLQuery q = parser.parse(line);
				if (q instanceof CreateTableQuery) this.processCT((CreateTableQuery)q);
				if (q instanceof CreateIndexQuery) this.processCI((CreateIndexQuery)q);
			}
			//parse the tables
			while (scanner.hasNextLine()) {
				String line = scanner.nextLine();
				//just in case there are no tables
				if (line.equals("")) {
					break;
				}
				ArrayList<String> tablelines = new ArrayList<String>();
				tablelines.add(line);
				while (scanner.hasNextLine()) {
					line = scanner.nextLine();
					if (line.equals("endTable")) {
						break;
					}
					tablelines.add(line);
				}
				Table.parseTable(tablelines);
			}
			//done parsing the previous backup
			scanner.close();
			
			//execute the queries that happened since the backup
			scanner = new Scanner(this.querylog);
			String line = null;
			while (scanner.hasNextLine()) {
				line = scanner.nextLine();
				if (line.equals("")) {
					break;
				}
				//get rid of the timestamp
				line = line.split("->")[1];
				//don't do the create queries
				this.execute(line);
			}
		}
		scanner.close();
	}

	public Table execute(String sql) throws JSQLParserException, IOException
	{	
		SQLParser parser = new SQLParser();
		SQLQuery query = parser.parse(sql);
		Table returnTable = null;
		
		if (query instanceof CreateTableQuery) returnTable = this.processCT((CreateTableQuery)query);
		if (query instanceof CreateIndexQuery) returnTable = this.processCI((CreateIndexQuery)query);
		if (query instanceof InsertQuery) returnTable = this.processI((InsertQuery)query);
		if (query instanceof DeleteQuery) returnTable = this.processD((DeleteQuery)query);
		if (query instanceof UpdateQuery) returnTable = this.processU((UpdateQuery)query);
		if (query instanceof SelectQuery) returnTable = this.processS((SelectQuery)query);
		
		//add to query log
		if (!(query instanceof SelectQuery)) {
			try (FileWriter fr = new FileWriter(this.querylog, true)) {
				//got the following line from MyKong https://www.mkyong.com/java/how-to-get-current-timestamps-in-java/
				Timestamp timestamp = new Timestamp(System.currentTimeMillis());
				fr.write(timestamp.getTime() + "->" + query.toString() + "\n");
			}
		}
		//add CreateQueries to createquerylog
		if (query instanceof CreateIndexQuery || query instanceof CreateTableQuery) {
			try (FileWriter fr = new FileWriter(this.createqueries, true)) {
				fr.write(query.toString() + "\n");
			}
		}
		//deal with backing up
		if (this.numRowsAffected >= 5) {
			this.backUp();
			this.numRowsAffected = 0;

			try (PrintWriter writer = new PrintWriter(this.querylog)) {
				writer.print("");
			}
		}	
		return returnTable;
	}

	private Table processCT(CreateTableQuery query)
	{
		//check the primary key
		ColumnDescription primary = query.getPrimaryKeyColumn();
		if (primary == null) {
			throw new IllegalArgumentException("You must specify a primary key column");
		}
		if (primary.getHasDefault()) {
			throw new IllegalArgumentException("The primary key column may not be have a default value");
		}

		//check that the table has a name
		if (query.getTableName() == null) {
			throw new IllegalArgumentException("You must specify a name for the table");
		}

		//check for existing table with same name
		if (Table.getTable(query.getTableName()) != null) {
			throw new IllegalArgumentException("Table \"" + query.getTableName() + "\" already exists");
		}

		//check each column
		HashSet<String> columnNames = new HashSet<String>();
		ColumnDescription[] cds = query.getColumnDescriptions();
		for (ColumnDescription cd : cds) {
			String name = cd.getColumnName().toLowerCase().trim();
			//check for multiple columns with the same name
			//it seems that if you make two columns with the same name then the parser goes wacko anyway
			//so I think that this is irrelevant
			if (columnNames.contains(name)) {
				throw new IllegalArgumentException(cd.getColumnName() + ": Multiple columns may not have the same name");
			}
			columnNames.add(name);

			//check that the default value, if any, is valid
			if (cd.getHasDefault()) {
				String defaultValue = cd.getDefaultValue();
				switch(cd.getColumnType()) {
					case INT:
						try {
							Integer.parseInt(defaultValue);
						} catch(NumberFormatException e) {
							throw new IllegalArgumentException("Column " + name + ", Value " + defaultValue + ": default value must be an integer");
						}
						break;
					case DECIMAL:
						try {
							Double.parseDouble(cd.getDefaultValue());
						} catch (NumberFormatException e) {
							throw new IllegalArgumentException("Column " + name + ", Value " + defaultValue + ": default value must be a DECIMAL");
						}
						String[] numArray = defaultValue.split("\\.");
						if (numArray.length == 1) {
							if (defaultValue.length() > cd.getWholeNumberLength()) {
								throw new IllegalArgumentException("Column " + name + ", Value " + defaultValue + ": default value must be at most " +
									cd.getWholeNumberLength() + " digits long");
							}
						} else {
							if (numArray[0].length() > cd.getWholeNumberLength()) {
								throw new IllegalArgumentException("Column " + name + ", Value " + defaultValue + ": Only " + cd.getFractionLength()
									+ " digits are allowed to the right of the period");
							}
							if (numArray[1].length() > cd.getFractionLength()) {
								throw new IllegalArgumentException("Column " + name + ", Value " + defaultValue + ": Only " + cd.getFractionLength()
									+ " digits are allowed to the left of the period");
							}
						}
						break;
					case BOOLEAN:
						defaultValue = defaultValue.trim().toLowerCase();
						if (!(defaultValue.equals("'true'") || defaultValue.equals("'false'"))) {
							throw new IllegalArgumentException("Column " + name + ", Value " + defaultValue + ": Value must be either 'true' or 'false'");
						}
						break;
					case VARCHAR:
						if (defaultValue.length() - 2 > cd.getVarCharLength()) {
							throw new IllegalArgumentException("Column " + name + ", Value " + defaultValue + ": Value must be at most "
								+ cd.getVarCharLength() + " digits long");
						}
						break;
				}
			}
		}

		//when everything checks out, make the table
		return new Table(query);
	}

	private Table processCI(CreateIndexQuery query) throws IllegalArgumentException
	{
		String tableName = query.getTableName();
		if (tableName == null) {
			throw new IllegalArgumentException("You must specify a table");
		}

		Table table = Table.getTable(tableName);
		if (table == null) {
			throw new IllegalArgumentException("No such table exists");
		}

		String columnName = query.getColumnName();
		if (columnName == null) {
			throw new IllegalArgumentException("You much specify a column");
		}

		MyColumn column = Table.getColumn(new ColumnID(columnName, tableName));
		if (column == null) {
			throw new IllegalArgumentException("No such column exists on this table");
		}

		String indexName = query.getIndexName();
		if (indexName == null) {
			throw new IllegalArgumentException("You must specify a name for the index");
		}
		
		if (column.getIndex() != null) {
			throw new IllegalArgumentException(tableName + "." + columnName + " is already indexed");
		}
		new Index(query);
		return DataBase.success();
	}

	private Table processU(UpdateQuery query) throws IllegalArgumentException
	{
		if (query.getTableName() == null) {
			throw new IllegalArgumentException("You must specify a table");
		}
		if (Table.getTable(query.getTableName()) == null) {
			throw new IllegalArgumentException("No such table exists");
		}

		TableUtility.update(query);
		return DataBase.success();
	}

	private Table processS(SelectQuery query) throws IllegalArgumentException
	{
		//not sure why I put them into a list first, but I'm sure that it made sense at the time
		ColumnID[] cns = Arrays.asList(query.getSelectedColumnNames()).toArray(new ColumnID[0]);
		String[] tns = Arrays.asList(query.getFromTableNames()).toArray(new String[0]);
		Map<ColumnID,FunctionInstance> fmap = query.getFunctionMap();

		//make sure at least one column was included. All possibilities for select require at least one
		if (cns.length == 0) {
			throw new IllegalArgumentException("Must include at least one column name");
		}

		//if * is present it should be the only column
		if (cns.length > 1) {
			for (ColumnID cid : cns) {
				if (cid.equals(new ColumnID("*", null))) {
					throw new IllegalArgumentException("* must be the only column in the query.");
				}
			}
		}

		//every query needs to specify at least one table
		if (tns.length == 0) {
			throw new IllegalArgumentException("Must include at least one table name");
		}
		//no more than two tables are allowed
		if (tns.length > 2) {
			throw new IllegalArgumentException("No more than two tables are allowed for a join");
		}

		//check that every specified tables and columns exist
		for (ColumnID cid : cns) {
			if (cid.equals(new ColumnID("*", null))) {
				break;
			}
			
			String tableName = cid.getTableName();
			String columnName = cid.getColumnName();
			if (tableName == null) {
				if (tns.length == 1) {
					tableName = tns[0];
					cid = new ColumnID(columnName, tableName);
				}
				else {
					throw new IllegalArgumentException("You must specidy a table for column \"" + columnName + "\".");
				}
			}
			Table table = Table.getTable(tableName);
			if (table == null) {
				throw new IllegalArgumentException("Table \"" + tableName + "\" does not exist");
			}
			if (Table.getColumn(cid) == null) {
				throw new IllegalArgumentException("Column \"" + columnName + "\" does not exist on table \"" + tableName + "\"");
			}
		}
		
		//check that all of the from tables exist
		for (String tn : tns) {
			if (Table.getTable(tn) == null) {
				throw new IllegalArgumentException("Table \"" + tn + "\" does not exist");
			}
		}

		//execute the query
		if (fmap.size() > 0) return TableUtility.evalFunctions(query);//execute function(s)
		if (tns.length == 1) return TableUtility.select(query);//execute select
		if (tns.length == 2) return TableUtility.join(query);//execute join
		return null;
	}

	private Table processD(DeleteQuery query) throws IllegalArgumentException
	{
		if (query.getTableName() == null) {
			throw new IllegalArgumentException("You must specify a table");
		}
		if (Table.getTable(query.getTableName()) == null) {
			throw new IllegalArgumentException("No such table exists");
		}

		TableUtility.delete(query);
		return DataBase.success();
	}

	private Table processI(InsertQuery query) throws IllegalArgumentException
	{
		if (query.getTableName() == null) {
			throw new IllegalArgumentException("You must specify a table");
		}
		if (Table.getTable(query.getTableName()) == null) {
			throw new IllegalArgumentException("No such table exists");
		}
		for (ColumnValuePair cvp : query.getColumnValuePairs()) {
			ColumnID cid = cvp.getColumnID();
			if (Table.getColumn(cid) == null) {
				throw new IllegalArgumentException("Column \"" + cid.getColumnName() + "\" does not exist on table \"" + cid.getTableName() + "\".");
			}
		}

		TableUtility.insert(query);
		return DataBase.success();
	}
	
	private static Table success() throws IllegalArgumentException
	{
		if (DataBase.success != null) {
			return DataBase.success;
		}
		
		String[] rowArray = {"true"};
		LinkedList<String[]> rows = new LinkedList<String[]>();
		rows.add(rowArray);
		DataBase.success = new Table(new ArrayList<ColumnID>(), rows);
		
		return DataBase.success;
	}
	
	public void tick()
	{
		this.numRowsAffected++;
	}
	
	private void backUp() throws FileNotFoundException, IOException
	{
		//copy current content into new file and clear current file
		Scanner oldBackupScanner = new Scanner(this.lastbackup);
		Timestamp timestamp = new Timestamp(System.currentTimeMillis());
		//if oldBackupFile was empty, do nothing. If not, copy content to new file
		if (oldBackupScanner.hasNext()) {
			int number = 0;
			String filename = "Backup" + number + ".txt";
			File oldBackup = new File(System.getProperty("user.dir"), filename);
			while(!oldBackup.createNewFile()) {
				number++;
				filename = "Backup" + number + ".txt";
				oldBackup = new File(System.getProperty("user.dir"), filename);
			}
			
			FileWriter oldBackupWriter = new FileWriter(oldBackup);
			while(oldBackupScanner.hasNextLine()) {
				String line = oldBackupScanner.nextLine();
				oldBackupWriter.write(line + "\n");
			}
			oldBackupWriter.close();
		}
		oldBackupScanner.close();

		//clear old file and start writing new file
		FileWriter newBackupWriter = new FileWriter(this.lastbackup);
		//add timestamp first
		newBackupWriter.write(timestamp.getTime() + "\n");
		//then copy the querylogs
		Scanner createQueryReader = new Scanner(this.createqueries);
		while (createQueryReader.hasNextLine()) {
			String line = createQueryReader.nextLine();
			newBackupWriter.write(line + "\n");
		}
		createQueryReader.close();
		
		//for parsing purposes
		newBackupWriter.write("endQueries" + "\n");
		//add the content of the tables
		for (Table table : Table.getTableSet()) {
			newBackupWriter.write(table.toString() + "endTable" + "\n");
		}
		
		newBackupWriter.close();
	}
	
	public void wipe()
	{
		Table.wipe();
		Index.wipe();
	}
	
	private static void wipeFiles() throws FileNotFoundException
	{
		PrintWriter writer = new PrintWriter(System.getProperty("user.dir") + "\\createqueries.txt");
		writer.print("");
		writer.close();
		writer = new PrintWriter(System.getProperty("user.dir") + "\\querylog.txt");
		writer.print("");
		writer.close();
		writer = new PrintWriter(System.getProperty("user.dir") + "\\lastbackup.txt");
		writer.print("");
		writer.close();
	}
	
}