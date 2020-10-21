public class CaseConverterImpl implements CaseConverter {

	public CaseConverterImpl() {

	}

	public String process(String fileContents) {
		return fileContents.toLowerCase();
	}
}