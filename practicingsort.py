#This a file
inp = int(input("how many numbers are there in your list? \n >>>"))
list1 = []
list2 = list1

for i in range(inp):
    inpu = int(input("Enter the value: "))
    list1.append(inpu)
print(list2)
print()

def sort():
    for i in range(len(list1)-1,0,-1):
        for j in range(i):
            if list1[j] > list1[j+1]:
                list1[j], list1[j+1] = list1[j+1], list1[j]


def sort2():

    for i in range(len(list1)):
        minpos = i
        for j in range(i,len(list1)):
            if list1[j] < list1[minpos]:
                minpos=j
        list1[i], list1[minpos] = list1[minpos], list1[i]
        print(list1)


print()
sort2()
print("The original list is :", list2)
print(list1)

print("bye")
