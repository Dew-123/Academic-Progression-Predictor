# Academic-Progression-Predictor

This is a python program to predict progression outcomes at the end of each academic year.

Progression outcomes as defined by the University regulations (see the table).

![Screenshot 2024-02-10 201121](https://github.com/Dew-123/Academic-Progression-Predictor/assets/128276406/db6496e5-2f00-4907-886c-55e2a42088af)

## Part 1 - Main Version

### A. Outcomes
• The program allows students to predict their progression outcome at the end of each academic year. The program prompt for the number of credits at pass, defer and fail and then display the appropriate progression outcome for an individual student (i.e., progress, trailing, module retriever or exclude).
 
### B. Validation 
• The program display ‘Integer required’ if a credit input is the wrong data type. 
• The program display ‘Out of range’ if credits entered are not in the range 0, 20, 40, 60, 80, 100 and 120. 
• The program display ‘Total incorrect’ if the total of the pass, defer and fail credits is not 120. 
• An example of the program running with user input (shown in bold): 

**Please enter your credits at pass:** p

Integer required 

**Please enter your credits at pass:** 140

Out of range. 

**Please enter your credits at pass:** 100

**Please enter your credit at defer:** 40

**Please enter your credit at fail:** 20

Total incorrect. 

**Please enter your credits at pass:** 100

**Please enter your credit at defer:** 20

**Please enter your credit at fail:** 0

Progress (module trailer) 

### C. Multiple Outcomes
• The program loops to allow a staff member to predict progression outcomes for multiple students. 
• The program prompt for credits at pass, defer and fail and display the appropriate progression for each individual student until the staff member enters ‘q’ to quit. Optionally you can use an input of ‘y’ to continue. 
• See example of program run combined with Histogram below. 

### D. Histogram
• When ‘q’ is entered, the program produces a ‘histogram’ where each star represents a student who achieved a progress outcome in the category range: progress, trailing, module retriever and exclude. The histogram relates to the data input entered during the program run and work for any number of outcomes. 
• Display the number of students for each progression category and the total number of students. 
• Example of a program run and input (in bold). Note: program should exit on ‘q’ to quit. ‘y’ to continue shown in the example is optional and depends on your program structure. 

Example Output: 
**Enter your total PASS credits:** 120
**Enter your total DEFER credits:** 0
**Enter your total FAIL credits:** 0
Progress 

Would you like to enter another set of data? 
Enter 'y' for yes or 'q' to quit and view results: y
**Enter your total PASS credits:** 100
**Enter your total DEFER credits:** 0
**Enter your total FAIL credits:** 20
Progress (module trailer) 

Would you like to enter another set of data? 
Enter 'y' for yes or 'q' to quit and view results: y 
**Enter your total PASS credits:** 80
**Enter your total DEFER credits:** 20
**Enter your total FAIL credits:** 20
Module retriever 

Would you like to enter another set of data? 
Enter 'y' for yes or 'q' to quit and view results: y
**Enter your total PASS credits:** 60
**Enter your total DEFER credits:** 0
**Enter your total FAIL credits:** 60
Module retriever 

Would you like to enter another set of data? 
Enter 'y' for yes or 'q' to quit and view results: y
**Enter your total PASS credits:** 40
**Enter your total DEFER credits:** 0
**Enter your total FAIL credits:** 80
Exclude 

Would you like to enter another set of data? 
Enter 'y' for yes or 'q' to quit and view results: q 

--------------------------------------------------------------- 
Histogram 

Progress 1 : * 
Trailer 1 : * 
Retriever 2 : ** 
Excluded 1 : * 

5 outcomes in total. 

## Part 2 – List (extension) 
For Part 1, most of the solutions would use variables to store the input data. For Part 2, extend your solution so that the program saves the input progression data to a list or nested list. Then access the stored data from the list and print the data in the following format below. Test plan not required. 

Example Output: The following should display after the histogram 

## Part 2 – List (extension)
the program saves the input progression data to a list or nested list

Example Output:

Progress - 120, 0, 0 
Progress (module trailer) - 100, 0, 20 
Module retriever - 80, 20, 20 
Module retriever - 60, 0, 60 
Exclude – 40, 0, 80 

## Part 3 - Text File
Example Output:

Progress - 120, 0, 0 
Progress (module trailer) - 100, 0, 20 
Module retriever - 80, 20, 20 
Module retriever - 60, 0, 60 
Exclude – 40, 0, 80 

## Part 4 – Dictionary (separate program)
Example Output:

w1234567 : Progress - 120, 0, 0 w1234566 : 
Progress (module trailer) - 100, 0, 20 w1234565 
: Module retriever - 80, 20, 20 w1234564 : 
Module retriever - 60, 0, 60 w1234563 : Exclude 
– 40, 0, 80
