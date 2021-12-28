'''grocery = {"우유" : [12,23,2],
           "계란" : 12,
           "빵" : 2}
print(grocery)
grocery["닭"] = 3

print(grocery)

print(len(grocery))

h = grocery.pop("우유")

print(grocery)
print(h)
print(grocery.values())

grades = {}

grades["a"] = [100, 70]
grades["b"] = [90, 100]
grades["c"] = [80, 40]

for students in grades.keys():
    print(students)
    
for quizzes in grades.values():
    print(sum(quizzes)/2)
print('-----------')
for students in grades.keys():
    scores = grades[students]
    print(scores)
    grades[students].append(sum(scores)/2)
print(grades)

print(grades["a"])'''
'''
employees = {"홍길동" : 34, "전우치" : 50, "성춘향" : 24}
for em in employees.keys():
    employees[em] += 1
    print(employees[em])
'''
'''
lyrics = "have a happy birthday"

counts = {}
words = lyrics.split()

for w in words:
    counts[w] = 1
    if w not in counts:
        counts[w] += 1
print(counts)
'''

'''
def square(x):
    return (x*x)
    
def circle(r):
    return (3.14*r*r)

areas = {"square" : square, "circle" : circle}

for s in areas.keys():
    print(areas[s](2))
'''

'''a = 1
print(id(a))

b = a
print(id(b))

a = 2
print(id(a))

print(id(b))
'''
'''
x = ["me", "i"]

y = x
print(id(y))

z = y
print(id(z))

a = ["me", "i"]
print(id(a))
'''
'''
def add_word(dic, word, definition):
    if word in dic:
        dic[word].append(definition)
    else:
        dic[word] = [definition]

words = {}
add_word(words, 'box', 'fight')
print(words)
add_word(words, 'box', 'asdas')
print(words)
'''
'''
artists = ["a", "b"]
painters = artists
painters.append('c') 
print(artists)
print(painters)       

painters = list(artists)
painters = artists.copy()

class human(object):
    def __init__(self):
        self.age = 0

class car(object):
    def __init__(self):
        self.num = 0
        self.kind
'''   

'''class door(object):
    def __init__(self):
        self.width = 1
        self.height = 1
        self.open = False
    def check_open(self):
        return self.open
    def size(self):
        return self.width * self.height'''
        
'''class door(object):
    def __inti__(self):
        self.width = 1
        self.height = 1
        self.open = False
        
    def change_state(self):
        self.open = not self.open
        
    def scale(self, factor):
        self.height *= factor
        self.width *= factor
        
square_door = door()
a = square_door.change_state()
b = square_door.scale(3)
print(a)
print(b)
'''

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def disp(self):
        print(self.name)
        print(self.age)
        
p1 = Person('홍길동', 22)
p1.disp()