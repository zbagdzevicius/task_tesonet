import pytest
from search import SoundexSearch

class TestSearch():
    def setup_class(self):
        self.required_length = 5
        self.search = SoundexSearch('wiki_lt.txt', 'lietuva', self.required_length)
    
    def test_length_of_results(self):
        assert len(self.search.found_words) == self.required_length