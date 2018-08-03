"'#Guess My Number Exercise'"

def main():
    l = 1
    h = 100
    a = input()
    while a != "c":
        s = (l + h)//2
        print("is your secret number is" +str(s))
        a = input()
        if a == "c":
            break
        elif a == "l":
            l = s
        elif a == "h":
            h = s
    print("your secret number is " + str(s))
    
if __name__== "__main__":
    main()