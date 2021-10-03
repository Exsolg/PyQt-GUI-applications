from PyQt5.QtWidgets import QApplication, QMainWindow, QListWidgetItem
from Ui_diary import Ui_MainWindow
import sys


class Window(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Ежедневник")
        self.setFixedSize(self.width(), self.height())
        self.event_list = {}
        self.addButton.clicked.connect(self.addEvent)
        self.removeButton.clicked.connect(self.removeFromList)

    def addEvent(self):
        item = QListWidgetItem(
            f'{self.calendar.selectedDate().toString("yyyy.MM.dd")} {self.timer.time().toString()} - {self.event.text()}') 

        self.event_list.update({item.text(): {'desc': self.event.text(
        ), 'time': self.timer.time(), 'date': self.calendar.selectedDate()}})
        
        self.eventList.addItem(item)
        self.eventList.sortItems()


    def removeFromList(self):
        if self.event_list:
            item = self.eventList.takeItem(self.eventList.currentRow())
            del self.event_list[item.text()]
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Window()

    win.show()
    sys.exit(app.exec())
