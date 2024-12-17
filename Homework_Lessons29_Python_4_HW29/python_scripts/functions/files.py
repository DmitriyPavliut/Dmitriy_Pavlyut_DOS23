import os

def find_files_with_substring(file_list, substring):
    result = [file for file in file_list if substring in file]
    print("Файлы с подстрокой:", result)