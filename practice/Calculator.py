user_name = input("What is your name?")
print("Welcome {}".format(user_name))
num_1 = int(input("Enter a number:"))
num_2 = int(input("Enter a number:"))

expression = "num_1 + num_2"

b = eval(expression)
print(b)
