
def makeIndentString(indentStr, level=0):
    out = ""
    if indentStr is not None:
        out = "\n" + (indentStr * level)
    return out
