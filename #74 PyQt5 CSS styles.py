#PyQt5 setStyleSheet()
#CSS = Cascading Style Sheets

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget, QHBoxLayout


class Windowww(QMainWindow):
    def __init__(self):
        super().__init__()
        self.button1 = QPushButton("#1") #since we're using a layout manager we don't need to add this button to self our window; ("#1", self)
        self.button2 = QPushButton("#2")
        self.button3 = QPushButton("#3")
        self.initUI()

#under normal circumstances we can't add a layout manager to our main window. with main window widgets there's already a specified layout and format. we're going to add a layout manager to a central widget(QWidget) and this widget will be added to the main window

    def initUI(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget) #'self' means our 'window'

        hbox = QHBoxLayout()

        hbox.addWidget(self.button1)
        hbox.addWidget(self.button2)
        hbox.addWidget(self.button3)

        central_widget.setLayout(hbox)

       #apply some CSS like styling

# what if you would like to apply CSS properties to only one widget rather than all of that
        self.button1.setObjectName("button1")
        self.button2.setObjectName("button2")
        self.button3.setObjectName("button3")

        #rather then apply the CSS properties individually
        #self.button1.setStyleSheet("")

#we are instead going to set the stylesheet of our 'window'
#we're going to use triple quotes. triple quotes are used to write very long strings in a more organized way
        self.setStyleSheet("""
            QPushButton{
                font-size: 40px; 
                font-family: Arial;
                padding: 15px 75px;
                margin: 25px;
                border: 3px solid;
                border-radius: 15px;  
            }
            QPushButton#button1{
                background-color: hsl(44, 98%, 50%);
            }
            QPushButton#button2{
                background-color: hsl(336, 98%, 50%);
            }
            QPushButton#button3{
                background-color: hsl(210, 98%, 50%);
            }
            
            
             QPushButton#button1:hover{
                background-color: hsl(44, 98%, 70%);
            }
            QPushButton#button2:hover{
                background-color: hsl(336, 98%, 70%);
            }
            QPushButton#button3:hover{
                background-color: hsl(210, 98%, 70%);
            }
            """) #be sure to end each CSS property with a semicolon
#1.by 'hsl' delete the degree symbol if there is some . by using hsl for color, you can also control the saturation and the lightness
#2.apply pseudo classes, such as when we hover over one of the buttons

#we could indivually apply CSS like properties to each of these widgets, but we could select an entire class of widgets too



def main():
    app = QApplication(sys.argv)

    window = Windowww()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
