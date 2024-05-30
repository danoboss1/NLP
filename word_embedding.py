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
    'Dogs do not drink coffe'
]

class UltraWordMachine:
    def __init__(self, word_dictionary):
        self.word_dictionary = word_dictionary

    def process_sentences(self, sentences):
        pass

    def generate_sentences(self, length):
        pass