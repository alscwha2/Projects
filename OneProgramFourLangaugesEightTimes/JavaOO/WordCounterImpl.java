import java.util.Map;
import java.util.HashMap;
import java.util.List;

public class WordCounterImpl implements WordCounter {
	public WordCounterImpl() {

	}

	public Map<String, Integer> process(List<String> wordList) {
		Map<String, Integer> wordCountMap = new HashMap<>();
		for(String word : wordList) {
			if(wordCountMap.containsKey(word)) {
				wordCountMap.put(word, wordCountMap.get(word) + 1);
			} else {
				wordCountMap.put(word, 1);
			}
		}
		return wordCountMap;
	}	
}