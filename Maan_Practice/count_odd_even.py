def count(num: list):
    even = 0
    odd = 0 

    for i in num:
        if i % 2 == 1:
            odd += 1
        else:
            even += 1

    print(f'{odd} are odds and {even} are evens')
    return even, odd



if __name__ == '__main__':
    list = [1,2,3,4,5,6,7,8,9,10,11]

    count(list)
    