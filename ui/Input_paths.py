from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton
from PySide6.QtCore import Qt

from .Path_selector import Path_selector

import dir_builder

class Input_paths(QWidget):
    def __init__(self):
        super().__init__()
              
        layout = QVBoxLayout(self)
        layout.setAlignment(Qt.AlignCenter)
        
        self.file_selector = Path_selector('file')
        self.folder_selector = Path_selector('folder')
        self.file_selector.setFixedSize(500,40)
        self.folder_selector.setFixedSize(500,40)
        
        layout.addWidget(self.file_selector)
        layout.addWidget(self.folder_selector)
        
        button = QPushButton("Execute")
        button.clicked.connect(self.handleExecute)
        button.setFixedSize(100, 40)
        
        layout.addWidget(button, alignment=Qt.AlignCenter)
        
    
    def handleExecute(self):
        input_file = self.file_selector.get_path()
        output_folder = self.folder_selector.get_path()
        
        if not input_file or not output_folder:
            raise Exception("Invalid Input or Output")
        
        dir_builder.create_main(input_file, output_folder, number = True)
        