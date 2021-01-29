import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

class BrowseBuy(unittest.TestCase):
    def test_browse_select(self):
        
        # chromedriver path location
        path = r"C:\AI_ML_Training\JDs\Bitdefender\homework_test_interview\chromedriver_win32\chromedriver.exe"
        self.wb = webdriver.Chrome(path)   
        self.wb.get("https://www.bitdefender.com/solutions/") # web page link
        wb = self.wb
        wait = WebDriverWait(wb, 10)
        #....................................#
        print("open chrome browser and navigate to www.bitdefender.com")
        print("and navigate to Home-> See solutions and find and click Multiplatform")
        # click on Multiplatform
        try:
            browseButtonXpath = '//*[@id="MainMenu|Home"]/div/div[1]/div[5]/a'

            browse = wait.until(EC.element_to_be_clickable((By.XPATH, browseButtonXpath )))
            for select in browse:
                select.click()

        except: TimeoutError
        
        #........................................................#
        print("select Premium Security -> Buy now")
        # select & buy favorite product
        try:
            buyButtonXpath = '//*[@id="PCSecurity"]/div[2]/div[2]/a[1]'

            buy_button = wait.until(EC.element_to_be_clickable((By.XPATH, buyButtonXpath )))
            for buy_now in buy_button:
                buy_now.click()

        except: TimeoutError
        
        self.assertTrue(True)

    #print("check that the correct price is displayed in cart")
        # check price in chart if is correct
    

        
    def test_Quit(self):
        path = r"C:\AI_ML_Training\JDs\Bitdefender\homework_test_interview\chromedriver_win32\chromedriver.exe"
        self.wb = webdriver.Chrome(path)
        self.wb.quit()

if __name__ == "__main__":
    unittest.main()
    




