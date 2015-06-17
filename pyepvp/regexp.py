import re

def match(pattern, string):
    match = re.search(re.compile(pattern), str(string))
    try:
        match = match.group(1)
    except AttributeError:
            match = ""
    finally:
        return match

def htmlTag(tag, string):
    nlineMatch = match("<{0}>\s+(.+)\s+<\/{0}>".format(tag), string)
    if len(nlineMatch) > 0:
        return nlineMatch
    else:
        return match("<{0}>(.+)<\/{0}>".format(tag), string)


def debug(file, text):
    with open(file, 'w') as file_:
        file_.write(text)