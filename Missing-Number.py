a = [1,2,3,4,5,8,9,11]
b = []

x = len(a)
p = a[x-1]
q = a[0]

for i in range(q, p+1):
    b.append(i)

y = len(b)
z = y - x

if z != 0:
    print("THERE", end=" ")
    print(z, end=" ")
    print("NUMBER MISSING")
    m = list(set(b) - set(a))
    print(m)
else:
    print("No number is missing")