import sys, time
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel


class MainWindowww(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My cool first GUI")
        self.setGeometry(700, 300, 500, 500)

        #when we click on our button let's change the the text of a label
        self.label = QLabel("Hello", self)
        self.initUI()

    def initUI(self):
        self.button = QPushButton("Click me!", self) #self refers to our 'window' object
        self.button.setGeometry(150, 200, 200, 100) #we could use a layout manager. but to keep simple i don't.
        self.button.setStyleSheet("font-size: 30px;") #we could use QFont but that might be overkill for this demonstration

        #set up a signal and slot for the button     signal.connect(slot)
        self.button.clicked.connect(self.on_click) #list the type of signal. so, the signal we're looking for is 'clicked'
        # 'connect' is a method
        #when we press this button we perform this slot this method of 'on_click'

        self.label.setGeometry(150, 300, 200, 100)
        self.label.setStyleSheet("font-size: 50px;")

    #connecting our button to a function
    def on_click(self, denemee):
        print("Button clicked!")
        self.button.setText("Clicked!")

    #to disable buttons when we click on them
        self.button.setDisabled(True) #call the 'setDisabled' method
        self.label.setText("Goodbye!")


    #normally when we creating widgets we would want to prefix that widget with self, then follow the name of the widget
    #imagine what happens when we don't do that. because without 'self' we're declaring a local variable

    #'button' is considered local to our 'initUI' method. our 'on_click' function doesn't recognize what our 'button' is.
    #That's why we're going to prefix our 'button' with 'self', so it's belongs to the class of 'MainWindowww' and not this 'initUI' method
    #any instance of 'button' we're going to prefix with 'self'



def main():
    app = QApplication(sys.argv)

    window = MainWindowww()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
