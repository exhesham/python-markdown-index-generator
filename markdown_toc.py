import re
with open('./README.md') as f:
    for line in f:
        if re.match(r'^#+ ', line):
            title = re.sub('#','',line).strip()
            hash = title.lower().replace(' ','-')
            manipulated_line = '**[%s](#%s)**' % (title,hash)
            tabs = re.sub('#','\t',line.strip()[:line.strip().index(' ')+1])
            print tabs+ '* ' + manipulated_line