# trieda ktora zobere vetu a ulozi slova do slovnika
# kazde slovo v slovniku bude mat priradene unikatne cislo
# slova sa nebudu opakovat
# v tom slovniku nebudu iba cisla toho slova ale aj slova pred nim a za nim ako hodnoty v sete
# a potom bude generovat nove slova, tak ze zobere nahodne slovo, ktore bolo prve 
# a podla mnozin predchodcov a naslednikov vytvori random dlhu vetu
# ktoru nasledne vypise

# demonstracia principu ako funguju word embeddings a zakladne algoritmy na NLP

sentences = [
    'I love dogs',
    'Dogs are usually outside',
    'You drink coffee',
    'You love going outside',
    'You and dogs are usually outside',
    'I drink coffee',
    'Dogs do not drink coffee'
]

class UltraWordMachine:
    def __init__(self):
        self.word_dictionary = {}
        self.word_dictionary_preceding_tokens = {}
        self.word_dictionary_following_tokens = {}

    def process_sentences(self, sentences):
        i = 0

        for sentence in sentences:
            sentences_split_to_words = sentence.split()
            for word in sentences_split_to_words:
                if word.lower() not in self.word_dictionary:
                    self.word_dictionary[word.lower()] = i
                    i += 1

    # TOTO TREBA Z DEBUGGOVAT
    def check_preceding_words(self, sentences):
        last_word = ''
        for sentence in sentences:
            sentences_split_to_words = sentence.split()
            for idx, word in enumerate(sentences_split_to_words):
                if word not in self.word_dictionary_preceding_tokens:
                    self.word_dictionary_preceding_tokens[word.lower()] = set()

                if idx == 0:
                    # to store word from last iteration, the preceding token
                    last_word = word
                    self.word_dictionary_preceding_tokens[word.lower()].add('-')
                else:
                    self.word_dictionary_preceding_tokens[word.lower()].add(last_word)
                    # to store word from this iteration, the preceding token, but before I have to use last_word
                    last_word = word

        print(self.word_dictionary_preceding_tokens)

    def check_following_words(self, sentences):
        # this take sentence by sentence, so we can check length of the sentences_split_to_words
        for sentence in sentences:
            sentences_split_to_words = sentence.split()
            for idx, word in enumerate(sentences_split_to_words):
                if word not in self.word_dictionary_following_tokens:
                    self.word_dictionary_following_tokens[word.lower()] = set()

                if idx < len(sentences_split_to_words) - 1:
                    following_word = sentences_split_to_words[idx + 1].lower()
                    self.word_dictionary_following_tokens[word.lower()].add(following_word)
                else:
                    self.word_dictionary_following_tokens[word.lower()].add('.')

        print(self.word_dictionary_following_tokens)

    def print_dictionary(self):
        print(self.word_dictionary)

    # I need to generate the words somehow
    def generate_sentences(self, length):
        pass

tokenizer = UltraWordMachine()
tokenizer.process_sentences(sentences)
tokenizer.check_preceding_words(sentences)
tokenizer.check_following_words(sentences)
tokenizer.print_dictionary()