import os

os.makedirs("mydir", exist_ok=True)

os.chdir("mydir")

for filename in ["file1.txt", "file2.txt", "file3.txt"]:
    with open(filename, "w") as file:
        pass


print("Список файлов в директории mydir:")
print(os.listdir("."))