import sys
from PyQt5.QtWidgets import (QMainWindow, QTextEdit,
    QAction, QFileDialog, QApplication, QPushButton, QLabel)
from PyQt5.QtGui import QIcon
import ker


class Example(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        #TODO добавить поля для ввода гиперпараметров и пути сохранения
        contentBtn = QPushButton('content', self)
        contentBtn.clicked.connect(self.showDialog)
        contentBtn.setToolTip('Select content image')
        contentBtn.resize(contentBtn.sizeHint())
        contentBtn.move(50, 50)

        self.contentLabel = QLabel(self)
        self.contentLabel.move(50, 70)
        self.contentLabel.setText('//content path//')

        styleBtn = QPushButton('style', self)
        styleBtn.clicked.connect(self.showDialog)
        styleBtn.setToolTip('Select style image')
        styleBtn.resize(styleBtn.sizeHint())
        styleBtn.move(50, 150)

        self.styleLabel = QLabel(self)
        self.styleLabel.move(50, 170)
        self.styleLabel.setText('//style path//')

        runBTn = QPushButton('RUN', self)
        runBTn.move(50, 250)
        runBTn.clicked.connect(self.run)

        self.setGeometry(300, 300, 650, 400)
        self.setWindowTitle('Style transfer')
        self.show()


    def showDialog(self):

        sender = self.sender()
        fname = QFileDialog.getOpenFileName(self, 'Open file', '/home')[0]
        if sender.text() == 'content':
            self.contentLabel.setText(fname)
            self.contentLabel.resize(self.contentLabel.sizeHint())
            # print(self.contentLabel.text())
        if sender.text() == 'style':
            self.styleLabel.setText(fname)
            self.styleLabel.resize(self.styleLabel.sizeHint())

    def run(self):
        ker.run_style_transfer(self.contentLabel.text(), self.styleLabel.text())


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
