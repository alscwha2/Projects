import java.util.HashMap;
import java.util.ArrayList;

public class ElementNode
{
	private String tag;
	private HashMap<String, String> attributes;
	private ElementNode parent;
	private ArrayList<ElementNode> children;
	private boolean hasID;

	public ElementNode(String tag)
	{
		super();
		this.tag = tag;
		this.attributes = new HashMap<String, String>();
		this.children = new ArrayList<ElementNode>();
		this.hasID = false;
	}

	public void addAttribute(String tag, String value)
	{
		attributes.put(tag, value);
		if (tag.equals("id")) {
			this.hasID = true;
		}
	}

	public ElementNode getParent()
	{
		return this.parent;
	}

	private void setParent(ElementNode parent)
	{
		this.parent = parent;
	}

	public ElementNode[] getChildren()
	{
		ElementNode[] array = new ElementNode[this.children.size()];
		return this.children.toArray(array);
	}

	public void addChild(ElementNode child)
	{
		this.children.add(child);
		child.setParent(this);
	}

	public void printInfo()
	{
		System.out.print("Tag: " + this.tag);
		System.out.print(" Attributes:");
		for (String attribute : attributes.keySet()) {
			System.out.print(" " + attribute + "=" + attributes.get(attribute));
		}
		System.out.println();
	}

	public boolean hasID()
	{
		return this.hasID;
	}
}