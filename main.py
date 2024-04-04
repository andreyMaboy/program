from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout
from widgets.incoming_material_form import IncomingMaterialForm

app = QApplication()


class FormIncomingMaterial(QWidget):
    def __init__(self):
        super(FormIncomingMaterial, self).__init__()


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.grid_layout = QGridLayout()
        provs = ['АО Кыштым']
        maters = ['73', '74', '75', '76', '77', '78']
        x = IncomingMaterialForm(provs, maters)
        self.grid_layout.addWidget(x)
        self.central_widget = QWidget()
        self.central_widget.setLayout(self.grid_layout)
        self.setCentralWidget(self.central_widget)


window = MainWindow()
window.show()
app.exec()
