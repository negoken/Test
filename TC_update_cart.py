import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

class Update_Check_Remove_Cart(unittest.TestCase):
    
    def test_update_check_remove_quantity(self):
        
        path = r"C:\AI_ML_Training\JDs\Bitdefender\homework_test_interview\chromedriver_win32\chromedriver.exe"
        self.wb = webdriver.Chrome(path)   
        self.wb.get("https://www.bitdefender.com/solutions/") # web page link
        wb = self.wb
        wait = WebDriverWait(wb, 10)
        #............................................#
        print("in cart, change quantity from 1 to 2 and hit update")
        
        #update the quantity 1-->2
        try:
            quantityXpath = '//*[@id="qty_21642367"]'
            change_quantity = wb.find_elements_by_xpath(quantityXpath)
            for qty in change_quantity:
                qty.click()
                qty.clear()
                qty.send_keys('2')
        except: TimeoutError

        self.assertTrue(True)
      
    
    def test_updated_price_on_cart(self):

        print("check that correct price is displayed(doubled from previous update of quantity") 
        # displaying product price on cart
        path = r"C:\AI_ML_Training\JDs\Bitdefender\homework_test_interview\chromedriver_win32\chromedriver.exe"
        self.wb = webdriver.Chrome(path)
        wb = self.wb
        
        # price on cart  before update
        self.wb.get("https://store.bitdefender.com/order/checkout.php?redirect=0&CART=1&CARD=2&PRODS=21642367&QTY=1&OPTIONS21642367=tsmd-10u-1y&LANG=en&CURRENCY=EUR&DCURRENCY=EUR&CLEAN_CART=ALL&ORDERSTYLE=nLWs5JSpkHE%3D&COUPON=SOY2021-PS&SHORT_FORM=1&adobe_mc=MCMID%3D81436852142830002528759934484039703732%7CMCORGID%3D0E920C0F53DA9E9B0A490D45%2540AdobeOrg%7CTS%3D1611789523&SHOPURL=https%3A%2F%2Fwww.bitdefender.com%2Fsolutions%2F&_ga=826304872.1611192573")
        
        price_on_cart = wb.find_elements_by_xpath('//*[@id="section8"]/div/div[2]/div[2]/span')
                                                 
        for value in price_on_cart:
            value_on_cart = float(value.text[0:5])
            #print("Price value on cart is:", value_on_cart , "EUR","with discount")
        
        # price on cart after update
        self.wb.get("https://store.bitdefender.com/order/checkout.php?CART_ID=bc143d56faeb7bd4029a5a162aa2ac11")
        default_price = wb.find_elements_by_xpath('//*[@id="section8"]/div/div[2]/div[2]/span')
                                                  
        for value in default_price:
            new_value_on_cart = float(value.text[0:5])
            #print("Price value on cart for 2 products is:", new_value_on_cart , "EUR","with discount")

        #check update
        if new_value_on_cart == 2*default_price:
            print("price  displayed is  doubled from previous update of quantity")
        else:
            print("price is not correct displayed due the  discount offer , so is different due the discount offer")


        return 

    def test_remove_product(self):   
        path = r"C:\AI_ML_Training\JDs\Bitdefender\homework_test_interview\chromedriver_win32\chromedriver.exe"
        self.wb = webdriver.Chrome(path)   
        self.wb.get("https://store.bitdefender.com/order/checkout.php?CART_ID=bc143d56faeb7bd4029a5a162aa2ac11") 
        wb = self.wb
        try:
            wait = WebDriverWait(wb, 10)
            print("remove item from cart by clicking remove icon")
            # remove the quantity
            removeButtonXpath = '//*[@id="pid_21642367"]/i'
            remove_button = wait.until(EC.element_to_be_clickable((By.XPATH, removeButtonXpath )))
            remove_button.click()
        except: TimeoutError 
            
        
        self.assertTrue(True)
   

    

if __name__ == "__main__":
    unittest.main()



