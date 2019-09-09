#!/usr/bin/env python3
from re import compile
from sys import exit
from pickle import load
import numpy as np

def build_energies(fn):
   # Get file contents
   try:
      file = open(fn, 'r')
      data = file.readlines()
      file.close()
   except FileNotFoundError:
      exit('{} is missing'.format(fn))
   # Pull out energy data
   energy_test_data = get_energy_data(iter(data))
   return energy_test_data

def build_forces(fn):
   # Get file contents
   try:
      file = open(fn, 'r')
      data = file.readlines()
      file.close()
   except FileNotFoundError:
      exit('{} is missing'.format(fn))
   # Pull out energy data
   force_test_data = get_force_data(iter(data))
   return force_test_data

def get_energy_data(iterator):
   RE1 = compile('^ Free energy of the ion-electron system')
   datadict = {}
   while True:
      try:
         t = next(iterator)
      except StopIteration:
         break
      if RE1.match(t):
         next(iterator)
         for j in range(5):
            t2 = next(iterator).split('=')
            key, value = t2[0].split()[-1], np.float32(t2[1])
            datadict[key] = value
         next(iterator) # PAW double counting, not considering this
         for j in range(4):
            t2 = next(iterator).split('=')
            key, value = t2[0].split()[-1], np.float32(t2[1])
            datadict[key] = value
         next(iterator) # Dashes
         t2 = next(iterator).split('=')
         key, value = t2[0].split()[-1], np.float32(t2[1].split()[0])
         datadict[key] = value
   # Make sure dict has expected number of entries
   if len(list(datadict.keys())) == 10:
      return datadict
   else:
      exit('Could not find expected energy data in OUTCAR')

def get_force_data(iterator):
   RE1 = compile(' POSITION')
   RE2 = compile('NIONS')
   NIONS = 0
   while True:
      try:
         t = next(iterator)
      except StopIteration:
         break
      if RE2.search(t):
         NIONS = int(t.split()[-1])
         data_array = np.zeros( (NIONS, 3), dtype=np.float16 )
      elif RE1.match(t):
         next(iterator)
         for i in range(NIONS):
            t2 = np.array([np.float16(j) for j in next(iterator).split()])[-3:]
            data_array[i,:] = t2
   try:
      np.testing.assert_equal(data_array, np.zeros((NIONS, 3), dtype=np.float16))
   except AssertionError:  # Not equal, so OK
      return data_array
   else:  # Equal, so couldn't find data
      exit('Could not find expected force data in OUTCAR')

def validate(refE, refF, testE, testF):
   diffE = None
   diffF = None
   try:
      for i in testE.keys():
         np.testing.assert_almost_equal(testE[i], refE[i], decimal=7)
      OK = True
   except AssertionError:
      OK = False
      diffE = {}
      for i in testE.keys():
         if abs(testE[i] - refE[i]) > 1e-7: diffE[i] = (i, testE[i], refE[i])

   try:
      np.testing.assert_almost_equal(testF, refF, decimal=4)
   except AssertionError:
      OK = False
      t = np.not_equal(testF, refF)
      diffF = (testF[t], refF[t])

   return OK, diffE, diffF

if __name__ == '__main__':
   ref_energies = build_energies('OUTCAR.ref')
   ref_forces = build_forces('OUTCAR.ref')
   test_energies = build_energies('OUTCAR')
   test_forces = build_forces('OUTCAR')
   v, errorE, errorF = validate(ref_energies, ref_forces, test_energies, test_forces)
   if v:
      print('Benchmark 2 validated')
   else:
      print('Benchmark 2 not validated')
      if errorE != None:
         print('Energies did not validate')
         for i in errorE: print("{0:s}  ref  {1:12.8f}  test  {2:12.8f}".format(errorE[i][0], errorE[i][1], errorE[i][2]))
      if errorF != None:
         print('Forces did not validate. Non-matching elements in test, reference:')
         print(errorF[0])
         print(errorF[1])

