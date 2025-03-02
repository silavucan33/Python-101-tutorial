# PyQt5 Checkboxes
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QCheckBox
#to work with different states we will also need the following import,
from PyQt5.QtCore import Qt #this module of QTCore, it contains non-gooey classes relevant to PyQt5 applications


class Windowww(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My cool first GUI")
        self.setGeometry(700, 300, 500, 500)

        #to create a checkbox
        self.checkbox = QCheckBox("Do you like food?", self) #the second argument is the parent widget, where we will be adding this checkbox. self will apply to 'window'
        self.initUI()

    def initUI(self):
        #method to initialize the user interface
        self.checkbox.setStyleSheet("font-size: 30px;"
                                    "font-family: Arial;")
        #and we should change the geometry of the label it's getting cut off
        self.checkbox.setGeometry(10, 0, 500, 100)

        #our checkbox has an initial state. it's normally unchecked, that's the default behavior
        #but we could set that to be checked with the following method when the window loads
        #self.checkbox.setChecked(True)
        self.checkbox.setChecked(False)

        # checkbox.*signal*.connect(*slot*)
        # we'll take our checkbox connect a signal to a slot. the slot can be a function or a method
        self.checkbox.stateChanged.connect(self.checkbox_changed)


#we will call this method when the state of our checkbox changes
    def checkbox_changed(self, stateee):
        #now when I uncheck it I instead would like to display you do not like food
        #so that's where our stateee is going to come in
        #print(stateee)    when I'm printing our state, our state is going to be a value
        #when we check the checkbox our stateee has a value of '2'. when we uncheck it, it has a value of '0'
        # 0 means unchecked. 2 means checked   (there' also one for partially checked, but that's not going to be relevant to this topic)

#       if stateee == 2:
#          print("You like food")

        #instead (for more readability)
        if stateee == Qt.Check: #accesss the class of 'Qt'. there's an built-in constant of 'Checked'
        #it's also equals '2', but it's more readable. it's a constant
            print("You like food")
        else:
            print("You DO NOT like food")

def main():
    app = QApplication(sys.argv)

    window = Windowww()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
