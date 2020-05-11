import pyperclip
import random
import string

def get_length():
    length = input('password length: ')
    if length.isdigit() and (int(length) > 0):
        generate_password(int(length))
    else:
        print('that was not a valid number, try again')
        get_length()

def generate_password(length):
    charset = string.ascii_letters + string.digits
    password = ''.join(random.choice(charset) for i in range(length))
    pyperclip.copy(password)
    print('password copied to clipboard')

get_length()