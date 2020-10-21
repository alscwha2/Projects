import java.util.Map;
import java.util.stream.Stream;
import java.util.stream.Collectors;
import java.util.function.Function;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.nio.file.InvalidPathException;


public class FileInfoUtility {
	enum Command {GREP, WC, GREPWC;}

	//got the following code from: https://stackoverflow.com/questions/4731055/whitespace-matching-regex-java
	private static final String whitespace_charclass =  "[" 
                        + "\\u0009" // CHARACTER TABULATION
                        + "\\u000A" // LINE FEED (LF)
                        + "\\u000B" // LINE TABULATION
                        + "\\u000C" // FORM FEED (FF)
                        + "\\u000D" // CARRIAGE RETURN (CR)
                        + "\\u0020" // SPACE
                        + "\\u0085" // NEXT LINE (NEL) 
                        + "\\u00A0" // NO-BREAK SPACE
                        + "\\u1680" // OGHAM SPACE MARK
                        + "\\u180E" // MONGOLIAN VOWEL SEPARATOR
                        + "\\u2000" // EN QUAD 
                        + "\\u2001" // EM QUAD 
                        + "\\u2002" // EN SPACE
                        + "\\u2003" // EM SPACE
                        + "\\u2004" // THREE-PER-EM SPACE
                        + "\\u2005" // FOUR-PER-EM SPACE
                        + "\\u2006" // SIX-PER-EM SPACE
                        + "\\u2007" // FIGURE SPACE
                        + "\\u2008" // PUNCTUATION SPACE
                        + "\\u2009" // THIN SPACE
                        + "\\u200A" // HAIR SPACE
                        + "\\u2028" // LINE SEPARATOR
                        + "\\u2029" // PARAGRAPH SEPARATOR
                        + "\\u202F" // NARROW NO-BREAK SPACE
                        + "\\u205F" // MEDIUM MATHEMATICAL SPACE
                        + "\\u3000" // IDEOGRAPHIC SPACE
                        + "]";

	public static void main(String[] args) throws IOException, InvalidPathException{
		Command command = checkArgsAndGetCommand(args);
		String fileName = command == Command.WC ? args[1] : args[2];

		Stream<String> stream = Files.lines(Paths.get(fileName)); //read the file 
		switch(command) {
			case GREP:
				stream.filter(line -> line.contains(args[1]))//Filter 
					  .forEach(s -> System.out.println(s)); //print lines
				break;
			case WC:
				stream
					.map(line -> line.toLowerCase()) //Convert Case
					.flatMap(line -> Stream.of(line.split(whitespace_charclass))) //Find Words
					.map(word -> word.replaceAll("[^a-zA-Z0-9]", "")) // nonABCConverter
					.filter(word -> !word.equals("")) //RemoveWhiteSpace
					.collect(Collectors.toMap(Function.identity(), word -> 1, (a, b) -> a + b)) //Count Words
					.forEach((word, count) -> System.out.println(word + " - " + count)); //Print;
				break;
			case GREPWC:	
				stream
					.filter(line -> line.contains(args[1]))//Filter Lines
					.map(line -> line.toLowerCase()) //Convert Case
					.flatMap(line -> Stream.of(line.split(whitespace_charclass))) //Find Words
					.map(word -> word.replaceAll("[^a-zA-Z0-9]", "")) // nonABCConverter
					.filter(word -> !word.equals("")) //RemoveWhiteSpace
					.collect(Collectors.toMap(Function.identity(), word -> 1, (a, b) -> a + b)) //Count Words
					.forEach((word, count) -> System.out.println(word + " - " + count)); //Print;
				break;
		}
	}

	private static Command checkArgsAndGetCommand(String[] args) {
		switch(args.length) {
			case 2:
				if (!args[0].toLowerCase().equals("wc")) throwImproperUsageException();
				return Command.WC;
			case 3:
				if (!args[0].toLowerCase().equals("grep")) throwImproperUsageException();
				return Command.GREP;
			case 5:
				if (!args[0].toLowerCase().equals("grep")) throwImproperUsageException();
				if (!args[3].toLowerCase().equals("|")) throwImproperUsageException();
				if (!args[4].toLowerCase().equals("wc")) throwImproperUsageException();
				return Command.GREPWC;
			default:
				throwImproperUsageException();
				return null;
		}
	}

	private static void throwImproperUsageException() {
		throw new IllegalArgumentException("Error: Improper usage.\nProper usage:\n grep \"<STRING>\" <FILEPATH>\nwc <FILEPATH>\ngrep \"<STRING>\" <FILEPATH> \"|\" wc");
	}
}