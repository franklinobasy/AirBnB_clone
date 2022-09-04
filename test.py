import re

pattern = re.compile(r"(\w+)\.(\w+)\(((\"[\w-]+\"),?\s?(\"\w+\")?,?\s?(\"?\w+\"?)?)?\)")

pattern1 = re.compile(r"{(([\"\']\w+[\"\'])\s?:\s?([\"\']?\w+[\"\'])?, \s?)+}")

# pattern1 = re.compile(r"(\w+)\.(\w+)\(\"([\w-]+)\",")
while True:
    line = input("(hbnb)$ ")
    match = re.search(pattern1, line)
    print(match)
    print(match.groups())
#

#User.update("38f22813-2753-4d42-b37c-57a17f1e4f88", {'first_name': "John", "age": 89})