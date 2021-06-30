from PySide6.QtWidgets import QWidget, QFileDialog, QLabel, QLineEdit, QHBoxLayout, QPushButton
# from PySide6.QtGui import QDialog


class Path_selector(QWidget):
    def __init__(self, type):
        super().__init__()
        
        if not (type == 'file' or type == 'folder'):
            raise Exception("invalid type when initializing Path_selector class instance")
        
        self.type = type
        
        self.label = QLabel(f"Select a {type}", self)
        self.input = QLineEdit(self)
        self.button = QPushButton(f"Select {type}", self)
        self.button.clicked.connect(self.navigate_for_path)
        
        self.layout = QHBoxLayout(self)
        
        self.layout.addWidget(self.label)
        self.layout.addWidget(self.input)
        self.layout.addWidget(self.button)
        
        self.resize(500, 200)
        
    
    def navigate_for_path(self):
        self.dialog = QFileDialog(self)
        path = ""
        
        if self.type == 'file':
            self.dialog.setFileMode(QFileDialog.ExistingFile)
            self.dialog.setNameFilter("Text files (*.txt)")
            self.dialog.exec()
            path = self.dialog.selectedFiles()[0]
            #path = self.dialog.getOpenFileName(self)[0]
        elif self.type == 'folder':
            path = self.dialog.getExistingDirectory(self)
            print(path)
            
        self.input.setText(path)
        return
        
    def get_path(self):
        return self.input.text()