#String Manipulation

##Problem Definition
Write a function to compact a string in place: 
A.	strip whitespace from the string.
B.	remove duplicate characters if they are next to each other

For example, consider the following input:
***
abb cddpddef gh
***

Then the output of your program should be:
***
abcdpdefgh
***


##Summary of my solution

###Strings in Python are immutable

Because strings in Python are immutable, I'm opting to leverage Python'sregex positive lookahead support to minimize the lines of code required.  Another approach to consider is converting the targetString to a list or bytearray, iterating over each character, and producing a new string to return. Both methods break the "in place" constraint in the requirements.

###regex: 

(.)(?=(\s+)?\1)|\s+

###regex sandbox

rubular: [http://rubular.com/r/1N7cbD90XB](http://rubular.com/r/1N7cbD90XB)

###test strings:

* ab b b c c cd defgg gf
* abb cddpddef gh
* abcd deffghhii

## Resources:
* http://www.rexegg.com/regex-lookarounds.html
* http://www.regular-expressions.info/lookaround.html

