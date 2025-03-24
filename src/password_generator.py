import random
import string
from abc import ABC, abstractmethod


class PasswordGenerator(ABC):
    @abstractmethod
    def generate(self):
        pass


class PinPassword(PasswordGenerator):
    def __init__(self, length: int = 4):
        self.length = length

    def generate(self):
        return ''.join([random.choice(string.digits) for _ in range(self.length)])


class RandomPassword(PasswordGenerator):
    def __init__(self, length: int = 8, numbers: bool = True, special_chars: bool = True):
        self.length = length
        self.numbers = numbers
        self.special_chars = special_chars
        self.chars = string.ascii_letters
        if numbers:
            self.chars += string.digits
        if special_chars:
            self.chars += string.punctuation

    def generate(self):
        password = ''.join([random.choice(self.chars) for _ in range(self.length)])
        if self.numbers and not any(char.isdigit() for char in password):
            return self.generate()
        if self.special_chars and not any(char in string.punctuation for char in password):
            return self.generate()
        return password


class MemorablePassword(PasswordGenerator):
    def __init__(self,
                 words_num: int = 4,
                 separator: str = '-',
                 capitalize: bool = True,
                 words_source: str = 'src/data/words.txt'
                 ):
        self.words_num = words_num
        self.separator = separator
        self.capitalize = capitalize
        self.words = []
        with open(words_source) as f:
            for line in f:
                self.words.append(line.strip())

    def generate(self):
        selected_words = [random.choice(self.words) for _ in range(self.words_num)]
        if self.capitalize:
            while True:
                selected_words = [word.capitalize() if random.choice([True, False]) else word for word in selected_words]
                if any(word.lower() == word for word in selected_words):
                    break
        password = self.separator.join(selected_words)
        return password
