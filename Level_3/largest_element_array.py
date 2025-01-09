class Calculating_Largest:
    def largest_element(num: list[int]):
        largest = num[0] 
        for i in range(1, len(num)):
            if num[i] > largest:
                largest = num[i]

        return largest
    
#---------------------------------------------OR-------------------------------------------------

    def second_method(num2: list[int]):
        num2.sort()
        return num2[-1]


if __name__ == '__main__':
    num = [2,1,23,35,16]
    obj1 = Calculating_Largest
    
    print(f'Largest Element using 1st method is {obj1.largest_element(num)}')
    print(f"Largest Element using 2nd method is {obj1.second_method(num)}")

