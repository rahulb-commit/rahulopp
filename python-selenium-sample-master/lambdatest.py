import unittest
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options as ChromeOptions

# Jenkins passes these via the environment block we created
username = os.getenv("LT_USERNAME")
access_key = os.getenv("LT_ACCESS_KEY")

options = ChromeOptions()
options.browser_version = "latest"
options.platform_name = "Windows 10"

lt_options = {}
lt_options["username"] = username
lt_options["accessKey"] = access_key
lt_options["network"] = True
lt_options["build"] = os.getenv("LT_BUILD_NAME", "Jenkins_Selenium_Build")
lt_options["name"] = "Selenium 4 Sample Test"
lt_options["w3c"] = True
lt_options["plugin"] = "python-python"

# FIXED: Changed "test" to a unique name to avoid the 'platform type app' conflict
lt_options["smartUI.project"] = "Rahul_Web_SmartUI" 

options.set_capability("LT:Options", lt_options)

class FirstSampleTest(unittest.TestCase):
    driver = None

    def setUp(self):
        # The hub URL remains standard for automation
        self.driver = webdriver.Remote(
            command_executor="http://{}:{}@hub.lambdatest.com/wd/hub".format(
                username, access_key
            ),
            options=options,
        )

    def test_demo_site(self):
        driver = self.driver
        driver.implicitly_wait(10)
        driver.set_page_load_timeout(30)
        driver.set_window_size(1920, 1080)

        print("Loading URL")
        driver.get("https://lambdatest.github.io/sample-todo-app/")

        # Interact with elements
        driver.find_element(By.NAME, "li1").click()
        driver.find_element(By.NAME, "li2").click()
        print("Clicked on the first two elements")

        driver.find_element(By.ID, "sampletodotext").send_keys("LambdaTest")
        driver.find_element(By.ID, "addbutton").click()
        print("Added LambdaTest checkbox")

        search = driver.find_element(By.XPATH, "//h1[contains(@class,'font-bold')]")
        assert search.is_displayed(), "heading is not displayed"
        print(f"Heading text: {search.text}")
        
        driver.execute_script("lambda-status=passed")
        print("Tests completed successfully!")

    def tearDown(self):
        if self.driver:
            self.driver.quit()

if __name__ == "__main__":
    unittest.main()
