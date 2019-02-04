# CPP lint MD
A tool that converts the output of `cpplint --quiet` into a nice md table for me to use with danger

## Run it 
like this
```bash
python main.py <cpplint output>
```

## Example
```bash
cpplint --recursive --quiet myproject/Source 2>lintout
python main.y lintout
# and poof one lintout.md is made
```