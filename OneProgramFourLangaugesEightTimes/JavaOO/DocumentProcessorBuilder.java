/*
 You will use the builder pattern. Specifically, you will define a DocumentProcessorBuilder, which has a separate
setter method for each of the five steps above. Each setter method takes as its parameter an object which will be used
for that step.
*/

public class DocumentProcessorBuilder {

	private LineFilterer lf;
	private CaseConverter cc;
	private WordFinder wf;
	private NonABCFilterer nabcf;
	private WordCounter wc;

	public DocumentProcessorBuilder() {

	}

	public void setLineFilterer(LineFilterer lf) {
		this.lf = lf;
	}

	public void setCaseConverter(CaseConverter cc) {
		this.cc = cc;
	}

	public void setWordFinder(WordFinder wf) {
		this.wf = wf;
	}

	public void setNonABCFilterer(NonABCFilterer nabcf) {
		this.nabcf = nabcf;
	}

	public void setWordCounter(WordCounter wc) {
		this.wc = wc;
	}

	public DocumentProcessor build() {
		return new DocumentProcessor(lf, cc, wf, nabcf, wc);
	}
	
}