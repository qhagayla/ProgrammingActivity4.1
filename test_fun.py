import unittest

def check(x):

	return x >= 100

class MyTest(unittest.TestCase):

	def test(self):
		self.assertEqual(check(100),True)

if __name__== '__main__':

	unittest.main()


