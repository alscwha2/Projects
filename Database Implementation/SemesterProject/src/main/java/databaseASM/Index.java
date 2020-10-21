package databaseASM;
import edu.yu.cs.dataStructures.fall2016.SimpleSQLParser.*;
import java.util.HashMap;
import java.util.LinkedList;

import databaseASM.BTree.Entry;

import java.util.ArrayList;

public class Index
{
	private static HashMap<ColumnID, Index> indexed = new HashMap<ColumnID, Index>();

	private BTree<String, LinkedList<String[]>> tree;

	public static Index getIndex(ColumnID cid)
	{
		return Index.indexed.get(new ColumnID(cid.getColumnName().toLowerCase(), cid.getTableName().toLowerCase()));
	}

	public Index(CreateIndexQuery query)
	{
		this(new ColumnID(query.getColumnName().toLowerCase(), query.getTableName().toLowerCase()));
	}

	public Index(ColumnID cid)
	{
		this.tree = new BTree<String, LinkedList<String[]>>();
		
		this.initiate(Table.getTable(cid.getTableName()), Table.getColumn(cid));
		Index.indexed.put(cid, this);
	}

	private void initiate(Table table, MyColumn column)
	{
		LinkedList<String[]> rows = table.getRows();
		int i = column.getPlace();
		for (String[] row : rows) {
			this.update(row[i], row);
		}
		column.setIndex(this);
	}

	public void update(String value, String[] row)
	{
		if (value == null) {
			return;
		}
		LinkedList<String[]> list = (LinkedList<String[]>)this.tree.get(value);
		if (list == null) {
			list = new LinkedList<String[]>();
			this.tree.put(value, list);
		}
		list.add(row);
	}

	public void delete(String value, String[] row)
	{
		if (value == null) {
			return;
		}
		LinkedList<String[]> list = (LinkedList<String[]>)this.tree.get(value);
		list.remove(row);
	}

	public ArrayList<Entry> getEntries()
	{
		return this.tree.getOrderedEntries();
	}
	
	public static void wipe()
	{
		Index.indexed.clear();
	}
}