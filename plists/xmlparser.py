
import xml.etree.ElementTree as ET


def parserFor(node):
    return {
        'plist': parsePlistNode,
        'true': parseBooleanNode,
        'key': parseStringNode,
        'string': parseStringNode,
        'false': parseBooleanNode,
        'array': parseListNode,
        'dict': parseDictNode,
    }[node.tag]


def parseFile(string_or_stream):
    return parseNode(ET.parse(string_or_stream).getroot())


def parse(string_or_stream):
    """
    This class enables the parsing of an plist stream in the XML format and returns
    a dictionary or list object that is at the root of the plist stream.
    To use the scanner simply do: ::

        obj = parse(string_or_stream)
    """
    return parseNode(ET.fromstring(string_or_stream))


def parseNode(node):
    return parserFor(node)(node)


def parsePlistNode(node):
    return parseNode(node.getchildren()[0])


def parseBooleanNode(node):
    return node.tag == 'true'


def parseStringNode(node):
    return node.text


def parseListNode(listnode):
    return [parserFor(node)(node) for node in listnode.getchildren()]


def parseDictNode(dictnode):
    out = {}
    children = dictnode.getchildren()
    for i in xrange(0, len(children), 2):
        keyNode = children[i]
        valueNode = children[i + 1]
        out[parseNode(keyNode)] = parseNode(valueNode)
    return out
