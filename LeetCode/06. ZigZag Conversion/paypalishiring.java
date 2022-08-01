public class paypalishiring {
	public static void main(String[] args) {
		paypalishiring p = new paypalishiring();
		System.out.println(p.convert("PAYPALISHIRING", 3));
	}

	public String convert(String s, int numRows) {
	    //next one is 2r-2 away   
	    //which means that there will be n % 2r-2 in the first row
	        
	    //1 - find column
	    //2 - find upzag
	    //repeat until finished.

	    int columnSpacer = (2 * numRows - 2);

		String str = "";
		for(int rowNum = 0; rowNum < numRows; rowNum++) {
			int index = rowNum;
			int column = 1;
			while(index < s.length()) {
				str += s.charAt(index);
				int nextColumn = rowNum + column * columnSpacer;
				index = (index - rowNum) % columnSpacer == 0 && rowNum != numRows - 1 ? nextColumn - 2 * rowNum : nextColumn;
				if(index % nextColumn == 0) column++;
			}
		}

		return str;
	}
}