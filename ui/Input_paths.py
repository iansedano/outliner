from PySide6.QtWidgets import QWidget, QVBoxLayout

from .Path_selector import Path_selector

class Input_paths(QWidget):
    def __init__(self):
        super().__init__()
        
        self.file_select = Path_selector('file')
        self.folder_select = Path_selector('folder')
        
        self.layout = QVBoxLayout(self)
        
        self.layout.addWidget(self.file_select)
        self.layout.addWidget(self.folder_select)