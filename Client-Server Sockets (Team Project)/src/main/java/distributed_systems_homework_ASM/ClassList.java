package distributed_systems_homework_ASM;

import java.util.ArrayList;
import java.util.List;
import java.util.Arrays;

public class ClassList
{
	public Class[] COM;
	public Class[] MAT;
	public Class[] BIO;

	public ClassList() 
	{
		
	}

	public String get(String code)
	{
		return codeToString(code);
	}

	public String add(String code, int crn, String title) throws IllegalArgumentException
	{
		ArrayList<Class> list = new ArrayList<Class>(Arrays.asList(this.COM));
		list.addAll(new ArrayList<Class>(Arrays.asList(this.MAT)));
		list.addAll(new ArrayList<Class>(Arrays.asList(this.BIO)));
		for (Class c : list) if (c.getCRN() == crn) return "FAILURE - CRN#" + crn + " already in use.";

		Class c = null;
		switch(code) {
			case "COM":
				c = new Class(crn, title);
				list = new ArrayList<Class>(Arrays.asList(this.COM));
				list.add(c);
				this.COM = list.toArray(new Class[this.COM.length + 1]);
				System.out.println(this.toString());
				return "SUCCESS";
			case "MAT":
				c = new Class(crn, title);
				list = new ArrayList<Class>(Arrays.asList(this.MAT));
				list.add(c);
				this.MAT = list.toArray(new Class[this.MAT.length + 1]);
				System.out.println(this.toString());
				return "SUCCESS";
			case "BIO":
				c = new Class(crn, title);
				list = new ArrayList<Class>(Arrays.asList(this.BIO));
				list.add(c);
				this.BIO = list.toArray(new Class[this.BIO.length + 1]);
				System.out.println(this.toString());
				return "SUCCESS";
			default: throw new IllegalArgumentException("Code received by the server is not COM MAT or BIO.");
		}
	}

	public String delete(int crn)
	{
		ArrayList<Class> list;
		list = new ArrayList<Class>(Arrays.asList(this.COM));
		for (Class c : list) if (c.getCRN() == crn) {
			list.remove(c);
			this.COM = list.toArray(new Class[this.COM.length - 1]);
			System.out.println(this.toString());
			return "SUCCESS";
		} 
		list = new ArrayList<Class>(Arrays.asList(this.MAT));
		for (Class c : list) if (c.getCRN() == crn) {
			list.remove(c);
			this.MAT = list.toArray(new Class[this.MAT.length - 1]);
			System.out.println(this.toString());
			return "SUCCESS";
		} 
		list = new ArrayList<Class>(Arrays.asList(this.BIO));
		for (Class c : list) if (c.getCRN() == crn) {
			list.remove(c);
			this.BIO = list.toArray(new Class[this.BIO.length - 1]);
			System.out.println(this.toString());
			return "SUCCESS";
		} 
		return "FAILURE - NO CLASS WITH CRN#" + crn;
	}

	public String toString()
	{
		return codeToString("COM") + codeToString("MAT") + codeToString("BIO");
	}

	private String codeToString(String code)
	{
		Class[] array = new Class[0];
		
		switch(code) {
			case "COM": array = this.COM; break;
			case "MAT":	array = this.MAT; break;
			case "BIO": array = this.BIO; break;
			default: throw new IllegalArgumentException("Error: Server GET request code was not COM MAT or BIO.");
		}

		String returnString = code + ":\n";
		for (Class c : array) returnString += "	" + c + "\n";
		return returnString;
	}
}