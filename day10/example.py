from unicodedata import name


def nameFormat(nameF, nameL):
    name1=nameF.title()
    name2=nameL.title()
    return f"{name1} {name2}"
stringFormat = nameFormat("faisal", "moose")
print(stringFormat)

