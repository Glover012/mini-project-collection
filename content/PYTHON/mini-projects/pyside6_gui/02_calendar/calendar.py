import sys
from PySide6.QtWidgets import QApplication, QWidget, QGridLayout, QLabel, QPushButton, QVBoxLayout
from PySide6.QtCore import QDate, QLocale
from PySide6.QtGui import QFont

class CalendarApp(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(512, 384)
        self.current_date = QDate.currentDate() 
        self.initializeUI() 
        self.show() 

    def initializeUI(self):
        self.layout = QVBoxLayout()
        self.grid_layout = QGridLayout()
        self.layout.addLayout(self.grid_layout)
        self.setLayout(self.layout)

        prev_button = QPushButton('< Previous')
        prev_button.clicked.connect(self.showPreviousMonth)
        next_button = QPushButton('Next >')
        next_button.clicked.connect(self.showNextMonth)

        self.layout.addWidget(prev_button)
        self.layout.addWidget(next_button)

        self.showCalendar(self.current_date.year(), self.current_date.month())

    def showCalendar(self, year, month):
        locale = QLocale(QLocale.Polish)
        month_name = locale.monthName(month)
        self.setWindowTitle(f'Calender: {month_name} {year}')

        for i in reversed(range(self.grid_layout.count())):
            widget = self.grid_layout.itemAt(i).widget()
            widget.deleteLater()

        days_of_week = ['Pon', 'Wt', 'Śr', 'Czw', 'Pt', 'Sob', 'Niedz']
        for i, day in enumerate(days_of_week):
            self.grid_layout.addWidget(QLabel(day), 0, i)

        first_day_of_month = QDate(year, month, 1)
        offset = first_day_of_month.dayOfWeek()-1

        for day in range(1, first_day_of_month.daysInMonth()+1):
            day_date = QDate(year, month, day)
            day_label = QLabel(str(day))
            if day_date == QDate.currentDate():
                day_label.setStyleSheet('color:red;')
                font = day_label.font()
                font.setBold(True)
                day_label.setFont(font)
            self.grid_layout.addWidget(day_label,
                                       (day + offset - 1) // 7 + 1,
                                       (day + offset - 1) % 7)

    def showPreviousMonth(self):
        self.current_date = self.current_date.addMonths(-1)
        self.showCalendar(self.current_date.year(), self.current_date.month())

    def showNextMonth(self):
        self.current_date = self.current_date.addMonths(1)
        self.showCalendar(self.current_date.year(), self.current_date.month())

def main():
    app = QApplication(sys.argv)
    window = CalendarApp()
    window.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()
