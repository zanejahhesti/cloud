from PyQt5.QtCore import QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWidgets import QApplication, QVBoxLayout, QWidget

app = QApplication([])

webview = QWebEngineView()
webview.load(QUrl("https://www.google.com"))

layout = QVBoxLayout()
layout.addWidget(webview)

main_widget = QWidget()
main_widget.setLayout(layout)
main_widget.show()

app.exec_()
