#!/usr/bin/env python3
"""Usage:
    extract_link.py <link>
    extract_link.py -i <link> -o FILE

-h, --help   show this help message and exit
--version    show program's version number and exit
-i <link>    specify input link
-o FILE      specify output file [default: ./extracted_links.txt]
"""

from docopt import docopt
from extracter import *

args = docopt(__doc__, version='1.0.0')

if args['<link>']:
    extracter(args['<link>'], args['-o'])
elif args['-i']:
    extracter(args['-i'], args['-o'])
