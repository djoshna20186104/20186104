'''
Given a  number int_input, find the product of all the digits
example:    input: 123    output: 6
'''


def main():
    '''
    Read any number from the input, store it in variable int_input.
    '''
    int_input = int(input())
    digit_product = 0
    rem = 0
    digit = 0
    if(n == 0):
        print("0")
    while n >= 0:
        rem = (n % 10)
        print(rem)
        digit = (rem*1)
        digit_product = digit*rem
        n = n//10
    print(digit_product)
if __name__ == "__main__":
    main()
