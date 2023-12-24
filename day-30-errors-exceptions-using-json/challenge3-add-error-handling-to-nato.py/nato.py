import pandas

PATH_TO_NATO_ALPHABET = "nato_phonetic_alphabet.csv"

nato_alphabet = pandas.read_csv(PATH_TO_NATO_ALPHABET)
nato_dict = {row.letter:row.code for (index,row) in nato_alphabet.iterrows()}

while True:
    phrase = input("Write the word or phrase you'd like to convert:").upper().replace(" ", "")
    
    try: 
        nato_phrase = [nato_dict[letter] for letter in phrase]
    except KeyError:
        print("phrase can only include letters. Symbols or Numbers not allowed")
    else:
        print(nato_phrase)