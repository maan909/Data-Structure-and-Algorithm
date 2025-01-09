def armstrong(num: int) -> bool:
    digits = []
    temp = num
    while temp > 0:
        digit = temp % 10
        digits.append(digit)
        temp = temp // 10
        
    
    print(digits)

    counter = 0

    for i in digits:
        counter += i**3
    return counter == num


print(armstrong(153))