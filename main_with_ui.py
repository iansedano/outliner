import sys
from PySide6.QtWidgets import QApplication

from ui.Input_paths import Input_paths

app = QApplication([])

widget = Input_paths()
widget.show()

sys.exit(app.exec())