import time

from selenium.webdriver import Keys

from core.logics.ui.BasePage import BasePage


class InputCarPlateNumberPage(BasePage):
    manual_input = 'new UiSelector().text("手动输入")'
    car_plate_number_input = "//android.widget.TextView[@text='车牌号']/parent::android.view.ViewGroup/android.view.ViewGroup[3]"
    car_plate_number_text_list = []
    car_plate_number_text = 'new UiSelector().text("%s")'
    search_car_plate_number = 'new UiSelector().text("搜 索")'
    continue_create = 'new UiSelector().text("继续创建")'
    confirm_button = 'new UiSelector().text("确定")'
    input_fin = "//android.widget.TextView[@text='VIN/FIN号']/following-sibling::android.view.ViewGroup"
    input_car_model = 'new UiSelector().text("请选择车型")'
    complete_button = 'new UiSelector().text("完成")'


    # def __init__(self, driver):
    #     self.driver = driver

    # 黑DJ3116  YURCHEN
    def input_car_plate_number(self, car_plate_number, fin_or_vin):
        self.click(self.manual_input)
        self.loop_input(car_plate_number)
        self.click(self.search_car_plate_number)
        if self.slide_find_page_ele_text("继续创建"):
            self.click(self.continue_create)
        elif self.slide_find_page_ele_text("请选择车型"):
            self.click(self.input_car_model)
            self.click(self.complete_button)
        elif self.slide_find_page_ele_text("VIN/FIN号") and self.is_element_existence('new UiSelector().text("VIN/FIN号")'):
            self.click(self.input_fin)
            self.loop_input(fin_or_vin)
        self.click(self.confirm_button)

    def seach_car_plate_page_loading(self,car_plate_number):
        return self.is_element_existence('new UiSelector().text("'+car_plate_number+'")')



    def find_car_plate_page_text(self, car_plate_number):
        return self.slide_find_page_ele_text(car_plate_number)

    def loop_input(self, number):
        for character in number:
            self.wait(1)
            text = 'new UiSelector().text("%s")' % str(character)
            self.click(text)


    # def aa_test(self, car_plate_number, fin_or_vin):
    #     self.click(self.manual_input)
    #     self.loop_input(car_plate_number)
    #     self.click(self.search_car_plate_number)
    #     while True:
    #         self.input('new UiSelector().text("'+car_plate_number+'")',Keys.ENTER)
    #         #self.enter()






