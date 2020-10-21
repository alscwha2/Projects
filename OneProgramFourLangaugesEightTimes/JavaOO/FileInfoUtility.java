import java.util.Set;
import java.util.Map;
import java.util.Iterator;
import java.io.File;
import java.io.FileReader;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.nio.file.InvalidPathException;


public class FileInfoUtility {
	private String[] args;

	/*
	No imperative steps in main(): you may not do any part of the logic in imperative code. All your main method is allowed to do is create an instance of some class and pass it the command line arguments. 
	*/
	public static void main(String[] args) {
		FileInfoUtility utility = new FileInfoUtility(args);
	}

	public FileInfoUtility(String[] args) {
		this.args = args;
		process();
	}

	private void process() {
		checkArgs();
		DocumentProcessorBuilder builder = new DocumentProcessorBuilder();
		prepareBuilder(builder);
		DocumentProcessor processor = builder.build();

		String fileName = getFileName();
		String fileContents = null;
		try {
			fileContents = processFile(fileName);
		} catch(IOException | InvalidPathException e) {
			System.err.println(e.getMessage());
			return;
		}

		Map<String, Integer> map = processor.process(fileContents);
		printContents(map);
	}

	private void checkArgs() {
		switch(args.length) {
			case 2:
				if (!args[0].toLowerCase().equals("wc")) throwImproperUsageException();
				break;
			case 3:
				if (!args[0].toLowerCase().equals("grep")) throwImproperUsageException();
				break;
			case 5:
				if (!args[0].toLowerCase().equals("grep")) throwImproperUsageException();
				if (!args[3].toLowerCase().equals("|")) throwImproperUsageException();
				if (!args[4].toLowerCase().equals("wc")) throwImproperUsageException();
				break;
			default:
				throwImproperUsageException();
				break;
		}
	}

	private void throwImproperUsageException() {
		throw new IllegalArgumentException("Error: Improper usage.\nProper usage:\n grep \"<STRING>\" <FILEPATH>\nwc <FILEPATH>\ngrep \"<STRING>\" <FILEPATH> \"|\" wc");
	}

	private void prepareBuilder(DocumentProcessorBuilder builder) {
		String fileName = null;
		switch(args.length) {
			//wc
			case 2:
			fileName = args[1];
			//grep | wc
			case 5:
				builder.setCaseConverter(new CaseConverterImpl());
				builder.setWordFinder(new WordFinderImpl());
				builder.setNonABCFilterer(new NonABCFiltererImpl());
				builder.setWordCounter(new WordCounterImpl());
				if (args.length == 2) break;
			//grep (and fallthrough for grep | wc)
			case 3:
				fileName = args[2];
				builder.setLineFilterer(new LineFiltererImpl(args[1]));
		}
	}

	private String getFileName() {
		if(args.length == 2) return args[1];
		return args[2];
	}

	private String processFile(String fileName) throws IOException, InvalidPathException{
		//got following code from https://howtodoinjava.com/java/io/java-read-file-to-string-examples/
        return new String (Files.readAllBytes(Paths.get(fileName)));

	}

	private void printContents(Map<String, Integer> map) {
		if (args.length == 3) {
			//grep
			System.out.print((String) map.keySet().toArray()[0]);
		} else {
			//wc or (grep | wc) 

			//got the following code from this link: https://stackoverflow.com/questions/1066589/iterate-through-a-hashmap
			Iterator it = map.entrySet().iterator();
		    while (it.hasNext()) {
		        Map.Entry pair = (Map.Entry)it.next();
		        System.out.println(pair.getKey() + " - " + pair.getValue());
		    }
		}
	}
}