h1 = int(input())
m1 = int(input())
s1 = int(input())
h2 = int(input())
m2 = int(input())
s2 = int(input())
h12 = (h2 - h1) * 3600
m12 = (m2 - m1) * 60
s12 = (s2 - s1)
t = h12 + m12 + s12
print(t)
