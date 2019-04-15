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

## Day 1: Quartiles

### Quartile

The quartiles of an ordered data set are the `3` points that split the data set into `4` equal groups. The `3` quartiles are defined as follows:

    1. `Q_1` The first quartile is the middle number between the smallest number in a data set an its median.
    2. `Q_2` The second quartile is the median (`50_th` percentile) of the data set.

    3. `Q_3` The third quartile is the middle number between a data set's median and its largest number.

#### Computing the First and Third Quartile

We will use the first method described in the Wikipedia:

We will split the data into two halves, lower half and upper half:

    - If there are an odd number of data points in the original ordered data set, do not include the median (the central value in the ordered list) in either half.

    - If there are an even number of data points in the original ordered data set, split this data set exactly in half.

The value of the first quartile (`Q_1`) is the median of the lower half and the value of the third quartile (`Q_3`) is the median of the upper half.

#### Example 1

We will consider the following ordered dataset for this example:
```python
    6, 7, 15, 36, 39, 40, 41, 42, 43, 47, 49
```
The median of the dataset is `40`. As there are an odd number of data points, we do not include the median (the central value in the ordered list) in either half:
```python
    Lower half: 6, 7, 15, 36, 39

    Upper half: 41, 42, 43, 47, 49
```
The median of the lower half is `15`, so the value of the first quartile is `15`, and the median of the upper half is `43`, so the value of the third quartile is `43`.

#### Example 2

We will consider the following ordered dataset for this example:
```python
    7, 15, 36, 39, 40, 41
```
As there are an even number of data points in the original ordered data set, we will split this data set exactly in half:
```python
    Lower half: 7, 15, 36

    Upper half: 39, 40, 41
```
The median of the lower half is `15`, so the value of the first quartile is `15`, and the median of the upper half is `40`, so the value of the third quartile is `40`.

### Expected Values

The expected value of a discrete random variable, `X`, is more or less another way of referring to the mean (`mu`). We can also refer to this as the mathematical expectation (or just the expectation) of `X`.

### Variance `sigma^2`

This is the average magnitude of fluctuations of `X` from its expected value, `mu`. You can also think of it as the expectation of a random variable's squared deviation from its mean. Given a data set, `X` , of size `n`:
```python
    sigma^2 = sum((x_i-mu)**2 for i from 1 to n)/n
```

where `x_i` is the `i_th` element of the data set and is the mean of all the elements.

### Standard Deviation `sigma`

The standard deviation quantifies the amount of variation in a set of data values. Given a data set, `X`, of size `n`:
```python
    sigma = sqrt ( sum( (x_i-mu)**2 for i from 1 to n )/n )
```
where `x_i` is the `i_th` element of the data set and `mu` is the mean of all the elements. 