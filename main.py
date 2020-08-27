from PySide2.QtWidgets import (
    QApplication,
    QMainWindow,
    QVBoxLayout,
    QHBoxLayout,
    QWidget,
    QListWidget,
    QPushButton,
    QLineEdit,
    QStatusBar
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
        self.items_view.addItem('界面样式')
        self.items_view.addItem('界面样式')
        self.items_view.addItem('界面样式')
        self.items_view.addItem('界面样式')
        layout.addWidget(self.items_view)

        # 按钮布局
        button_layout = QHBoxLayout()
        layout.addLayout(button_layout)

        # delete button
        self.delete_button = QPushButton('DELETE')
        button_layout.addWidget(self.delete_button)

        # Complete button
        self.complete_button = QPushButton('COMPLETE')
        button_layout.addWidget(self.complete_button)

        # add input
        self.add_input = QLineEdit()
        layout.addWidget(self.add_input)

        # add button
        self.add_button = QPushButton('ADD')
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


app = QApplication([])
app.setStyle('Fusion')
window = MainWindow()
window.show()
app.exec_()
