# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainscreen.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import scanner as sc

class Ui_compilerQDialog(object):
    def setupUi(self, compilerQDialog):
        compilerQDialog.setObjectName("compilerQDialog")
        compilerQDialog.resize(1024, 620)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(compilerQDialog.sizePolicy().hasHeightForWidth())
        compilerQDialog.setSizePolicy(sizePolicy)
        compilerQDialog.setStyleSheet("")
        self.horizontalLayoutWidget = QtWidgets.QWidget(compilerQDialog)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 1021, 80))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(320, 0, 320, 0)
        self.horizontalLayout.setSpacing(15)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.compile_button = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.compile_button.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";")
        self.compile_button.setObjectName("compile_button")
        self.horizontalLayout.addWidget(self.compile_button)
        self.verticalLayoutWidget = QtWidgets.QWidget(compilerQDialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 80, 1021, 381))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 15, 0, 15)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.code_editor_plaintext = QtWidgets.QPlainTextEdit(self.verticalLayoutWidget)
        self.code_editor_plaintext.setEnabled(True)
        self.code_editor_plaintext.setStyleSheet("font: 75 10pt \"Nirmala UI\";\n"
                                                 "font-weight: normal;\n"
                                                 "color: rgb(0, 0, 0);\n"
                                                 "")
        self.code_editor_plaintext.setObjectName("code_editor_plaintext")
        self.verticalLayout.addWidget(self.code_editor_plaintext)
        self.gridLayoutWidget = QtWidgets.QWidget(compilerQDialog)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 460, 1021, 161))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(4)
        self.gridLayout.setObjectName("gridLayout")
        self.output_textbrowser = QtWidgets.QTextBrowser(self.gridLayoutWidget)
        self.output_textbrowser.setStyleSheet("color: rgb(57, 57, 57);")
        self.output_textbrowser.setAcceptRichText(True)
        self.output_textbrowser.setSource(QtCore.QUrl("http://output.txt"))
        self.output_textbrowser.setObjectName("output_textbrowser")
        self.gridLayout.addWidget(self.output_textbrowser, 0, 0, 1, 1)
        self.compile_button.clicked.connect(self.show_compilation)

        self.retranslateUi(compilerQDialog)
        QtCore.QMetaObject.connectSlotsByName(compilerQDialog)

    def show_compilation(self):
        my_scanner = sc.Scanner()
        tiny_code = self.code_editor_plaintext.toPlainText()
        my_scanner.scan(tiny_code)
        my_scanner.output()
        output_message = my_scanner.print_output()
        self.output_textbrowser.clear()
        self.output_textbrowser.setPlainText(output_message)

    def retranslateUi(self, compilerQDialog):
        _translate = QtCore.QCoreApplication.translate
        compilerQDialog.setWindowTitle(_translate("compilerQDialog", "TINY Compiler"))
        self.compile_button.setToolTip(_translate("compilerQDialog",
                                                  "<html><head/><body><p><span style=\" font-size:10pt; font-style:italic;\">Execute TINY code</span></p></body></html>"))
        self.compile_button.setWhatsThis(_translate("compilerQDialog",
                                                    "<html><head/><body><p><span style=\" font-size:10pt; font-style:italic;\">Execute TINY code</span></p></body></html>"))
        self.compile_button.setText(_translate("compilerQDialog", "Compile"))
        self.code_editor_plaintext.setToolTip(_translate("compilerQDialog",
                                                         "<html><head/><body><p><span style=\" font-size:10pt; font-weight:400; font-style:italic;\">TINY code editor</span></p></body></html>"))
        self.code_editor_plaintext.setWhatsThis(_translate("compilerQDialog",
                                                           "<html><head/><body><p><span style=\" font-size:10pt; font-weight:400; font-style:italic;\">TINY code editor</span></p></body></html>"))
        self.code_editor_plaintext.setPlainText(_translate("compilerQDialog", "int x; \n"
                                                                              "if x > 0 then {don’t compute if x <= 0 }\n"
                                                                              "fact := 1;\n"
                                                                              "repeat \n"
                                                                              "fact:= fact * x;\n"
                                                                              "x := x –1; \n"
                                                                              "until x = 0 write fact; end"))
        self.output_textbrowser.setToolTip(_translate("compilerQDialog",
                                                      "<html><head/><body><p><span style=\" font-size:10pt; font-style:italic;\">Output screen</span></p></body></html>"))
        self.output_textbrowser.setWhatsThis(_translate("compilerQDialog",
                                                        "<html><head/><body><p><span style=\" font-size:10pt; font-style:italic;\">Output screen</span></p></body></html>"))
        self.output_textbrowser.setHtml(_translate("compilerQDialog",
                                                   "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                   "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                   "p, li { white-space: pre-wrap; }\n"
                                                   "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                                                   "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    compilerQDialog = QtWidgets.QDialog()
    ui = Ui_compilerQDialog()
    ui.setupUi(compilerQDialog)
    compilerQDialog.show()
    sys.exit(app.exec_())
