# Topsis implemented by Nipun Garg 102003674

[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)  
[![Python 3.6](https://img.shields.io/badge/python-3.6-blue.svg)](https://www.python.org/downloads/release/python-360/)

## Functionality of the Package

- Outputs the result(topsis score) and ranking of items in output.csv file you will mention in terminal or command promt
- Inputs the file path of input csv file in terminal

## Example

```
#test.py
##
type:
from Topsis_Nipun_Garg_102003674 import main
n=len(sys.argv)
inputFile= sys.argv[1]
weight=sys.argv[2]
impact=sys.argv[3]
outputFile=sys.argv[4]
# main.get_score(inputFile, weight, impact, outputFile)
```

## Usage

- Make sure you have Python installed in your system.
- Run Following command in the CMD.

```
 pip install Topsis_Nipun_Garg_102003674
```

## Run the following Script.

```
 python <Filename.py> <inputfile.csv> weight impact <outputfile.csv>
```

## Note

- I have tried to implement all the functionality, it might have some bugs also. Ignore that or please try to solve that bug.
- Rank 1 corresponds to minimum performance score and so on.
