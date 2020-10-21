import java.util.List;
import java.util.ListIterator;
import java.util.LinkedList;

public class NonABCFiltererImpl implements NonABCFilterer {
	public NonABCFiltererImpl() {

	}

	public List<String> process(List<String> words) {
		ListIterator<String> it = words.listIterator();
		String currentString = null;
		while(it.hasNext()) {
			currentString = it.next();
			currentString = currentString.replaceAll("[^a-z0-9]", "");
			if (currentString.equals("")) {
				it.remove();
				continue;
			}
			it.set(currentString);
		}
		return words;
	}
}