# CASE STUDY I:

# Task I:

x = 8
y = 3.2
z = 8j + 18
a = "Hello World"
b = True
c = 23 < 22
l = [1, 2, 3, 4]
d = {"Name": "Jake", "Age": 27, "Address": "Downtown"}
t = ("Machine Learning", "Data Science")
s = {"Python", "Machine Learning", "Data Science"}
type_list = []
variable_names = ["x", "y", "z", "a", "b", "c", "l", "d", "t", "s"]
for i in [x, y, z, a, b, c, l, d, t, s]:
    type_list.append(i)

result = list(map(lambda x: type(x), type_list))
print("Task 1:", list(zip(variable_names, result)))

# Task II:

text = "The goal is to turn data into information, and information into insight"

result_text = text.upper()
result_text = result_text.replace(",", "")
print(result_text.split())

# Task III:

lst = ["D", "A", "T", "A", "S", "C", "I", "E", "N", "C", "E"]
# step I:
print(len(lst))
# step II:
print(lst[0], lst[10])
# step III:
new_lst = lst[0:4]
# step IV:
del lst[8]
# step V:
lst.append("X")
# step VI:
lst.insert(8, "N")

# Task IV:

dict = {"Christian": ["America", 18],
        "Daisy": ["England", 12],
        "Antonio": ["Spain", 22],
        "Dante": ["Italy", 25]}

# step I:
print(dict.keys())
# step II:
print(dict.values())
# step III:
dict.update({"Daisy": ["England", 13]})
# step IV:
dict.__setitem__("Ahmet", ["Turkey", 24])  # OR dict.update({"Ahmet": ["Turkey" , 24]})
# step V:
dict.pop("Antonio")

# Task V:

l = [2, 13, 18, 93, 22]


def func(list):
    even_list = []
    odd_list = []
    for i in list:
        if i % 2 == 0:
            even_list.append(i)
        else:
            odd_list.append(i)
    return even_list, odd_list


func(l)

# Task VI:

students = ["Ali", "Veli", "Ayşe", "Talat", "Zeynep", "Ece"]


def student_enumerate(student_list):
    for i, student in enumerate(student_list[:3], 1):
        print(f"Engineering Faculty {i}. student: {student} ")
    for i, student in enumerate(student_list[3:], 1):
        print(f"Medicine Faculty {i}. student: {student} ")


student_enumerate(students)

# Task VII:

course_code = ["CMP1005", "PSY1001", "HUK1005", "SEN2204"]
credit = [3, 4, 2, 4]
quota = [30, 75, 150, 25]

course_credit = list(zip(course_code, credit))
overall = list(zip(course_credit, quota))
for (course, credit), quota in overall:
    print(f"{course} has {credit} credits and a quota of {quota}")

# Task VII:

set1 = set(["data", "python"])
set2 = set(["data", "function", "qcut", "lambda", "python", "miuul"])


def set_diff(set_first, set_second):
    if set_first.issuperset(set_second):
        return set_first.intersection(set_second)
    else:
        return set_second - set_first


set_diff(set1, set2)
