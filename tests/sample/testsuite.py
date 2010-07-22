import unittest
import random
import sampletest

class AllTests(unittest.TestSuite):
	def __init__(self):
		self.addTest(sampletest.TestSequenceFunctions)
