from selenium import webdriver
import pytest
#METHOD -1 Without pytest
#setup
'''driver=webdriver.Chrome(executable_path="C:/Users/dsrid/chromedriver_win32/chromedriver.exe")
driver.implicitly_wait(10)
driver.maximize_window()
#get application
driver.get("https://opensource-demo.orangehrmlive.com/")
driver.find_element_by_id("txtUsername").send_keys("Admin")
driver.find_element_by_id("txtPassword").send_keys("admin123")
driver.find_element_by_id("btnLogin").click()

#teardown lines
driver.close()
driver.quit()
print("test completed successfully")

#METHOD-2: WITH pytest test runner approach
def test_setup():
    global driver
    driver=webdriver.Chrome(executable_path="C:/Users/dsrid/chromedriver_win32/chromedriver.exe")
    driver.implicitly_wait(10)
    driver.maximize_window()
def test_login():
    driver.get("https://opensource-demo.orangehrmlive.com/")
    driver.find_element_by_id("txtUsername").send_keys("Admin")
    driver.find_element_by_id("txtPassword").send_keys("admin123")
    driver.find_element_by_id("btnLogin").click()

def test_teardown():
    driver.close()
    driver.quit()
    print("test completed successfully")'''

#METHOD-3: USING PYTEST CONVENTIONS
#class Test
class TestClass(): #here Test is mandatory according to pytest convention
    @pytest.fixture()
    def test_setup(self):
        global driver
        driver=webdriver.Chrome(executable_path="C:/Users/dsrid/chromedriver_win32/chromedriver.exe")
        driver.implicitly_wait(10)
        driver.maximize_window()
        yield
        driver.close()
        driver.quit()
        print("test completed successfully")

    def test_login(self,test_setup):
        driver.get("https://opensource-demo.orangehrmlive.com/")
        driver.find_element_by_id("txtUsername").send_keys("Admin")
        driver.find_element_by_id("txtPassword").send_keys("admin123")
        driver.find_element_by_id("btnLogin").click()
        x=driver.title
        print(x)
        #assert x=="abc"
        assert x =="OrangeHRM"

#def test_teardown():
    #driver.close()
    #driver.quit()
    #print("test completed successfully")

