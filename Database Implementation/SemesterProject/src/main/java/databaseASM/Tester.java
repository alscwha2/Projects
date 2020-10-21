package databaseASM;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.Map;
import java.util.Scanner;

import edu.yu.cs.dataStructures.fall2016.SimpleSQLParser.ColumnDescription;
import edu.yu.cs.dataStructures.fall2016.SimpleSQLParser.ColumnID;
import edu.yu.cs.dataStructures.fall2016.SimpleSQLParser.ColumnValuePair;
import edu.yu.cs.dataStructures.fall2016.SimpleSQLParser.CreateTableQuery;
import edu.yu.cs.dataStructures.fall2016.SimpleSQLParser.InsertQuery;
import edu.yu.cs.dataStructures.fall2016.SimpleSQLParser.SQLParser;
import edu.yu.cs.dataStructures.fall2016.SimpleSQLParser.SQLQuery;
import edu.yu.cs.dataStructures.fall2016.SimpleSQLParser.SelectQuery;
import edu.yu.cs.dataStructures.fall2016.SimpleSQLParser.SelectQuery.FunctionInstance;
import net.sf.jsqlparser.JSQLParserException;

/*
 * IGNORE THIS CLASS! IGNORE THIS CLASS! IGNORE THIS CLASS! IGNORE THIS CLASS!
 * 
 * the purpose of this class is to see what the query objects look like for a 
 * given query input. My tests are in a main method in the database class
 */
public class Tester 
{
	public static void main(String[] args) throws FileNotFoundException, JSQLParserException
	{
		File inputFile = new File(System.getProperty("user.dir") + "\\input2.txt");
		SQLParser parser = new SQLParser();
		try (Scanner scanner = new Scanner(inputFile)) {
			while (scanner.hasNextLine()) {
				String line = scanner.nextLine();
				System.out.println("#" + line);
				SQLQuery q = parser.parse(line);
				if (q instanceof InsertQuery) System.out.println(Tester.getInsertString((InsertQuery)q));
				if (q instanceof SelectQuery) System.out.println(Tester.getSelectString((SelectQuery)q));
				if (q instanceof CreateTableQuery) System.out.println(Tester.getCreateTableString((CreateTableQuery)q));
			}
		}
	}
		
	public static String getSelectString(SelectQuery q)
	{
		String s = "";
		s += "CNs: ";
		for (ColumnID cid : q.getSelectedColumnNames()) {
			s += cid.getTableName() + ":" + cid.getColumnName() + ", ";
		}
		s += "\nTNs: ";
		for (String name : q.getFromTableNames()) {
			s += name + ", ";
		}
		s += "\nFNs: ";
		Map<ColumnID, FunctionInstance> map = q.getFunctionMap();
		for (java.util.Map.Entry<ColumnID, FunctionInstance> e : map.entrySet()) {
			s += e.getKey().getTableName() + ":" + e.getKey().getColumnName() + "->" + e.getValue().function.toString() + ", ";
		}
		s += "\n";
		return s;
	}
	
	public static String getInsertString(InsertQuery q)
	{
		String s = "";
		s += "TableName: " + q.getTableName() + "\n";
		s += "cvps:\n";
		for (ColumnValuePair cvp : q.getColumnValuePairs()) {
			s += cvp.getColumnID().getTableName() + "." + cvp.getColumnID().getColumnName() + "." + cvp.getValue() + "\n";
		}
		return s;
	}
	
	public static String getCreateTableString(CreateTableQuery q)
	{
		String s = "";
		s += "TableName: " + q.getTableName() + "\n";
		ColumnDescription pk = q.getPrimaryKeyColumn();
		s += "Primary Key Coumn: " + pk.getColumnName() + "." + pk.getColumnType() + "."
				+ "HasDefault:" + pk.getHasDefault() + ".DefaultValue:" + pk.getDefaultValue() + "." +  pk.getWholeNumberLength()
				+ "," + pk.getFractionLength() + "." + pk.getVarCharLength() + ".NotNull:" + pk.isNotNull() + ".isUnique:" +pk.isUnique() + "\n";
		for (ColumnDescription cd : q.getColumnDescriptions()) {
			s += cd.getColumnName() + "." + cd.getColumnType() + "."
					+ "HasDefault:" + cd.getHasDefault() + ".DefaultValue:" + cd.getDefaultValue() + "." +  cd.getWholeNumberLength()
					+ "," + cd.getFractionLength() + "." + cd.getVarCharLength() + ".NotNull:" + cd.isNotNull() + ".isUnique:" +cd.isUnique() + "\n";
		}
		return s;
	}
}
