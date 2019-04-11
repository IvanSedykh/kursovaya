import sys
from PyQt5.QtWidgets import (QMainWindow, QTextEdit,
    QAction, QFileDialog, QApplication, QPushButton, QLabel, QLineEdit)
from PyQt5.QtGui import QIcon
import ker


class Example(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        # TODO отображение картинок и редизайн
        contentBtn = QPushButton('select content', self)
        contentBtn.clicked.connect(self.choosePicture)
        contentBtn.setToolTip('Select content image')
        contentBtn.resize(contentBtn.sizeHint())
        contentBtn.move(50, 50)

        self.contentLabel = QLabel(self)
        self.contentLabel.setText('//content path//')
        self.contentLabel.move(50, 70)

        self.content_weightLine = QLineEdit(self)
        self.content_weightLine.setText('1.0')
        self.content_weightLine.setToolTip('content picture weight\n1.0 - 0.001 recommended')
        self.content_weightLine.resize(60, 17)
        self.content_weightLine.move(50, 95)

        styleBtn = QPushButton('select style', self)
        styleBtn.clicked.connect(self.choosePicture)
        styleBtn.setToolTip('Select style image')
        styleBtn.resize(styleBtn.sizeHint())
        styleBtn.move(50, 150)

        self.styleLabel = QLabel(self)
        self.styleLabel.setText('//style path//')
        self.styleLabel.move(50, 170)

        self.style_weightLine = QLineEdit(self)
        self.style_weightLine.setText('1.0')
        self.style_weightLine.setToolTip('style picture weight\n1.0 - 0.001 recommended')
        self.style_weightLine.resize(60, 17)
        self.style_weightLine.move(50, 195)

        self.prefixBtn = QPushButton('result directory', self)
        self.prefixBtn.move(200, 150)
        self.prefixBtn.clicked.connect(self.choosePath)

        self.prefixLabel = QLabel(self)
        self.prefixLabel.setText('//saving path//')
        self.prefixLabel.move(200, 175)



        self.iter_numLine = QLineEdit(self)
        self.iter_numLine.setText('10')
        self.iter_numLine.setToolTip('number of iterations')
        self.iter_numLine.resize(40, 17)
        self.iter_numLine.move(50, 230)

        runBTn = QPushButton('RUN', self)
        runBTn.move(50, 250)
        runBTn.clicked.connect(self.run)

        self.setGeometry(300, 300, 650, 400)
        self.setWindowTitle('Style transfer')
        self.show()


    def choosePicture(self):

        sender = self.sender()
        fname = QFileDialog.getOpenFileName(self, 'Open file', '/home')[0]
        if sender.text() == 'select content':
            self.contentLabel.setText(fname)
            self.contentLabel.resize(self.contentLabel.sizeHint())
        if sender.text() == 'select style':
            self.styleLabel.setText(fname)
            self.styleLabel.resize(self.styleLabel.sizeHint())

    def choosePath(self):
        dirname = QFileDialog.getExistingDirectory(self, '/home')
        self.prefixLabel.setText(dirname)
        self.prefixLabel.resize(self.prefixLabel.sizeHint())

    def run(self):
        # TODO сделать поле для ввода имени результата
        prefix = self.prefixLabel.text() + '/result'
        ker.run_style_transfer(self.contentLabel.text(),
                               self.styleLabel.text(),
                               float(self.content_weightLine.text()),
                               float(self.style_weightLine.text()),
                               int(self.iter_numLine.text()),
                               prefix
                               )


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
