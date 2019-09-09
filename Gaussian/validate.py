#!/usr/bin/env python

import re
from sys import argv
from numpy import array
from numpy.testing import assert_allclose

RE = re.compile('Excited State.*eV +(?P<nm>[0-9\.]+) nm')

valid_data = array([454.71, 451.05, 368.4])

file = open(argv[1], 'r')
data = file.readlines()
file.close()

test_data = []
for i in data:
   if RE.search(i):
      test_data.append(float(RE.search(i).group('nm')))
test_data = array(test_data)

try:
   assert_allclose(test_data, valid_data, 0., 0.03)
   print('{} validated'.format(argv[1]))
except AssertionError:
   print('{} not validated', argv[1])
   print('Test data')
   print(test_data)
   print('Difference from valid data')
   print(test_data - valid_data)

