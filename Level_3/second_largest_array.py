class second_largest:
    def method1(num: list[int]):
        largest = second = -1

        for i in num:
            # print(num[i])
            if i > largest:
                second = largest
                largest = i
            elif i > second and i!=largest:
                second = i
                        
        return second
    
#---------------------------------------------OR------------------------------------------------
    
    def method2(num : list[int]):
        num.sort()
        return num[-2]
    
if __name__ == '__main__':
    num = [3,2,4,8,34]
    object = second_largest
    print(object.method2(num))
    print(object.method1(num))