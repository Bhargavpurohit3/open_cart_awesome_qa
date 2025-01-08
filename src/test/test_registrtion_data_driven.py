import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


def test_registraion():

    file_path = r"C:\Users\puroh\PycharmProjects\open_cart_awesomeQA_ui_project\src\Register_Test_Data.xlsx"
    data = pd.read_excel(file_path)

    driver = webdriver.Chrome()
    driver.get("https://awesomeqa.com/ui/index.php?route=account/register")

    for index,raw in data.iterrows():

        driver.find_element(By.ID, "input-firstname").send_keys(raw["First Name"])
        driver.find_element(By.ID, "input-lastname").send_keys(raw["Last Name"])
        driver.find_element(By.ID, "input-email" ).send_keys(raw["E-Mail"])
        driver.find_element(By.ID, "input-telephone").send_keys(raw["Telephone"])
        driver.find_element(By.ID, "input-password").send_keys(raw["Your Password"])
        driver.find_element(By.ID, "input-confirm").send_keys(raw["Password Confirm"])

        if raw["Newsletter"] == "Subscribe":
            driver.find_element(By.XPATH,"//input[@name='newsletter' and @value='1']").click()
        else:
            driver.find_element(By.XPATH, "//input[@name='newsletter' and @value='0']").click()

        driver.find_element(By.XPATH, "//input[@name='agree' and @value='1']").click()


        time.sleep(5)

        message = driver.find_element(By.TAG_NAME,"h1")

        assert message.text == "Register Account"
        driver.refresh()

    driver.quit()