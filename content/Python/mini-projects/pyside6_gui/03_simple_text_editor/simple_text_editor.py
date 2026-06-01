import sys, os
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget, QMessageBox, QListWidget, QTextEdit, QFileDialog, QToolBar
from PySide6.QtGui import QAction

os.chdir(os.path.dirname(__file__)) 

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('My first App')
        self.resize(768, 512)

        self.text_edit = QTextEdit()
        self.setCentralWidget(self.text_edit)

        self.toolbar = QToolBar('Main tools')
        self.addToolBar(self.toolbar)

        open_action = QAction('Open', self)
        open_action.triggered.connect(self.open_file)
        self.toolbar.addAction(open_action)

        save_action = QAction('Save', self)
        save_action.triggered.connect(self.save_file)
        self.toolbar.addAction(save_action)

    def open_file(self):
        file_path, _ = QFileDialog.getOpenFileName(self, 'Open file', '', 'Text files (*.txt);; All files (*)')
        if file_path:
            with open(file_path, 'r') as file:
                content = file.read()
                self.text_edit.setText(content)
                file.close()

    def save_file(self):
        file_path, _ = QFileDialog.getSaveFileName(self, 'Save file', '', 'Text files (*.txt);; All files (*)')
        if file_path:
            with open(file_path, 'w') as file:
                content = self.text_edit.toPlainText()
                file.write(content)
                file.close()

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()
