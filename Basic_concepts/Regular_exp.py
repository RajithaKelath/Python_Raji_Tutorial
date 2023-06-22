"""
import re

price = 'Price $1,823.839'
expression = '[A-z]* \$([0-9,]*\.[0-9]*)'

matches = re.search(expression, price)
print(matches[0])
print(matches[1])

number_without_comma = matches[1].replace(',','')
convert_float = float(number_without_comma)

print(convert_float)
"""

import re
"""
Our definition of a secure filename is:
- The filename must start with an English letters or a number (a-zA-Z0-9).
- The filename can **only** contain English letters, numbers and symbols among these four: `-_()`.
- The filename must end with a proper file extension among `.jpg`, `.jpeg`, `.png` and `.gif`
"""


def is_filename_safe(filename):
    # you only need to change the regular expression (regex) below
    #regex = '^[a-zA-Z0-9][a-zA-Z0-9_()-]*(\.jpg|\.jpeg|\.png|\.gif)$'
    regex = '^([A-Za-z0-9])[A-z0-9\-_()]*\.(jpg|jpeg|png|gif)$'
    match = re.match(regex, filename)
    print(match)
    return re.match(regex, filename) is not None

print(is_filename_safe('738-newfile.jpg'))
print(is_filename_safe('New_file.png'))
print(is_filename_safe('new_file.png'))
print(is_filename_safe('new_(file).png'))
print(is_filename_safe('__new_(file).png'))
print(is_filename_safe('__New_(fi-le).png'))

"""
price = '78new_(file).png'
expression = '^[0-9]*'

matches = re.match(expression, price)
print(matches[0])

"""