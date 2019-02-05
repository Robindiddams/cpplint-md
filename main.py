import sys
import re

def main():
    mdout = """## Linter Errors

| file | error |
|:-----|:------|
"""
    filename = sys.argv[1]
    file = open(filename, "r")
    errors = False
    for line in file:
        data = re.findall("^(.*\:\d+):\s+(.*)\s+\[(.*)\]\s+\[(.*)\]", line)
        if (data):
            errors = True
            data = data[0]
            filepath = data[0]
            error = data[1]
            # error_type = data[2]
            mdout += "| {} | {} |\n".format(filepath, error)
    postfix = ""
    contents = """## No linter Errors :tada:
    """
    if (errors):
        postfix= "_errors"
        contents = mdout
    out = open("{}{}.md".format(filename, postfix), "w")
    out.write(contents)
    out.close()

if __name__ == '__main__':
    main()