package edu.yc.oats.algs;

import java.util.Random;
import java.util.Arrays;
import java.util.Iterator;
import java.util.NoSuchElementException;

public class IndexMinPQ<Key extends Comparable<Key>> implements Iterable<Integer>
{
	private int N;			// number of elements on PQ
	private int[] pq;		// binary heap using 1-based indexing
	private int[] qp;		// inverse: qp[pq[i]] = pq[qp[i]] = i
							//	I.E. THE PLACE THAT YOU COULD FIND THIS
							//		NUMBER KEY ON THE pq
	private Key[] keys;		// items with priorities

	public IndexMinPQ(int maxN)
	{
		keys = (Key[]) new Comparable[maxN + 1];
		pq   = new int[maxN + 1];
		qp   = new int[maxN + 1];
		for (int i = 0; i <= maxN; i++) qp[i] = -1;
	}

	public void insert(int i, Key key)
	{
		if (i < 0) throw new IllegalArgumentException("The index may not be negative.");
		if (keys[i] != null) throw new IllegalArgumentException("Index " + i + " has already been associated with a key.");
		if (key == null) throw new IllegalArgumentException("You may not insert \"null\".");
		
		N++;
		qp[i] = N;
		pq[N] = i;
		keys[i] = key;
		swim(N);
	}

	private void printInfo()
	{
		for (int i = 0; i < pq.length; i++) 
			System.out.print(i + ":" + pq[i] + " ");
		System.out.println();
		for (int i = 0; i < qp.length; i++) 
			System.out.print(i + ":" + qp[i] + " ");
		System.out.println();
		for (int i = 0; i < keys.length; i++) 
			System.out.print(i + ":" + keys[i] + " ");
		System.out.println();
	}

	public int delMin()
	{
		if (N == 0) throw new NoSuchElementException("The queue is empty.");

		int indexOfMin = pq[1];
		exch(1, N--);
		sink(1);
		keys[pq[N + 1]] = null;
		qp[pq[N + 1]] = -1;
		return indexOfMin;
	}

	private void swim(int  k)
	{
		while (k > 1 && greater(k/2, k)) {
			exch(k/2, k);
			k = k/2;
		}
	}

	private void sink(int k)
	{
		while (2*k <= N)
		{
			int j = 2*k;
			if (j < N && greater(j, j+1)) j++;
			if (!greater(k, j)) break;
			exch(k, j);
			k = j;
		}
	}

	private boolean greater(int i, int j)
	{ return keys[pq[i]].compareTo(keys[pq[j]]) > 0; }

	private void exch(int i, int j)
	{ 
		int k = pq[i]; 
		int l = pq[j];
		pq[i] = l; pq[j] = k;
		qp[k] = j; qp[l] = i;
	}

	public int size() 
	{ return N; }

	public boolean isEmpty()
	{ return N == 0; }

	public boolean contains(int i)
	{ return qp[i] != -1; }

	public Key minKey()
	{ return keys[pq[1]]; }

	public int minIndex()
	{
		if (N == 0) throw new NoSuchElementException("The queue is empty.");
		int minIn = -1;
		for (int i = 0; i < keys.length; i++) 
			{ if (keys[i] != null) { minIn = i; break; } }
		return minIn;
	}

	public Key keyOf(int i) 
	{ 
		Key k = keys[i];
		if (k == null) throw new NoSuchElementException("No key has been associated with index: " + i + ".");
		return k;
	}

	private IndexMinPQ getCopy()
	{
		IndexMinPQ<Key> copy = new IndexMinPQ<Key>(keys.length - 1);
		copy.keys = Arrays.copyOf(this.keys, this.keys.length);
		copy.pq = Arrays.copyOf(this.pq, this.pq.length);
		copy.qp = Arrays.copyOf(this.qp, this.qp.length);
		copy.N = this.N;
		return copy;
	}

	public Iterator<Integer> iterator()
	{
		return new IndexMinPQIterator(this.getCopy());
	}

	private class IndexMinPQIterator implements Iterator<Integer>
	{
		int[] array;
		int upTo = 0;
		int maxIndex;

		private IndexMinPQIterator(IndexMinPQ helper)
		{
			this.array = new int[keys.length];

			int i = 0;
			while (!helper.isEmpty()) this.array[i++] = helper.delMin();
			this.maxIndex = i;
		}
		public boolean hasNext()
		{ return upTo <= this.maxIndex; }

		public Integer next()
		{ return new Integer(this.array[upTo++]); }
	}

	private static IndexMinPQ construct(int N)
	{
		Random r = new Random();
		IndexMinPQ<Integer> q = new IndexMinPQ<Integer>(N);
		while(q.size() < N) {
			int i = r.nextInt(N);
			if (!q.contains(i)) {
				int k = r.nextInt(N);
				System.out.println("Inserting: index: " + i + ", key: " + k);
				q.insert(i, k);
			}
		}
	 	return q;
	}

	private void testEmpty()
	{	
		Iterator<Integer> it = this.iterator();
		while (this.size() != 0 && it.hasNext()) {
			System.out.println(
			"minIndex: " + this.minIndex() 
			+ ", it.Next: " + it.next()
			+ ", minKey: " + this.minKey()
			+ ", indexOfMin: " + pq[1] 
			+ ", keyOfIndexOfMin: " + keyOf(pq[1])
			+ ", delMin: " + this.delMin()
			+ ", isEmpty: " + this.isEmpty()
			+ ", size: " + this.size());
		}
	}

	public static void main(String[] args) throws Exception {
		IndexMinPQ q = construct(20);
		q.printInfo();
		q.testEmpty();
	}
}