import cStringIO


def writerFor(obj):
    return {
        dict: writeDict,
        list: writeList,
        str:  writeString,
        bool: writeBoolean
    }[type(obj)]


def makeIndentString(indentStr, level=0):
    out = ""
    if indentStr is not None:
        out = "\n" + (indentStr * level)
    return out


def write(obj, outstream=None, indentStr=None, level=0):
    outstream = outstream or cStringIO.StringIO()
    indStr = makeIndentString(indentStr, level)
    outstream.write("""%s<?xml version="1.0" encoding="UTF-8"?>""", indStr)
    outstream.write("""%s<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">""", indStr)
    outstream.write("""%s<plist version="1.0">""", indStr)
    writeObject(obj, outstream, indentStr, level)
    outstream.write("""%s</plist>""", indStr)
    return outstream


def writeObject(obj, outstream=None, indentStr=None, level=0):
    """
    Writes an object to an output stream
    """
    outstream = outstream or cStringIO.StringIO()
    return writerFor(obj)(obj, outstream, indentStr, level)


def writeList(listObject, outstream=None, indentStr=None, level=0):
    outstream = outstream or cStringIO.StringIO()
    indentString = makeIndentString(indentStr, level)
    outstream.write("%s<array>" % indentString)
    for value in listObject:
        writeObject(value, outstream, indentStr, level + 1)
    outstream.write("%s</array>" % indentString)
    return outstream


def writeDict(dictObject, outstream=None, indentStr=None, level=0):
    outstream = outstream or cStringIO.StringIO()
    indentString = makeIndentString(indentStr, level)
    outstream.write("%s<dict>" % indentString)
    for key, value in dictObject.iteritems():
        writeKey(key, outstream, indentStr, level + 1)
        writeObject(value, outstream, indentStr, level + 1)
    outstream.write("%s</dict>" % indentString)
    return outstream


def writeBoolean(value, outstream=None, indentStr=None, level=0):
    outstream = outstream or cStringIO.StringIO()
    outstream.write("%s<%s/>" %
                    (makeIndentString(indentStr, level),
                     ("true" if value else "false")))
    return outstream


def writeKey(key, outstream=None, indentStr=None, level=0):
    outstream = outstream or cStringIO.StringIO()
    outstream.write("%s<key>%s</key>" %
                    (makeIndentString(indentStr, level), str(key)))
    return outstream


def writeString(value, outstream=None, indentStr=None, level=0):
    outstream = outstream or cStringIO.StringIO()
    outstream.write("%s<string>%s</string>" %
                    (makeIndentString(indentStr, level), value))
    return outstream
