# -*- coding: utf-8 -*-
"""
Created on Thu Oct 18 00:49:05 2018

@author: jtotten
"""
import random

import numpy as np
from numpy.random import seed
from numpy.random import randint

import matplotlib.pyplot as plt
import time

np.random.seed(seed=123)
fact_arr = np.random.randint(100, high=500, size=10)
print(fact_arr)
# [465 482 422 198 330 117 183 206 223 157]

def fact(x):
  if x == 1:
    return 1
  else:
    return x * fact(x-1)

print(fact(5))

# fact(465)
foursixfive_start = time.clock()
foursixfive_fact = fact(465)
foursixfive_stop = time.clock()
fact465_time = foursixfive_stop - foursixfive_start

# fact(482)
foureighttwo_start = time.clock()
foureighttwo_fact = fact(482)
foureighttwo_stop = time.clock()
fact482_time = foureighttwo_stop - foureighttwo_start

# fact(422)
fourtwotwo_start = time.clock()
fourtwotwo_fact = fact(422)
fourtwotwo_stop = time.clock()
fact422_time = fourtwotwo_stop - fourtwotwo_start

# fact(198)
onenineeight_start = time.clock()
onenineeight_fact = fact(198)
onenineeight_stop = time.clock()
fact198_time = onenineeight_stop - onenineeight_start

# fact(330)
threethreezero_start = time.clock()
threethreezero_fact = fact(330)
threethreezero_stop = time.clock()
fact330_time = threethreezero_stop - threethreezero_start

# fact(117)
oneoneseven_start = time.clock()
oneoneseven_fact = fact(117)
oneoneseven_stop = time.clock()
fact117_time = oneoneseven_stop - oneoneseven_start

# fact(183)
oneeightthree_start = time.clock()
oneeightthree_fact = fact(183)
oneeightthree_stop = time.clock()
fact183_time = oneeightthree_stop - oneeightthree_start

# fact(206)
twozerosix_start = time.clock()
twozerosix_fact = fact(206)
twozerosix_stop = time.clock()
fact206_time = twozerosix_stop - twozerosix_start

# fact(223)
twotwothree_start = time.clock()
twotwothree_fact = fact(223)
twotwothree_stop = time.clock()
fact223_time = twotwothree_stop - twotwothree_start

# fact(157)
onefiveseven_start = time.clock()
onefiveseven_fact = fact(157)
onefiveseven_stop = time.clock()
fact157_time = onefiveseven_stop - onefiveseven_start

###############################################################################
#forLoop
# [465 482 422 198 330 117 183 206 223 157]
# Python program to find the factorial of a number provided by the user.

# change the value for a different result
num465 = 465
num482 = 482
num422 = 422
num198 = 198
num330 = 330
num117 = 117
num183 = 183
num206 = 206
num223 = 223
num157 = 157


# uncomment to take input from the user
#num = int(input("Enter a number: "))

factorial = 1
#######################################
# for loop 465
start465 = time.clock()
# check if the number is negative, positive or zero
if num465 < 0:
   print("Sorry, factorial does not exist for negative numbers")
elif num465 == 0:
   print("The factorial of 0 is 1")
else:
   for i in range(1,num465 + 1):
       factorial = factorial*i
   print("The factorial of",num465,"is",factorial)
stop465 = time.clock()
for465_time = stop465 - start465

#######################################
# for loop 482
start482 = time.clock()
# check if the number is negative, positive or zero
if num482 < 0:
   print("Sorry, factorial does not exist for negative numbers")
elif num482 == 0:
   print("The factorial of 0 is 1")
else:
   for i in range(1,num482 + 1):
       factorial = factorial*i
   print("The factorial of",num482,"is",factorial)
stop482 = time.clock()
for482_time = stop482 - start482

#######################################
# for loop 422
start422 = time.clock()
# check if the number is negative, positive or zero
if num422 < 0:
   print("Sorry, factorial does not exist for negative numbers")
elif num422 == 0:
   print("The factorial of 0 is 1")
else:
   for i in range(1,num422 + 1):
       factorial = factorial*i
   print("The factorial of",num422,"is",factorial)
stop422 = time.clock()
for422_time = stop422 - start422

#######################################
# for loop 198
start198 = time.clock()
# check if the number is negative, positive or zero
if num198 < 0:
   print("Sorry, factorial does not exist for negative numbers")
elif num198 == 0:
   print("The factorial of 0 is 1")
else:
   for i in range(1,num198 + 1):
       factorial = factorial*i
   print("The factorial of",num198,"is",factorial)
stop198 = time.clock()
for198_time = stop198 - start198

#######################################
# for loop 330
start330 = time.clock()
# check if the number is negative, positive or zero
if num330 < 0:
   print("Sorry, factorial does not exist for negative numbers")
elif num330 == 0:
   print("The factorial of 0 is 1")
else:
   for i in range(1,num330 + 1):
       factorial = factorial*i
   print("The factorial of",num330,"is",factorial)
stop330 = time.clock()
for330_time = stop330 - start330

#######################################
# for loop 117
start117 = time.clock()
# check if the number is negative, positive or zero
if num117 < 0:
   print("Sorry, factorial does not exist for negative numbers")
elif num117 == 0:
   print("The factorial of 0 is 1")
else:
   for i in range(1,num117 + 1):
       factorial = factorial*i
   print("The factorial of",num117,"is",factorial)
stop117 = time.clock()
for117_time = stop117 - start117

#######################################
# for loop 183
start183 = time.clock()
# check if the number is negative, positive or zero
if num183 < 0:
   print("Sorry, factorial does not exist for negative numbers")
elif num183 == 0:
   print("The factorial of 0 is 1")
else:
   for i in range(1,num183 + 1):
       factorial = factorial*i
   print("The factorial of",num183,"is",factorial)
stop183 = time.clock()
for183_time = stop183 - start183

#######################################
# for loop 206
start206 = time.clock()
# check if the number is negative, positive or zero
if num206 < 0:
   print("Sorry, factorial does not exist for negative numbers")
elif num206 == 0:
   print("The factorial of 0 is 1")
else:
   for i in range(1,num206 + 1):
       factorial = factorial*i
   print("The factorial of",num206,"is",factorial)
stop206 = time.clock()
for206_time = stop206 - start206

#######################################
# for loop 223
start223 = time.clock()
# check if the number is negative, positive or zero
if num223 < 0:
   print("Sorry, factorial does not exist for negative numbers")
elif num223 == 0:
   print("The factorial of 0 is 1")
else:
   for i in range(1,num223 + 1):
       factorial = factorial*i
   print("The factorial of",num223,"is",factorial)
stop223 = time.clock()
for223_time = stop223 - start223

#######################################
# for loop 157
start157 = time.clock()
# check if the number is negative, positive or zero
if num157 < 0:
   print("Sorry, factorial does not exist for negative numbers")
elif num157 == 0:
   print("The factorial of 0 is 1")
else:
   for i in range(1,num157 + 1):
       factorial = factorial*i
   print("The factorial of",num157,"is",factorial)
stop157 = time.clock()
for157_time = stop157 - start157
###############################################################################
# create time deltas
# [465 482 422 198 330 117 183 206 223 157]
#465
delta_465 = for465_time - fact465_time
#482
delta_482 = for482_time - fact482_time
#422
delta_422 = for422_time - fact422_time
#198
delta_198 = for198_time - fact198_time
#330
delta_330 = for330_time - fact330_time
#117
delta_117 = for117_time - fact117_time
#183
delta_183 = for183_time - fact183_time
#206
delta_206 = for206_time - fact206_time
#223
delta_223 = for223_time - fact223_time
#157
delta_157 = for157_time - fact157_time
###############################################################################
# create factorial numbers
#Try this:
from decimal import Decimal
fact465 = "{:.2e}".format(Decimal(foursixfive_fact))
fact482 = "{:.2e}".format(Decimal(foureighttwo_fact))
fact422 = "{:.2e}".format(Decimal(fourtwotwo_fact))
fact198 = "{:.2e}".format(Decimal(onenineeight_fact))
fact330 = "{:.2e}".format(Decimal(threethreezero_fact))
fact117 = "{:.2e}".format(Decimal(oneoneseven_fact))
fact183 = "{:.2e}".format(Decimal(oneeightthree_fact))
fact206 = "{:.2e}".format(Decimal(twozerosix_fact))
fact223 = "{:.2e}".format(Decimal(twotwothree_fact))
fact157 = "{:.2e}".format(Decimal(onefiveseven_fact))



###############################################################################
# create a table
Table = np.array([["Integer", "Factorial", "Recursion Time", "For Loop Time","Delta"],
                  ['465', fact465, fact465_time ,for465_time,delta_465],
                  ['482', fact482, fact482_time, for482_time, delta_482],
                  ['422', fact422, fact422_time, for422_time, delta_422],
                  ['198', fact198, fact198_time, for198_time, delta_198],
                  ['330', fact330, fact330_time, for330_time, delta_330],
                  ['117',fact117,fact117_time,for117_time,delta_117],
                  ['183',fact183,fact183_time,for183_time,delta_183],
                  ['206',fact206,fact206_time,for206_time,delta_206],
                  ['223',fact223,fact223_time,for223_time,delta_223],
                  ['157',fact157,fact157_time,for157_time,delta_157]])

Table
##############################################################################
# Plot recursion vs loop


plt.plot([117, 157, 183, 198, 206, 223, 330, 422, 465, 482],
         [for117_time,for157_time,for183_time,for198_time,for206_time,for223_time,for330_time,for422_time,for465_time,for482_time],
         'g--',
         [117, 157, 183, 198, 206, 223, 330, 422, 465, 482],
         [fact117_time,fact157_time,fact183_time,fact198_time,fact206_time,fact223_time,fact330_time,fact422_time,fact465_time,fact482_time],
         'r--')
plt.xlabel('Problem Size')
plt.ylabel('Execution Time')
plt.title('Problem Size vs Execution Time')
plt.legend(['For Loop', 'Recursion'], loc=2)
plt.show()


