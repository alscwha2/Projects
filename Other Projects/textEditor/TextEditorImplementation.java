import java.util.Scanner;
import java.util.NoSuchElementException;

public class TextEditorImplementation
{
	private static TextEditor editor;

	public static void main(String[] args)
	{
		editor = new TextEditor();
		Scanner scanner = new Scanner(System.in);
		String input = "";
		try{
			while(!input.equals("#exit")) {
				System.out.print(">");
				input = scanner.nextLine();
				parse(input);
			}
		} catch(NoSuchElementException e) {
			System.err.println("Caught NoSuchElementException: " + e.getMessage());
		} catch(IllegalStateException e) {
			System.err.println("Caught IllegalStateException: " + e.getMessage());
		} finally {
			scanner.close();
		}
	}

	private static void parse(String input)
	{
		input.trim();
		if(input.startsWith("#print")) {
			parsePrint(input);
			return;
		}
		if(input.startsWith("#delete")) {
			parseDelete(input);
			return;
		}
		editor.addLine(input);
	}

	private static void parsePrint(String input)
	{
		if(input.equals("#print")) {
			editor.printAll();
			return;
		}

		String[] args = input.split(" ");
		if(args.length != 2 || !args[0].equals("#print")) {
			editor.addLine(input);
			return;
		}
		if(args.length == 2) {
			try{
				editor.printLine(Integer.parseInt(args[1]));
			}
			catch(NumberFormatException e) {
				System.err.println("Caught NumberFormatException: " + e.getMessage());
			}
		}
	}

	private static void parseDelete(String input)
	{
		if(input.equals("#delete")) {
			editor.deleteAll();
			return;
		}

		String[] args = input.split(" ");
		if(args.length != 2) {
			editor.addLine(input);
			return;
		}
		if(args.length == 2) {
			try{
				editor.deleteLine(Integer.parseInt(args[1]));
			}
			catch(NumberFormatException e) {
				System.err.println("Caught NumberFormatException: " + e.getMessage());
			}
		}

	}
}