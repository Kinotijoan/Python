# this is a calculator program inclusive of grahical user interface
# it is a simple calculator that can perform basic arithmetic operations

import tkinter as tk
import math


def calculate_square_root(number):
    # assign the number to the input by the user
    try:
        number = float(textbox.get("1.0", "end-1c"))
        result = math.sqrt(number)
        textbox.delete("1.0", tk.END)
        textbox.insert(tk.END, str(result))
    except ValueError:
        textbox.delete("1.0", tk.END)
        textbox.insert(tk.END, "Error")

def button_click(char):
    current_text = textbox.get("1.0", "end-1c")  # Get the current text in the textbox
   
    if char == "=":
        try:
            current_text = current_text.replace(multiplication_sign, "*")
            current_text = current_text.replace(f"{superscript_2}", "**2")
            current_text = current_text.replace(square_root_sign, "calculate_square_root")
            result = eval(current_text)
            textbox.delete("1.0", tk.END)
            textbox.insert(tk.END, str(result))
        
        except ZeroDivisionError:
            textbox.delete("1.0", tk.END)
            textbox.insert(tk.END, "Math error")
        except Exception as e:
            textbox.delete("1.0", tk.END)
            textbox.insert(tk.END, "Error")
    elif char == "CLEAR":
        textbox.delete("1.0", tk.END)
    elif char == delete_symbol:
        textbox.delete("end-2c", tk.END)  # Delete the last character
    else:
        if char == f"x{superscript_2}":
            textbox.insert(tk.END, f"{superscript_2}")
        else:
            textbox.insert(tk.END, char)  # Append the character to the textbox



multiplication_sign = "\u00D7"
square_root_sign = "\u221A"
superscript_2 = "²"
delete_symbol = "\u232B"
lighter_gray = "#E0E0E0"

# create a window
root = tk.Tk()
root.title("CALCULATOR")
root.geometry("500x435")
root.resizable(False,False)
root.config(bg = "grey", bd = 7, relief = "sunken")

#create a label widget that changes with the operation being performed
label = tk.Label(root, text ="operation", width = 10, height = 1, bg = "white", fg = "black", anchor = "w", 
                font = ("Times", "12", "bold"), bd = 4, relief = "ridge")
label.pack(padx = 5, pady = 5)
label.place(x = 1, y = 1)
label.config(bg = "grey", bd = 6)

frame = tk.Frame(root)
frame.pack(pady=10)

# Create two labels for the text box
# The first label for the user input
# The second label for the result
label1 = tk.Label(frame, text="User Input", width=10, height=1, bg="grey", fg="black")
label2 = tk.Label(frame, text="Result", width=10, height=1, bg="grey", fg="black")
label1.place(x = 1, y = 0)
label2.place(x = 400, y = 0, )

# create a text box widget
textbox = tk.Text(root, height = 7, font = ("arial", 12), width = 40, bg = "white", fg = "black", bd = 5, relief = "sunken")
textbox.place(x = 1, y = 25)
textbox.config(bg = "lightgray", bd = 6)

# create a frame for buttons use grid to place the buttons and use a dictionary to store the buttons
button_frame = tk.Frame(root)
button_frame.place(x = 1, y = 175)
button_frame.config(bg = "grey", width = 500, height = 300, bd = 6, relief = "raised")
for i in range(5):
    button_frame.columnconfigure(i, weight = 1)
    button_frame.rowconfigure(i,weight = 1)

# create a dictionary to store the buttons
number_buttons = {1: (0,0), 2: (0,1), 3: (0,2,), 
                4: (1,0), 5: (1,1), 6: (1,2), 
                7: (2,0), 8: (2,1), 9: (2,2), 
                0: (3,1), ".": (3,2), 
}

for button, position in number_buttons.items():
    button = tk.Button(button_frame, text = button, width = 10, height = 2, bg = "lightgrey", fg = "black", bd = 5, relief = "raised",
                        command = lambda x = button: button_click(x))
    button.grid(row = position[0], column = position[1], padx = 5, pady = 5, sticky = "nsew")
    button.config(font = ("Times", "10", "bold"))

# a dictionary for the operation functions
operation_buttons = {"+": (0,3), "-": (0,4), f"{multiplication_sign}": (1,3),
                    "/": (1,4), f"{square_root_sign}": (2,3), f"x{superscript_2}": (2,4)}

for button, position in operation_buttons.items():
    button = tk.Button(button_frame, text = button, width = 10, height = 2, bg = "lightblue", fg = "black", bd = 5, relief = "raised",
                        command = lambda x = button: button_click(x))
    button.grid(row = position[0], column = position[1], padx = 5, pady = 5, sticky = "nsew")
    button.config(font = ("Times", "10", "bold"))

#create a delete button
delete_button = tk.Button(button_frame, text = f"{delete_symbol}", width = 10, height = 2, bg = "lightblue", fg = "black", bd = 5,
                 relief = "raised", command = lambda: button_click(delete_symbol))
delete_button.grid(row = 3, column = 3, padx = 5, pady = 5, sticky = "nsew")
button.config(font = ("Times", "10", "bold"))

# create an equal button
equal_button = tk.Button(button_frame, text = "=", width = 10, height = 2, bg = "red", fg = "black", bd = 5, relief = "raised",
                        command = lambda: button_click("="))
equal_button.grid(row = 3, column = 4, padx = 5, pady = 5, sticky = "nsew")
button.config(font = ("Times", "10", "bold"))

#create a clear button
clear_button = tk.Button(button_frame, text = "CLEAR", width = 10, height = 2, bg = "lightgrey", fg = "black", bd = 5, relief = "raised",
                        command = lambda: button_click("CLEAR"))
clear_button.grid(row = 3, column = 0, padx = 5, pady = 5, sticky = "nsew")
button.config(font = ("Times", "10", "bold"))

# # create a on button
# on_button = tk.Button(button_frame, text = "ON", width = 10, height = 2, bg = "red", fg = "black", bd = 5, relief = "raised",
#                         command = lambda: button_click("ON"))
# on_button.grid(row=0, column=4, padx=5, pady=5, sticky="e")
# button.config(font = ("Times", "10", "bold"))

# # create an off button
# off_button = tk.Button(button_frame, text = "OFF", width = 10, height = 2, bg = "red", fg = "black", bd = 5, relief = "raised",
#                         command = lambda: button_click("OFF"))
# off_button.grid(row=1, column=4, padx=5, pady=5, sticky="e")
# button.config(font = ("Times", "10", "bold"))

root.mainloop()
