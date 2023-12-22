import random

class Letter():
    def __init__(self,letter_dir):
        self.letter_dir = letter_dir
        self.email_message = ""
        
                
    def choose_letter(self):
        random_letter = f"letter_{random.randint(1,3)}.txt"
        path_to_letter = f"{self.letter_dir}/{random_letter}"
        with open(path_to_letter) as file:
            self.letter_message = file.read()

    def write_letter(self, name):
        self.choose_letter()
        self.email_message = self.letter_message.replace("[NAME]",name.strip())
