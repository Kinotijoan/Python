import json
from PyQt5 import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt

def main():
    to_do = QApplication([])
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
        button.setCheckable(True)
        button.setStyleSheet(button_styles)
        buttons.addButton(button)
        buttons_layout.addWidget(button)


    # create a widget that the user writes a note to self
    note_to_self = QTextEdit()
    note_to_self.setPlaceholderText("Write a note to yourself...")  # Placeholder text
    note_to_self.setStyleSheet("background-color: white; color: black; font-family: arvo; font-size: 14px; border: 1px solid black; padding: 5px;")

   

    calendar = QCalendarWidget()
    calendar_layout = QHBoxLayout()
    calendar.setFixedSize(400, 300)
    calendar.setGridVisible(False)
    calendar.setStyleSheet("background-color: pink; color: black; font-family: arvo; font-size: 7px; font-weight: bold; padding: 7px; border: 10px;")
    calendar_layout.addStretch(1)
    calendar_layout.addWidget(calendar)
    calendar_layout.addStretch(1) 

    layout.addWidget(title)
    layout.addLayout(calendar_layout)
    layout.addWidget(note_to_self)
    layout.addLayout(buttons_layout)

    window.setLayout(layout)

    def on_button_clicked(button):
        if button.text() == "Today's list":
            tasks = load_tasks("today.json")
        elif button.text() == "This week's list":
            tasks = load_tasks("week.json")
        elif button.text() == "This month's list":
            tasks = load_tasks("month.json")

        for task in tasks:
            print(task)

    def load_tasks(filename):
        with open(filename, "r") as f:
            tasks = json.load(f)

        return tasks

    # connect the button click events to the on_button_clicked function
    for button in buttons.buttons():
        button.clicked.connect(on_button_clicked)

    window.show()
    to_do.exec_()

if __name__ == "__main__":
    main()

