import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QRadioButton, QButtonGroup

class Windowww(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My cool first GUI")
        self.setGeometry(700, 300, 500, 500)
        self.radio1 = QRadioButton("Visa", self) #we will add this radio button directly to our window. that would be 'self'
        self.radio2 = QRadioButton("Master", self)
        self.radio3 = QRadioButton("Gift Card", self)

        #with the default behavior of PyQt5 all radio buttons unless explicitly stated are all part of the same group
        #to demonstrate that let's create two additional radio buttons
        self.radio4 = QRadioButton("In-Store", self) #radio button 'button4' will be for a payment method rather then a payment type
        self.radio5 = QRadioButton("Online", self)

        #all radio buttons will be within the same button group. if I was to select in store, we deselect one of these options
        #what I would like is one option from this first group and another option from this other group
        self.button_group1 = QButtonGroup(self) #pass in 'self' to set the parent widget to be the 'window'
        self.button_group2 = QButtonGroup(self)

        self.initUI()

    def initUI(self):
        #we need to set the geometry of these radio buttons because we're not using a layout manager
        #to initialize user interface
        self.radio1.setGeometry(0, 0, 300, 50)
        self.radio2.setGeometry(0, 50, 300, 50)
        self.radio3.setGeometry(0, 100, 300, 50)
        self.radio4.setGeometry(0, 150, 300, 50)
        self.radio5.setGeometry(0, 200, 300, 50)

        #stylesheet
        #tricks with stylesheets

#we can apply multiple CSS like properties to an entire group of widgets, rather then having to type them and apply them indivually
        # we will add a selector. the selector is going to be the name of the widget

        self.setStyleSheet("QRadioButton{"
                           "font-size: 40px;"
                           "font-family: Arial;"
                           "padding: 10px;"
                           "}")

        self.button_group1.addButton(self.radio1)
        self.button_group1.addButton(self.radio2)
        self.button_group1.addButton(self.radio3)
        self.button_group2.addButton(self.radio4)
        self.button_group2.addButton(self.radio5)

        self.radio1.toggled.connect(self.radio_button_changed)
        self.radio2.toggled.connect(self.radio_button_changed)
        self.radio3.toggled.connect(self.radio_button_changed)
        self.radio4.toggled.connect(self.radio_button_changed)
        self.radio5.toggled.connect(self.radio_button_changed)


#for each radio button connect a signal to a slot
    def radio_button_changed(self):
#what we're going to need to do is get the sender widget which radio button send the signal of toggled

#I will create a local radio button, to store that radio button
        radio_button = self.sender()
#the sender method is going to return the widget that sent the signal

        if radio_button.isChecked(): #isChecked method will return a boolean
            print(f"{radio_button.text()} is selected")
#call the text method to return the text of the radio button


def main():
    app = QApplication(sys.argv)

    window = Windowww()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()


