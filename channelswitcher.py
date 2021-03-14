# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.chrome.options import Options
import unittest, time, re
import logging
logging.basicConfig(format='[%(asctime)s][%(levelname)s] %(message)s',filename="channel.log",level=logging.INFO)

class Channelswitch(unittest.TestCase):
    def setUp(self):


        options = Options()
        options.add_argument('--headless')
        options.add_argument('--disable-gpu')  # Last I checked this was necessary.
        options.add_argument("--window-size=1920,1080")
        self.driver = webdriver.Chrome(chrome_options=options)

        self.driver.implicitly_wait(5)
        self.base_url = "https://www.google.com/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_channelswitch(self):

        driver = self.driver
        driver.get("http://192.168.42.1/")
        driver.maximize_window()
        try:
            driver.find_elements_by_class_name("password-hidden")[2].send_keys("Rmu020Sd!")
            driver.find_element_by_id("login-btn").click()
            time.sleep(4)
            try:
                driver.find_element_by_id("user-conflict-msg-container").find_elements_by_tag_name("button")[1].click()
                logging.info("had to log out other device")
                time.sleep(4)
            except Exception as ex2:
                pass

            driver.find_element_by_name("advanced").click()
            driver.find_element_by_id("show_5g_wireless").click()
            time.sleep(2)
            curchan=driver.find_element_by_id("wireless_5g_channel").text

            driver.find_element_by_id("menu-advanced-wireless-li").click()
            driver.find_element_by_name("wireless-settings").click()
            driver.find_element_by_id("show_5g").click()
            time.sleep(5)

            selchan=driver.find_element_by_id("channel-5g").get_attribute("value")

            input5gC=driver.find_element_by_id("channel-5g")
            parent5gC=input5gC.find_element_by_xpath("./..")
            ddclicker=parent5gC.find_element_by_tag_name("a")
            ddclicker.click()
            #driver.find_element_by_id("channel-5g").find_element_by_tag_name("a").click()
            time.sleep(2)
            cbox=driver.find_element_by_id("channel-5g").find_element_by_xpath("./..").find_element_by_tag_name("ul")
            centries=cbox.find_elements_by_tag_name("li")
            selectedLi=cbox.find_element_by_class_name("selected")
            selectedIndex=centries.index(selectedLi)
            if(int(curchan)<100):
                if(selectedIndex<11):
                    clickIndex=11
                else:
                    clickIndex=10
                centries[clickIndex].click()
                for but in driver.find_elements_by_tag_name("button"):
                    if but.text.strip() == "Save":
                        but.click()
                        print(but.text)
                        logging.info("SAVED")
            else:
                logging.info("NTD: {} {}".format(curchan,selchan))
            time.sleep(2)
            driver.find_element_by_id("top-control-logout").click()
        except Exception as ex:
            print(ex)
            driver.get_screenshot_as_file("issue.png")
            logging.exception(ex)

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.driver.switch_to_alert()
        except NoAlertPresentException as e:
            return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:
            self.accept_next_alert = True

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()

