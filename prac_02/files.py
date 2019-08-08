FILE = "txt_files/name.txt"
open(FILE, 'r')

input_file = open(FILE, 'w')
name = str(input("Enter Your Name: "))
print("Your Name is : {}".format(name), file=input_file)
input_file.close()
output_file = open(FILE, 'r')
for line_str in output_file:
    print(line_str)
output_file.close()