public class TextEditor
{
	private MyStack stack;
	private int numLines;

	public TextEditor()
	{
		this.stack = new MyStack();
		this.numLines = 0;
	}

	public void addLine(String line)
	{
		this.stack.push(line);
		this.numLines++;
	}

	public void deleteLine(int lineNumber)
	{
		//check bounds
		if(lineNumber > this.numLines) {
			this.printOutOfBoundsError();
		}
		if(lineNumber < 1) {
			return;
		}

		//store everything in the stack into a new stack until you reach
		//the line that you want to delete
		MyStack newStack = new MyStack();
		int numPopped = 0;
		while(((this.numLines - numPopped) - lineNumber) != 0) {
			newStack.push(this.stack.pop());
			numPopped++;
		}

		//delete the line
		this.stack.pop();

		//put everything back into the original stack
		String line = newStack.pop();
		while(line != null) {
			this.stack.push(line);
			line = newStack.pop();
		}

		//update the numLines field
		this.numLines--;
	}

	public void deleteAll()
	{
		stack.clear();
		numLines = 0;
	}

	public void printLine(int lineNumber)
	{
		//check bounds
		if(lineNumber > this.numLines) {
			this.printOutOfBoundsError();
			return;
		}
		if(lineNumber < 1) {
			return;
		}

		//store everything in the stack into a new stack until you reach
		//the line that you want to print
		MyStack copy = this.stack.clone();
		int numPopped = 0;
		while(((this.numLines - numPopped) - lineNumber) != 0) {
			copy.pop();
			numPopped++;
		}
		System.out.println(copy.pop());
	}

	public void printAll()
	{
		//make a stack such that the lines will be popped in order
		MyStack backwards = this.stack.clone();
		MyStack forwards = new MyStack();
		String line = backwards.pop();
		while(line != null) {
			forwards.push(line);
			line = backwards.pop();
		}

		//pop each line and print it
		line = forwards.pop();
		while(line != null) {
			System.out.println(line);
			line = forwards.pop();
		}
	}

	private void printOutOfBoundsError()
	{
		System.out.println("Error: There are only " + this.numLines + " lines in this document.");
	}
}