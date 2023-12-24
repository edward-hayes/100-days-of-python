import random

LETTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
NUMBERS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
SYMBOLS = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


class PasswordGenerator:
  def __init__(self) -> None:
    self.generated_password = ""
    self.password_list = []

  def refresh(self):
    self.password_list = []
    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)
    password_letters = [random.choice(LETTERS) for char in range(nr_letters)]
    password_symbols = [random.choice(SYMBOLS) for char in range(nr_symbols)]
    password_numbers = [random.choice(NUMBERS) for char in range(nr_numbers)]
    self.password_list = password_letters + password_symbols + password_numbers

  def generate(self):
    self.refresh()
    self.generated_password = ""
    random.shuffle(self.password_list)
    self.generated_password = ''.join(self.password_list)
