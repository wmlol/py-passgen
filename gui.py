import sys
import string
import symbol
import random
import pyperclip
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog

class App(QWidget):
    def __init__(self):
        super().__init__()
        length, okPressed = QInputDialog.getInt(self, "password length","password length:", 16, 1, 64, 1)
        if okPressed and length:
            pyperclip.copy(''.join(random.choice(string.ascii_letters + string.digits + string.punctuation) for i in range(length)))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())