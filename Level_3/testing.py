list = [1,2,23,4,5,67,8]

for i in list:
    print(i)
    # print(list[i])

for i in list:
    print(i)


largest = second = -1

for i in list:
    if i > largest:
        second = largest
        largest = i 
    elif i > second and i!=largest:
        second = i 

print (f"{second} is second largest number")
print("---------------")
print(2%5)