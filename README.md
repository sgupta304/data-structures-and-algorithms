Table of contents
=================

<!--ts-->
   * [Challenges](#challenges)
      * [Reverse an Array](#reverse-an-array)
      * [ArrayShift](#array-shift)
      * [Binary Search](#binary-search)
<!--te-->

# Challenges
## Reverse an Array
Write a function called `reverseArray` which takes an array as an argument. Without utilizing any of the built-in methods available to your language, return an array with elements in reversed order.

#### Example
|  Input | Output  | 
|---|---|
| ```[1, 2, 3, 4, 5, 6]```  |  ```[6, 5, 4, 3, 2, 1]``` | 
| ```[89, 2354, 3546, 23, 10, -923, 823, -12]```  |  ```[-12, 823, -923, 10, 23, 3546, 2354, 89]``` | 
| ```[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199]```  |  ```[199, 197, 193, 191, 181, 179, 173, 167, 163, 157, 151, 149, 139, 137, 131, 127, 113, 109, 107, 103, 101, 97, 89, 83, 79, 73, 71, 67, 61, 59, 53, 47, 43, 41, 37, 31, 29, 23, 19, 17, 13, 11, 7, 5, 3, 2]``` | 
	
Utilize the Single-responsibility principle: any methods you write should be clean, reusable, abstract component parts to the whole challenge. You will be given feedback and marked down if you attempt to define a large, complex algorithm in one function definition.

__Note__: There is no test requirement for Class01. Going forward you will be required to test any code you produce unless otherwise directed by your instructional team.

#### Approach & Efficiency/Solution
The approach I took for this was simple. 
* I loop through the array starting at the last index and looping until I reach the first.
* I added each element into a new array
* Then returned the newly created array since it has all the elements from the initial array in reverse
* The complexity of this solution is `O(n)` as it depends on the size of the array since we are iterating over all the elements in the initial array

#### Check List
- [ ] Take a photo of your completed whiteboard, matching the example whiteboard layout.
    - [ ] Copy your photo into an /assets directory in your repo
    - [ ] Give the image file the same name as the branch you are working on
    - [ ] Embed the image in your README.md documentation
- [x] Create a pull request from your branch to your master branch
- [x] In your open pull request, leave as a comment a checklist of the specifications and tasks above, with the actual steps that you completed checked off
- [x] Submitting your completed work to Canvas:
    - [x] Copy the link to your open pull request and paste it into the corresponding Canvas assignment
    - [x] Leave a description of how long this assignment took you in the comments box
    - [x] Add any additional comments you like about your process or any difficulties you may have had with the assignment
- [x] Merge your branch into master, and delete your branch (don’t worry, the PR link will still work)

## Array Shift
Write a function called `insertShiftArray` which takes in an array and the value to be added. Without utilizing any of the built-in methods available to your language, return an array with the new value added at the middle index.

#### Example
|  Input | Output  | 
|---|---|
| ```[2,4,6,8], 5```  |  ```[2,4,5,6,8]``` | 
| ```[4,8,15,23,42], 16```  |  ```[4,8,15,16,23,42]``` | 

#### Approach & Efficiency/Solution
The approach I took for this challenge was first to get the index where I should be inserting the new value. I need to find what the middle point is of the given array, even if it has an even number of elements or odd.
Once I knew that there were two approaches I took:
* One was to use the in build `insert()` function as it allows us to insert an element at a specified index. This function has complexity of `O(n)` since insert it depends on the size of the array. 
* The second approach I took was to loop through the array and insert elements into a new array from the previous array until I reach the index that is the mid point, at the instance I would insert the 
new value and increment the counter (For this approach I need to keep track of multiple counters as one is for the old array and one is for the new array) for the new array in order to "shift" all the elements from the 
previous array in the new array. 

#### Check List
 - [x] Top-level README “Table of Contents” is updated
 - [x] Feature tasks for this challenge are completed
 - [x] Unit tests written and passing
     - [x] “Happy Path” - Expected outcome
     - [x] Expected failure
     - [x] Edge Case (if applicable/obvious)
 - [x] README for this challenge is complete
     - [x] Summary, Description, Approach & Efficiency, Solution
     - [x] Link to code
     - [ ] Picture of whiteboard
   
## Binary Search
Write a function called `BinarySearch` which takes in 2 parameters: a sorted array and the search key. Without utilizing any of the built-in methods available to your language, return the index of the array’s element that is equal to the search key, or -1 if the element does not exist.

#### Example
|  Input | Output  | 
|---|---|
| ```[4,8,15,16,23,42], 15```  |  ```2``` | 
| ```[11,22,33,44,55,66,77], 90```  |  ```-1``` | 

#### Approach & Efficiency/Solution
The approach I took for this challenge was first to get the index where I should be inserting the new value. I need to find what the middle point is of the given array, even if it has an even number of elements or odd.
Once I knew that there were two approaches I took:
* One was to use the in build `insert()` function as it allows us to insert an element at a specified index. This function has complexity of `O(n)` since insert it depends on the size of the array. 
* The second approach I took was to loop through the array and insert elements into a new array from the previous array until I reach the index that is the mid point, at the instance I would insert the 
new value and increment the counter (For this approach I need to keep track of multiple counters as one is for the old array and one is for the new array) for the new array in order to "shift" all the elements from the 
previous array in the new array. 

#### Check List
 - [x] Top-level README “Table of Contents” is updated
 - [x] Feature tasks for this challenge are completed
 - [x] Unit tests written and passing
     - [x] “Happy Path” - Expected outcome
     - [x] Expected failure
     - [x] Edge Case (if applicable/obvious)
 - [x] README for this challenge is complete
     - [x] Summary, Description, Approach & Efficiency, Solution
     - [x] Link to code
     - [ ] Picture of whiteboard 
     
## Mock Interviews
* Read all of the following instructions carefully.
* Today, you and a peer will take turns interviewing each other with a code challenge
* The interviewer will score the candidate according to the Whiteboard Rubric
    * Notes can be taken in an electronic copy of the doc, or a print out of it
    * In either case, the completed rubric will be given to the candidate for review purposes
* The candidate submits the rubric with the score they achieved as a candidate
* Each interview should be timeboxed to a strict 30 minutes

Interview questions
* Don’t look at the interview questions until you decide who will be the first interviewer.
    1. The first interviewer will ask this [question](https://codefellows.github.io/common_curriculum/data_structures_and_algorithms/Code_401/class-04/interview-01.html)
    2. The second interviewer will ask this [question](https://codefellows.github.io/common_curriculum/data_structures_and_algorithms/Code_401/class-04/interview-02.html)

#### Example
##### Interview 01
Given a matrix, find the sum of each row.

|  Input | Output  | 
|---|---|
| ```[[1, 2, 3], [3, 5, 7], [1, 7, 10]]```  |  ```[6, 15, 18]``` | 
| ```[ [0, 1, 5], [-4, 7, 2], [-3, 12, 11] ]```  |  ```[6, 5, 20]``` | 

##### Interview 02
Generate the nth Fibonacci number, 2 different ways.

|  Input | Output  | 
|---|---|
| ```0```  |  ```0``` | 
| ```1```  |  ```1``` | 
| ```2```  |  ```1``` | 
| ```3```  |  ```2``` | 
| ```4```  |  ```3``` | 
| ```5```  |  ```5``` | 
| ```6```  |  ```8``` | 
| ```7```  |  ```13``` | 
| ```8```  |  ```21``` | 
| ```...```  |  ```...``` | 
| ```14```  |  ```377``` | 
| ```...```  |  ```...``` | 
| ```45```  |  ```1134903170``` | 
| ```...```  |  ```...``` | 

#### Approach & Efficiency/Solution
The approach I took for this challenge was to get traverse the row/column of each the multidimensional array.
Once I was done traversing the array, I took the sum of the current array and added the sum to a new list.
I, then, returned the list. The `Big-O` notation for this function would depend on the size of the array, so
the bigger the array, the bigger the time it would take to complete it. So it would be `O(n^2)`.

#### Check List
 - [x] Top-level README “Table of Contents” is updated
 - [x] Feature tasks for this challenge are completed
 - [x] Unit tests written and passing
     - [x] “Happy Path” - Expected outcome
     - [x] Expected failure
     - [x] Edge Case (if applicable/obvious)
 - [x] README for this challenge is complete
     - [x] Summary, Description, Approach & Efficiency, Solution
     - [x] Link to code
     - [ ] Picture of whiteboard 