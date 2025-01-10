import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


def test_login():
    file_path = r"C:\Users\puroh\PycharmProjects\open_cart_awesomeQA_ui_project\src\Register_Test_Data.xlsx"
    data = pd.read_excel(file_path)

    driver = webdriver.Chrome()
    driver.get("https://awesomeqa.com/ui/index.php?route=account/login")

    for index,raw in data.iterrows():
        driver.find_element(By.ID,"input-email").send_keys(raw["E-Mail"])
        driver.find_element(By.ID,"input-password").send_keys(raw["Your Password"])

        driver.find_element(By.XPATH,"//input[@class='btn btn-primary']").click()
        assert driver.current_url == "https://awesomeqa.com/ui/index.php?route=account/account"

        driver.find_element(By.XPATH,"//a[text()='Desktops']").click()
        driver.find_element(By.XPATH, "//a[contains(text(),'Mac')]").click()
        #upper one  is new





