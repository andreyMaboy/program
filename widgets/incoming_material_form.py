from datetime import datetime

from PySide6.QtCore import QDate, QDateTime
from PySide6.QtGui import QDoubleValidator
from PySide6.QtWidgets import QWidget, QGridLayout, QDateEdit, QLabel, QLineEdit, QComboBox


class IncomingMaterialForm(QWidget):
    def __init__(self, providers: list[str], materials: list[str]):
        super(IncomingMaterialForm, self).__init__()

        self.grid_layout = QGridLayout()
        self.setLayout(self.grid_layout)

        self.date_label = QLabel('Дата')
        self.date_value = QDateEdit()
        self.date_now = datetime.now()
        self.q_date = QDate(self.date_now.year, self.date_now.month, self.date_now.day)
        self.date_value.setDate(self.q_date)
        self.date_value.setDisplayFormat('dd-MM-yyyy')
        self.grid_layout.addWidget(self.date_label, 0, 0, 1, 2)
        self.grid_layout.addWidget(self.date_value, 0, 2, 1, 1)

        self.provider_label = QLabel('Поставщик')
        self.provider_value = QComboBox()
        self.provider_value.addItems(providers)
        self.grid_layout.addWidget(self.provider_label, 1, 0, 1, 2)
        self.grid_layout.addWidget(self.provider_value, 1, 2, 1, 1)

        self.material_label = QLabel('Наименование')
        self.material_value = QComboBox()
        self.material_value.addItems(materials)
        self.grid_layout.addWidget(self.material_label, 2, 0, 1, 2)
        self.grid_layout.addWidget(self.material_value, 2, 2, 1, 1)

        self.batch_num_label = QLabel('Номер партии')
        self.batch_num_value = QLineEdit()
        self.grid_layout.addWidget(self.batch_num_label, 3, 0, 1, 2)
        self.grid_layout.addWidget(self.batch_num_value, 3, 2, 1, 1)

        self.validator = QDoubleValidator()
        self.validator.setDecimals(3)

        self.weight_kg_label = QLabel('Вес (кг)')
        self.weight_kg_value = QLineEdit('0,00')
        self.weight_kg_value.setValidator(self.validator)
        self.grid_layout.addWidget(self.weight_kg_label, 4, 0, 1, 2)
        self.grid_layout.addWidget(self.weight_kg_value, 4, 2, 1, 1)

        self.thickness_mm_label = QLabel('Толщина (мм)')
        self.thickness_mm_value = QLineEdit('0,00')
        self.thickness_mm_value.setValidator(self.validator)
        self.grid_layout.addWidget(self.thickness_mm_label, 5, 0, 1, 2)
        self.grid_layout.addWidget(self.thickness_mm_value, 5, 2, 1, 1)



