package distributed_systems_homework_ASM;

public class Class
{
	private int crn;
	private String name;

	public Class(int crn, String name) 
	{
		this.crn = crn;
		this.name = name;
	}

	public int getCRN()
	{
		return this.crn;
	}

	public String toString()
	{
		return "crn: " + this.crn + " --- name: " + this.name;
	}
}