int_input = int(input())
    digit_product = 0
    rem = 0
    digit = 0
    if n = 0:
        print("0")
    while n >= 0:
        rem = n % 10
        print(rem)
        digit = rem*1
        digit_product = digit*rem
        n = n//10
    print(digit_product)