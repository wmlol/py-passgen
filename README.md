# py-passgen
generates a secure password with length specified and copies it to your clipboard

CLI Usage:
`python3 cli.py [length] [s]`

Both arguments are optional.
Specifying a length in the arguments will skip over the length input process in the script and automatically copy your password to your clipboard.
Adding 's' will add symbols to the charset, if this argument is not added it will default to only letters and numbers.


Dependencies:  
CLI:  
pyperclip (pip3 install pyperclip) 

GUI:  
PyQt5 (pip3 install PyQt5)  
pyperclip (pip3 install pyperclip)
