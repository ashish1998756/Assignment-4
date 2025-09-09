# Task 2: Write and Append Data to a File

with open("output.txt", "w") as file:
  i=input("Enter text to write to the file :")
  file.write(i)
print("Data successfully written to output.txt.","\n")





with open("output.txt","a") as file:
    a=input("Enter additional text to append :")
    file.write("\n" +a)
print("Data successfully append.","\n")



with open("output.txt", "r") as file:
    z = file.read()
print("Final content of output.txt:\n", z)
