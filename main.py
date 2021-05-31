import scanner as sc
import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5.uic import loadUi


class Compiler(QDialog):
    def __init__(self):
        super(Compiler, self).__init__()
        loadUi('mainscreen.ui', self)
        self.compile_button.clicked.connect(self.show_compilation)

    def show_compilation(self):
        my_scanner = sc.Scanner()
        tiny_code = self.code_editor_plaintext.toPlainText()
        my_scanner.scan(tiny_code)
        my_scanner.output()
        output_message = my_scanner.print_output()
        self.output_textbrowser.clear()
        self.output_textbrowser.setPlainText(output_message)


app = QApplication(sys.argv)
main_window = Compiler()
widget = QtWidgets.QStackedWidget()
widget.addWidget(main_window)
widget.show()
widget.setFixedWidth(1024)
widget.setFixedHeight(620)
app.exec_()
