import java.util.Map;
import java.util.HashMap;
import java.util.List;
public class DocumentProcessor {

	private LineFilterer lf;
	private NonABCFilterer nabcf;
	private WordFinder wf;
	private CaseConverter cc;
	private WordCounter wc;

	public DocumentProcessor(LineFilterer lf, CaseConverter cc, WordFinder wf, NonABCFilterer nabcf, WordCounter wc) {
		if (!(cc == null && wf == null && nabcf == null && wc == null) && 
			!(cc != null && wf != null && nabcf != null && wc != null)) throw new IllegalArgumentException("Either all of NonABCFilterer, WordFinder, CaseConverter and WordCounter must be null or not-null.");
		
		this.lf = lf;
		this.nabcf = nabcf;
		this.wf = wf;
		this.cc = cc;
		this.wc = wc;
	}

	public Map<String, Integer> process(String fileContents) {
		boolean grep = lf != null;
		boolean wordcount = nabcf != null;

		if (grep) {
			fileContents = lf.process(fileContents);
			if(!wordcount) {
				HashMap<String, Integer> returnMap = new HashMap<>();
				returnMap.put(fileContents, null);
				return returnMap;
			}
		}
		if (wordcount) {
			fileContents = cc.process(fileContents);
			List<String> words = wf.process(fileContents);
			words = nabcf.process(words);
			return wc.process(words);
		}

		System.err.println("Error: You have a bug in your code, because the process() method in DocumentProcessor class is under the impression that it is possible to have a command that is neither \"grep\" nor \"wc\".");
		return null;
	}
}