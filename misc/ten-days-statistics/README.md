# 10 days of statistics

## Day 0: mean, median and modal

### Mean (also called average, represented by the `mu` greek letter)

The average of all the integers in a set of values. Here is the basic formula for calculating the mean of a set of `n` values:
```
mu = sum(x_i from 1 to n)/n
```
Where `x_i` is the `i_th` element of the set.

### Median

The midpoint value of a data set for which an equal number of samples are less than and greater than the value. For an odd sample size, this is the middle element of the sorted sample; for an even sample size, this is the average of the `2` middle elements of the sorted sample.

### Mode

The element(s) that occur most frequently in a data set. For the set `{1,1,1,2,2,3,4,4}`, the mode is because the number appears three times in the set and every other number in the set has a frequency `<3`. In contrast, the set `{1,2,3,4}` is multimodal because no number in the set appears more than `1` time, so every number in the set is a valid mode.

### Precision and Scale

These are important terms to understand when formatting your output:

- Precision refers to the number of significant digits in a number. For example, the numbers and both have a precision of `5`.
- Scale refers to the number of significant digits to the right of the decimal point. For example, the number `123.45` has a scale of `2` decimal places. This term is sometimes misrepresented as precision in documentation. 

### Setting precision in python

There are many ways to set precision of floating point value. Some of them is discussed below.
```python
# Python code to demonstrate precision 
# and round() 
  
# initializing value 
a = 3.4536
```

1. Using “%” :- “%” operator is used to format as well as set precision in python. This is similar to “printf” statement in C programming.
```python
# using "%" to print value till 2 decimal places  
print ("The value of number till 2 decimal place(using %) is : ",end="") 
print ('%.2f'%a) 
```

2. Using format() :- This is yet another way to format the string for setting precision.
```python
# using format() to print value till 2 decimal places  
print ("The value of number till 2 decimal place(using format()) is : ",end="") 
print ("{0:.2f}".format(a)) 
```

3. Using round(x,n) :- This function takes 2 arguments, number and the number till which we want decimal part rounded.
```python
# using round() to print value till 2 decimal places  
print ("The value of number till 2 decimal place(using round()) is : ",end="") 
print (round(a,2)) 
```
