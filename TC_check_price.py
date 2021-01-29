import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time



class CheckPrice(unittest.TestCase):

    def test_price_on_page_cart_compare(self):
        # displaying product price on main page
        path = r"C:\AI_ML_Training\JDs\Bitdefender\homework_test_interview\chromedriver_win32\chromedriver.exe"
        self.wb = webdriver.Chrome(path)   
        #.....................................................#
        self.wb.get("https://www.bitdefender.com/solutions/") # web page link
        wb = self.wb
        price_on_page = wb.find_elements_by_xpath('//*[@id="MacSecurity"]/div[2]/div[1]/div[2]/span[3]')

        for value in price_on_page:
            value_on_page = float(value.text[1:])
            print("Price value on main page is:", value_on_page , "EUR")
        #return value_on_page
    
        # displaying product price on cart
        self.wb.get("https://store.bitdefender.com/order/checkout.php?redirect=0&CART=1&CARD=2&PRODS=21642367&QTY=1&OPTIONS21642367=tsmd-10u-1y&LANG=en&CURRENCY=EUR&DCURRENCY=EUR&CLEAN_CART=ALL&ORDERSTYLE=nLWs5JSpkHE%3D&COUPON=SOY2021-PS&SHORT_FORM=1&adobe_mc=MCMID%3D81436852142830002528759934484039703732%7CMCORGID%3D0E920C0F53DA9E9B0A490D45%2540AdobeOrg%7CTS%3D1611789523&SHOPURL=https%3A%2F%2Fwww.bitdefender.com%2Fsolutions%2F&_ga=826304872.1611192573")
        
        
        price_on_cart = wb.find_elements_by_xpath('//*[@id="section8"]/div/div[2]/div[2]/span')

        for value in price_on_cart:
            value_on_cart = float(value.text[0:5])
            print("Price value on cart is:", value_on_cart , "EUR","with discount")
            

        # price on main page & price on cart comparison
        
        if value_on_page == value_on_cart:
            print("correct price is displayed in cart")
        else:
            print("price on cart is different due the provided discount!")
        
        return 
        
    def test_Quit(self):
        path = r"C:\AI_ML_Training\JDs\Bitdefender\homework_test_interview\chromedriver_win32\chromedriver.exe"
        self.wb = webdriver.Chrome(path)
        self.wb.quit()


if __name__ == "__main__":
    
    unittest.main()

    
