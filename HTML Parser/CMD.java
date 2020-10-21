import java.io.*;
import java.nio.*;
import java.util.regex.*;

//this is a test Command Line class that I used. The "main" and "parse" methods 
//were the ones that I mainly used. I don't remember what the rest of the methods
//did exactly or if they still work.

public class CMD
{
	public static void main(String[] args) 
	{
		String fileName = args[0];
		String string = "";
		try{
			FileReader fr = new FileReader(fileName);
			while(fr.ready()) {
				char[] buffer = new char[100];
				fr.read(buffer);
				string += new String(buffer);
			}
			fr.close();
		} catch(IOException e) {
			System.err.println("Caught IOException: " + e.getMessage());
		}
		parse(string);
	}

	public static void parse(String string)
	{

		MyParser parser = new MyParser();
		parser.parse(string);
		parser.depthFirst();
		System.out.println();
		System.out.println();
		parser.breadthFirst();
	}

	public static void test1(String[] args)
	{
		//MyParser p = new MyParser();
		//p.parse(args[0]);
		//p.breadthFirst();
		//System.out.println();
		//System.out.println();
		//p.depthFirst();
		String string = "";
		for (String s : args) {
			string = string + s + " ";
		}
		string = string.trim();

		//break up string into list of elements and text
		Pattern opener = Pattern.compile("<.*?>");
		Pattern closer = Pattern.compile("</.*?>");
		String[] tokens = string.split("(?=<)|(?<=>)");

		//parse the elements and text in order. Ignore the first and last 
		// tokens, as they are empty strings.
		for (int i = 0; i < (tokens.length); i++) {
			if (tokens[i].equals("") || tokens[i].equals(" ")) {
				System.out.println("EMPTY!! OH NO!!");
			} else {
				System.out.println(tokens[i]);
			}

			String token = tokens[i];
			Matcher isOpener = opener.matcher(token);
			Matcher isCloser = closer.matcher(token);
			if (isOpener.matches()) {
				parseElement(token);
			}
			if (!(isOpener.matches() || isCloser.matches())) {
				System.out.println("Text");
			}
		}
	}

	private static void parseElement(String element)
	{
		//removes the < and > characters from the string
		element = element.substring(1, element.length() - 1);

		//splits element into array containing element and attributes
		String[] tokens = element.split("(\\s+?)(?=(\\S*?=))");

		for (int i = 1; i < tokens.length; i++) {
			String token = tokens[i];
			String[] tokens2 = token.split("=");
			String key = tokens2[0];
			String value = tokens2[1];
			System.out.println(key + "--" + value);
		}
	}
}