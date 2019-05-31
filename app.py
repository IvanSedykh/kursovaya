import sys
from PyQt5 import QtWidgets
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtCore import Qt
import transfer
import design


class App(QtWidgets.QMainWindow, design.Ui_MainWindow):
	def __init__(self):
		super().__init__()
		self.setupUi(self)
		# connecting actions to buttons
		self.contentBtn.clicked.connect(self.choosePicture)
		self.styleBtn.clicked.connect(self.choosePicture)
		self.prefixBtn.clicked.connect(self.choosePath)
		self.runBTn.clicked.connect(self.run)


	def choosePicture(self):
		"""
		тупа открывает проводник и сохрнаяет имена выбранных картинок
		и отображает миниатюры
		"""
		sender = self.sender()
		fname = QtWidgets.QFileDialog.getOpenFileName(self, 'Open file', 'C:/Users/ivan/PycharmProjects/kursovaya/data')[0]
		if sender.text() == 'select content':
			self.contentLabel.setText(fname)

			# честно хз как это работает но оно делает миниатюру
			pixmap = QPixmap(fname)
			self.content_imageLabel.setPixmap(pixmap.scaled(200, 200, Qt.KeepAspectRatio))
			self.content_imageLabel.resize(150, 150)
		if sender.text() == 'select style':
			self.styleLabel.setText(fname)

			pixmap = QPixmap(fname)
			self.style_imageLabel.setPixmap(pixmap.scaled(200, 200, Qt.KeepAspectRatio))
			self.style_imageLabel.resize(150, 150)

	def choosePath(self):
		"""
		тупа открывает проводник для выбора директории результата
		"""
		dirname = QtWidgets.QFileDialog.getExistingDirectory(self,
		                                           'C:/Users/ivan/PycharmProjects/kursovaya/transfered_imgs/trash')
		self.prefixLabel.setText(dirname)

	def run(self):

		prefix = self.prefixLabel.text() + '/' + self.result_nameLine.text()
		try:
			transfer.run_style_transfer(
				self.contentLabel.text(),
				self.styleLabel.text(),
				float(self.content_weightLine.text()),
				float(self.style_weightLine.text()),
				int(self.maxLenghtLine.text()),
				int(self.iter_numLine.text()),
				prefix
			)
		except FileNotFoundError:
			print('ERROR, check paths')


def main():
	app = QtWidgets.QApplication(sys.argv)
	window = App()
	window.show()
	app.exec_()


if __name__ == '__main__':
	main()
