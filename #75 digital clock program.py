# Python PyQt5 Digital Clock
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt5.QtCore import QTimer, QTime, Qt
from PyQt5.QtGui import QFont, QFontDatabase

class DigitalClock(QWidget): #instead of inheriting from the main window widget we will inherit from the base class of 'QWidget'
    def __init__(self):
        super().__init__() #if there are any arguments to send to the parent we will call the constructor of the parent; the 'super' class
        self.time_label = QLabel("12:00:00", self)
        self.timer = QTimer(self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Digital Clock")
        self.setGeometry(600, 400, 300, 100)

        vbox = QVBoxLayout()
        vbox.addWidget(self.time_label)
        self.setLayout(vbox)

        self.time_label.setAlignment(Qt.AlignCenter)

        self.time_label.setStyleSheet("font-size: 150px;"
                                      "color: hsl(274, 54%, 43%)")
        self.setStyleSheet("background-color: gray;")

        #if you would like to download a custom font
        font_id = QFontDatabase.addApplicationFont("DS-DIGI.TTF")
#QFontDatabase is a class for managing and querying fonts available to the application

        font_family = QFontDatabase.applicationFontFamilies(font_id)[0]
#we're going to use index of operator and get the index of zero. this will retrieve the first element of the font family, that's because we're working with the list.
#we will need just the first element at index zero
        my_font = QFont(font_family, 150)
        self.time_label.setFont(my_font)


        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000) #every 1000 millisecond, every second


        self.update_time()



    def update_time(self):
        current_time = QTime.currentTime().toString("hh:mm:ss")
        self.time_label.setText(current_time)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    clock = DigitalClock()
    clock.show()
    sys.exit(app.exec_())

