package databaseASM;
import edu.yu.cs.dataStructures.fall2016.SimpleSQLParser.*;
import edu.yu.cs.dataStructures.fall2016.SimpleSQLParser.ColumnDescription.DataType;

import java.util.HashSet;
import java.util.LinkedList;

public class MyColumn
{
	private ColumnDescription columnDescription;
	private LinkedList<String> values;
	private int place;
	private Index index;
	private boolean isPrimaryKey = false;

	public MyColumn(ColumnDescription columnDescription, int i)
	{
		this.columnDescription = columnDescription;
		this.values = new LinkedList<String>();
		this.place = i;
	}

	public ColumnDescription getDescription()
	{
		return this.columnDescription;
	}
	
	public LinkedList<String> getValues()
	{
		return new LinkedList<String>(this.values);
	}

	public boolean containsValue(String value)
	{
		return this.values.contains(value);
	}

	public int getPlace()
	{
		return this.place;
	}

	public Index getIndex()
	{
		return this.index;
	}

	public void setIndex(Index index)
	{
		this.index = index;
	}

	public void addValue(String value, String[] row)
	{
		this.values.add(value);
		if (this.index != null) {
			this.index.update(value, row);
		}
	}

	public boolean removeValue(String value, String[] row)
	{
		if (this.index != null) {
			this.index.delete(value, row);
		}
		return this.values.remove(value);
	}
	
	public int getCount(boolean isDistinct)
	{
		int count = 0;
		if (isDistinct) {
			HashSet<String> set = new HashSet<String>(this.values);
			count = set.size();
			if (set.contains(null)) {
				count--;
			}
		} else {
			for (String value : values) {
				if (value != null) {
					count++;
				}
			}
		}
		return count;
	}
	
	public String getMax(boolean isDistinct)
	{
		if (this.values.size() == 0) {
			return null;
		}
		
		LinkedList<String> values = this.values;
		//I think that this logic here is uneless because isDistinct doesn't change anything when
		// it comes to max and min, but whatever. I'm not changing this now
		if (isDistinct) values = new LinkedList<String>(new HashSet<String>(this.values));
		
		DataType type = this.columnDescription.getColumnType();
		
		switch(type){
		case INT:
			int imax = Integer.parseInt(values.getFirst());
			for (String value : values) {
				int v = Integer.parseInt(value);
				if (v > imax) {
					imax = v;
				}
			}
			return "" + imax;
		case DECIMAL:
			double dmax = Double.parseDouble(values.getFirst());
			for (String value : values) {
				double v = Double.parseDouble(value);
				if (v > dmax) {
					dmax = v;
				}
			}
			return "" + dmax;
		case VARCHAR:
			String max = values.getFirst();
			for (String value : values) {
				if (value.compareTo(max) > 0) {
					max = value;
				}
			}
			return max;
		case BOOLEAN:
			for (String value : values) {
				if (value.equals("'true'")) {
					return value;
				}
			}
			return "'false'";
		}
		//to make the compiler happy
		return null;
	}
	
	public String getMin(boolean isDistinct)
	{
		if (this.values.size() == 0) {
			return null;
		}
		
		LinkedList<String> values = this.values;
		//I think that this logic here is uneless because isDistinct doesn't change anything when
		// it comes to max and min, but whatever. I'm not changing this now
		if(isDistinct) values = new LinkedList<String>(new HashSet<String>(this.getValues()));
		
		DataType type = this.columnDescription.getColumnType();
		
		switch(type){
		case INT:
			int imin = Integer.parseInt(values.getFirst());
			for (String value : values) {
				int v = Integer.parseInt(value);
				if (v < imin) {
					imin = v;
				}
			}
			return "" + imin;
		case DECIMAL:
			double dmin = Double.parseDouble(values.getFirst());
			for (String value : values) {
				double v = Double.parseDouble(value);
				if (v < dmin) {
					dmin = v;
				}
			}
			return "" + dmin;
		case VARCHAR:
			String min = values.getFirst();
			for (String value : values) {
				if (value.compareTo(min) < 0) {
					min = value;
				}
			}
			return min;
		case BOOLEAN:
			for (String value : values) {
				if (value.equals("'false'")) {
					return value;
				}
			}
			return "'true'";
		}
		//to make the compiler happy
		return "If you made it here then there's a problem";
	}
	
	public double getSum(boolean isDistinct)
	{
		DataType type = this.columnDescription.getColumnType();
		LinkedList<String> values = this.values;
		if(isDistinct) {
			values = new LinkedList<String>(new HashSet<String>(this.values));
		}
		
		switch(type) {
		case BOOLEAN:
		case VARCHAR:
			throw new UnsupportedOperationException();
		default:
			double sum = 0;
			for (String value : values) {
				sum += Double.parseDouble(value);
			}
			return sum;
		}
	}
	
	public double getAvg(boolean isDistinct)
	{
		double sum = this.getSum(isDistinct);
		if (sum == 0) return 0;
		return sum / ((double)this.getCount(isDistinct));
	}
	
	public boolean isPrimaryKey()
	{
		return this.isPrimaryKey;
	}
	
	public void setPrimaryKey()
	{
		this.isPrimaryKey = true;
	}
}