FILE = "txt_files/numbers.txt"
source_file = open(FILE, 'r')
result = 0
line1 = int(source_file.readline())
line2 = int(source_file.readline())
result = line1+line2
print("Result ; {}".format(result))
source_file.close()
