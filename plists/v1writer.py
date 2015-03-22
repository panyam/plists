import cStringIO
from utils import makeIndentString
import v1parser


def writerFor(obj):
    if isinstance(obj, dict):
        return writeDict
    return {
        v1parser.Token: writeToken,
        dict: writeDict,
        list: writeList,
        str:  writeString,
        bool: writeBoolean
    }[type(obj)]


def write(obj, outstream=None, indentStr=None, level=0):
    outstream = outstream or cStringIO.StringIO()
    pos = outstream.tell()
    writeObject(obj, outstream, indentStr, level)
    outstream.seek(pos)
    return outstream


def writeObject(obj, outstream=None, indentStr=None, level=0):
    """
    Writes an object to an output stream
    """
    outstream = outstream or cStringIO.StringIO()
    return writerFor(obj)(obj, outstream, indentStr, level)


def writeDict(dictObject, outstream=None, indentStr=None, level=0):
    outstream = outstream or cStringIO.StringIO()
    indentString = makeIndentString(indentStr, level)
    outstream.write("{")
    for key, value in dictObject.iteritems():
        writeKey(key, outstream, indentStr, level + 1)
        writeObject(value, outstream, indentStr, level + 1)
        outstream.write(";")
    outstream.write("%s}" % indentString)
    return outstream


def writeList(listObject, outstream=None, indentStr=None, level=0):
    outstream = outstream or cStringIO.StringIO()
    indentString = makeIndentString(indentStr, level)
    nextIndentString = makeIndentString(indentStr, level + 1)
    outstream.write("(")
    for value in listObject:
        outstream.write(nextIndentString)
        writeObject(value, outstream, indentStr, level + 1)
        outstream.write(";")
    outstream.write("%s)" % indentString)
    return outstream


def writeKey(key, outstream=None, indentStr=None, level=0):
    outstream = outstream or cStringIO.StringIO()
    outstream.write("%s%s = " %
                    (makeIndentString(indentStr, level), str(key)))
    return outstream


def writeString(value, outstream=None, indentStr=None, level=0):
    outstream = outstream or cStringIO.StringIO()
    outstream.write("\"%s\"" % value)
    return outstream


def writeBoolean(value, outstream=None, indentStr=None, level=0):
    outstream = outstream or cStringIO.StringIO()
    outstream.write("%s" % "YES" if value else "NO")
    return outstream


def writeToken(token, outstream=None, identStr=None, level=0):
    outstream = outstream or cStringIO.StringIO()
    if token.toktype == v1parser.TOKEN_STRING:
        outstream.write("\"%s\"" % str(token.value))
    else:
        outstream.write("%s" % str(token.value))
    return outstream

