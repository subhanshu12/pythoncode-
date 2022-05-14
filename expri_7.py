n = int(input())
a = 0
b = 1
i = 1 #initialsing the looping variable to 1
print(a)
while i <=n: 
    c = a+b
    a =b
    b =c
    i = i+1
    print(a)
    