#include <stdlib.h>
#include <stddef.h>
#include <stdio.h>
#include <string.h>
#include <regex.h>
#include <ctype.h>

#define GREP 4
#define WC 3
#define GREPWC 6

typedef struct Word_Count {
	char *word;
	size_t count;
} word_count;

void to_lower_case(char *lines[]);
int check_args(int argc, char *argv[]);
char *get_file_contents(char *file_name);
char **convert_string_to_array_of_lines(char *string);
void filter_lines(char **lines, char *grep_string);
char **convert_case(char **lines);
char **convert_nonABC(char **lines);
char *convert_nonABC_line(char *line);
char **find_words(char **lines);
word_count *count_words(char **words);
void print_count(word_count *words);
void print_lines(char **lines);
int cmpstr(void const *a, void const *b);

int main(int argc, char *argv[]) {
	if (check_args(argc, argv) == EXIT_FAILURE) {
		fprintf(stderr, "Error: Improper usage.\nProper usage:\n grep \"<STRING>\" <FILEPATH>\nwc <FILEPATH>\ngrep \"<STRING>\" <FILEPATH> \"|\" wc");
		return EXIT_FAILURE;
	}
	
	char *file_name = argc == WC ? argv[2] : argv[3];
	char *file_contents = get_file_contents(file_name);
	char **lines = convert_string_to_array_of_lines(file_contents);
	free(file_contents);

	if (argc == GREP || argc == GREPWC) {
		filter_lines(lines, argv[2]);
	}
	if (argc == WC || argc == GREPWC) {
		to_lower_case(lines);
		char **words = find_words(lines);
		words = convert_nonABC(words);
		word_count *words_and_count = count_words(words);
		print_count(words_and_count);
		return EXIT_SUCCESS;
	}
	if (argc == GREP) {
		print_lines(lines);
	}
	
	return EXIT_SUCCESS;
}

void to_lower_case(char *lines[]) {
	int number_of_lines = atoi(lines[0]);
	for(int i = 1; i <= number_of_lines; i++) strlwr(lines[i]);
}

int check_args(int argc, char *argv[]) {
	switch(argc) {
		case 3:
			if (strcmp(strlwr(argv[1]), "wc")) return EXIT_FAILURE;
			return EXIT_SUCCESS;
		case 4:
			if (strcmp(strlwr(argv[1]), "grep")) return EXIT_FAILURE;
			return EXIT_SUCCESS;
		case 6:
			if (strcmp(strlwr(argv[1]), "grep") 
				|| strcmp(argv[4], "|")
				|| strcmp(strlwr(argv[5]), "wc")) return EXIT_FAILURE;
			return EXIT_SUCCESS;
		default:
			return EXIT_FAILURE;
	}
}

char *get_file_contents(char *file_name) {
	FILE *file = fopen(file_name, "r");
	if (file == NULL) return NULL;
	fseek(file, 0, SEEK_END);
	long file_length = ftell(file);
	char * file_contents = malloc(file_length + 1);
	rewind(file);
	fread(file_contents, sizeof(char), file_length, file);
	file_contents[file_length + 1] = '\0';
	return file_contents;
}

char **convert_string_to_array_of_lines(char *file_contents) {
	int max_lines = 10;
	char ** lines = calloc(max_lines, sizeof(char *));

	int i = 0;
	for(char *line = strtok(file_contents, "\n"); line != NULL; line = strtok(NULL, "\n")) {
		i++;

		if (i == max_lines - 1) {
			max_lines += 10;
			lines = realloc(lines, max_lines * sizeof(char *));
		}

		lines[i] = malloc(strlen(line) + 1);
		strcpy(lines[i], line);
	}

	lines[0] = malloc(10);
	sprintf(lines[0], "%d", i);
	return lines;
}

void filter_lines(char **lines, char *grep_string) {
	int number_of_lines = atoi(lines[0]);
	int new_number_of_lines = 0;

	for (int i = 1; i <= number_of_lines; i++) {
		if(!(strstr(lines[i], grep_string) == NULL)) lines[++new_number_of_lines] = lines[i];
		else free(lines[i]);
	}
	lines = realloc(lines, (new_number_of_lines + 1) * sizeof(char *));
	sprintf(lines[0], "%d", new_number_of_lines);
}

char **find_words(char **lines) {
	int number_of_lines = atoi(lines[0]);

	int current_number_of_words = 0;
	int max_words = 100;
	char **words = calloc(max_words + 1, sizeof(char *));

	char *word = NULL;
	char *line = NULL;
	for(int i = 1; i <= number_of_lines; i++) {
		line = lines[i];
		for(word = strtok(line, " "); word != NULL; word = strtok(NULL, " ")) {
			if (current_number_of_words == max_words) {
				max_words += 100;
				words = realloc(words, max_words * sizeof(char *));
			}
			words[current_number_of_words + 1] = word;
			current_number_of_words++;
		}
	}

	words[0] = malloc(sizeof(int));
	sprintf(words[0], "%d", current_number_of_words);
	free(lines);
	return words;
}

char **convert_nonABC(char **lines) {
	int number_of_lines = atoi(lines[0]);
	int new_number_of_lines = 0;
	char **new_lines = calloc(number_of_lines + 1, sizeof(char *));
	for(int i = 1; i <= number_of_lines; i++) {
		char *converted_line = convert_nonABC_line(lines[i]);
		if(strcmp(converted_line, "") == 0) continue;
		new_lines[++new_number_of_lines] = converted_line;
		//Why does the following free destroy my code?
		//free(lines[i]);
	}
	new_lines[0] = malloc(10);
	sprintf(new_lines[0], "%d", new_number_of_lines);
	new_lines[0][strlen(new_lines[0])] = '\0';
	free(lines);
	return new_lines;
}

char *convert_nonABC_line(char *line) {
	int length = strlen(line);

	char *new_line = malloc(length + 1);
	int new_line_index = 0;

	for(int i = 0; i < length; i++) {
		char c = line[i];
		if(isalnum(c)) {
			new_line[new_line_index] = c;
			new_line_index++;
		}
	}

	new_line = realloc(new_line, (new_line_index + 2) * sizeof(char));
	new_line[new_line_index] = '\0';
	return new_line;
}

word_count *count_words(char **words) {
	int number_of_words = atoi(words[0]);

	qsort(words + 1, number_of_words, sizeof(char *), cmpstr);
	word_count *words_and_count = calloc(number_of_words, sizeof(word_count));
	size_t amount_of_words = 0;
	word_count last_word_seen = {NULL, 0};
	for(int i = 1; i <= number_of_words; i++) {
		char *word = words[i];
		if(last_word_seen.word == NULL || strcmp(word, last_word_seen.word) != 0) {
			last_word_seen = (word_count) {word, 1};
			words_and_count[++amount_of_words] = last_word_seen;
		} else {
			words_and_count[amount_of_words].count++;
			free(word);
		}
	}

	free(words);
	words_and_count[0] = (word_count) {NULL, amount_of_words};
	return words_and_count;
}

//got this code from: https://stackoverflow.com/questions/3757899/sorting-strings-using-qsort
// and: https://stackoverflow.com/questions/3489139/how-to-qsort-an-array-of-pointers-to-char-in-c
int cmpstr(void const *a, void const *b) { 
    char const *aa = *(char const **)a;
    char const *bb = *(char const **)b;

    return strcmp(aa, bb);
}

void print_count(word_count *words) {
	size_t number_of_words = words[0].count;
	for (int i = 1; i <= number_of_words; i++) printf("%s - %d\n", words[i].word, words[i].count);
}

void print_lines(char **lines) {
	size_t number_of_lines = atoi(lines[0]);
	for (int i = 1; i <= number_of_lines; i++) printf("%s\n", lines[i]);
}