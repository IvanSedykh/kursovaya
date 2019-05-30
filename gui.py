import sys
from PyQt5.QtWidgets import (QMainWindow,
                             QFileDialog, QApplication, QPushButton, QLabel, QLineEdit, QProgressBar)
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtCore import Qt
import ker

class App(QMainWindow):

	def __init__(self):
		super().__init__()

		self.initUI()

	def initUI(self):
		# TODO редизайн

		# select content image
		self.contentBtn = QPushButton('select content', self)
		self.contentBtn.clicked.connect(self.choosePicture)
		self.contentBtn.setToolTip('Select content image')
		self.contentBtn.resize(self.contentBtn.sizeHint())
		self.contentBtn.move(50, 50)

		# show content name
		self.contentLabel = QLabel(self)
		self.contentLabel.setText('//content path//')
		self.contentLabel.move(50, 70)

		# show content image
		self.content_imageLabel = QLabel(self)
		self.content_imageLabel.move(400, 200)

		# input content weight
		self.content_weightLine = QLineEdit(self)
		self.content_weightLine.setText('1.0')
		self.content_weightLine.setToolTip('content picture weight\n1.0 - 0.001 recommended')
		self.content_weightLine.resize(60, 17)
		self.content_weightLine.move(50, 95)

		# show style image
		self.style_imageLabel = QLabel(self)
		self.style_imageLabel.move(400, 400)

		# select style image
		self.styleBtn = QPushButton('select style', self)
		self.styleBtn.clicked.connect(self.choosePicture)
		self.styleBtn.setToolTip('Select style image')
		self.styleBtn.resize(self.styleBtn.sizeHint())
		self.styleBtn.move(50, 150)

		# show style image name
		self.styleLabel = QLabel(self)
		self.styleLabel.setText('//style path//')
		self.styleLabel.move(50, 170)

		# input style weight
		self.style_weightLine = QLineEdit(self)
		self.style_weightLine.setText('1.0')
		self.style_weightLine.setToolTip('style picture weight\n1.0 - 0.001 recommended')
		self.style_weightLine.resize(60, 17)
		self.style_weightLine.move(50, 195)

		# select the result directory
		self.prefixBtn = QPushButton('result directory', self)
		self.prefixBtn.setToolTip('directory to save result where')
		self.prefixBtn.move(200, 150)
		self.prefixBtn.clicked.connect(self.choosePath)

		# show the result directory
		self.prefixLabel = QLabel(self)
		self.prefixLabel.setText('//saving path//')
		self.prefixLabel.move(200, 175)

		# input result file name
		self.result_nameLine = QLineEdit(self)
		self.result_nameLine.setToolTip('result file name')
		self.result_nameLine.setText('result')
		self.result_nameLine.resize(100, 20)
		self.result_nameLine.move(200, 200)

		# input number of iterations
		self.iter_numLine = QLineEdit(self)
		self.iter_numLine.setText('10')
		self.iter_numLine.setToolTip('number of iterations')
		self.iter_numLine.resize(40, 17)
		self.iter_numLine.move(50, 230)

		# progress-bar vpizdu ego
		# self.progressBar = QProgressBar(self, )
		# self.progressBar.resize(200, 30)
		# self.progressBar.move(50, 290)

		# run button
		self.runBTn = QPushButton('RUN', self)
		self.runBTn.move(50, 250)
		self.runBTn.clicked.connect(self.run)

		# window settings
		self.setGeometry(300, 300, 750, 500)
		self.setWindowTitle('Style transfer')
		icon_path = 'C:/Users/ivan/PycharmProjects/kursovaya/data/hotline.png'
		self.setWindowIcon(QIcon(icon_path))
		self.show()

	def choosePicture(self):
		"""
		тупа открывает проводник и сохрнаяет имена выбранных картинок
		и отображает миниатюры
		"""
		sender = self.sender()
		fname = QFileDialog.getOpenFileName(self, 'Open file', 'C:/Users/ivan/PycharmProjects/kursovaya/data')[0]
		if sender.text() == 'select content':
			self.contentLabel.setText(fname)
			self.contentLabel.resize(self.contentLabel.sizeHint())

			# честно хз как это работает но оно делает миниатюру
			pixmap = QPixmap(fname)
			self.content_imageLabel.setPixmap(pixmap.scaled(150, 150, Qt.KeepAspectRatio))
			self.content_imageLabel.resize(150, 150)
		if sender.text() == 'select style':
			self.styleLabel.setText(fname)
			self.styleLabel.resize(self.styleLabel.sizeHint())

			pixmap = QPixmap(fname)
			self.style_imageLabel.setPixmap(pixmap.scaled(150, 150, Qt.KeepAspectRatio))
			self.style_imageLabel.resize(150, 150)

	def choosePath(self):
		"""
		тупа открывает проводник для выбора директории результата
		"""
		dirname = QFileDialog.getExistingDirectory(self, 'C:/Users/ivan/PycharmProjects/kursovaya/transfered_imgs/trash')
		self.prefixLabel.setText(dirname)
		self.prefixLabel.resize(200, 20)

	def run(self):
		# TODO сделать try except
		# todo progress-bar

		prefix = self.prefixLabel.text() + '/' + self.result_nameLine.text()
		try:
			ker.run_style_transfer(
		    self.contentLabel.text(),
			self.styleLabel.text(),
			float(self.content_weightLine.text()),
			float(self.style_weightLine.text()),
			int(self.iter_numLine.text()),
			prefix
			)
		except FileNotFoundError:
			print('ERROR, check paths')


if __name__ == '__main__':
	app = QApplication(sys.argv)
	ex = App()
	sys.exit(app.exec_())
