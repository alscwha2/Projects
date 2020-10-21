package edu.yc.oats.algs;

import java.util.Queue;
import java.util.LinkedList;
import java.util.HashSet;

/*
 * Your assignment is to implement a Queue based topological sort (Sedgewick 4.2.39 on page 601).
 * You may use any JDK class such as java.util.{Set,Queue} etc.
 * You may use any Sedgewick code from the textbook.
 * You must implement the Digraph API from Sedgewick (page 569) as a class named Digraph.java, copying his code if you want.
 * You must implement the topological sort code in a class named TopologicalQ.java and provide the
 * following public API
 */
public class TopologicalQ
{
	Iterable<Integer> order;
	Digraph g;
	boolean hasOrder = false;
	
	/*Constructor, TopologicalQ(Digraph G) . 
	 *The constructor determines whether the digraph has a cycle or not. 
	 *If it does not have a cycle, the ctor determines a valid topological sort for the digraph.
	 */
	public TopologicalQ(Digraph G)
	{
		Digraph outDegreeMap = G;
		Digraph inDegreeMap = outDegreeMap.reverse();

		int v = outDegreeMap.V();
		int totalEdges = outDegreeMap.E();
		int seenEdges = 0;

		LinkedList<Integer> finalOrder = new LinkedList<Integer>();
		Queue<Integer> parentNodes = new LinkedList<Integer>();

		/*
		 * Add all of the roots. If there are no parent elements for a node add it to the queue
		 *
		 * I originally wanted to write:
		 *     for (int i = 0; i < v; i++) if (inDegreeMap.adj(i).isEmpty()) parentNodes.add(i);
		 * That would have been simpler. The problem is that adj() returns an Iterable, not a Collection
		 */
		for (int i = 0; i < v; i++) if (!inDegreeMap.adj(i).iterator().hasNext()) parentNodes.add(i);

		while (!parentNodes.isEmpty()) {
			Integer parent = parentNodes.poll();
			finalOrder.add(parent);
			
			childrenLoop:
			for (int child : outDegreeMap.adj(parent)) {
				seenEdges++;
				/*
				 * By the way, I originally wanted to write this as: 
				 *    if (finalOrder.containsAll(inDegreeMap(child))) parentNodes.add(child);
				 * That would have looked a lot simpler, and based on that it's easier to understand
				 *     what it is that I'm trying to do here. The problem is that the adj() returns 
				 *     an iterable, not a collection. That made my life harder in a few places.
				 */
				for (int myParent : inDegreeMap.adj(child)) if (!finalOrder.contains(myParent)) continue childrenLoop;
				parentNodes.add(child);
			}
		}		

		this.order = finalOrder;
		this.hasOrder = seenEdges == totalEdges ? true : false;
	}
	
	//return true iff G has a topological order, false otherwise
	public boolean hasOrder()
	{
		return this.hasOrder;
	}
	
	/*
	 *return an Iterator over the vertices in a valid topological sort. 
	 *The method returns null if no topological order exists.
	 */
	public Iterable<Integer> order()
	{
		return this.hasOrder ? this.order : null;
	}
}