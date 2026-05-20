import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QColorDialog, QFileDialog
from PySide6.QtGui import QPainter, QPen, QPixmap
from PySide6.QtCore import Qt, QPoint

class DrawingArea(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = 'Aplikacja do rysowania'
        self.drawing = False
        self.last_point = QPoint()
        self.pen_color = Qt.black
        self.canvas = QPixmap(512, 384)
        self.canvas.fill(Qt.white)

        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(128, 96, 512, 384)
        self.save_button = QPushButton('Save', self)
        self.save_button.move(16, 16)
        self.save_button.clicked.connect(self.save)
        self.color_button = QPushButton('Color', self)
        self.color_button.move(64, 16)
        self.color_button.clicked.connect(self.select_color)
        self.show()

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.drawing = True
            self.last_point = event.pos()

    def mouseMoveEvent(self, event):
        if event.buttons() & Qt.LeftButton and self.drawing:
            painter = QPainter(self.canvas)
            pen = QPen(self.pen_color, 2, Qt.SolidLine)
            painter.setPen(pen)
            painter.drawLine(self.last_point, event.pos())
            self.last_point = event.pos()
            self.update()

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.drawing = False

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.drawPixmap(self.rect(), self.canvas)

    def select_color(self):
        self.pen_color = QColorDialog.getColor()

    def save(self):
        file_path, _ = QFileDialog.getSaveFileName(self, 'Save image', '', 'PNG(*.png);;JPEG(*.jpg *.jpeg);;All Files(*.*)')
        if file_path == '':
            return
        self.canvas.save(file_path)

def main():
    app = QApplication(sys.argv)
    window = DrawingArea()
    window.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()
