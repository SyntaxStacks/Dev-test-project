#Find Source

##Problem definition
In a field, we have hidden an object with a radio transmitter. However, a battery failure has made it so that the transmitter emits pulses only once every 6 hours. You have already taken measurements at two points and, from the strength of the signal, determined the distance that the object must be from those points. Your job now is to write a program to find all of the locations, if any, where the object might be. You only have the two datapoints you have already taken, and you can’t wait to take any more.

Your program will be given an input file that contains two data points that look like the following, each on a separate line. 

<x position> <y position> <distance from object>

For example, consider the following input:
***
6.0 8.0 5.0
0.0 0.0 5.0
***

Then the output of your program should be:
***
3.0 4.0
***
which indicates that the object must reside at coordinates x = 3, y = 4.

##Summary of my solution


##Resources

* http://mathworld.wolfram.com/Circle-CircleIntersection.html
* http://www.ambrsoft.com/TrigoCalc/Circles2/Circle2.htm
