
import sys
import re
import string

TRANSLATOR=str.maketrans(' ',' ', string.punctuation)

def clean(text):

    cln = text.lower()

    # strip out punctuation
    cln = cln.translate(TRANSLATOR)
    cln = re.sub('\s+', ' ', cln)

    # clean out words that are less than or equal to 2 chars
    toks = cln.split(' ')
    # put each word on a new line for easier reading
    cln = '\n'.join(t for t in toks if len(t) >= 3)

    return cln


if __name__ == '__main__':

    infile = sys.argv[1]
    outfile = sys.argv[2]

    # get text string
    text = open(infile, encoding='utf-8', errors='ignore').read()

    # clean the text
    outstr = clean(text)

    # write final output
    with open(outfile, 'w') as out:
        out.write(outstr)

