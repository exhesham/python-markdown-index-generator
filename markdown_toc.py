import re
import argparse
parser = argparse.ArgumentParser(description='generate table of contents for md file')
parser.add_argument('--file', help='The file to run the markdown on',  default="README.md", nargs=1, required=True)
args = parser.parse_known_args()
filename = args[0].file[0]
with open(filename) as f:
    for line in f:
        if re.match(r'^#+ ', line):
            title = re.sub('#','',line).strip()
            hash = title.lower().replace(' ','-')
            manipulated_line = '**[%s](#%s)**' % (title,hash)
            tabs = re.sub('#','\t',line.strip()[:line.strip().index(' ')+1])
            print tabs+ '* ' + manipulated_line
