import json
from PySide2.QtCore import Slot, QSize
from PySide2.QtGui import QIcon
from PySide2.QtWidgets import (
    QApplication,
    QMainWindow,
    QVBoxLayout,
    QHBoxLayout,
    QWidget,
    QListWidget,
    QPushButton,
    QLineEdit,
    QStatusBar,
    QListWidgetItem
)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('清单')
        self.setFixedSize(320, 480)

        # 布局
        layout = QVBoxLayout()

        # 清单视图
        self.items_view = QListWidget()
        self.items_view.setIconSize(QSize(14, 14))
        self.items_view.doubleClicked.connect(self.toggle_complete)
        layout.addWidget(self.items_view)

        # 按钮布局
        button_layout = QHBoxLayout()
        layout.addLayout(button_layout)

        # delete button
        self.delete_button = QPushButton('DELETE')
        self.delete_button.clicked.connect(self.delete)
        button_layout.addWidget(self.delete_button)

        # Complete button
        self.complete_button = QPushButton('COMPLETE')
        self.complete_button.clicked.connect(self.complete)
        button_layout.addWidget(self.complete_button)

        # add input
        self.add_input = QLineEdit()
        self.add_input.returnPressed.connect(self.add)
        layout.addWidget(self.add_input)

        # add button
        self.add_button = QPushButton('ADD')
        self.add_button.clicked.connect(self.add)
        layout.addWidget(self.add_button)

        # status bar
        self.setStatusBar(QStatusBar())

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        self.setStyleSheet("""
            QListWidget {
                border: 1px solid #999;
                font-size: 13px;
            }
            
            QListWidget::item {
                color: #000;
                height: 30px;
                border-bottom: 1px solid #dedede;
            }
            QListWidget::item:selected {
                background-color: #fff9dd;
            }
            
            QPushButton {
                height: 24px;
                background-color: #fddb3a;
                font-weight: 900;
            }
            
            QLineEdit {
                padding: 5px;
            }
        """)

        self.items = []
        self.load()
        self.list_items()

    @Slot()
    def add(self):
        name = self.add_input.text()
        if name:
            self.items_view.addItem(QListWidgetItem(name))
            self.add_input.setText('')
            self.items.append({'name': name, 'done': False})
            self.save()
            print('add item')

    @Slot()
    def delete(self):
        items = self.items_view.selectedItems()
        if items:
            self.items.pop(self.items_view.currentRow())
            self.items_view.clear()
            self.list_items()
            self.save()
        print('delete item')

    @Slot()
    def complete(self):
        items = self.items_view.selectedItems()
        if items:
            item_data = self.items[self.items_view.currentRow()]
            if not item_data['done']:
                icon = QIcon('done.svg')
                items[0].setIcon(icon)
                item_data['done'] = True
                print('complete item')
                self.save()

    @Slot()
    def toggle_complete(self):
        items = self.items_view.selectedItems()
        if items:
            item_data = self.items[self.items_view.currentRow()]
            if not item_data['done']:
                icon = QIcon('done.svg')
                items[0].setIcon(icon)
                item_data['done'] = True
            else:
                icon = QIcon('')
                items[0].setIcon(icon)
                item_data['done'] = False
            self.save()

    def list_items(self):
        for item in self.items:
            list_item = QListWidgetItem(item['name'])
            if item['done']:
                icon = QIcon('done.svg')
                list_item.setIcon(icon)
            self.items_view.addItem(list_item)

    def load(self):
        with open('data.json', 'r') as f:
            self.items = json.load(f)

    def save(self):
        with open('data.json', 'w') as f:
            json.dump(self.items, f)


app = QApplication([])
app.setStyle('Fusion')
window = MainWindow()
window.show()
app.exec_()
