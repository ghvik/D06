import os

os.chdir("D02/HW02")
print(os.getcwd())
for file_name in os.listdir():
    if file_name[-3:] == ".py":
        print(file_name)
