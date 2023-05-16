# Consider this list

# french_words= ["Bonjour", "Au revoir", "Bienvenue", "A bientôt"] 
# Look at this result :
# {"Bonjour": "Hello", "Au revoir": "Goodbye", "Bienvenue": "Welcome", "A bientôt": "See you soon"}
# You have to recreate the result using a translator module.


from deep_translator import GoogleTranslator
french_words= ["Bonjour", "Au revoir", "Bienvenue", "A bientôt"]

for word in french_words:
    english_translation = GoogleTranslator(source='french', target='english').translate(word)
    translation_dict = {}
    translation_dict[word] = english_translation
    print(translation_dict)

# example = GoogleTranslator(source='auto', target='fr').translate(french_words) 
# print(example)

# french_words= ["Bonjour", "Au revoir", "Bienvenue", "A bientôt"]
# translated_word = LingueeTranslator(source='english', target='french').translate(french_words)
# print(translated_word)

# can't finish because I am having trouble with the modules