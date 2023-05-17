
class Text:
    def __init__(self, text):
        self.text = text

    def word_frequency(self, word):
        words = self.text.split()
        count = words.count(word)
        if count == 0:
            return f"The word '{word}' does not appear in the text."
        else:
            return f"The word '{word}' appears {count} time(s) in the text."

    def most_common_word(self):
        words = self.text.split()
        word_counts = {}
        for word in words:
            word_counts[word] = word_counts.get(word, 0) + 1
        if not word_counts:
            return "The text is empty."
        most_common = max(word_counts, key=word_counts.get)
        return f"The most common word in the text is '{most_common}'."

    def unique_words(self):
        words = self.text.split()
        unique_words = list(set(words))
        return unique_words
    

text = "A good book would sometimes cost as much as a good house."
my_text = Text(text)

print(my_text.word_frequency("good"))
print(my_text.most_common_word())
print(my_text.unique_words())