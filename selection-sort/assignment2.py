# -*- coding: utf-8 -*-
"""
Created on Tue Oct  9 23:35:56 2018

@author: jtotten
"""

import random
import numpy as np
from numpy.random import seed
from numpy.random import randint
import matplotlib.pyplot as plt
import time

###############################################################################
###############################################################################
# Sort algorithms 

#create selection sort algorithms
  
# Finds the smallest value in an array
def findSmallest(arr):
  # Stores the smallest value
  smallest = arr[0]
  # Stores the index of the smallest value
  smallest_index = 0
  for i in range(1, len(arr)):
    if arr[i] < smallest:
      smallest_index = i
      smallest = arr[i]      
  return smallest_index

# Sort array
def selectionSort(arr):
  newArr = []
  for i in range(len(arr)):
      # Finds the smallest element in the array and adds it to the new array
      smallest = findSmallest(arr)
      newArr.append(arr.pop(smallest))
  return newArr

print(selectionSort([5, 3, 6, 2, 10]))

# quickSort
def quicksort(array):
  if len(array) < 2:
    # base case, arrays with 0 or 1 element are already "sorted"
    return array
  else:
    # recursive case
    pivot = array[0]
    # sub-array of all the elements less than the pivot
    less = [i for i in array[1:] if i <= pivot]
    # sub-array of all the elements greater than the pivot
    greater = [i for i in array[1:] if i > pivot]
    return quicksort(less) + [pivot] + quicksort(greater)

print(quicksort([10, 5, 2, 3]))
###############################################################################
# create random number arrays of 5,000, 10,000, 15,000, 20,000, 25,000
# seed random number generator 

np.random.seed(seed=123)
small = np.random.randint(99999, size=5000).tolist()

np.random.seed(seed=123)
medium = np.random.randint(99999, size=10000).tolist()

np.random.seed(seed=123)
big = np.random.randint(99999, size=15000).tolist()

np.random.seed(seed=123)
bigger = np.random.randint(99999, size=20000).tolist()

np.random.seed(seed=123)
biggest = np.random.randint(99999, size=25000).tolist()

np.random.seed(seed=123)
z = np.random.randint(99999, size=256).tolist()

###############################################################################
# find the smallest value in an array

# z warmup
z  = np.sort(z)

# findSmallest - small array
sm_findsm_start = time.clock()
small_findSmall = findSmallest(small)
sm_findsm_stop = time.clock()
smallFindsm_time = sm_findsm_stop - sm_findsm_start


#  findSmallest - medium array
m_findsm_start = time.clock()
medium_findSmall = findSmallest(medium)
m_findsm_stop = time.clock()
mediumFindsm_time = m_findsm_stop - m_findsm_start


#  findSmallest - big array
b_findsm_start = time.clock()
big_findSmall = findSmallest(big)
b_findsm_stop = time.clock()
bigFindsm_time = b_findsm_stop - b_findsm_start


# findSmallest - bigger array
br_findsm_start = time.clock()
bigger_findSmall = findSmallest(bigger)
br_findsm_stop = time.clock()
biggerFindsm_time = br_findsm_stop - br_findsm_start


#  findSmallest - biggest array
bs_findsm_start = time.clock()
biggest_findSmall = findSmallest(biggest)
bs_findsm_stop = time.clock()
biggestFindsm_time = bs_findsm_stop - bs_findsm_start

###############################################################################

np.random.seed(seed=123)
small = np.random.randint(99999, size=5000).tolist()

np.random.seed(seed=123)
medium = np.random.randint(99999, size=10000).tolist()

np.random.seed(seed=123)
big = np.random.randint(99999, size=15000).tolist()

np.random.seed(seed=123)
bigger = np.random.randint(99999, size=20000).tolist()

np.random.seed(seed=123)
biggest = np.random.randint(99999, size=25000).tolist()

np.random.seed(seed=123)
z = np.random.randint(99999, size=256).tolist()

###############################################################################
# sort arrays using selectionSort
# note the execution time

# small selectionSort
s_selection_start = time.clock()
smallSelection = selectionSort(small)
s_selection_stop = time.clock()
smallSelection_time = s_selection_stop - s_selection_start


# medium selectionSort
med_selection_start = time.clock()
mediumSelection = selectionSort(medium)
med_selection_stop = time.clock()
mediumSelection_time = med_selection_stop - med_selection_start


# big selectionSort
big_selection_start = time.clock()
bigSelection = selectionSort(big)
big_selection_stop = time.clock()
bigSelection_time = big_selection_stop - big_selection_start


# bigger selectionSort
bigger_selection_start = time.clock()
biggerSelection = selectionSort(bigger)
bigger_selection_stop = time.clock()
biggerSelection_time = bigger_selection_stop - bigger_selection_start


# biggest selectionSort
biggest_selection_start = time.clock()
biggestSelection = selectionSort(biggest)
biggest_selection_stop = time.clock()
biggestSelection_time = biggest_selection_stop - biggest_selection_start

###############################################################################

np.random.seed(seed=123)
small = np.random.randint(99999, size=5000).tolist()

np.random.seed(seed=123)
medium = np.random.randint(99999, size=10000).tolist()

np.random.seed(seed=123)
big = np.random.randint(99999, size=15000).tolist()

np.random.seed(seed=123)
bigger = np.random.randint(99999, size=20000).tolist()

np.random.seed(seed=123)
biggest = np.random.randint(99999, size=25000).tolist()

np.random.seed(seed=123)
z = np.random.randint(99999, size=256).tolist()

###############################################################################


# sort each array from smallest to largest

# z warmup
z  = np.sort(z)

# sort small array
sm_start = time.clock()
small_sort = np.sort(small)
sm_stop = time.clock()
smallSort_time = sm_stop - sm_start

# z warmup
# z  = np.sort(z)
# sort medium array
m_start = time.clock()
medium_sort = np.sort(medium)
m_stop = time.clock()
mediumSort_time = m_stop - m_start

# z warmup
#z  = np.sort(z)
# sort big array
b_start = time.clock()
big_sort = np.sort(big)
b_stop = time.clock()
bigSort_time = b_stop - b_start

# z warmup
#z  = np.sort(z)
# sort bigger array
br_start = time.clock()
bigger_sort = np.sort(bigger)
br_stop = time.clock()
biggerSort_time = br_stop - br_start

# z warmup
#z  = np.sort(z)
# sort biggest array
bs_start = time.clock()
biggest_sort = np.sort(biggest)
bs_stop = time.clock()
biggestSort_time = bs_stop - bs_start

###############################################################################


np.random.seed(seed=123)
small = np.random.randint(99999, size=5000).tolist()

np.random.seed(seed=123)
medium = np.random.randint(99999, size=10000).tolist()

np.random.seed(seed=123)
big = np.random.randint(99999, size=15000).tolist()

np.random.seed(seed=123)
bigger = np.random.randint(99999, size=20000).tolist()

np.random.seed(seed=123)
biggest = np.random.randint(99999, size=25000).tolist()

np.random.seed(seed=123)
z = np.random.randint(99999, size=256).tolist()

###############################################################################
###############################################################################
# sort each array from smallest to largest using quicksort

# z warmup
z  = np.sort(z)

# quicksort small array
sm_quick_start = time.clock()
small_quick = quicksort(small)
sm_quick_stop = time.clock()
smallQuick_time = sm_quick_stop - sm_quick_start

# quicksort medium array
m_quick_start = time.clock()
medium_quick = quicksort(medium)
m_quick_stop = time.clock()
mediumQuick_time = m_quick_stop - m_quick_start

# quicksort big array
b_quick_start = time.clock()
big_quick = quicksort(big)
b_quick_stop = time.clock()
bigQuick_time = b_quick_stop - b_quick_start


# quicksort bigger array
br_quick_start = time.clock()
bigger_quick = quicksort(bigger)
br_quick_stop = time.clock()
biggerQuick_time = br_quick_stop - br_quick_start


# quicksort biggest array
bs_quick_start = time.clock()
biggest_quick = quicksort(biggest)
bs_quick_stop = time.clock()
biggestQuick_time = bs_quick_stop - bs_quick_start

###############################################################################

# create a 5 column array showing length of random array and execution in
# milliseconds of the remaining columns

fiver = np.array([["Array Length", "Sort", "quickSort","Find_Smallest", "selectionSort"],
                  ['5000', smallSort_time,smallQuick_time, smallFindsm_time ,smallSelection_time],
                  ['10000', mediumSort_time, mediumQuick_time, mediumFindsm_time, mediumSelection_time],
                  ['15000', bigSort_time, bigQuick_time, bigFindsm_time, bigSelection_time],
                  ['20000', biggerSort_time,biggerQuick_time, biggerFindsm_time, biggerSelection_time],
                  ['25000', biggestSort_time,biggestQuick_time, biggestFindsm_time, biggestSelection_time]])

fiver

###############################################################################
# use matplotlib to generate a plot with the size of the random array on the horizontal
# and the execution time in milliseconds on the vertical axis. This should be 
# for sequential and binary search algorithms only

plt.plot([5000, 10000, 15000, 20000, 25000],
         [smallFindsm_time, mediumFindsm_time, bigFindsm_time, biggerFindsm_time, biggestFindsm_time],
         'b--',
         [5000, 10000, 15000, 20000, 25000],
         [smallSelection_time, mediumSelection_time,bigSelection_time,biggerSelection_time,biggestSelection_time],
         'r--')
plt.axis([5000,25000,-1,10])
plt.xlabel('Array Size')
plt.ylabel('Execution Time')
plt.title('Size vs. Execution Time')
plt.legend(['selectionSort', 'findSmallest'], loc=2)
plt.show()

###############################################################################

# use matplotlib to generate a plot withthe size of the random array on the horizontal
# and the execution time in milliseconds on the vertical axis. The plot should 
# show exectuion time against array size for each form of the algorithm being tested

plt.plot([5000, 10000, 15000, 20000, 25000],
         [smallSort_time,mediumSort_time,bigSort_time,biggerSort_time,biggestSort_time],
         'g--',
         [5000, 10000, 15000, 20000, 25000],
         [smallFindsm_time, mediumFindsm_time, bigFindsm_time, biggerFindsm_time, biggestFindsm_time],
         'r--',
         [5000, 10000, 15000, 20000, 25000],
         [smallQuick_time, mediumQuick_time, bigQuick_time, biggerQuick_time, biggestQuick_time],
         'b-',
         [5000, 10000, 15000, 20000, 25000],
         [smallSelection_time, mediumSelection_time,bigSelection_time,biggerSelection_time,biggestSelection_time],
         'b--')
plt.axis([5000,25000,-1,10])
plt.xlabel('Problem Size')
plt.ylabel('Execution Time')
plt.title('Problem Size vs Execution Time')
plt.legend(['Sort', 'findSmallest','quickSort', 'selectionSort'], loc=2)
plt.show()



plt.plot([5000, 10000, 15000, 20000, 25000],
         [smallSort_time,mediumSort_time,bigSort_time,biggerSort_time,biggestSort_time],
         'g--',
         [5000, 10000, 15000, 20000, 25000],
         [smallFindsm_time, mediumFindsm_time, bigFindsm_time, biggerFindsm_time, biggestFindsm_time],
         'r--',
         [5000, 10000, 15000, 20000, 25000],
         [smallQuick_time, mediumQuick_time, bigQuick_time, biggerQuick_time, biggestQuick_time],
         'b-')
#plt.axis([5000,25000,-1,10])
plt.xlabel('Problem Size')
plt.ylabel('Execution Time')
plt.title('Problem Size vs Execution Time')
plt.legend(['Sort', 'findSmallest','quickSort'], loc=2)
plt.show()