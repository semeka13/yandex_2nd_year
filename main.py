import sys

from PyQt5 import uic  # Импортируем uic
from PyQt5.QtWidgets import QApplication, QMainWindow


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('qt.ui', self)  # Загружаем дизайн
        self.btn.clicked.connect(self.run)
        # Обратите внимание: имя элемента такое же как в QTDesigner

    def run(self):
        buttons = [self.coolor_1_blue,
                   self.coolor_1_green,
                   self.coolor_1_red,
                   self.coolor_2_blue,
                   self.coolor_2_green,
                   self.coolor_2_red,
                   self.coolor_3_blue,
                   self.coolor_3_green,
                   self.coolor_3_red]
        data = list()
        for b in buttons:
            if b.isChecked():
                data.append(b.text())
        self.output_label.resize(300, 40)
        self.output_label.setText(f"Итого: {', '.join(data)}", )


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())