# PyQt5 introduction    # GUI = Graphical User Interface

#import sys
#this module provides access to some variables used or maintained by the interpreter and to functions that interact strongly with the interpreter. It is always available

#from PyQt5.QtWidgets import QApplication, QMainWindow
#widgets are the building blocks of a PyQt5 application
#they begin with Q. that helps distinguish them from widgets from other libraries

#class MainWindow(QMainWindow):
#    def __init__(self):
#        super().__init__()

#def main():
#    app = QApplication(sys.argv) #by passing in this argument this allows PyQt to process any command line arguments intended for it. that's if we use command prompt or terminal
                                 #otherwise you may see people pass in an empty list; '([])'
#    window = MainWindow()
#    window.show() #it pops up for a brief second. we need to ensure that the window stays until we interact with it or close it
#    sys.exit(app.exec_()) #the exit method ensures a clean exit of our program
    #.exec() is used for older code bases
    #our app.exec_() method it waits around for user input and handles events such as if we click buttons, press keys or close the window

#if __name__ == "__main__":
#    main()

#that's all the boilerplate code that we need for a basic window
#let's customize it

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
#in order to work with icons
from PyQt5.QtGui import QIcon

class Windowww(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My cool first GUI")
        self.setGeometry(700, 300, 500, 500) #there 4 arguments (x, y, width, height)
        self.setWindowIcon(QIcon("profilepic1.jpg")) #we'll pass in either a relative file path or an absolute file path


def main():
    app = QApplication(sys.argv)

    window = Windowww()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()

