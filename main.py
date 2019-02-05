import sys
import re

def main():
    mdout = """## Linter Errors

| file | error |
|:-----|:------|
"""
    filename = sys.argv[1]
    file = open(filename, "r")
    for line in file:
        data = re.findall("^(.*\:\d+):\s+(.*)\s+\[(.*)\]\s+\[(.*)\]", line)
        if (data):
            data = data[0]
            filepath = data[0]
            error = data[1]
            # error_type = data[2]
            mdout += "| {} | {} |\n".format(filepath, error)
    out = open("{}.md".format(filename), "w")
    out.write(mdout)
    out.close()

if __name__ == '__main__':
    main()