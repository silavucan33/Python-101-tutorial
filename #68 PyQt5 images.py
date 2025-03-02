# PyQt5 images

#how to add images to PyQt5
import sys

from PyQt5.QtGui import QPixmap
#the class of 'QPixmap' it's used for handling images and provides functionality for loading, manipulating and displaying images
# (we will load our image to a 'QPixmap' object. then add this 'QPixmap' object to a label, in order to display it

# the most common and straightforward approach to displaying an image is to add an image to a label, in order to display it
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel


class Windowww(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(700, 300, 500, 500)

        label = QLabel(self) #'self' refers to the 'window' object. our 'window' will be the parent widget. our 'label' widget is one of its children
        label.setGeometry(0, 0, 250, 250)

        pixmap = QPixmap("profilepic1.jpg")
        #we don't see our image. we have to add the pixmap object to the label. we have to set it
        label.setPixmap(pixmap)

        #the image doesn't scale according the size of the label. to enable that we have to call folowing method
        label.setScaledContents(True)

        #TRICKS to do with positioning of the image

        label.setGeometry(0, 0, label.width(), label.height()) #??????? WHY. it's for to make it automatically and avoid to change manually; if you change it at the top. but we already have a label variable. so why we should do have one more??

        #so now our image is right justified within our window
        label.setGeometry(self.width() - label.width(),
                          0,
                          label.width(),
                          label.height())

        #for the bottom right corner
        label.setGeometry(self.width() - label.width(),
                          self.height() - label.height(),
                          label.width(),
                          label.height())

        #for the bottom left corner
        label.setGeometry(0,
                          self.height() - label.height(),
                          label.width(),
                          label.height())

        #to have our image placed in the center of our window
        label.setGeometry((self.width() - label.width()) // 2, #for integer division we'll be using double forward slashes. we need our pixels to be whole integers, so we're going to be using integer division and not standard division '/'
                          (self.height() - label.height()) // 2,
                          label.width(),
                          label.height())


def main():
    app = QApplication(sys.argv)

    window = Windowww()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
