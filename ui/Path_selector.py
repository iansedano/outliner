from PySide6.QtWidgets import QWidget, QFileDialog, QLabel, QLineEdit, QHBoxLayout, QPushButton


class Path_selector(QWidget):
    def __init__(self, type):
        super().__init__()
        
        if not (type == 'file' or type == 'folder'):
            raise Exception("invalid type when initializing Path_selector class instance")
        
        self.type = type
        
        self.label = QLabel(f"Select a {type}", self)
        self.input = QLineEdit(self)
        self.button = QPushButton(f"Select {type}", self)
        self.button.clicked.connect(self.get_path)
        
        self.layout = QHBoxLayout(self)
        
        self.layout.addWidget(self.label)
        self.layout.addWidget(self.input)
        self.layout.addWidget(self.button)
        
        self.resize(500, 200)
        
    
    def get_path(self):
        self.dialog = QFileDialog(self)
        
        if self.type == 'file':
            self.dialog.setFileMode(QFileDialog.ExistingFile)
            self.dialog.setNameFilter("Text files (*.txt)")
        elif self.type == 'folder':
            self.dialog.setFileMode(QFileDialog.Directory)
        
        path = self.dialog.getOpenFileName(self)
        self.input.setText(path[0])
        return