from PySide6.QtWidgets import QWidget, QPushButton

class Button(QWidget):
    def __init__(self, text, callback):
        button = QPushButton(text)
        button.clicked.connect(callback)