
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
```

### Reading V1 (Old Style) plists from string

```
import plists

obj = plists.v1parser.parse("some_loaded_string")
```


### Reading XML plists from file

```
from plists import xmlparser

obj = xmlparser.parseFile("path_to_file")
```

### Reading XML plists from string

```
from plists import xmlparser

obj = xmlparser.parse("some_loaded_string")
```

### Reading Binary plists

Coming Soon
