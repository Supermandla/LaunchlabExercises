
def switch():
    userString = input("Please input the word you want to reverse")
    new = ""
    for i in userString:
        new = i + new
    print(new)

switch()
