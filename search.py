from difflib import SequenceMatcher
import re
from threading import Thread
import argparse

class SoundexSearch:
    def __init__(self, filepath, query, words_to_return = 5):
        self.words_to_return = words_to_return
        self.found_words = []
        self.found_fallback_words = []
        
        self.soundex_string_to_search = self.soundex(query)
        
        self.search_file(filepath)
    
    @staticmethod
    def run(job_fn, argument):
        job_thread = Thread(target=job_fn, args=(argument,))
        job_thread.start()

        
    def search_file(self, filepath):
        with open(filepath) as reading_file:
            for line in reading_file:
                self.run(self.search_line, line)
        number_of_words = len(self.found_words)
        if number_of_words < self.words_to_return:
            self.fill_result_with_callbacks(number_of_words)
        else:
            self.remove_overflow_of_words()

    def search_line(self, line):
        words = line.split()
        for word in words:
            word = self.clean_word(word)
            if word not in self.found_words:
                self.search_word(word)
    
    def search_word(self, word):
        soundex_word = self.soundex(word)
        similarity = self.soundex_query_similarity(soundex_word)
        if similarity == 1.0:
            print(f"thats a match ! appending {word}")
            self.found_words.append(word)
        else:
            if similarity >= 0.75:
                self.found_fallback_words.append(word)
    
    def fill_result_with_callbacks(self, number_of_words):
        words_to_fill = self.words_to_return - number_of_words
        if len(self.found_fallback_words) >= words_to_fill:
            print("not enough words, filling")
            for x in range(words_to_fill):
                print(f"filling with: {self.found_fallback_words[x]}")
                self.found_words.append(self.found_fallback_words[x])
    
    def remove_overflow_of_words(self):
        self.found_words = self.found_words[0:self.words_to_return]
        
        
    
    def soundex_query_similarity(self, word):
        match = SequenceMatcher(None, self.soundex_string_to_search, word)
        return match.ratio()

    @staticmethod
    def clean_word(word):
        return re.sub(r'\W+', '', word)


    def soundex(self, query: str):
        query = query.lower()
        letters = [char for char in query if char.isalpha()]


        if len(query) == 1:
            return query + "000"
        elif len(letters) == 0:
            return ""

        characters_to_remove = ('a', 'e', 'i', 'o', 'u', 'y', 'h', 'w')

        first_letter = letters[0]
        letters = letters[1:]
        letters = [char for char in letters if char not in characters_to_remove]

        if len(letters) == 0:
            return first_letter + "000"


        to_replace = {('b', 'f', 'p', 'v'): 1, ('c', 'g', 'j', 'k', 'q', 's', 'x', 'z'): 2,
                    ('d', 't'): 3, ('l',): 4, ('m', 'n'): 5, ('r',): 6}

        first_letter = [value if first_letter else first_letter for group, value in to_replace.items()
                        if first_letter in group]
        letters = [value if char else char
                for char in letters
                for group, value in to_replace.items()
                if char in group]

        letters = [char for ind, char in enumerate(letters)
                if (ind == len(letters) - 1 or (ind+1 < len(letters) and char != letters[ind+1]))]

        if first_letter == letters[0]:
            letters[0] = query[0]
        else:
            letters.insert(0, query[0])

        first_letter = letters[0]
        letters = letters[1:]

        letters = [char for char in letters if isinstance(char, int)][0:3]

        while len(letters) < 3:
            letters.append(0)

        letters.insert(0, first_letter)

        string = "".join([str(l) for l in letters])

        return string
    
parser = argparse.ArgumentParser()
parser.add_argument("file_path")
parser.add_argument("query")
parser.add_argument("--number_of_words", help="number of words", type=int)
arguments = parser.parse_args()
file_path = arguments.file_path
query = arguments.query
number_of_words = arguments.number_of_words
if number_of_words == None:
    number_of_words = 5

soundex = SoundexSearch(file_path, query, number_of_words)
print(soundex.found_words)