import os

#read(), read with indexing (n), readline(), readlines()

#file = open("C:\\NR\\ReadText.txt")
#file = open("C:\\Users\\ynrbt\\OneDrive - kwamenkrumahacademy.org\\Automation\\SeleniumPython-Pycharm\\ReadText1.txt")
print(os.getcwd())
# file = open(os.getcwd()+"\\ReadText.txt") #one drive path not reading properly

#print(file.read())

# for line in file.readlines():
#     print(line)

# file =open(os.getcwd()+"\\test.csv", 'w')
# file.write("sample write to see how it works")

file =open(os.getcwd()+"\\test.csv", 'w')
arrayList=["Testing\n", "Developing\n", "Deploying\n"]
file.writelines(arrayList)



file.close()




