import sys

from jesuit_coajudor_bio import BriefBiography
from PySide6 import QtCore
from PySide6.QtGui import QFont
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QWidget, QVBoxLayout, QGridLayout, QPushButton, \
    QLineEdit, QTextEdit, QComboBox, QListWidget, QFormLayout, QGroupBox, QTreeWidget, QTreeWidgetItem
from PySide6.QtCore import Qt

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.bios = BriefBiography.load_from_json('biographies.json')
        self.list_atributes = {
            "education": "Education",
            "religion": "Religion",
            "occupations": "Occupations",
            "locales_of_operation": "Locales of Operation",
            "known_for": "Known For",
            "jesidue_class_attributes": "Jesidue Class Attributes",
            "orders_knighthoods": "Orders/Knighthoods",
        }
        self.setWindowTitle("Jesuit Coajudors Dossier")
        self.setFont(QFont("Segoe UI"))

        # 1.container and layout
        conMain = QWidget()
        self.setCentralWidget(conMain)
        layMain = QVBoxLayout(conMain)

        # 2. Header Section
        lblWelcome = QLabel("Jesuit Coajudors", alignment=QtCore.Qt.AlignCenter)
        lblWelcome.setFont(QFont("Segoe UI", 16, QFont.Bold))
        lblNamePrompt = QLabel("Select a Dossier",
                           alignment=QtCore.Qt.AlignCenter)
        layMain.addWidget(lblWelcome)
        layMain.addWidget(lblNamePrompt)

        # Form Section
        self.layForm = QFormLayout()
        # Dossier choice
        self.cbxDossier = QComboBox()
        for bio in self.bios:
            self.cbxDossier.addItem(str(bio.name))
        self.cbxDossier.currentIndexChanged.connect(self.load_data)
        self.layForm.addRow("&Dossier:", self.cbxDossier)
        layMain.addLayout(self.layForm)

        #Basic Info layout
        gbxBasicInfo = QGroupBox("Basic Information")
        layBasicInfo = QFormLayout()
        #Basic Info Labels
        self.lblDOB = QLabel('')
        self.lblLocaleOfOrigin = QLabel('')
        self.lblAlive = QLabel('')

        layBasicInfo.addRow('Date of Birth:', self.lblDOB)
        layBasicInfo.addRow('Birthplace:', self.lblLocaleOfOrigin)
        layBasicInfo.addRow('Alive:', self.lblAlive)

        gbxBasicInfo.setLayout(layBasicInfo)
        layMain.addWidget(gbxBasicInfo)

        self.treeLists = QTreeWidget()
        self.treeLists.setHeaderHidden(True)
        self.treeLists.setAlternatingRowColors(True)
        layMain.addWidget(self.treeLists)

        self.load_data()

    def load_data(self):
        selected_index = self.cbxDossier.currentIndex()
        if selected_index < 0 or selected_index >= len(self.bios):
            return
        bio = self.bios[selected_index]

        self.lblDOB.setText(str(bio.date_of_birth) or "Unknown")
        self.lblLocaleOfOrigin.setText(bio.locale_of_origin or "Unknown")
        self.lblAlive.setText("Yes" if bio.alive else "No")

        self.treeLists.clear()

        for field, display_title in self.list_atributes.items():

            list_data = getattr(bio, field, [])

            parent_item = QTreeWidgetItem(self.treeLists, [display_title])

            font = parent_item.font(0)
            font.setBold(True)
            parent_item.setFont(0, font)

            if list_data and list_data != ['none']:
                for item_text in list_data:
                    QTreeWidgetItem(parent_item, [str(item_text)])
            else:
                empty_item = QTreeWidgetItem(parent_item, ["none"])
                empty_item.setDisabled(True)
            parent_item.setExpanded(True)


# init
appAntiInquisition = QApplication(sys.argv)
frmMain = MainWindow()
frmMain.show()
appAntiInquisition.exec()