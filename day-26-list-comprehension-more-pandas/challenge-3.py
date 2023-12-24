from file2list import File2List

FILE1_PATH = "file1.txt"
FILE2_PATH = "file2.txt"

file1 = File2List(FILE1_PATH)
file2 = File2List(FILE2_PATH)

result = [int(num.strip()) for num in file1.list if num in file2.list]

print(result)