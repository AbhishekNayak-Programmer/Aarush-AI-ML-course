# List
my_list = [1, 2,2, 3, 4, 5]
my_list.append("Abhishek")
print(my_list)
print(my_list.count(2))

# my_list.append(["Nayak", "AI/ML"])
my_list.extend(["Nayak", "AI/ML"])
print(my_list)

my_list.remove("Nayak")
print(my_list)

t = (1,2,2,3,3,3,3)
print(type(t))
print(t.count(3))


student = {
    "name" : "Abhishek",
    "age": 28
}

print(student)
student["name"] = "Adarsh"
print(student)
student["name"] = [1,2,3]
print(student)

print(student.keys())
print(student.values())


# WAP to count characters frequency in a string
text = "hello"
freq = {}

for char in text:
    freq[char] = freq.get(char, 0) + 1

# {}
# {"h": 1}
# {"h": 1, "e" : 1}
# {"h": 1, "e" : 1, "l" : 1}
# {"h": 1, "e" : 1, "l" : 2}
# {"h": 1, "e" : 1, "l" : 2, "o" : 1}

print(freq)
# print(freq.get('Z', "Abhishek"))

# File Handeling
# file = open("data.txt", "r")
# content = file.read()
# print(content)
# file.close()

# file = open("data.txt", 'w')
# file.write("Cool Stuffs")
# file.close()

# Short and most used trick in file handeling
with open("data.txt", 'r') as file:
    content = file.read()
    print(content)
    lines = file.readlines()
    print("Number of lines", len(lines))

with open("dataa.txt", 'w') as file:
    file.write("Abhishek Nayak")

with open("dataa.txt", 'a') as file:
    file.write("\nAdarsh Nayak")
  

# Homework
# 1. Write a program to copy content of one file to another file