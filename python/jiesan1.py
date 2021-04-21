

def convertString(str_list, N):
    res = []
    for s in str_list:
        if len(s) > N:
            res.append(s.upper())
        else:
            res.append(s)
    return res

str_list = ["Programming", "Coding", "Python", "Hello"]
# print(convertString(str_list, 7))


def sunOfunique(nums):
    n = len(nums)
    if n == 0:
        return 0
    dic = {}
    for num in nums:
        if num in dic:
            dic[num] += 1
        else :
            dic[num] = 1
    res = 0
    for (k, v) in dic.items():
        if v == 1:
            res += k
    return res

nums = [1,2,3,4,5]
# print(sunOfunique(nums))

def divisible(N, denominator):
    if N < 1:
        print("N must be greater than 10!")
        return
    for n in range(N, 0, -1):
        if n % denominator == 0:
            print(n, "is divisible by", denominator, '!')
    print("End")

# divisible(10, 5)


def checkArmstrong(filename):
    def check(num):
        nums = str(num)
        n = len(nums)
        s = 0
        for i in range(n):
            s += int(nums[i]) ** 3
        return True if s == num else False
    for num in filename:
        if check(num):
            print("True")
        else:
            print("False")

# checkArmstrong([150, 371, 343])


class Student:
    
    def __init__(self, name, ID, marks = {}):
        # write your code here
        self.name = name
        self.id = ID
        self.marks = marks
    
    def update_mark(self, unit, mark):
        # write your code here
        self.marks[unit] = mark

    def avg_mark(self):
        # write your code here
        s = 0
        for value in self.marks.values():
            s += value
        return s / len(self.marks)

    def __str__(self):
        # write your code here
        print("name:", self.name)
        print("ID:", self.id)
        for k, v in self.marks.items():
            print(k, ":", v)

    def __eq__(self, other):
        # write your code here
        return self.__dict__ == other.__dict__

s1 = Student("liu", 1, {"python": 90, "java": 91})
s2 = Student("liu", 1, {"python": 90, "java": 91})
print(s1.__eq__(s2))
print()
s1.__str__()
print("avg_mark:", s1.avg_mark())
print()
s1.update_mark("web", 92)
s1.update_mark("python", 93)
s1.__str__()
print("avg_mark:", s1.avg_mark())

print()
print(s1.__eq__(s2))