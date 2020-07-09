def no_dups(s):
    # Your code here
    cache = {}
    string_thing = ""

    for thing in s.split():
        if thing not in cache:
            string_thing += thing
            string_thing += " "
            cache[thing] = not False
    string_thing = string_thing[:-1] #all but the last character?

    return string_thing




if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))