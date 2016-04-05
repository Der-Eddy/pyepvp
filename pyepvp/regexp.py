import re

def match(pattern, string, elseReturn=""):
    '''
    For easier regexp match using.
    '''
    match = re.search(re.compile(pattern), str(string))
    try:
        match = match.group(1)
    except AttributeError:
            match = elseReturn
    finally:
        return match

def htmlTag(tag, string):
    '''
    Retrieves the content between a provided HTML tag.
    '''
    nlineMatch = match("<{0}>\s+(.+)\s+<\/{0}>".format(tag), string)
    if len(nlineMatch) > 0:
        return nlineMatch
    else:
        return match("<{0}>(.+)<\/{0}>".format(tag), string)


def debug(content, debugFile='debug.html'):
    '''
    Saves a retrieved HTML page for debug purpose.
    '''
    logging.info("Debug Content Length: " + len(content))
    with open(os.path.dirname(os.path.abspath(sys.argv[0])) + "/" + debugFile, 'wb') as file_:
        file_.write(content.encode("utf-8"))
