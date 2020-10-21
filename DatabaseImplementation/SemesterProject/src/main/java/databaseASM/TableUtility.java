package databaseASM;
import edu.yu.cs.dataStructures.fall2016.SimpleSQLParser.*;
import edu.yu.cs.dataStructures.fall2016.SimpleSQLParser.Condition.Operator;
import edu.yu.cs.dataStructures.fall2016.SimpleSQLParser.SelectQuery.FunctionInstance;

import java.util.LinkedList;
import java.util.Map;
import java.util.ArrayList;
import java.util.HashSet;

public class TableUtility
{
	public static void insert(InsertQuery query)
	{
		Table table = Table.getTable(query.getTableName());
		ColumnValuePair[] cvps = query.getColumnValuePairs();

		RowChecker.checkCompatability(cvps);
		RowChecker.checkCompleteness(table, cvps);

		table.insert(TableUtility.createRow(table, cvps));
	}

	public static void delete(DeleteQuery query)
	{
		LinkedList<String[]> rows;
		Table table = Table.getTable(query.getTableName());
		rows = RowFinder.getConditionalTable(table, query.getWhereCondition()).getRows();
		for (String[] row : rows) {
			table.delete(row);
		}
	}

	public static void update(UpdateQuery query)
	{
		ColumnValuePair[] cvps = query.getColumnValuePairs();
		Table table = Table.getTable(query.getTableName());

		RowChecker.checkCompatability(cvps);

		LinkedList<String[]> rows = RowFinder.getConditionalTable(table, query.getWhereCondition()).getRows();
		table.update(rows, cvps);
	}

	public static Table select(SelectQuery query)
	{
		//retrieve a subtable containing 
		//	all of the rows but only with values for the requested columns
		Table subTable;
		Table table = Table.getTable(query.getFromTableNames()[0]);
		subTable = table.getSubTable(TableUtility.getCompleteCIDs(query));
		subTable.setName(table.getName());
		subTable = RowFinder.getConditionalTable(subTable, query.getWhereCondition());
		subTable = RowFinder.getDistinctTable(subTable, query.isDistinct());
		subTable = RowFinder.getOrderedTable(subTable, query.getOrderBys());
		return subTable;
	}

	public static Table join(SelectQuery query)
	{
		String[] tableNames = query.getFromTableNames();
		Table[] tables = new Table[tableNames.length];
		for (int i = 0; i < tableNames.length; i++) {
			tables[i] = Table.getTable(tableNames[i]);
		}

		Table returnTable;
		//first get the cartesian product. The desired table is this table minus some rows and columns
		returnTable = RowFinder.getCartesianProduct(tables);
		//remove all of the rows that don't match the condition
		returnTable = RowFinder.getConditionalTable(returnTable, query.getWhereCondition());

		//make an array of the CIDs of the columns that we are returning. If there is an inner join
		//	then remove the extra CID
		ArrayList<ColumnID> cidList = returnTable.getCIDs();
		ArrayList<ColumnID> extras = TableUtility.getExtraJoinCIDs(query.getWhereCondition());
		cidList.removeAll(extras);

		//remove all of the columns that we don't need
		returnTable = returnTable.getSubTable(cidList);
		
		//edit the inner join CIDs to take away the table name;
		HashSet<String> colNames = new HashSet<String>();
		for (ColumnID cid : extras) {
			colNames.add(cid.getColumnName().toLowerCase());
		}
		for (int i = 0; i < cidList.size(); i++) {
			ColumnID cid = cidList.get(i);
			String name = cid.getColumnName().toLowerCase();
			if (colNames.contains(name)) {
				cid = new ColumnID(name, null);
				cidList.set(i, cid);
			}
		}
		//make a new table with the same rows but with the editted cids
		returnTable = new Table(cidList, returnTable.getRows());
		return returnTable;
	}

	public static Table evalFunctions(SelectQuery query)
	{
		Map<ColumnID, FunctionInstance> fMap = query.getFunctionMap();
		
		ArrayList<ColumnID> cids = new ArrayList<ColumnID>();
		LinkedList<String[]> rows = new LinkedList<String[]>();
		
		String[] valueArray = new String[fMap.size()];
		
		int i = 0;
		for (ColumnID cid : query.getSelectedColumnNames()) {
			FunctionInstance fi = fMap.get(cid);
			if (cid.getTableName() == null) cid = new ColumnID(cid.getColumnName(), query.getFromTableNames()[0]);
			
			String functionName = "";
			if (fi.isDistinct) functionName += "distinct_";
			functionName += fi.function.toString() + "_" + cid.getColumnName();
			
			cids.add(new ColumnID(functionName, cid.getTableName()));
			valueArray[i] = TableUtility.evalFunction(cid, fi);
			i++;
		}
		rows.add(valueArray);
		
		return new Table(cids, rows);
	}

	private static String evalFunction(ColumnID cid, FunctionInstance fi)
	{
		MyColumn column = Table.getColumn(cid);
		String value = null;
		boolean isDistinct = fi.isDistinct;
		
		switch(fi.function) {
		case AVG:
			try {value = "" + column.getAvg(isDistinct);}
			catch(UnsupportedOperationException e) {
				throw new IllegalArgumentException("You cannot ask for the average of a BOOLEAN or VARCHAR column");
			}
			break;
		case COUNT: value = "" + column.getCount(isDistinct);
			break;
		case MAX: value = column.getMax(isDistinct);
			break;
		case MIN: value = column.getMin(isDistinct);
			break;
		case SUM:
			try {value = "" + column.getSum(isDistinct);}
			catch (UnsupportedOperationException e) {
				throw new IllegalArgumentException("You cannot ask for the sum of a BOOLEAN or VARCHAR column");
			}
			break;
		}
		return value;
	}

	private static ArrayList<ColumnID> getExtraJoinCIDs(Condition where)
	{
		ArrayList<ColumnID> returnList = new ArrayList<ColumnID>();
		if (where == null) {
			return returnList;
		}
		Operator operator = where.getOperator();
		Object left = where.getLeftOperand();
		Object right = where.getRightOperand();
		if (operator == Operator.AND) {
			returnList = TableUtility.getExtraJoinCIDs((Condition)left);
			returnList.addAll(TableUtility.getExtraJoinCIDs((Condition)right));
		}
		if (operator == Operator.EQUALS) {
			if (left instanceof ColumnID && right instanceof ColumnID) {
				if(((ColumnID)left).getColumnName().toLowerCase().equals(((ColumnID)right).getColumnName().toLowerCase())) {
					returnList.add((ColumnID)right);
				}
			}
		}
		return returnList;
	}
	
	private static String[] createRow(Table table, ColumnValuePair[] cvps)
	{
		String[] newRow = new String[table.getCIDs().size()];
		for (ColumnValuePair cvp : cvps) {
			MyColumn column = Table.getColumn(cvp.getColumnID());
			int place = column.getPlace();
			newRow[place] = cvp.getValue();
		}

		//figure out which ColumnValuePairs we need to make
		ArrayList<ColumnID> cids = table.getCIDs();
		for (ColumnValuePair cvp : cvps) {
			cids.remove(cvp.getColumnID());
		}

		//make them by setting them to the default value if they exist. Leave null if no defualt
		for (ColumnID cid : cids) {
			MyColumn column = Table.getColumn(cid);
			ColumnDescription cd = Table.getDescription(cid);
			int place = column.getPlace();
			String value = null;

			if (cd.getHasDefault()) {
				value = cd.getDefaultValue();
			}
			
			newRow[place] = value;
		}
		return newRow;
	}
	
	private static ArrayList<ColumnID> getCompleteCIDs(SelectQuery query)
	{
		ArrayList<ColumnID> returnCIDArray = new ArrayList<ColumnID>();
		ColumnID[] queryArray = query.getSelectedColumnNames();
		
		String tableName = query.getFromTableNames()[0].toLowerCase();
		
		if (queryArray[0].equals(new ColumnID("*", null))) {
			return Table.getTable(tableName).getCIDs();
		}
		
		for (ColumnID cid : queryArray) {
			String tn = cid.getTableName();
			if (tn == null) tn = tableName;
			String cn = cid.getColumnName().trim().toLowerCase();
			
			returnCIDArray.add(new ColumnID(cn, tn));
		}
		return returnCIDArray;
	}
}