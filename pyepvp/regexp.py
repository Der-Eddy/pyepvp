import re

def match(pattern, string):
    match = re.search(re.compile(pattern), str(string))
    try:
        match = match.group(1)
    except AttributeError:
        match = ""
    finally:
        return match


def debug(file, text):
    with open(file, 'w') as file_:
        file_.write(text)