package edu.yc.oats.algs;

public class ColoredItem extends Item
{
	private Color color;

	public ColoredItem(final String description, final double price, final Color color)
	{
		super(description, price);
		this.color = color;
	}
	
	public Color getColor()
	{
		return this.color;
	}

	@Override
	public int hashCode() {
		final int prime = 31;
		int result = super.hashCode();
		result = prime * result + ((color == null) ? 0 : color.hashCode());
		return result;
	}

	@Override
	public boolean equals(Object obj) {
		if (this == obj)
			return true;
		if (!super.equals(obj))
			return false;
		if (getClass() != obj.getClass())
			return false;
		ColoredItem other = (ColoredItem) obj;
		if (color != other.color)
			return false;
		return true;
	}

	@Override
	public String toString() {
		return "ColoredItem [getDescription()=" + getDescription() + ", getPrice()=" + getPrice()
				+ "color=" + color + "]";
	}
}