p1 = int(input())
p2 = int(input())
p3 = int(input())
j1 = int(input())
j2 = int(input())

rp1 = p2 if p1 > p2 else p1
rp2 = p3 if rp1>p3 else rp1

rj1 = j2 if j1>j2 else j1

resultP = rp2+(rp2*0.1)
resultJ = rj1+(rj1*0.1)

print(resultP+resultJ)