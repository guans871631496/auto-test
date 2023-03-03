import hashlib
import os
import time

from selenium.webdriver import Keys

from core.utils.log import logger
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.remote.webdriver import WebDriver
from config.project_path import screenshot_path


class BasePage:

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def __find_ele(self, locator):
        """
        统一定位方式：支持XPath,text
        :param locator:
        :return:
        """
        try:
            if locator is None or locator == '':
                return None
            elif type(locator) == list:
                for index in range(len(locator)):
                    try:
                        ele = self.driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value=locator[index])
                        if ele != None:
                            logger.info("参数为:%s" % locator[index])
                            return ele
                    except:
                        continue
            elif locator.startswith('/'):
                logger.info("参数为:%s" % locator)
                return self.driver.find_element(by=AppiumBy.XPATH, value=locator)
            else:
                logger.info("参数为:%s" % locator)
                return self.driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value=locator)
        except:
            logger.error("元素定位失败")

    def click_and_check(self, locator, check_ele):
        n = 0
        while n < 10:
            n += 1
            logger.info("第%s次尝试点击" % n)
            self.__find_ele(locator).click()
            if self.is_element_existence(check_ele) is True:
                break
            else:
                continue

    # 文本输入
    def input(self, locator, value):
        self.__find_ele(locator).send_keys(value)

    def click(self, locator):
        self.__find_ele(locator).click()

    #获取文本信息
    def get_text(self, locator):
        ele = self.__find_ele(locator)
        return ele.text

    # 清除文本框
    def clear(self, locator):
        self.__find_ele(locator).clear()

    #强制等待
    def wait(self, second):
        time.sleep(second)

    # 截图并保存
    # 在这里我们把file_path这个参数写死，直接保存到我们项目根目录的一个文件.\Screenshots下
    def get_windows_img(self):
        screenshot_dir = screenshot_path
        if not os.path.exists(screenshot_dir):
            os.makedirs(screenshot_dir)
        rq = time.strftime('%y%m%d %H:%M:%S', time.localtime(time.time()))
        screen_name = screenshot_dir + "/" + rq + '.png'
        try:
            self.driver.get_screenshot_as_file(screen_name)
        except NameError as e:
            logger.error(msg="截图失败：%s" % e)

    # 判断 md5 值是否相同
    def compare_pictures(self, old_image, new_image):
        old_image_val = self.to_md5(old_image)
        new_image_val = self.to_md5(new_image)
        return old_image_val == new_image_val

    # 使用 md5() 对图片内容的加密后
    def to_md5(self, image_path):
        m = hashlib.md5()
        m.update(image_path)
        md5_val = m.hexdigest()
        return md5_val


    # 关闭浏览器，一般在测试最后的时候后关闭的
    def quit(self):
        self.driver.quit()

    #关闭当前窗口
    def close(self):
        self.driver.close()

        # 检查元素是否存在

    def is_element_existence(self, locator):
        ele = self.__find_ele(locator)
        if ele == None:
            logger.info("当前页面元素%s不存在" % locator)
            return False
        else:
            return True

        # 循环检查元素

    def is_element_existence_loop(self, locator):
        query_ele = False
        number = 1
        while (not query_ele and number < 3):
            query_ele = self.is_element_existence(locator)
            number += 1
        if number == 3 and not query_ele:
            logger.error("页面加载时间超长")
            return False
        else:
            return True

        # 获取当前页面的尺寸大小

    def get_size(self):
        x = self.driver.get_window_size()['width']
        y = self.driver.get_window_size()['height']
        return (x, y)

        # 定义向上滑动的方法

    def swip_top(self, slidingScale):
        gs = self.get_size()
        x1 = int(gs[0] * 0.5)
        y1 = int(gs[1] * 0.9)
        y2 = int(gs[1] * slidingScale)
        self.driver.swipe(x1, y1, x1, y2)

        # 定义向下滑动的方法,可以刷新页面

    def swip_down(self):
        gs = self.get_size()
        x1 = int(gs[0] * 0.25)
        y1 = int(gs[1] * 0.75)
        y2 = int(gs[1] * 0.9)
        self.driver.swipe(x1, y1, x1, y2)

    # 从一个元素滑动到另一个元素
    def scroll_to(self, locator1, locator2):
        e1 = self.__find_ele(locator1)
        e2 = self.__find_ele(locator2)
        self.driver.scroll(e1, e2)

    # 拖拽 滑动
    def drag_and_drop(self, locator1, locator2):
        e1 = self.__find_ele(locator1)
        e2 = self.__find_ele(locator2)
        self.driver.drag_and_drop(e1, e2)

    # 滑动页面检查当前页面是否包含该元素文本
    def slide_find_page_ele_text(self, text):
        pagesource = self.driver.page_source
        old_pagesource = ''
        # while循环---如果未找到text,且未到最后一页则滑屏
        while text not in pagesource and pagesource != old_pagesource:
            old_pagesource = self.driver.page_source
            # 每次滑动页面的30%
            self.swip_top(0.6)
            pagesource = self.driver.page_source
        if pagesource.find(text) != -1:
            return True
        else:
            logger.info("文本'%s'未找到" % text)
            return False

    # 回车
    def enter(self):
        self.driver.press_keycode(66)

    #键盘操作
    def keyboard_operation(self,locator,keyboardName):
        #回车
        if keyboardName == 'enter':
            self.driver.find_element(by=AppiumBy.XPATH,value=locator).send_keys(Keys.ENTER)

    #滑动到屏幕底部
    def slide_to_the_bottom_of_the_screen(self):
        pagesource = self.driver.page_source
        old_pagesource = ''
        count = 0
        while pagesource != old_pagesource and count<10:
            old_pagesource = self.driver.page_source
            self.swip_top(0.1)
            pagesource = self.driver.page_source
            count+=1







