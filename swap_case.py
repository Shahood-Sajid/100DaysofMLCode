def swap_case(s):
    new = ""
    for i in s:
        if i.isupper() == True:
            new  += i.lower()
        elif i.islower() == True:
            new += i.upper() 
        else:
            new += i
    return new

if __name__ == '__main__':
    s = input("Enter sentence: ")
    result = swap_case(s)
    print(result)