
# What is this?

This is a package for reading, writing and managing [Apple plist files](https://developer.apple.com/library/mac/documentation/Darwin/Reference/ManPages/man5/plist.5.html).  

# Installation

```
pip install plists
```

# Examples

## Reading plist files

### Reading V1 (Old Style) plists from file

```
import plists

obj = plists.v1parser.parseFile("path_to_file")

# ... use obj as a normal python object
```

### Reading V1 (Old Style) plists from string

```
import plists

obj = plists.v1parser.parse("some_loaded_string")

# ... use obj as a normal python object
```


### Reading XML plists from file

```
from plists import xmlparser

obj = xmlparser.parseFile("path_to_file")

# ... use obj as a normal python object
```

### Reading XML plists from string

```
from plists import xmlparser

obj = xmlparser.parse("some_loaded_string")

# ... use obj as a normal python object
```

### Reading Binary plists

Coming Soon


## Writing objects to plist files

### Writing to Old style plists

Objects can be written to old style plists with:

```
from plists import v1parser
from plists import v1writer

obj = v1parser.parseFile(<path_to_plist_file>)

v1writer.write(obj, outstream, indentString, level)
```

The parameters are:

* obj         -   The object being serialized
* outstream   -   The output stream to which the object will be serialized.  If this is None, then a new string outputstream is written to and returned.
* indentString  - Indentation string to be used.  If this value is None then no indentation or pretification is applied.  Otherwise this is used.
* level       -   The level to start with when serializing.  Each child node is indented an extra level (if indentString is not None).

### Writing to XML plists

Objects can be written to xml plists with:

```
from plists import xmlparser
from plists import xmlwriter

obj = xmlparser.parseFile(<path_to_plist_file>)

xmlwriter.write(obj, outstream, indentString, level)
```

The parameters are:

* obj         -   The object being serialized
* outstream   -   The output stream to which the object will be serialized.  If this is None, then a new string outputstream is written to and returned.
* indentString  - Indentation string to be used.  If this value is None then no indentation or pretification is applied.  Otherwise this is used.
* level       -   The level to start with when serializing.  Each child node is indented an extra level (if indentString is not None).

### Writing to Binary plists

Coming Soon.
