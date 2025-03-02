# PyQt5 LineEdit
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QPushButton


class Windowww(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(700, 300, 500, 500)
        self.line_edit = QLineEdit(self) #accessing our 'window' of 'self'
        self.button = QPushButton("Submit", self)
        self.initUI()

    def initUI(self):
        self.line_edit.setGeometry(10, 10, 200, 40)
        self.button.setGeometry(210, 10, 100, 40)
        self.line_edit.setStyleSheet("font-size: 25px;"  #we can pass in some CSS like properties, including font size
                                     "font-family: Arial")
        self.button.setStyleSheet("font-size: 25px;"
                                  "font-family: Arial")

        #add some placeholder text
        self.line_edit.setPlaceholderText("Enter your name")

        self.button.clicked.connect(self.submit)

    def submit(self):
#let's create a local variable of text
        text = self.line_edit.text()
        print(f"Hello {text}")


def main():
    app = QApplication(sys.argv)

    window = Windowww()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()

#line edit widgets (also commonly referred to as textboxes)
