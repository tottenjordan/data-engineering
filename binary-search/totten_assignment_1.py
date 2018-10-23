# -*- coding: utf-8 -*-
"""
Created on Fri Oct  5 18:24:18 2018

@author: jtotten
"""

import random

import numpy as np
from numpy.random import seed
from numpy.random import randint

import matplotlib.pyplot as plt
import time

# create simple search algo
def simpleSearch(list, item):
    for i in list:
        if i == item:
            return i
    # item doesnt exist
    return None
    
# create binary search algo

def binary_search(list, item):
  # low and high keep track of which part of the list you'll search in.
  low = 0
  high = len(list) - 1

  # While you haven't narrowed it down to one element ...
  while low <= high:
    # ... check the middle element
    mid = (low + high) // 2
    guess = list[mid]
    # Found the item.
    if guess == item:
      return mid
    # The guess was too high.
    if guess > item:
      high = mid - 1
    # The guess was too low.
    else:
      low = mid + 1

  # Item doesn't exist
  return None

###############################################################################
# create random number arrays of 512, 1024, 2048, 4096, 8192
# seed random number generator 

np.random.seed(seed=123)
small = np.random.randint(9999, size=512)

np.random.seed(seed=123)
medium = np.random.randint(9999, size=1024)

np.random.seed(seed=123)
big = np.random.randint(9999, size=2048)

np.random.seed(seed=123)
bigger = np.random.randint(9999, size=4096)

np.random.seed(seed=123)
biggest = np.random.randint(9999, size=8192)

np.random.seed(seed=123)
z = np.random.randint(9999, size=256)

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
# search for the array max value using simpleSearch
# note the execution time

# z warmup
#z  = np.sort(z)
# small simpleSearch
s_start = time.clock()
smallSimple = simpleSearch(small_sort, small_sort[-1])
s_stop = time.clock()
smallSimple_time = s_stop - s_start

# z warmup
# z  = np.sort(z)
# medium simpleSearch
med_start = time.clock()
mediumSimple = simpleSearch(medium_sort, medium_sort[-1])
med_stop = time.clock()
mediumSimple_time = med_stop - med_start

# z warmup
#z  = np.sort(z)
# big simpleSearch
big_start = time.clock()
bigSimple = simpleSearch(big_sort, big_sort[-1])
big_stop = time.clock()
bigSimple_time = big_stop - big_start

# z warmup
#z  = np.sort(z)
# bigger simpleSearch
bigger_start = time.clock()
biggerSimple = simpleSearch(bigger_sort, bigger_sort[-1])
bigger_stop = time.clock()
biggerSimple_time = bigger_stop - bigger_start

# z warmup
#z  = np.sort(z)
# biggest simpleSearch
biggest_start = time.clock()
biggestSimple = simpleSearch(biggest_sort, biggest_sort[-1])
biggest_stop = time.clock()
biggestSimple_time = biggest_stop - biggest_start

###############################################################################
# search for the array max value using binary_Search
# note the execution time

# z warmup
#z  = np.sort(z)
# small binary_search
sbi_start = time.clock()
small_bi = binary_search(small_sort, small_sort[-1])
sbi_stop = time.clock()
small_bi_time = sbi_stop - sbi_start

# z warmup
#z  = np.sort(z)
# medium binary_search
medbi_start = time.clock()
medium_bi = binary_search(medium_sort, medium_sort[-1])
medbi_stop = time.clock()
medium_bi_time = medbi_stop - medbi_start

# z warmup
#z  = np.sort(z)
# big binary_search
bigbi_start = time.clock()
big_bi = binary_search(big_sort, big_sort[-1])
bigbi_stop = time.clock()
big_bi_time = bigbi_stop - bigbi_start

# z warmup
#z  = np.sort(z)
# bigger binary_search
biggerbi_start = time.clock()
bigger_bi = binary_search(bigger_sort, bigger_sort[-1])
biggerbi_stop = time.clock()
bigger_bi_time = biggerbi_stop - biggerbi_start

# z warmup
#z  = np.sort(z)
# biggest binary_search
biggestbi_start = time.clock()
biggest_bi = binary_search(biggest_sort, biggest_sort[-1])
biggestbi_stop = time.clock()
biggest_bi_time = biggestbi_stop - biggestbi_start

###############################################################################
# create simpleSort times
smallSimpSort = smallSort_time + smallSimple_time
mediumSimpSort = mediumSort_time + mediumSimple_time
bigSimpSort = bigSort_time + bigSimple_time
biggerSimpSort = biggerSort_time + biggerSimple_time
biggestSimpSort = biggestSort_time + biggestSimple_time

# create binarySort times
smallBiSort = smallSort_time + small_bi_time
mediumBiSort = mediumSort_time + medium_bi_time
bigBiSort = bigSort_time + big_bi_time
biggerBiSort = biggerSort_time + bigger_bi_time
biggestBiSort = biggestSort_time + biggest_bi_time

# create a 6 column array showing length of random array and execution in
# milliseconds of the remaining columns

sixer = np.array([["Array Length", "Sort", "Simple Search", "Binary Search","SimpleSort", "BinarySort"],
                  ['512', smallSort_time, smallSimple_time ,small_bi_time,smallSimpSort,smallBiSort],
                  ['1024', mediumSort_time, mediumSimple_time, medium_bi_time, mediumSimpSort, mediumBiSort],
                  ['2048', bigSort_time, bigSimple_time, big_bi_time, bigSimpSort, bigBiSort],
                  ['4096', biggerSort_time, biggerSimple_time, bigger_bi_time, biggerSimpSort, biggerBiSort],
                  ['8192', biggestSort_time, biggestSimple_time, biggest_bi_time, biggestSimpSort, biggestBiSort]])

sixer

###############################################################################
# use matplotlib to generate a plot with the size of the random array on the horizontal
# and the execution time in milliseconds on the vertical axis. This should be 
# for sequential and binary search algorithms only

plt.plot([512, 1024, 2048, 4096, 8192],
         [smallSimple_time, mediumSimple_time, bigSimple_time, biggerSimple_time, biggestSimple_time],
         'b--',
         [512, 1024, 2048, 4096, 8192],
         [small_bi_time,medium_bi_time,big_bi_time,bigger_bi_time,biggest_bi_time],
         'r--')

plt.xlabel('Array Size')
plt.ylabel('Execution Time')
plt.title('Size vs. Execution Time')
plt.legend(['SimpleSearch', 'Binary'], loc=2)
plt.show()

###############################################################################

# use matplotlib to generate a plot withthe size of the random array on the horizontal
# and the execution time in milliseconds on the vertical axis. The plot should 
# show exectuion time against array size for each form of the algorithm being tested

plt.plot([512, 1024, 2048, 4096, 8192],
         [smallSort_time,mediumSort_time,bigSort_time,biggerSort_time,biggestSort_time],
         'g--',
         [512, 1024, 2048, 4096, 8192],
         [smallSimple_time,mediumSimple_time,bigSimple_time,biggerSimple_time,biggestSimple_time],
         'r--',
         [512, 1024, 2048, 4096, 8192],
         [small_bi_time,medium_bi_time,big_bi_time,bigger_bi_time,biggest_bi_time],
         'b--',
         [512, 1024, 2048, 4096, 8192],
         [smallSimpSort,mediumSimpSort,bigSimpSort,biggerSimpSort,biggestSimpSort],
         'r-',
         [512, 1024, 2048, 4096, 8192],
         [smallBiSort,mediumBiSort,bigBiSort,biggerBiSort,biggestBiSort],
         'b-')
plt.xlabel('Problem Size')
plt.ylabel('Execution Time')
plt.title('Problem Size vs Execution Time')
plt.legend(['Sort', 'Simple', 'Binary', 'SimpleSort', 'BinarySort'], loc=2)
plt.show()










###############################################################################
seed(161)
small = randint(512, size=512)
seed(161)
medium = randint(1024, size=1024)
seed(161)
big = randint(2048, size=2048)
seed(161)
bigger = randint(4096, size=4096)
seed(161)
biggest = randint(8192, size=8192)


