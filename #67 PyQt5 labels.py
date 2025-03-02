# PyQt5 QLabels
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
#this label class is used to create label widgets that can display text or images
from PyQt5.QtGui import QFont
#to work with alignments
from PyQt5.QtCore import Qt

class Windowww(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My cool first GUI")
        self.setGeometry(700, 300, 500, 500)

        labell1 = QLabel("Hello", self) #self refers to 'window' object that we're calling and instantiating (window will be a parent widget)
        labell1.setFont(QFont("Arial", 30)) #pick a font and the second argument is a font size
        labell1.setGeometry(0, 0, 500, 100)
        #within this method we will pass in some CSS like properties such as a color. these CSS like properties should end with a semicolon
        #labell1.setStyleSheet("color: blue;")
        #you could also use RGB values or heximal values. you could always look up a color picker
        labell1.setStyleSheet("color: #8034eb;"
                              "background-color: #3474eb;"
                              "font-weight: bold;"
                              "font-style: italic;"
                              "text-decoration: underline;")
#to center the text of our label at the top vertically
        labell1.setAlignment(Qt.AlignTop)  # VERTICALLY TOP
        labell1.setAlignment(Qt.AlignBottom)  # VERTICALLY BOTTOM
        labell1.setAlignment(Qt.AlignVCenter)  # VERTICALLY CENTER

        labell1.setAlignment(Qt.AlignRight)  # HORIZONTALLY RIGHT
        labell1.setAlignment(Qt.AlignHCenter)  # HORIZONTALLY TOP
        labell1.setAlignment(Qt.AlignLeft)  # HORIZONTALLY LEFT
        #to combine both horizontal and vertical positioning

        labell1.setAlignment(Qt.AlignHCenter | Qt.AlignTop) # CENTER & TOP
                                        # '|'  or bitwise operator. this allows us to combine flags
        labell1.setAlignment(Qt.AlignHCenter | Qt.AlignBottom) # CENTER & BOTTOM
        #for the very center of our label
        labell1.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter) # CENTER & CENTER

        #there is a shortcut for the very center we don't need both of these flags
        labell1.setAlignment(Qt.AlignCenter) # CENTER & CENTER




def main():
    app = QApplication(sys.argv)

    window = Windowww()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
