import java.util.ArrayList;
import java.util.regex.*;
import java.util.concurrent.LinkedBlockingQueue;

public class MyParser
{
	private MyTreeBuilder tree;

	public MyParser()
	{
	}

	public void parse(String string)
	{
		this.tree = new MyTreeBuilder();

		//break up string into list of elements and text
		Pattern opener = Pattern.compile("<.*?>");
		Pattern closer = Pattern.compile("</.*?>");
		String[] tokens = string.split("(?=<)|(?<=>)");

		//parse the elements and text in order. Ignore the first and last 
		// tokens, as they are empty strings.
		for (int i = 0; i < (tokens.length); i++) {
			String token = tokens[i];
			Matcher isOpener = opener.matcher(token);
			Matcher isCloser = closer.matcher(token);
			if (isCloser.matches()) {
				this.tree.returnToParent();
			}
			else if (isOpener.matches()) {
				parseElement(token);
			}
			else {
				if(!token.trim().equals("")) {
					parseText(token);
				}
			}
		}
	}

	private void parseElement(String element)
	{
		//removes the < and > characters from the string
		element = element.substring(1, element.length() - 1);

		//splits element into array containing element and attributes
		String[] tokens = element.split("(\\s+?)(?=(\\S*?=))");

		//makes element node in tree
		this.tree.addChild(tokens[0]);

		//adds attributes
		for (int i = 1; i < tokens.length; i++) {
			parseAttribute(tokens[i]);
		}
	}

	private void parseAttribute(String attribute)
	{
		//split the attribute tag from the value
		String[] tokens = attribute.split("=");
		String key = tokens[0];
		String value = tokens[1];

		//add attribute. If attirbute is ID then it will replace the previous one

		this.tree.addAttribute(key, value);
	}

	private void parseText(String text)
	{
		this.tree.addChild("text");
		this.tree.addAttribute("content", text);
		this.tree.returnToParent();
	}

	public void breadthFirst()
	{
		try{
			LinkedBlockingQueue<ElementNode> q = new LinkedBlockingQueue<ElementNode>();
			ElementNode currentNode = this.tree.getRoot();
			while (currentNode != null) {	

				//print the information for the node
				currentNode.printInfo();
				//add its children to the queue
				for(ElementNode child : currentNode.getChildren()) {
					q.put(child);
				}
				currentNode = q.poll();
			}
		} catch (InterruptedException e) {
			System.out.println("Caught InterruptedException: " + e.getMessage());
		}
	}

	public void depthFirst()
	{
		ElementNode root = this.tree.getRoot();
		root.printInfo();
		depthFirstPart2(root);
	}

	private void depthFirstPart2(ElementNode root)
	{
		for (ElementNode child : root.getChildren()) {
			child.printInfo();
			depthFirstPart2(child);
		}
	}
}