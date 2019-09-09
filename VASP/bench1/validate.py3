#!/usr/bin/env python3

from re import compile
from sys import exit, argv
import numpy as np

def build_array(tp, nk, nb, fn):
# GGA and HSE data:
# k-point    34 :       0.3000    0.2000    0.2000
#  band No.  band energies     occupation
#      1     -11.4239      2.00000
# GW data:
# k-point  34 :       0.3000    0.2000    0.2000
#  band No.  KS-energies  QP-energies   sigma(KS)   V_xc(KS)     V^pw_x(r,r')   Z            occupation
#
#      1     -13.6327     -13.8221     -18.7012     -18.4394     -24.9401       0.7235       2.0000       0.2828
   RE1 = compile('^ k-point +[0-9]{1,3} :   (    [0-9]\.[0-9]{4}){3}')

   # Get file contents
   try:
      file = open(fn, 'r')
      filedata = file.readlines()
      file.close()
   except FileNotFoundError:
      exit(fn + ' is missing')
   
   # If reference file, need to acquire nb and return. nb is passed as 0 in this case.
   if nb == 0: ref = True
   else: ref = False

   if ref:
      data = iter(filedata)
      while True:
         t2 = next(data)
         if RE1.match(t2):
            next(data)  # Header line
            if tp == 'gw':  # Extra blank line
               next(data)
            while True:
               t = next(data)
               if len(t) > 1:
                  nb += 1
               else: # Only '\n'
                  break
            break

   # Now regardless of ref or test, we have nb correct. Pull out band structure.
   data = iter(filedata)
   block = np.zeros((nk, nb), dtype=np.float16)
   i = -1
   while True:
      t2 = next(data)
      if RE1.match(t2):
         i += 1
         next(data)
         if tp == 'gw':  # Extra blank line
            next(data)
         KS_energies = []
         for j in range(nb):
            KS_energies.append(np.float16(next(data).split()[1]))
         block[i,:] = np.transpose(np.array(KS_energies))
      if i == numkpoints-1:
         break

   # Make sure block is not still all zeros
   try:
      np.testing.assert_equal(block, np.zeros((nk, nb), dtype=np.float16))
   except AssertionError:  # Not equal, so OK
      if ref:
         return block, nb
      else:
         return block
   else:  # Equal, so couldn't find data
      exit('Could not find data in ' + fn)

def validate(tp, test_array, ref_array):
   diff = None
   try:
      np.testing.assert_allclose(test_array, ref_array, rtol=1e-6) # Test equality to 1 part in 10^6
      OK = True
   except AssertionError:
      OK = False
      t = np.not_equal(test_array, ref_array)
      diff = (test_array[t], ref_array[t])
   return OK, diff

if __name__ == '__main__':

   try: # A filename has been supplied
      test_filename = argv[1]
      RE_filename = compile('OUTCAR-(?P<type>[a-z]{2,3})-(?P<rankcount>[0-9]+)')
      t = RE_filename.match(test_filename)
      run_type = t.group('type')
      numranks = t.group('rankcount')
      if run_type == 'gga' or run_type == 'hse':
         reference_filename = 'OUTCAR-{}.ref'.format(run_type)
      elif run_type == 'gw':
         reference_filename = 'OUTCAR-{}-{}.ref'.format(run_type, t.group('rankcount'))
   except IndexError:
      exit('A test filename was not supplied to validate.py as an argument')

   numkpoints = 63  # This is set by INCAR, fixed for all runs

   reference, numbands = build_array(run_type, numkpoints, 0, reference_filename)
   test = build_array(run_type, numkpoints, numbands, test_filename)
   IS_OK = validate(run_type, test, reference)
   
   if IS_OK[0]:
      print('Benchmark 1 {} {} ranks validated'.format(run_type, numranks))
   else:
      print('Benchmark 1 {} {} ranks not validated'.format(run_type, numranks))
      print('Differences found')
      print('Test data')
      print(IS_OK[1][0])
      print('Reference data')
      print(IS_OK[1][1])
