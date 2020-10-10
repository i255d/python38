#  collections.counter lets you find the most common
#  elements in an iterabe:
#  There are 3 l's 2 o's, and the rest are in the order of the alphabit.

import collections
c = collections.Counter('helloworld')

# print(c)

print(c.most_common(3))