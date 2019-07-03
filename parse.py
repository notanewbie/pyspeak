def harshChars(t):
    t = t.replace("'", "")
    t = t.replace('"', "")
    return t
def parseChars(t):
    t = t.replace("?", "")
    t = t.replace('"', "")
    t = t.replace('PH/', "")
    t = t.replace('\n', "")
    t = t.replace('<', "")
    t = t.replace('>', "")
    t = t.replace('/', "")
    t = t.replace(':', "")
    t = t.replace('*', "")
    t = t.replace('\\', "")
    return t
