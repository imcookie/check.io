import string


def checkio(data: str) -> bool:
    cond1 = False
    cond2 = False
    cond3 = False
    if len(data) < 10:
        return False
    for i in range(0, len(data)):
        if data[i] in string.ascii_lowercase:
            cond1 = True
        elif data[i] in string.ascii_uppercase:
            cond2 = True
        elif data[i] in string.digits:
            cond3 = True

    if cond1 and cond2 and cond3:
        return True
    else:
        print(cond1, cond2, cond3)
        return False


print(checkio("ULFFunH8ni"))
