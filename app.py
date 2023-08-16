
import sys


def print_python_version():
    print(sys.version)

print("Hello World")
print("*" * 10)

course2 = "Python p"
print(len(course2))
print(course2[0:3])
print(course2[2:])

first_name = "ali"
last_name = "nakhaei"
full_name = first_name + " " + last_name
full = f"{len(first_name)} {last_name} {1+2}"
print(full_name)
print(full)

cousre = "   py programming"
print(cousre.upper())
print(cousre.lower())
print(cousre.title())
print(cousre.strip())
print(cousre.find("p"))
print(cousre.replace("p", "j"))
print("p" in cousre)
print("swift" not in cousre)