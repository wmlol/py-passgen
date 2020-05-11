import pyperclip
import random
import string
import sys

args = sys.argv[1:]

def get_length():
    length = input('password length: ')

    if length.isdigit() and (int(length) > 0):
        generate_password(int(length))
    else:
        print('that was not a valid number, try again')
        get_length()

def generate_password(length):
    if 's' in args:
        charset = string.ascii_letters + string.digits + string.punctuation
    else:
        charset = string.ascii_letters + string.digits
    password = ''.join(random.choice(charset) for i in range(length))
    pyperclip.copy(password)
    print('password copied to clipboard')

for i in args:
    if i.isdigit():
        length = int(i)

if 'length' in globals():
    generate_password(length)
else:
    get_length()