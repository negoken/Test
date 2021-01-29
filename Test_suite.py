import unittest , sys

from TC_browse_and_buy import BrowseBuy
from TC_update_cart import Update_Check_Remove_Cart
from TC_check_price import CheckPrice

# Display all tests from BrowseBuy , Update_Check_Remove_Cart

tc1 = unittest.TestLoader().loadTestsFromTestCase(BrowseBuy)
tc2 = unittest.TestLoader().loadTestsFromTestCase(CheckPrice)
tc3 = unittest.TestLoader().loadTestsFromTestCase(Update_Check_Remove_Cart)

#Test suite scenario

# Sanity suite: check if the website can be accessed and product is available
sanityTestSuite = unittest.TestSuite([tc1])  

# Functional suite: checking the prices on page & cart
functionalTestSuite = unittest.TestSuite([tc2])

# Functional suite: udpating the  new prices and items removing
functionalTestSuite = unittest.TestSuite([tc3])   

# Master Test Plan containing all TCs
masterTestPlan = unittest.TestSuite([tc1,tc2,tc3])

# Test execution
unittest.TextTestRunner(verbosity=2).run(masterTestPlan)
#///////////////////////////////////////////////////////////////////#



def main(out = sys.stderr, verbosity = 2): 
	loader = unittest.TestLoader() 

	suite = loader.loadTestsFromModule(sys.modules[__name__]) 
	unittest.TextTestRunner(out, verbosity = verbosity).run(suite) 
	
if __name__ == '__main__': 
	with open(r"C:\AI_ML_Training\JDs\Bitdefender\homework_test_interview\myfile.txt", 'w') as f: 
		main(f) 

 
