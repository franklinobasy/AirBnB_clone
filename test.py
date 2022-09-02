import re

pattern = re.compile(r"(\w+)\.(\w+)\(((\"[\w|-]+\"),?\s?[(\"\w+\")|{'\w+':}]?,?\s?(\"?\w+\"?)?)?\)")


while True:
    line = input("(hbnb)$ ")
    match = re.search(pattern, line)
    print(match)
    if match:
        for i in match.groups():
            print(i)