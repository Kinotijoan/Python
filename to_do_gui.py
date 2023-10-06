# This is the main file for the to-do list Gui
from PyQt5 import *
from PyQt5.QtWidgets import QButtonGroup, QCalendarWidget, QGridLayout, QHBoxLayout, QLabel, QPushButton, QTextEdit, QVBoxLayout, QWidget, QApplication
from PyQt5.QtCore import Qt
from to_do_class import ToDo 


def main():
    app = QApplication([])
    To_do = ToDo()

    window = QWidget()
    window.setWindowTitle("EVERYDAY PLANNER")
    window.setGeometry(500,500,600,500)
    window.setStyleSheet("background-color: black; padding: 60px; border: 5px solid black; border-radius: 20px;")

    layout = QVBoxLayout() 
    layout.setSpacing(10)

    title = QLabel(window)
    title.setText("Joan's To-Do List")
    title.setStyleSheet("color: pink; font-family: pattaya; font-size: 30px; font-weight: bold; padding: 5px;")
    title.setAlignment(Qt.AlignTop | Qt.AlignHCenter)

    # 3 buttons that when pressed lead you to the list of the day month or week
    buttons = QButtonGroup()
    buttons_layout = QVBoxLayout()

    button_names = ["Today's list", "This week's list", "This month's list"]
    button_styles = "background-color: pink; color: black; font-family: arvo; font-size: 20px; font-weight: bold; padding: 7px; border: 10px;"

    for button_name in button_names:
        button = QPushButton(button_name)
        button.setStyleSheet(button_styles)
        button.setCheckable(True)
        buttons.addButton(button)
        buttons_layout.addWidget(button)
        button.clicked.connect(lambda checked, b=button_name: To_do.button_clicked(b))

# create a widget that the user writes a note to self
    note_to_self = QTextEdit()
    note_to_self.setPlaceholderText("Write a note to yourself...")
    note_to_self.setStyleSheet("background-color: white; color: black; font-family: arial; font-size: 14px; border: 1px solid black; padding: 5px;")

    calendar = QCalendarWidget()
    calendar_layout = QHBoxLayout()
    calendar.setFixedSize(400, 300)
    calendar.setGridVisible(False)
    calendar.setStyleSheet("background-color: pink; color: black; font-family: arial; font-size: 7px; font-weight: bold; padding: 7px; border: 10px;")
    calendar_layout.addStretch(1)
    calendar_layout.addWidget(calendar)
    calendar_layout.addStretch(1) 

    layout.addWidget(title)
    layout.addLayout(calendar_layout)
    layout.addWidget(note_to_self)
    layout.addLayout(buttons_layout)
    layout.addLayout(To_do.add_task_layout)

    window.setLayout(layout)

    window.show()
    app.exec_()


if __name__ == "__main__":
    main()
