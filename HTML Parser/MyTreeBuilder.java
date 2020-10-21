import java.util.HashSet;

/**
*MyTreeBuilder class provides a framework to build a DOM tree efficiently.
*It holds onto the last node added for easy access. Since we are dealing with nested elements
*we do not know that we are done with a given element until we find its closing <\> symbol. Once
*we are done with it, we want to go to its parent (i.e. the next outer element in the nest) in order 
*to add more nested elements as its child. The returnToParent() method sets the current node's parent as
*the current node.
*/
public class MyTreeBuilder
{
	private ElementNode root;
	private ElementNode current;
	private HashSet<String> ids;
	private int lastIdGenerated;

	public MyTreeBuilder()
	{
		ids = new HashSet<String>();
		this.lastIdGenerated = 0;
	}

	public void addChild(String tag)
	{
		ElementNode child = new ElementNode(tag);
		this.assignID(child);
		//if this is the first node, make it the root
		if (this.root == null) {
			root = child;
		}
		else {
			this.current.addChild(child);
		}
		this.current = child;
	}

	public void addAttribute(String tag, String value)
	{
		//if assigning id, make sure that this id hasn't been used before. if it has,
		//replace it with a new generated id. Add the id to the set of ids
		if (tag.equals("id")) {
			while (ids.contains(value)) {
				value = this.nextID();
			}
			ids.add(value);
		}

		this.current.addAttribute(tag, value);
	}

	public ElementNode getRoot()
	{
		return this.root;
	}

	public void returnToParent()
	{
		this.current = current.getParent();
	}

	private void assignID(ElementNode child)
	{
		String id = nextID();
		while (ids.contains(id)) {
			id = nextID();
		}

		child.addAttribute("id", id);
	}

	private String nextID()
	{
		this.lastIdGenerated++;
		return "ID#" + this.lastIdGenerated;
	}
}