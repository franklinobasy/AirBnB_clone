import re

# pattern = re.compile(r"(\w+)\.(\w+)\(((\"[\w-]+\"),?\s?(\"\w+\")?,?\s?(\"?\w+\"?)?)?\)")

# pattern1 = re.compile(r"{(([\"\']\w+[\"\'])\s?:\s?([\"\']?\w+[\"\'])?, \s?)+}")
# pattern2 = re.compile(r"([\"\']\w+[\"\'])\s?:\s?([\"\']?\w+[\"\']?)+")
# pattern1 = re.compile(r"(\w+)\.(\w+)\(\"([\w-]+)\",")
# pattern1 = re.compile(r"(\w+)\.(\w+)\(\"([\w-]+)\",\s?{([\w:\'\",\s]+)}")

pattern = re.compile(r"(\w+)\.(\w+)\((\"[\w-]+\"),\s?\{(.+)\}\)")
while True:
    line = input("(hbnb)$ ")
    match = pattern.search(line)
    print(match.groups()[0])
    print(match.groups()[1])
    print(match.groups()[2])
    print(match.groups()[3])
    dict_pattern = re.compile(r"[\'\"](\w+)[\'\"]\s?:\s?[\'\"]?(\w+)[\'\"]?,?\s?")
    match2 = dict_pattern.finditer(match.groups()[3])
    for m in match2:
        for part in m.groups():
            print(part)
#

#User.update("38f22813-2753-4d42-b37c-57a17f1e4f88", {'first_name': "John", "age": 89})