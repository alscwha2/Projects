import java.util.Map;
import java.util.List;

public interface WordCounter {
	Map<String, Integer> process(List<String> wordList);
}