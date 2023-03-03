import time

from core.logics.ui.BasePage import BasePage
from core.utils.log import logger


class VccPage(BasePage):

    back_order_main = "//android.widget.TextView[@text='车辆与客户信息']/parent::android.view.ViewGroup/" \
                      "android.view.ViewGroup/android.widget.ImageView"

    # repair_person_same_with_car_owner = 'new UiScrollable(new UiSelector().scrollable(true)\
    #     .instance(0)).scrollIntoView(new UiSelector()\
    #     .text("添加与车主相同信息"));'

    repair_person_same_with_car_owner = 'new UiSelector().text("添加与车主相同信息")'
    vehicle_and_customer_information = 'new UiSelector().text("车辆与客户信息")'

    repair_person = 'new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().text("送修人"));'
    add_repair_person = "//android.widget.TextView[@text='送修人']/following-sibling::android.view.ViewGroup/android.widget.TextView[@text='添加']"
    search_repair_person_name = 'new UiSelector().text("输入 送修人姓名 / 手机号码 进行搜索")'
    vehicle_ownership = 'new UiSelector().text("公司")'
    add_repair_person = "//android.widget.TextView[@text='送修人']/following-sibling::android.view.ViewGroup/android.widget.TextView[@text='添加']"
    add_owner_information = "//android.widget.TextView[@text='个人车主']/following-sibling::android.view.ViewGroup/android.widget.TextView[@text='添加']"
    search_owner_information = 'new UiSelector().text("输入 车主姓名 / 手机号码 进行搜索")'
    validata_repair_person = "//android.widget.TextView[@text='送修人']/parent::android.view.ViewGroup/following-sibling::android.view.ViewGroup[1]/android.widget.TextView[1]"

    #黄玉如  暂无个人车主信息

    # def __init__(self, driver):
    #     self.driver = driver

    #有车主信息
    # def vcc_repair_person_same_with_car_owner(self):
    #     self.click(self.repair_person_same_with_car_owner)

    #添加车主信息
    def vcc_add_repair_person_and_car_owner_information(self, owner_name):
        # #添加送修人信息
        # self.click(self.add_repair_person)
        # #self.click(self.search_repair_person_name)
        # self.input(self.search_repair_person_name, repair_person_name)
        # self.enter()
        # self.click("//android.widget.TextView[@text='添加送修人']/parent::android.view.ViewGroup/android.view.ViewGroup/android.widget.TextView[@text='"+repair_person_name+"']")
        #添加车主信息
        self.slide_to_the_bottom_of_the_screen()
        if self.slide_find_page_ele_text("暂无个人车主信息"):
            self.click(self.add_owner_information)
            self.click(self.search_owner_information)
            self.input(self.search_owner_information, owner_name)
            self.enter()
            # while True:
            #     time.sleep(1)
            #     self.click("//android.widget.TextView[@text='添加新车主']/parent::android.view.ViewGroup/android.view.ViewGroup/android.widget.TextView[@text='"+owner_name+"']")
            #     p = self.driver.page_source
            #     if p.find("添加与车主相同信息") != -1:
            #         logger.info("页面跳转成功")
            #         return
            self.click_and_check("//android.widget.TextView[@text='添加新车主']/parent::android.view.ViewGroup/android.view.ViewGroup/android.widget.TextView[@text='"+owner_name+"']",self.vehicle_ownership)
        if self.slide_find_page_ele_text("添加与车主相同信息"):
            self.click(self.repair_person_same_with_car_owner)
        self.click(self.vehicle_ownership)

    def back_order_main_page(self):
        self.click(self.back_order_main)

    def vehicle_and_customer_information_page_loading(self):
        return self.is_element_existence_loop(self.vehicle_and_customer_information)

    def get_repair_person_name(self):
        return self.get_text(self.validata_repair_person)
