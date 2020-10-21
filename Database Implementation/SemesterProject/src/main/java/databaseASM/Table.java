package databaseASM;
import edu.yu.cs.dataStructures.fall2016.SimpleSQLParser.*;
import edu.yu.cs.dataStructures.fall2016.SimpleSQLParser.ColumnDescription.DataType;

import java.util.LinkedList;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.HashSet;

public class Table
{
	private static HashMap<String, Table> tables = new HashMap<String, Table>();
	
	private String name;
	private HashMap<ColumnID, MyColumn> columns;
	private LinkedList<String[]> rows;
	private ArrayList<ColumnID> cidArray;
	
	private static DataBase db;
	
	//only used to keep track of how many lines were effected
	public static void setDB(DataBase db)
	{
		Table.db = db;
	}
	
	public static Table getTable(String name)
	{
		if (name == null) {
			throw new IllegalArgumentException("TableName is null");
		}
		return Table.tables.get(name.toLowerCase());
	}

	private static void putTable(String name, Table table)
	{
		Table.tables.put(name.toLowerCase(), table);
	}

	public static MyColumn getColumn(ColumnID cid)
	{
		String tableName = cid.getTableName();
		Table table = Table.getTable(tableName);
		if (table == null) {
			throw new IllegalArgumentException("Table \"" + tableName + "\" does not exist.");
		}
		return table.getColumnFromTable(cid);
	}

	public static ColumnDescription getDescription(ColumnID cid)
	{
		MyColumn column = Table.getColumn(cid);
		if (column == null) {
			return null;
		}
		return column.getDescription();
	}
	
	public static HashSet<Table> getTableSet()
	{
		return new HashSet<Table>(Table.tables.values());
	}

	public Table(CreateTableQuery query)
	{	
		ColumnDescription[] columnDescriptions = query.getColumnDescriptions();
		int numColumns = columnDescriptions.length;

		this.name = query.getTableName().toLowerCase();
		this.columns = new HashMap<ColumnID, MyColumn>();
		this.rows = new LinkedList<String[]>();
		this.cidArray = new ArrayList<ColumnID>();
		
		//Make MyColumn objects, make cidArray, store MyColumns in map
		for(int i = 0; i < numColumns; i++) {
			ColumnDescription cd = columnDescriptions[i];
			ColumnID cid = new ColumnID(cd.getColumnName().toLowerCase(), this.name.toLowerCase());
			MyColumn column = new MyColumn(cd, i);
			if (cd.equals(query.getPrimaryKeyColumn())) {
				column.setPrimaryKey();
			}
			this.columns.put(cid, column);
			this.cidArray.add(cid);
		}

		//so that we can find the table if we have its name
		Table.putTable(this.name, this);

		//create primary index
		new Index(new ColumnID(query.getPrimaryKeyColumn().getColumnName().toLowerCase(), this.name.toLowerCase()));
	}
	
	public Table(ArrayList<ColumnID> cids, LinkedList<String[]> rows)
	{
		this.columns = new HashMap<ColumnID, MyColumn>();
		this.cidArray = cids;
		this.rows = rows;
		
		//to solve an exception that I'm getting for join
		for (ColumnID cid : this.cidArray) if (cid.getTableName() == null) return;
		
		//set the columns
		for (int i = 0; i < this.cidArray.size(); i++) {
			ColumnID cid = this.cidArray.get(i);
			columns.put(cid, new MyColumn(Table.getDescription(cid), i));
		}
		for (String[] row : rows) {
			for (int i = 0; i < this.cidArray.size(); i++) {
				this.columns.get(this.cidArray.get(i)).addValue(row[i], row);
			}
		}
	}

	public String getName()
	{
		return this.name;
	}

	public MyColumn getColumnFromTable(ColumnID cid)
	{
		return this.columns.get(new ColumnID(cid.getColumnName().toLowerCase(), cid.getTableName().toLowerCase()));
	}

	public LinkedList<String[]> getRows()
	{
		return new LinkedList<String[]>(this.rows);
	}

	public ArrayList<ColumnID> getCIDs()
	{
		return new ArrayList<ColumnID>(this.cidArray);
	}

	public void insert(String[] row)
	{
		this.rows.add(row);

		for (int i = 0; i < this.cidArray.size(); i++) {
			MyColumn column = Table.getColumn(this.cidArray.get(i));
			if (column.getDescription().getColumnType() == DataType.BOOLEAN) {
				if (row[i] != null) row[i] = row[i].toLowerCase();
			}
			column.addValue(row[i], row);
		}
		
		Table.db.tick();
	}

	public void delete(String[] row)
	{
		this.rows.remove(row);
		
		for (int i = 0; i < this.cidArray.size(); i++) {
			MyColumn column = Table.getColumn(this.cidArray.get(i));
			column.removeValue(row[i], row);
		}
		
		Table.db.tick();
	}

	public void update(LinkedList<String[]> rows, ColumnValuePair[] cvps)
	{
		int[] indecies = new int[cvps.length];
		//iterate through new column ids
		for (int i = 0; i < cvps.length; i++) {
			//iterate through row column ids
			indecies[i] = this.cidArray.indexOf(cvps[i].getColumnID());
		}

		//iterate through the new cvps
		for (int i = 0; i < cvps.length; i++) {
			MyColumn column = Table.getColumn(cvps[i].getColumnID());
			//for each row:
			for (String[] row : rows) {
				String oldValue = row[indecies[i]];
				String newValue = cvps[i].getValue();
				if(column.getDescription().getColumnType() == DataType.BOOLEAN) newValue = newValue.toLowerCase();

				//update values stored in MyColumn object
				column.removeValue(oldValue, row);
				column.addValue(newValue, row);

				//update the values stored in the row;
				row[indecies[i]] = newValue;
			}
		}
		
		for (int i = 0; i < rows.size(); i++) {
			Table.db.tick();
		}
	}

	public Table getSubTable(ArrayList<ColumnID> cids)
	{
		if (cids.get(0).getColumnName().equals("*") || cids == this.cidArray) {
			return new Table(this.getCIDs(), this.getRows());
		}

		int[] indecies = new int[cids.size()];
		for (int i = 0; i < cids.size(); i++) {
			ColumnID cid = cids.get(i);
			if (cid.equals(new ColumnID("*", null))) {
				throw new IllegalArgumentException("*, if present, must be the only column name");
			}
			indecies[i] = this.cidArray.indexOf(cid);
		}

		LinkedList<String[]> subRows= new LinkedList<String[]>();
		for (String[] row : this.rows) {
			String[] subRow = new String[cids.size()];
			for (int i = 0; i < cids.size(); i++) {
				subRow[i] = row[indecies[i]];
			}
			subRows.add(subRow);
		}
		return new Table(cids, subRows);
	}
	
	public void setName(String name)
	{
		this.name = name;
	}
	
	public String toString()
	{
		String returnString = "";
		String rowString = "";
		for (ColumnID cid : this.getCIDs()) {
			rowString += cid.toString() + ", ";
		}
		returnString += rowString + "\n";
		
		for (String[] row : rows) {
			rowString = "";
			for (String value : row) {
				rowString += value + ", ";
			}
			returnString += rowString + "\n";
		}
		
		return returnString;
	}

	public static void parseTable(ArrayList<String> tablelines)
	{
		Table table = Table.getTable(tablelines.get(0).split("\\.")[0]);
		tablelines.remove(0);
		for (String rowstring : tablelines) {
			String[] row = rowstring.split(", ");
			row = Arrays.copyOf(row, row.length);
			table.insert(row);
		}
	}
	
	public static void wipe()
	{
		Table.tables.clear();
	}
}