# this script make a trianlge
rows = input('enter the a number ')
row = int(rows)
r = 0
for i in range(1, row+1):
    for space in range(1, (row-i)+1):
        print(end=" ")
    while r != (2*i-1):
        print("*", end=" ")
        r += 1
    r = 0
    print()
# this python script is to create a tress star to created from a number
# this create an inverted diamond
colums_user = input('enter a number')
colums = int(colums_user)
for h in range(colums +1, 1, -1):
    print(" "*((colums+2)-h), end="")
    for g in range(h, 1, -1):
        print('*', end=" ")
    print(" ")

for d in range(1, colums+1):
    print(" "*((colums+1)-1), end="")
    for c in range(1, d+1):
        print('*', end=" ")
    print(' ')