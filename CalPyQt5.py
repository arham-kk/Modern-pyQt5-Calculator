import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton, QHBoxLayout

class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Calculator')
        self.setStyleSheet('background-color: #1F1F23')
        self.setFixedSize(350, 450)
        
        layout = QVBoxLayout()
        self.display = QLineEdit()
        self.display.setFixedHeight(70)
        self.display.setAlignment(Qt.AlignRight)
        self.display.setStyleSheet('QLineEdit {font-size: 28px; background-color: #2E2E32; color: white; border: 2px solid #5A5A5E; border-radius: 10px; padding-right: 10px;}')
        layout.addWidget(self.display)
        
        buttons = ['7', '8', '9', '/', '4', '5', '6', '*', '1', '2', '3', '-', '0', '.', '=', '+']
        button_layout = QVBoxLayout()
        
        for i in range(0, 16, 4):
            row_layout = QHBoxLayout()
            for j in range(i, i+4):
                button = QPushButton(buttons[j])
                button.setFixedSize(70, 70)
                button.setStyleSheet('QPushButton {font-size: 28px; background-color: #2E2E32; color: white; border: 2px solid #5A5A5E; border-radius: 35px;} QPushButton:hover {background-color: #4E4E4E;}')
                button.clicked.connect(lambda _, text=buttons[j]: self.handle_button(text))
                row_layout.addWidget(button)
            button_layout.addLayout(row_layout)
            
        layout.addLayout(button_layout)
        self.setLayout(layout)
        
    def handle_button(self, text):
        if text == '=':
            try:
                result = str(eval(self.display.text()))
                self.display.setText(result)
            except:
                self.display.setText('Error')
        elif text == 'C':
            self.display.setText('')
        else:
            self.display.setText(self.display.text() + text)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    calculator = Calculator()
    calculator.show()
    sys.exit(app.exec_())
