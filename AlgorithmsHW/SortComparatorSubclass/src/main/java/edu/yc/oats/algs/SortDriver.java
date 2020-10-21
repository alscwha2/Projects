package edu.yc.oats.algs;

import java.util.Arrays;
import java.util.Comparator;

public class SortDriver
{
	 static public void sort(Item[] a)
	 {
		 Arrays.sort(a, new Comparator<Item>() {
		 	public int compare(Item i, Item j)
			{
				int returnValue = i.getDescription().compareTo(j.getDescription());
				if(returnValue == 0) {
					returnValue = Double.compare(i.getPrice(), j.getPrice());
					if (returnValue == 0) {
						if (i instanceof ColoredItem && j instanceof ColoredItem) {
							returnValue = ((ColoredItem)i).getColor().compareTo(((ColoredItem)j).getColor());
						}
					}
				}
				return returnValue;
			}
		 });
	 }

	 //	The result of invoking the sortByPrice() method, passing an Item[] is that the Array is sorted in
	 //ascending order on getPrice() .
	 static public void sortByPrice(Item[] a)
	 {
		 Arrays.sort(a, new Comparator<Item>() {
		 	public int compare(Item i, Item j)
		 	{
				double p1 = i.getPrice();
				double p2 = j.getPrice();
				if(p1 > p2) return 1;
				if(p1 < p2) return -1;
				return 0;
		 	}
		 });
	 }
}