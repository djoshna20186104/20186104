#Guess My Number Exercise

def main():
    l = 0
    h = 100
    a = input()
    while a !=  "c":
        s=(l+h)//2 
        print ("Is your secreat number is" + str(s) )
        a=input()
        if a == "c":
            break
        elif a == "l":
            l=s
        elif a == "h":
            h=s
    print(" your secreat number was " + str(s))

if __name__== "__main__":
	main()