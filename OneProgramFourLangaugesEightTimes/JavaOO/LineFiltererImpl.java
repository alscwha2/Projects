import java.util.Scanner;

public class LineFiltererImpl implements LineFilterer {

	private String grepCriteria;

	public LineFiltererImpl(String grepCriteria){
		this.grepCriteria = grepCriteria;
	}

	public String process(String fileContents) {
		String returnLine = "";

		Scanner sc = new Scanner(fileContents);
		String currentLine = null;
		while (sc.hasNextLine()) {
			currentLine = sc.nextLine();
			if (currentLine.contains(grepCriteria)) returnLine += currentLine + "\n";
		}

		return returnLine;
	}
}