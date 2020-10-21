package databaseASM;
import edu.yu.cs.dataStructures.fall2016.SimpleSQLParser.*;
import edu.yu.cs.dataStructures.fall2016.SimpleSQLParser.ColumnDescription.DataType;

import java.util.ArrayList;
import java.util.HashSet;

public class RowChecker
{
	public static void checkCompatability(ColumnValuePair[] cvps)
	{
		RowChecker.checkForDuplicates(cvps);

		for (ColumnValuePair cvp : cvps) {
			MyColumn column = Table.getColumn(cvp.getColumnID());
			ColumnDescription cd = column.getDescription();
			DataType type = cd.getColumnType();
			String value;
			
			//deal with null
			if (cvp.getValue() == null) {
				//deal with not-null column
				if (column.isPrimaryKey() || cd.isNotNull()) {
					throw new IllegalArgumentException(cvp.getColumnID().toString() + " is not-null");
				}
				else {
					//set it to the default if there is one
					if (cd.getHasDefault()) {
						value = cd.getDefaultValue();
					}
					else {
						//if there's no default then the value remains as null
						//and my logic doesn't support null so just check for unique and 
						//if it passes, skip the rest of the logic and go onto the next cvp
						if ((cd.isUnique() || column.isPrimaryKey()) && column.containsValue(null)) {
							throw new IllegalArgumentException(null + " already exists on unique column " + cvp.getColumnID().getColumnName());
						}
						continue;
					}
				}
			}
			
			value = cvp.getValue().trim();

			//check type and lengths
			if (type == DataType.INT) {
				try {
					Integer.parseInt(value);
				} catch(NumberFormatException e) {
					throw new IllegalArgumentException("Value must be an intger");
				}
			}
			if (type == DataType.VARCHAR) {
				if (!(value.startsWith("'") && value.endsWith("'"))){
					throw new IllegalArgumentException("Strings must be in format 'string'.");
				}
				String value2 = value.substring(1, value.length() - 1);
				if (value2.length() > cd.getVarCharLength()) {
					throw new IllegalArgumentException("VARCHAR Value must be at most " + cd.getVarCharLength() + " characters long");
				}
			}
			if(type == DataType.DECIMAL) {
				try {
					Double.parseDouble(value);
				} catch(NumberFormatException e) {
					throw new IllegalArgumentException("Value must be a DECIMAL");
				}
				String[] parts = value.split("\\.");
				if (parts.length == 0) {
					value = value + ".0";
					parts = value.split(".");
				}
				if (parts[0].startsWith("-")) {
					parts[0] = parts[0].substring(1);
				}
				if (parts[0].length() > cd.getWholeNumberLength()) {
					throw new IllegalArgumentException("Whole number value must be at most " + cd.getWholeNumberLength() + " digits long");
				}
				if (parts.length > 1) {
					if(parts[1].length() > cd.getFractionLength()) {
					throw new IllegalArgumentException("At most " + cd.getFractionLength() + " digits are allowed left of the zero");
					}
				}
			}
			if(type == DataType.BOOLEAN) {
				value = value.toLowerCase();	
				if(!(value.equals("'true'") || value.equals("'false'"))) {
					throw new IllegalArgumentException("Value must be 'true' or 'false'");
				}
			}
			//check unique
			if(cd.isUnique() || column.isPrimaryKey()) {
				if (column.containsValue(value)) {
					throw new IllegalArgumentException("Value " + value + " already exists on unique column " + cvp.getColumnID().getColumnName());
				}
			}
		}
	}

	private static void checkForDuplicates(ColumnValuePair[] cvps)
	{
		HashSet<ColumnID> cids = new HashSet<ColumnID>();
		for (ColumnValuePair cvp : cvps) cids.add(cvp.getColumnID());
		if (cids.size() != cvps.length) {
			throw new IllegalArgumentException("Only one value may be specified per column");
		}
	}

	public static void checkCompleteness(Table table, ColumnValuePair[] cvps)
	{
		ArrayList<ColumnID> badcids = table.getCIDs();
		ArrayList<ColumnID> cids = new ArrayList<ColumnID>();
		for (ColumnID cid : badcids) {
			cids.add(new ColumnID(cid.getColumnName().toLowerCase(), cid.getTableName().toLowerCase()));
		}
		for (ColumnValuePair cvp : cvps) {
			ColumnID cid = cvp.getColumnID();
			cid = new ColumnID(cid.getColumnName().toLowerCase(), cid.getTableName().toLowerCase());
			if (!cids.remove(cid)) {
				throw new IllegalArgumentException("No column " + cid.getColumnName() + " in table " + table.getName());
			}
		}
		for(ColumnID cid : cids) {
			MyColumn column = Table.getColumn(cid);
			if (column.getDescription().isNotNull() || column.isPrimaryKey()) {
				throw new IllegalArgumentException("Value must be specified for not-null column " + cid.getColumnName());
			}
		}
	}
}