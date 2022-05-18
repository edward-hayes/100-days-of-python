def pig_it(text):
    split = text.split()
    pig_latin = [f"{word[1:]}{word[0]}ay"  if word.isalpha() else word for word in split]
    return ' '.join(pig_latin)

while True:
    phrase = input("Write the word or phrase you'd like to convert: ")
    print(pig_it(phrase))