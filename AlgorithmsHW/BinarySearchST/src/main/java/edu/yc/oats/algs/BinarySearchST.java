package edu.yc.oats.algs;

import java.util.concurrent.LinkedBlockingQueue;
import java.util.Random;
import java.util.Iterator;

public class BinarySearchST<Key extends Comparable<Key>, Value>
{
	private Key[] keys;
	private Value[] vals;
	private int N;
	static Random random = new Random();

	public BinarySearchST(int capacity)
	{
		keys = (Key[]) new Comparable[capacity];
		vals = (Value[]) new Object[capacity];
	}

	/** Initializes the ST with initial keys and corresponding values. The keys
	 * and values are inserted in array order: i.e., first (initialKeys[0],
	 * initialValues[0], then (initialKeys[1], initialValues[1])
	 * .... (initialKeys[n-1], initialValues[n-1])
	 */
	public BinarySearchST(Key[] initialKeys, Value[] initialValues)
	{
		if (initialKeys.length != initialValues.length) throw new IllegalArgumentException("Number of initial keys and values must be equal.");
		
		keys = (Key[]) new Comparable[initialKeys.length];
		vals = (Value[]) new Object[initialKeys.length];

		for (int i = 0; i < initialKeys.length; i++) this.put(initialKeys[i], initialValues[i]);
	} 

	public int size() { return N; }

	public boolean isEmpty() { return N == 0; }

	public Value get(Key key)
	{
		if (key == null) throw new IllegalArgumentException("You may not ask for the value of a null key.");

		if (isEmpty()) return null;
		int i = rank(key);
		if (i < N && keys[i].compareTo(key) == 0) return vals [i];
		else return null;
	}

	public int rank(Key key)
	{
		if (key == null) throw new IllegalArgumentException("You may not ask for the rank of a null key.");

		int lo = 0, hi = (N - 1);
		while (lo <= hi) {
			int mid = lo + ((hi - lo) / 2);
			int cmp = key.compareTo(keys[mid]);
			if      (cmp < 0) hi = mid - 1;
			else if (cmp > 0) lo = mid + 1;
			else return mid;
		}
		return lo;
	}

	public void put(Key key, Value val)
	{
		if (val == null) throw new IllegalArgumentException("You may not input a null value.");
		if (key == null) throw new IllegalArgumentException("You may not input a null key.");

		int i = rank(key);
		if (i < N && keys[i].compareTo(key) == 0) 
		{ vals[i] = val; return; }
		for (int j = N; j > i; j--) 
		{ keys[j] = keys[j-1]; vals[j] = vals[j-1]; }
		keys[i] = key; vals[i] = val;
		N++;
	}

	public void delete(Key key)
	{
		if (key == null) throw new IllegalArgumentException("You may not delete a null key.");

		int i = rank(key);
		if (i < N && keys[i].compareTo(key) == 0) {
			N--;
			for (int j = i; j < N; j++) { keys[j] = keys[j+1]; vals[j] = vals[j+1]; }
		}
	}

	public Key min() { return keys[0]; }

	public Key max() { return keys[N-1]; }

	public Key select(int k) { return keys[k]; } 

	public Key ceiling(Key key)
	{
		int i = rank(key);
		return keys[i];
	}

	public Key floor(Key key)
	{
		int lo = 0, hi = (N - 1);
		while (lo <= hi) {
			int mid = lo + ((hi - lo) / 2);
			int cmp = key.compareTo(keys[mid]);
			if      (cmp < 0) hi = mid - 1;
			else if (cmp > 0) lo = mid + 1;
			else return keys[mid];
		}
		if (hi < 0) return null;
		return keys[hi];
	}

	public Iterable<Key> keys()
	{
		return keys(keys[0], keys[N - 1]);
	}

	public Iterable<Key> keys(Key lo, Key hi)
	{
		if (lo == null || hi == null) throw new IllegalArgumentException("You cannot use null keys as bounds for key sublist.");
		LinkedBlockingQueue<Key> q = new LinkedBlockingQueue<Key>();
		try {
			for (int i = rank(lo); i < rank(hi); i++) q.put(keys[i]);
			if(contains(hi)) q.put(keys[rank(hi)]);
		} catch(InterruptedException e) {
			e.printStackTrace();
		}
		return q;
	}

	public boolean contains(Key key)
	{
		return this.get(key) != null;
	}

	/*
	 *************************************************
	 *************************************************
	 *FROM HERE UNTIL THE END IS JUST TESETING STUFF
	 *************************************************
	 *************************************************
	 */
	public void printKeys()
	{
		String returnString = "[";
		for(int i = 0; i < N; i++) returnString += keys[i] + ",";
		returnString += "]";
		System.out.println(returnString);
	}

	public String getKeyString()
	{
		String returnString = "[";
		for(int i = 0; i < N; i++) returnString += keys[i] + ",";
		returnString += "]";
		return returnString;	
	}


	public static void main(String[] args) {
		int n = Integer.parseInt(args[0]);
		BinarySearchST st = initialize(n);
		testFloorCeiling(st);
		testKeys(st);
		testKeysWithoutParameters(st);
		testDelete(st);
		testNewConstructor();
	}

	public static BinarySearchST initialize(int n)
	{
		BinarySearchST st = new BinarySearchST<Integer, Integer>(n * 2);
		for (int i = 0; i < n; i++) {
			st.put(new Integer(random.nextInt(n * 5)), new Integer(random.nextInt(n * 5)));
		}
		return st;
	}

	public static void testDelete(BinarySearchST st)
	{
		System.out.println("-----TESTING DELETE-----");

		st.printKeys();

		//delete each key one by one
		while (st.N > 0) {
			Comparable deletedKey = st.keys[random.nextInt(st.N)];
			st.delete(deletedKey);
			System.out.println(st.getKeyString() + " Deleted: " + deletedKey + ", ");
		}

		System.out.println();
	}

	public static void testFloorCeiling(BinarySearchST st)
	{
		System.out.println("-----TESTING FLOOR AND CEILING-----");

		int n = st.N;
		st.printKeys();

		//test with N random keys
		for (int i = 0; i < n; i++) {
			Integer key = new Integer(random.nextInt(n * 5));
			System.out.println("Key: " + key + "----> " + "floor: " + st.floor(key) + ", ceiling: " + st.ceiling(key));
		}

		//testing key that is smaller than any key stored in ST
		Integer key = new Integer(-1);
		System.out.println("Key: " + key + "----> " + "floor: " + st.floor(key) + ", ceiling: " + st.ceiling(key));
		
		//testing key that is larger than any key in ST
		key = new Integer(n * 20);
		System.out.println("Key: " + key + "----> " + "floor: " + st.floor(key) + ", ceiling: " + st.ceiling(key));

		System.out.println();
	}

	public static void testKeys(BinarySearchST st)
	{
		System.out.println("-----TESTING KEYS METHOD -----");
		for (int i = 0; i < 10; i++) {
			int a = random.nextInt(st.N * 5), b = random.nextInt(st.N * 5);
			int max = Math.max(a, b), min = Math.min(a, b);
			st.printKeys();
			System.out.print("min: " + min + ", max: " + max + " ------>");
			String returnString = "[";
			Iterator it = st.keys(new Integer(min), new Integer(max)).iterator();
			while(it.hasNext()) returnString += it.next() + ", ";
			System.out.println(returnString + "]");
		}
		System.out.println();
	}

	public static void testKeysWithoutParameters(BinarySearchST st)
	{
		System.out.println("-----TESTING KEYS METHOD WITH NO PARAMETERS-----");

		st.printKeys();

		String returnString = "[";
		Iterator it = st.keys().iterator();
		while (it.hasNext()) returnString += it.next() + ",";
		System.out.println(returnString + "]");

		System.out.println();
	}

	public static void testNewConstructor()
	{
		System.out.println("-----TESTING NEW CONSTRUCTOR-----");

		//test that the lengths of the input arrays are equal
		try {
			BinarySearchST bs = new BinarySearchST(new Comparable[1], new Comparable[2]);
			System.out.println("FAULURE - FAILED TO CHECK THAT THE KEY AND VALUE ARRAYS ARE OF THE SAME LENGTH");
		} catch(IllegalArgumentException e) {
			System.out.println("SUCCESSFULLY COMPARED LENGTH OF INPUT ARRAYS");
		}

		//test that nulls are not allowed
		try{
			BinarySearchST bs = new BinarySearchST(new Comparable[1], new Comparable[1]);
			System.out.println("FAULURE - FAILED TO CHECK THAT ALL OF THE KEYS AND VALUES ARE NOT NULL");
		} catch(IllegalArgumentException e) {
			System.out.println("SUCCESSFULLY CHECKED FOR NULL VALUES");
		}

		//test that it maintains order
		Comparable[] initialKeys = {new Integer(5), new Integer(3)};
		Comparable[] initialValues = {new Integer(7), new Integer(9)};
		BinarySearchST bs = new BinarySearchST(initialKeys, initialValues);
		if (bs.keys[0].compareTo(bs.keys[1]) > 0) System.out.println("FAILED TO INITIALIZE KEYS IN ORDER");
		else System.out.println("SUCCESSFULLY INITIALIZED KEYS IN ORDER");

		System.out.println();
	}
}