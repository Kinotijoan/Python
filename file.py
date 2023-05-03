try:
    f = open("myData2.txt", "w") 
    f.write("I am joan")
    f.close()

    file = open("myData3.txt")
except FileNotFoundError :
    print("The file you want was not found")
else:
    f = open("myData2.txt")
    print(f.read())
finally:
    print("In finally")
