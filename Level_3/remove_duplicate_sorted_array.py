def remove_duplicate(num: list):
    if not num:
        return 0
    k=1
    for i in range(1, len(num)):
        if num[i] != num[k-1]:
            num [k]= num[i]
            k+=1
    print(k)

#---------------------------------------------------------------OR--------------------------------------------------------

def using_set_function(num: list):
    new_num = set(num)
    

    return list(new_num)


if __name__ == '__main__':
    num = [3,1,1,2,0,4,5]
    num2 = [4,4,5,3,1,0]
    num3 = [0,0,1,1,1,2,2,3,4,5,6]
    remove_duplicate(num2)
    # print(using_set_function(num3))

