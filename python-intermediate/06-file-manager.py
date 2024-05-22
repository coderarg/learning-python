# File Handling

# .txt
file_txt = open("./python-intermediate/my_file.txt", "r+", encoding='UTF-8')
#r+ = reading and writing
#w+ = reading and writing but overwriting if doesn't exist

#print(file_txt.read())
#print(file_txt.read(10)) #We can read the first ten characters
#print(file_txt.readlines()) #Read each line

for line in file_txt.readlines():
    print(line)

file_txt.write("Esta escritura está realizada con python")