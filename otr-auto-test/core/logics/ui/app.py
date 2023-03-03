import time

from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.options.android import UiAutomator2Options
from selenium.common.exceptions import WebDriverException
from selenium.common.exceptions import NoSuchElementException

from core.logics.ui.BasePage import BasePage
from core.utils.download_app import DownloadApp
from config.project_path import *
from core.utils.log import logger

class App:
    def start(self):
        global page_source
        options = UiAutomator2Options()
        server_url ='http://127.0.0.1:4723/wd/hub'
        options.platform_name = "Android"
        options.device_name = 'emulator-5554'
        options.app_package = "com.daimler.otr_hd.uat"
        options.app_activity = "com.otrastabletapp.MainActivity"

        try:
            self.driver = webdriver.Remote(server_url, options=options)
            logger.info("app第一次连接成功")
            time.sleep(12)
            page_source = self.driver.page_source
        except WebDriverException:
            logger.info("没有安装包，开始下载")
            DownloadApp.download_app(app_package_path)
            options.app = app_package_path
            self.driver = webdriver.Remote(server_url, options=options)
            page_source = self.driver.page_source
        finally:
            basePage = BasePage(self.driver)
            self.driver.implicitly_wait(20)
            while True:
                if "登 录" in page_source:
                    return self.driver
                elif ("CONTINUE" in page_source) or ("Continue" in page_source):
                    # try:
                    #     self.driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value='new UiSelector().text("CONTINUE")').click()
                    # except NoSuchElementException:
                    #     self.driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value='new UiSelector().text("Continue")').click()
                    list = ['new UiSelector().text("Continue")', 'new UiSelector().text("CONTINUE")']
                    basePage.click(list)
                    #self.driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value='new UiSelector().text("OK")').click()
                    basePage.click('new UiSelector().text("OK")')
                    page_source = self.driver.page_source
                elif "立即更新" in page_source:
                    logger.info("没有安装最新的包，开始下载")
                    self.driver.quit()
                    DownloadApp.download_app(app_package_path)
                    options.app = app_package_path
                    self.driver = webdriver.Remote(server_url, options=options)
                    page_source = self.driver.page_source
                else:
                    time.sleep(2)
                    page_source = self.driver.page_source

    @staticmethod
    def quit(self):
        self.driver.quit()


if __name__ == '__main__':
    driver = App().start()
    driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value='new UiSelector().text("用户名")').send_keys("hahhah")
    time.sleep(5)
    driver.quit()
