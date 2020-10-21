public class MyStack
{	
	private String[] stackArray;
	private int tail;
	private int stackSize;

	public MyStack()
	{
		this.stackArray = new String[100];
		this.tail = -1;
		this.stackSize = 100;
	}

	public void push(String entry)
	{
		this.tail++;

		if(this.tail == this.stackSize) {
			this.doubleSize();
		}

		stackArray[this.tail] = entry;

	}

	public String pop()
	{
		if(this.tail == -1) {
			return null;
		}

		String entry = stackArray[this.tail];
		stackArray[this.tail] = null;
		this.tail--;

		return entry;
	}

	private void doubleSize()
	{

		String[] newArray = new String[this.stackSize * 2];

		for(int i = 0; i < stackSize; i++){
			newArray[i] = stackArray[i];
		}

		this.stackArray = newArray;
		this.stackSize = this.stackSize * 2;
	}

	public void clear()
	{
		for(int i = 0; i < stackSize; i++) {
			stackArray[i] = null;
		}

		this.tail = -1;
	}

	public MyStack clone()
	{
		MyStack newStack = new MyStack();

		for(int i = 0; i <= this.tail; i++) {
			newStack.push(this.stackArray[i]);
		}

		return newStack;
	}
}