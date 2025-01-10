from functions.ping import *
from functions.string import *
from functions.list import *
from functions.numbers import *
from functions.cortege import *
from functions.files import *


# 1 Ping
ip_addresses = ["8.8.8.8", "127.0.0.1", "192.168.1.1", "256.256.256.256"]
output_file = "ping_results.txt"
check_ping(ip_addresses, output_file)

# 2 analyze string
analyze_string("Hello, World! 12345.")

# 3 list common_elements
common_elements([1, 2, 3, 4], [3, 4, 5, 6])

# 4 sort_numbers
sort_descending([5, 2, 9, 1, 5, 6])

# 5 cortege check uniqueness
check_uniqueness((1, 2, 3, 4))
check_uniqueness((1, 2, 2, 3))

# 6 find files with substring
files = ["report1.txt", "data_analysis.csv", "report_final.doc", "notes.txt"]
find_files_with_substring(files, "report")

# 7 common characters
common_characters("hello", "world")

#  8 find_median
find_median([5, 3, 8, 1, 4])
find_median([5, 3, 8, 1])

# 9 replace_vowels
replace_vowels("Привет, как дела?")

# 10 unique_common_elements
unique_common_elements([1, 2, 3, 4], [3, 4, 4, 5, 6])