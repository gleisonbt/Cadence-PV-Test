# Cadence PV Test
## Solution of Cadence's Product Verification Tests

### Questions


#### 1. Algorithms and Data Structures

1.2 You were given an array of unknown length containing sorted elements that if you access a random position out of the bounds of the array an exception is thrown. Describe an efficient algorithm to search an element.

1.3 Consider the graph to the right:

a)	Starting on node 1, and always visiting nodes from left to the right:

i.	Write the numbers corresponding to the nodes in the order  

ii.	Now do the same using a DFS

b)	Describe an algorithm that could be used to find a path between two nodes of this graph. Give a high-level explanation of it and justify why you chose it


#### 2.	Product Verification

1.4	Write a function that gets a list of songs and needs to play the songs randomly so that in each play each song will only be heard once. The number of songs is unknown.


#### 3.	Scripting

A certain system needs a password validator module, which upon receiving a string with a password and a list with the requirements of this password, return whether the password is valid or not. The list of the password requirements is composed of tuples containing the following:
-	First value:
    - LEN – password length
    - LETTERS – # of letters
    - NUMBERS – # of numbers
    - SPECIALS – # of special characters
  
-	Second value: <, > or =
-	Third value: an integer number

Ex.:
req = [(‘LEN’, ‘=’, 8), (‘SPECIALS’, ‘>’, 1)]

req specify a password with eight characters and at least two special characters.

3.1	Write a Python 3 script to solve this problem and the unit test to validate it, without installing external packages. 
