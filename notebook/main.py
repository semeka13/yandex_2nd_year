import sys

from PyQt5 import uic  # Импортируем uic
from PyQt5.QtWidgets import QApplication, QMainWindow


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('notebook_qt.ui', self)  # Загружаем дизайн
        self.add_btn.clicked.connect(self.run)
        # Обратите внимание: имя элемента такое же как в QTDesigner

    def run(self):
        name = self.name.text()
        tel = self.tel.text()
        prev_text = f"{name} {tel}"
        self.output.addItem(prev_text)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())