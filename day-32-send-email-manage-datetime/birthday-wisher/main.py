from mailer import Email
from letter import Letter
from celebrant import Celebrant


PATH_TO_LETTER_DIR = "letter_templates"
BIRTHDAYS_FILE = "birthdays.csv"

letter = Letter(PATH_TO_LETTER_DIR)
celebrant = Celebrant(BIRTHDAYS_FILE)
email = Email()

def wish_happy_birthday():
    celebrant.get_todays_birthdays()
    for index, row in celebrant.todays_birthdays.iterrows():
        letter.write_letter(row['name'])
        email.send_msg(
            to_address=row['email'],
            subject=f"Happy Birthday, {row['name']}!",
            message=letter.email_message
            )
        
wish_happy_birthday()
