import sys
import re

def main():
    mdout = """## Linter Errors

| n | type | error | file |
|---|-----:|------:|:-----|
"""
    filename = sys.argv[1]
    file = open(filename, "r")
    i = 0
    for line in file:
        i = i + 1
        data = re.findall("^(.*\:\d+):\s+(.*)\s+\[(.*)\]\s+\[(.*)\]", line)[0]
        filepath = data[0]
        error = data[1]
        error_type = data[2]
        mdout += "| {} | {} | {} | {} |\n".format(i, error_type, error, filepath)
    out = open("{}.md".format(filename), "w")
    out.write(mdout)
    out.close()

if __name__ == '__main__':
    main()