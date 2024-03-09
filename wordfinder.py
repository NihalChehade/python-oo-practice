"""Word Finder: finds random words from a dictionary."""

import random
class WordFinder:
     """Finds random words from file of words using the path to that file
    
         >>> words = WordFinder("words.txt")
         235886 words read

         >>> words.random()  random word everytime random is called on words
         'sourish'

        >>> words.random() 
        'unrousable'

         >>> words.random() 
         'overhardness'    
     """
         
     def __init__(self, path):
        """generate a word finder from file path of file ofwords"""
        self.path = path
        self.word_list=[]
        
        self.fill_word_list_from_file()
        self.print_num_of_words_read()
       

     def print_num_of_words_read(self):
         """prints the number pf words in a file"""
         print(f'{len(self.word_list)} words read')
    
     def fill_word_list_from_file(self):
        """Opens a file and fill the words in that file in  word_list"""
        file = open(self.path, "r")
        for word in file:
            self.word_list.append(word.strip())
        file.close()

     def random(self):
        """Returns a random word from word_list"""
        return random.choice(self.word_list)


class SpecialWordFinder(WordFinder): 
    """SpecialWordFinder handles files that includes empty lines and comments.
    It does not print them when picking random words!
    
    >>> s_word = SpecialWordFinder("specialwords.txt")
    3 words read

    >>> s_word.random() # never returns an empty string with newline tag or a comment
    'mango'

    >>> s_word.random() 
    'kale'

    >>> s_word.random() 
    'apple'
    """
    def __init(self, path):
        super().__init__(path)

    def fill_word_list_from_file(self):
        """Opens a file and fill the words in that file in  word_list"""
        file = open(self.path, "r")
        for word in file:
            if not word =="\n" and not word.startswith("#"):
                self.word_list.append(word.strip())
        file.close()
        
