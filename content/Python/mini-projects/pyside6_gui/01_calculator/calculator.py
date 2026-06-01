import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget, QGridLayout
from PySide6.QtCore import Qt
from PySide6.QtGui import QShortcut, QKeySequence

class CalculatorWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Calculator')
        self.initUI() 

    def initUI(self):
        self.mainLayout = QVBoxLayout()
        self.central_widget = QWidget()
        self.central_widget.setLayout(self.mainLayout)
        self.setCentralWidget(self.central_widget)

        self.display = QLabel('0') 
        self.display.setStyleSheet('border: 1px solid black; padding: 10px;') 
        self.display.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.mainLayout.addWidget(self.display) 

        self.buttonsLayout = QGridLayout() 
        buttonsGrid = [
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['C', '0', '=', '+']
        ]
        self.createButtonsGrid(buttonsGrid)
        self.mainLayout.addLayout(self.buttonsLayout)

    def setButtonWidgetShortcuts(self, buttonWidget: QPushButton, keySequence: list[QKeySequence]):
        for key in keySequence:
            shortcut = QShortcut(key, self)
            shortcut.activated.connect(buttonWidget.animateClick)

    def createButtonsGrid(self, buttonsGrid):
        row, column = 0, 0
        while row < len(buttonsGrid):
            buttonRow = buttonsGrid[row]
            while column < len(buttonRow):
                button = buttonRow[column]
                buttonWidget = QPushButton(button, default=False)
                if button == '=':
                    self.setButtonWidgetShortcuts(buttonWidget, [QKeySequence(Qt.Key.Key_Return), QKeySequence(Qt.Key.Key_Space)])
                if button == 'C':
                    self.setButtonWidgetShortcuts(buttonWidget, [QKeySequence(Qt.Key.Key_Delete),])
                buttonWidget.setShortcut(button)
                buttonWidget.clicked.connect(self.onButtonClick)
                self.buttonsLayout.addWidget(buttonWidget, row, column)
                column+=1
            else:
                column = 0           
            row+=1

    def onButtonClick(self):
        senderText = self.sender().text()
        displayText = self.display.text()
        if senderText == 'C':
            self.display.setText('0')
        elif senderText == '=':
            self.calculate()
        else:
            if displayText == '0' or 'Error' in displayText:
                self.display.setText(senderText)
            else:
                self.display.setText(displayText + senderText)
    
    def calculate(self):
        if 'Error' in self.display.text():
            self.display.setText('0')
        try:
            result = str(eval(self.display.text()))
            self.display.setText(result)
        except Exception as e:
            self.display.setText(f'Error: {e}')
                
def main():
    app = QApplication(sys.argv)
    window = CalculatorWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()
