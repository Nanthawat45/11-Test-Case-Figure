import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By

class TTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("D:\\webdriver\\chromedriver.exe")
        self.driver.get("http://127.0.0.1/Customerphp/customer.php")

        
    def safe_screenshot(self, file_path):
        try:
            self.driver.save_screenshot(file_path)
            print(f"Screenshot saved: {file_path}")
        except Exception as e:
            print(f"Failed to save screenshot: {e}")

    def testInput1(self):
        
        name = self.driver.find_element(By.ID, "ff")
        last = self.driver.find_element(By.ID, "lastName")
        age = self.driver.find_element(By.ID, "age")


        name.send_keys("johnjohn")
        last.send_keys("canonc")
        age.send_keys(str("2"))

        submit = self.driver.find_element(By.ID,"submit")
        submit.click()
    
        file_path = "001.png"
        self.safe_screenshot(file_path)

    def testInput2(self):
        
        name = self.driver.find_element(By.ID, "ff")
        last = self.driver.find_element(By.ID, "lastName")
        age = self.driver.find_element(By.ID, "age")


        name.send_keys("johnj")
        last.send_keys("canoncanoncano")
        age.send_keys(str("149"))

        submit = self.driver.find_element(By.ID,"submit")
        submit.click()
    
        file_path = "002.png"
        self.safe_screenshot(file_path)
    
    def testInput3(self):
        
        name = self.driver.find_element(By.ID, "ff")
        last = self.driver.find_element(By.ID, "lastName")
        age = self.driver.find_element(By.ID, "age")


        name.send_keys("johnjo")
        last.send_keys("canoncanoncanon")
        age.send_keys(str("150"))

        submit = self.driver.find_element(By.ID,"submit")
        submit.click()
    
        file_path = "003.png"
        self.safe_screenshot(file_path)

    def testInput4(self):
        
        name = self.driver.find_element(By.ID, "ff")
        last = self.driver.find_element(By.ID, "lastName")
        age = self.driver.find_element(By.ID, "age")


        name.send_keys("johnjohnjohnjo")
        last.send_keys("canoncan")
        age.send_keys(str("75"))

        submit = self.driver.find_element(By.ID,"submit")
        submit.click()
    
        file_path = "004.png"
        self.safe_screenshot(file_path)

    def testInput5(self):
        
        name = self.driver.find_element(By.ID, "ff")
        last = self.driver.find_element(By.ID, "lastName")
        age = self.driver.find_element(By.ID, "age")


        name.send_keys("johnjohnjohnjoh")
        last.send_keys("canoncan")
        age.send_keys(str("75"))

        submit = self.driver.find_element(By.ID,"submit")
        submit.click()
    
        file_path = "005.png"
        self.safe_screenshot(file_path)

    def testInput6(self):
        
        name = self.driver.find_element(By.ID, "ff")
        last = self.driver.find_element(By.ID, "lastName")
        age = self.driver.find_element(By.ID, "age")


        name.send_keys("john")
        last.send_keys("canoncan")
        age.send_keys(str("75"))

        submit = self.driver.find_element(By.ID,"submit")
        submit.click()
    
        file_path = "006.png"
        self.safe_screenshot(file_path)

    def testInput7(self):
        
        name = self.driver.find_element(By.ID, "ff")
        last = self.driver.find_element(By.ID, "lastName")
        age = self.driver.find_element(By.ID, "age")


        name.send_keys("johnjohnjohnjohn")
        last.send_keys("canoncan")
        age.send_keys(str("75"))

        submit = self.driver.find_element(By.ID,"submit")
        submit.click()
    
        file_path = "007.png"
        self.safe_screenshot(file_path)

    def testInput8(self):
        
        name = self.driver.find_element(By.ID, "ff")
        last = self.driver.find_element(By.ID, "lastName")
        age = self.driver.find_element(By.ID, "age")


        name.send_keys("johnjohn")
        last.send_keys("cano")
        age.send_keys(str("75"))

        submit = self.driver.find_element(By.ID,"submit")
        submit.click()
    
        file_path = "008.png"
        self.safe_screenshot(file_path)

    def testInput9(self):
        
        name = self.driver.find_element(By.ID, "ff")
        last = self.driver.find_element(By.ID, "lastName")
        age = self.driver.find_element(By.ID, "age")


        name.send_keys("johnjohn")
        last.send_keys("canoncanoncanonc")
        age.send_keys(str("75"))

        submit = self.driver.find_element(By.ID,"submit")
        submit.click()
    
        file_path = "009.png"
        self.safe_screenshot(file_path)

    def testInput10(self):
        
        name = self.driver.find_element(By.ID, "ff")
        last = self.driver.find_element(By.ID, "lastName")
        age = self.driver.find_element(By.ID, "age")


        name.send_keys("johnjohn")
        last.send_keys("canoncann")
        age.send_keys(str("0"))

        submit = self.driver.find_element(By.ID,"submit")
        submit.click()
    
        file_path = "010.png"
        self.safe_screenshot(file_path)

    def testInput11(self):
        
        name = self.driver.find_element(By.ID, "ff")
        last = self.driver.find_element(By.ID, "lastName")
        age = self.driver.find_element(By.ID, "age")


        name.send_keys("johnjohn")
        last.send_keys("canoncan")
        age.send_keys(str("151"))

        submit = self.driver.find_element(By.ID,"submit")
        submit.click()
    
        file_path = "011.png"
        self.safe_screenshot(file_path)

        
        


if __name__ == "__main__":
    unittest.main()

