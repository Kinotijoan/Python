# this is a to_do list app class
# it containts th attribute of the to_do list
# it contains the methods of the to_do list
# the inputs by the user are stored in a json file
from PyQt5 import *
from PyQt5.QtWidgets import QButtonGroup, QCalendarWidget, QGridLayout, QHBoxLayout, QLabel, QPushButton, QTextEdit, QVBoxLayout, QWidget, QApplication
from PyQt5.QtCore import Qt

class ToDo:
    def __init__(self,):
        self.to_do = []
        self.deadline = []
        self.priority = []
        self.add_task_layout = QGridLayout()


    def add_to_list(self):
        # get the task from the user
        # the user should enter tasks until they are done adding tasks
        while True:
            task = input("Enter a task: ")

            # add the task to the list
            self.to_do.append(task)

            # ask the user if they want to add more tasks
            choice = input("Do you want to add more tasks? (y/n): ")
            if choice == "n":
                break

    # def add_task(self):
    #     # call the add_to_list function
    #     self.add_to_list()

    def button_clicked(self, button):
        print("Button clicked:", button)
        if button == "Today's list":
        # create a widget that the user clicks on to start adding the to_do list")
            add_task_widget = QPushButton("Add task")
            add_task_widget.setCheckable(True)
            add_task_widget.setStyleSheet("background-color: pink; color: black; font-family: arvo; font-size: 20px; font-weight: bold; padding: 7px; border: 10px;")

            self.add_task_layout.addWidget(add_task_widget)

        # # connect the button click event to the add_task function
            add_task_widget.clicked.connect(lambda checked :self.add_to_list())

        if button == "This week's list":
            week_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
            for day in week_days:
                selected_day = QLabel(window)
                selected_day.setText(day)
                selected_day.setStyleSheet("color: pink; font-family: pattaya; font-size: 30px; font-weight: bold; padding: 5px;")
                selected_day.setAlignment(Qt.AlignTop | Qt.AlignHCenter)
                layout.addWidget(selected_day)
                selected_day.clicked.connect(self.add_task())

        if button == "This month's list":
       # when this is clicked i want it to display a calendar
        # one is able to click on a day and add a task
            # display the calendar
            calendar_widget = QCalendarWidget()
            calendar_widget.setGridVisible(True)
            calendar_widget.setStyleSheet("background-color: pink; color: black; font-family: arvo; font-size: 15px; font-weight: bold; padding: 5px;")
            calendar_widget.show()

            # connect the day click event to the add_task function use lambda
            calendar_widget.selectionChanged.connect(lambda :self.add_task())

    def display_list():
        # print the list of tasks
        for task in tasks:
            print(task)

    def edit_to_do(self):
        pass

    def delete_to_do(self):
        pass

    def save_to_do(self):
        pass
