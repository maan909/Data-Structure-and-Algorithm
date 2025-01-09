def palindrome(word: str):
    reverse_str = word[::-1]
    if word == reverse_str:
        return True
    else:
        return False
print(palindrome("nayan"))


def average(num: list):
    n = len(num) - 1
    total = 0 
    for i in num:
        total += i
    average = total/n
    return average
list = [1,2,3,4,5,6]
print(average(list))
print(list[::-1])