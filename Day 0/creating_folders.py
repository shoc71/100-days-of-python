import os

folder_path = "/enter/your/folder/path/here/100-days-of-python/" #last / important, I have lost files not doing this

for day in range (0, 101):
    folder_name = f"Day {day}"
    folder_creation = os.path.join(folder_name, folder_path)
    os.makedirs(folder_creation)
