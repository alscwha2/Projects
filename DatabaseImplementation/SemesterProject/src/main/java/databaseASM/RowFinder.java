package databaseASM;
import edu.yu.cs.dataStructures.fall2016.SimpleSQLParser.*;
import edu.yu.cs.dataStructures.fall2016.SimpleSQLParser.ColumnDescription.DataType;
import edu.yu.cs.dataStructures.fall2016.SimpleSQLParser.Condition.Operator;
import edu.yu.cs.dataStructures.fall2016.SimpleSQLParser.SelectQuery.OrderBy;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.LinkedList;

import databaseASM.BTree.Entry;

import java.util.HashSet;

public class RowFinder
{
	public static Table getConditionalTable(Table table, Condition where)
	{
		LinkedList<String[]> rows = table.getRows();
		if (where == null) {
			return table;
		}

		//create data structure to be filled and returned
		LinkedList<String[]> returnRows = new LinkedList<String[]>();

		Operator operator = where.getOperator();
		switch(operator) {
			case AND:
			case OR:
				if(!(where.getLeftOperand() instanceof Condition && where.getRightOperand() instanceof Condition)) {
					throw new IllegalArgumentException("AND and OR operators only operate on two conditions");
				}
				Table left = getConditionalTable(table, (Condition)where.getLeftOperand());
				Table right = getConditionalTable(table, (Condition)where.getRightOperand());
				if (operator == Operator.OR) {
					HashSet<String[]> rowsSet = new HashSet<String[]>(left.getRows());
					for (String[] row : right.getRows()) {
						rowsSet.add(row);
					}
					returnRows = new LinkedList<String[]>(rowsSet);
				}
				if (operator == Operator.AND) {
					for (String[] lRow : left.getRows()) {
						boolean isDuplicate = false;
						for (String[] rRow : right.getRows()) {
							if (lRow == rRow) {
								isDuplicate = true;
								break;
							}
						}
						if (isDuplicate) {
							returnRows.add(lRow);
						}
					}
				}
				break;
			//i.e. if it's not AND or OR
			default:
				Object leftObject = where.getLeftOperand();
				Object rightObject = where.getRightOperand();
				if (leftObject instanceof ColumnID) {
					if (((ColumnID)leftObject).getTableName() == null) {
						leftObject = new ColumnID(((ColumnID)leftObject).getColumnName(), table.getName());
					}
				}
				if (rightObject instanceof ColumnID) {
					if (((ColumnID)rightObject).getTableName() == null) {
						rightObject = new ColumnID(((ColumnID)rightObject).getColumnName(), table.getName());
					}
				}
				RowFinder.checkWhereValidity(leftObject, rightObject, table);

				DataType type = null;
				if (leftObject instanceof ColumnID) {
					type = Table.getDescription((ColumnID)leftObject).getColumnType();
				}
				if (rightObject instanceof ColumnID) {
					type = Table.getDescription((ColumnID)rightObject).getColumnType();
				}
				
				//deal with index
				Index index = null;
				boolean leftIndex = true;
				if (leftObject instanceof ColumnID) {
					index = Index.getIndex((ColumnID)leftObject);
				}
				if (rightObject instanceof ColumnID && index == null) {
					index = Index.getIndex((ColumnID)rightObject);
					leftIndex = false;
				}
				//checking if no name because if no name then it's a join and joins use different
				// tables so the indices are useless unless I change the order in which I do joins.
				if (index != null && table.getName() != null) {
					return new Table(table.getCIDs(), RowFinder.getIndexedConditionalRows(leftObject, operator, rightObject, index, leftIndex, table, type));
				}

				//if there's no index, do it the hard way
				String lString = "";
				String rString = "";

				if (leftObject instanceof String) {
					lString = (String)leftObject;
				}
				if (rightObject instanceof String) {
					rString = (String)rightObject;
				}

				for(String[] row : rows) {
					if (leftObject instanceof ColumnID) {
						int place = table.getCIDs().indexOf((ColumnID)leftObject);
						lString = row[place];
						if (lString == null) {
							continue;
						}
					}
					if (rightObject instanceof ColumnID) {
						int place = table.getCIDs().indexOf((ColumnID)rightObject);
						rString = row[place];
						if (rString == null) {
							continue;
						}
					}
					if (RowFinder.isMatch(lString, rString, type, operator)) {
						returnRows.add(row);
					}
				}
				break;
		}
		return new Table(table.getCIDs(), returnRows);
	}

	private static void checkWhereValidity(Object left, Object right, Table table)
	{
		if (left instanceof Condition || right instanceof Condition) {
			throw new IllegalArgumentException("conditions cannnot be compared");
		}
		if (left instanceof String && right instanceof String) {
			throw new IllegalArgumentException("two strings cannot be compared as a WHERE condition");
		}
		
		if (left instanceof ColumnID) {
			if (Table.getColumn((ColumnID)left) == null) {
			throw new IllegalArgumentException("Column \"" + ((ColumnID)left).getColumnName() + "\" does not exist on table \"" + ((ColumnID)left).getTableName() +"\"");
			}
		}
		if (right instanceof ColumnID) {
			if (Table.getColumn((ColumnID)right) == null) {
			throw new IllegalArgumentException("Column \"" + ((ColumnID)right).getColumnName() + "\" does not exist on table \"" + ((ColumnID)right).getTableName() +"\"");
			}
		}
		if (left instanceof ColumnID && right instanceof ColumnID) {
			DataType lType = Table.getDescription((ColumnID)left).getColumnType();
			DataType rType = Table.getDescription((ColumnID)right).getColumnType();
			if (lType != rType) {
				throw new IllegalArgumentException("Different types may not be compared");
			}
			if (left.equals(right)) {
				throw new IllegalArgumentException("You cannot compare a column to itself");
			}
		} else {
			ColumnID cid = (left instanceof ColumnID) ? (ColumnID)left : (ColumnID)right;
			String string = (left instanceof String) ? (String)left : (String)right;
			string = string.trim().toLowerCase();
			switch(Table.getDescription(cid).getColumnType()) {
			case BOOLEAN:
				if (!string.equals("'true'") && !string.equals("'false'")) {
					throw new IllegalArgumentException("Column " + cid.toString() +", Value " + string + ": value must be a either 'true' or 'false'.");
				}
				break;
			case INT:
				try {
					Integer.parseInt(string);
				} catch (NumberFormatException e) {
					throw new IllegalArgumentException("Column " + cid.toString() +", Value " + string + ": value must be an INT");
				}
				break;
			case DECIMAL:
				try {
					Double.parseDouble(string);
				} catch (NumberFormatException e) {
					throw new IllegalArgumentException("Column " + cid.toString() +", Value " + string + ": value must be a DECIMAL");
				}
				break;
			case VARCHAR:
				if (!(string.startsWith("'") && (string.endsWith("'")))) {
					throw new IllegalArgumentException("String must be in format 'string'.");
				}
			}
		}
	}

	private static LinkedList<String[]> getIndexedConditionalRows(Object left, Operator operator, Object right, Index index, boolean leftIndex, Table table, DataType type)
	{
		LinkedList<String[]> rows = table.getRows();
		ArrayList<ColumnID> cids = table.getCIDs();
		
		LinkedList<String[]> returnList = new LinkedList<String[]>();
		
		Object nonIndexedObject = (leftIndex ? right : left);
		String nonIndexedValue = null;
		
		if (nonIndexedObject instanceof String) {
			nonIndexedValue = (String)nonIndexedObject;
			
			ArrayList<Entry> entries = index.getEntries();
			for (Entry e : entries) {
				boolean isMatch = false;
				if (leftIndex) {
					isMatch = RowFinder.isMatch((String)e.getKey(), nonIndexedValue, type, operator);
				}
				if (!leftIndex) {
					isMatch = RowFinder.isMatch(nonIndexedValue, (String)e.getKey(), type, operator);
				}
				if (isMatch) {
					@SuppressWarnings("unchecked")
					LinkedList<String[]> goodRows = (LinkedList<String[]>)e.getValue();
					for (String[] row : goodRows) {
						returnList.add(row);
					}
				}
			}
		}
		else if (nonIndexedObject instanceof ColumnID) {
			int place = cids.indexOf((ColumnID)nonIndexedObject);
			for (String[] row : rows) {
				String value2 = row[place];
				LinkedList<String[]> goodRows = null;
				if (leftIndex) {
					goodRows = RowFinder.getIndexedConditionalRows(left,  operator, value2, index, leftIndex, table, type);
				}
				if (!leftIndex) {
					goodRows = RowFinder.getIndexedConditionalRows(value2, operator, right, index, leftIndex, table, type);
				}
				for (String[] row2 : goodRows) {
					returnList.add(row2);
				}
			}
		}
		return returnList;
	}

	private static boolean isMatch(String lString, String rString, DataType type, Operator operator)
	{
		int compare;
		switch(type) {
			case BOOLEAN:
				lString = lString.substring(1, lString.length() - 1).toLowerCase();
				rString = rString.substring(1, rString.length() - 1).toLowerCase();
				//if one of them is null then the comparing won't work right
				if (lString.equals("null") || rString.equals("null")) {
					//if both of them are null then the comparing will work
					//if one is and one isn't then just return false
					if (!(lString.equals("null") && rString.equals("null"))) {
						return false;
					}
				}
				compare = (new Boolean(lString)).compareTo(new Boolean(rString));
				break;
			case INT:
				compare = (new Integer(lString)).compareTo(new Integer(rString));
				break;
			case DECIMAL:
				compare = (new Double(lString)).compareTo(new Double(rString));
				break;
			case VARCHAR:
				compare = lString.compareTo(rString);
				break;
			default:
				//this can't happen. for compiling purposes
				compare = 0;
		}

		switch(operator) {
			case EQUALS:
				if (compare == 0) {
					return true;
				}
				break;
			case NOT_EQUALS:
				if (compare != 0) {
					return true;
				}
				break;
			case LESS_THAN:
				if (compare < 0) {
						return true;
				}
				break;
			case lESS_THAN_OR_EQUALS:
				if (compare <= 0) {
						return true;
				}
				break;
			case GREATER_THAN:
				if (compare > 0) {
						return true;
				}
				break;
			case GREATER_THAN_OR_EQUALS:
				if (compare >= 0) {
						return true;
				}
				break;
			case AND:
			case OR:
				//this can't happen
				break;
		}
		return false;
	}

	public static Table getDistinctTable(Table table, boolean isDistinct)
	{
		LinkedList<String[]> rows = table.getRows();
		if (!isDistinct) {
			return table;
		}
		LinkedList<String[]> returnRows = new LinkedList<String[]>(rows);

		int numColumns = rows.getFirst().length;
		for (int i = 0; i < numColumns; i++) {
			HashSet<String> values = new HashSet<String>();
			for (String[] row : rows) {
				if (values.contains(row[i])) {
					returnRows.remove(row);
				}
			}
		}

		return new Table(table.getCIDs(), returnRows);
	}
	
	public static Table getOrderedTable(Table table, OrderBy[] orderbys)
	{
		if (orderbys.length == 0) {
			return table;
		}
		
		LinkedList<String[]> rows = table.getRows();
		rows = RowFinder.getOrderedRows(rows, orderbys);
		
		return new Table(table.getCIDs(), rows);
	}
	
	public static LinkedList<String[]> getOrderedRows(LinkedList<String[]> rows, OrderBy[] orderbys)
	{
		for (OrderBy ob : orderbys) {
			MyColumn column = Table.getColumn(ob.getColumnID());
			int place = column.getPlace();
			DataType type = column.getDescription().getColumnType();
			
			switch(type) {
			case INT:
			case DECIMAL:
			case BOOLEAN:
			case VARCHAR:
			default:
			}
		}
		return rows;
	}

	public static Table getCartesianProduct(Table[] tables)
	{
		LinkedList<String[]> returnRows = tables[0].getRows();
		ArrayList<ColumnID> newcids = tables[0].getCIDs();
		
		for (int i = 1; i < tables.length; i++) {
			LinkedList<String[]> rows1 = returnRows;
			LinkedList<String[]> rows2 = tables[i].getRows();
			if (rows1.size() == 0) {
				returnRows = rows2;
				continue;
			}
			int length1 = newcids.size();
			int length2 = tables[i].getCIDs().size();
			int length = length1 + length2;

			if (length1 == 0) {
				returnRows = rows2;
				continue;
			}
			if (length2 == 0) {
				returnRows = rows1;
				continue;
			}

			LinkedList<String[]> newRows = new LinkedList<String[]>();

			for (String[] row : rows1) {
				for (String[] row2: rows2) {
					String[] newRow = Arrays.copyOf(row, length);
					for (int j = 0; j < length2; j++) {
						newRow[length1 + j] = row2[j];
					}
					newRows.add(newRow);
				}
			}
			returnRows = newRows;
			newcids.addAll(tables[i].getCIDs());
		}
		return new Table(newcids, returnRows);
	}
}