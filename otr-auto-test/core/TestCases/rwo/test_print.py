import time

import pytest

import allure
from appium.webdriver.common.appiumby import AppiumBy

from core.logics.ui.PageObject.InputCarPlateNumberPage import InputCarPlateNumberPage
from core.logics.ui.PageObject.LoginPage import LoginPage
from core.logics.ui.PageObject.MainPage import MainPage
from core.logics.ui.PageObject.OrderMainPage import OrderMainPage
from core.logics.ui.PageObject.PreInspectionPage import PreInspectionPage
from core.logics.ui.PageObject.VccPage import VccPage
from core.logics.ui.app import App
from core.utils.log import logger
from core.utils.yaml_operation import read_testcase_path_yaml


@allure.story("维修订单（含工时）-story")
@allure.suite("维修订单（含工时）-suite")
class Test05MaintenanceOrderLabour:

    def setup_class(self):
        self.driver = App.start(self)
        self.orderMain = OrderMainPage(self.driver)

    @allure.sub_suite("登录-sub_suite")
    @allure.title("登录-title")
    def test_login(self):
        logger.info("=====开始测试登录=====")
        # login_parameter = read_testcase_path_yaml("config/account.yaml")
        # user_name = login_parameter['account-uat']['ASSA']['username']
        # pwd = login_parameter['account-uat']['pwd']
        # if LoginPage(self.driver).is_element_exist():
        #     logger.info("页面加载成功")
        # else:
        #     logger.info("页面加载失败")
        #     return
        LoginPage(self.driver).login('YURCHEN', '789@Test')  # 登录
        assert LoginPage(self.driver).get_user_name() == '雨柔程'  # 验证登录成功
        # LoginPage(self.driver).screenshot_save();

    def test_search_car_plate_number(self):
        logger.info("=====开始测试查询车牌号=====")
        MainPage(self.driver).enter_create_order_input_car_plate_number_page()  # 创建订单
        InputCarPlateNumberPage(self.driver).input_car_plate_number('黑DJ3116','WDD2221621A198066')  # 输入车牌号
#        assert InputCarPlateNumberPage(self.driver).find_car_plate_page_text(['parameter']['validata']) == True
        #InputCarPlateNumberPage(self.driver).aa_test('黑DJ3116','WDD2221621A198066')

    @allure.sub_suite("添加车主信息-sub_suite")
    @allure.title("添加车主信息-title")
    def test_add_owner_information(self):
        self.orderMain.enter_vcc_page()  # 进入vcc
        Vcc = VccPage(self.driver)
        # Vcc.vcc_repair_person_same_with_car_owner()  # 添加与车主相同信息
        Vcc.vcc_add_repair_person_and_car_owner_information("黄玉如")
        repair_person = Vcc.get_repair_person_name()
        Vcc.back_order_main_page()  # 返回订单主页面
        assert repair_person == '黄玉如'  # 验证送修人信息添加成功

    # @allure.sub_suite("打印工单-sub_suite")
    # @allure.title("打印工单-title")
    # def test_search_car_plate_number(self):
    #     logger.info("=====开始打印工单=====")
    #     self.driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR,value='new UiSelector().text("处理中")').click()
    #     self.driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR,value='new UiSelector().text("崔哈哈勿动")').click()
    #

    def test_seach(self):
        LoginPage(self.driver).login('YURCHEN', '789@Test')  # 登录
        self.driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value='new UiSelector().text("处理中")').click()
        self.driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR,value='new UiSelector().text("黄玉如")').click()
        #self.driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value='new UiSelector().text("处理中")').click()
        #self.driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value='new UiSelector().text("黄胖子")').click()
        time.sleep(3)
        OrderMain = OrderMainPage(self.driver)
        OrderMain.enter_preinspection_page()  # 进入预检页面
        preinspection = PreInspectionPage(self.driver)
        loading_pre_inspection_page = preinspection.pre_inspection_page_loading()
        if loading_pre_inspection_page:
            logger.info("车辆预检页面加载成功")
        else:
            logger.info("车辆预检页面加载失败")
        assert loading_pre_inspection_page == True
        preinspection.add_basic_information(202)  # 车辆公里数修改
        preinspection.enter_normal_inspection_page()
        loading_normal_inspection_page = preinspection.normal_inspection_page_loading()
        if loading_normal_inspection_page:
            logger.info("标准检查项页面加载成功")
        else:
            logger.info("标准检查项页面加载成功")
        assert loading_normal_inspection_page == True
        preinspection.add_normal_inspection()  # 标准检查项
        assert OrderMain.find_page_text("查看车辆预检结果") == True
    #
    # def test_111(self):
    #     LoginPage(self.driver).login('YURCHEN', '789@Test')  # 登录
    #     assert LoginPage(self.driver).get_user_name() == '雨柔程'  # 验证登录成功
    #     self.driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value='new UiSelector().text("处理中")').click()
    #     self.driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR,value='new UiSelector().text("黄玉如")').click()
    #     self.driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR,value='new UiSelector().text("黑DJ3116")').click()
    #    # self.orderMain.enter_vcc_page()  # 进入vcc
    #     Vcc = VccPage(self.driver)
    #     # Vcc.vcc_repair_person_same_with_car_owner()  # 添加与车主相同信息
    #     Vcc.vcc_add_repair_person_and_car_owner_information("黄玉如")
    #     Vcc.back_order_main_page()  # 返回订单主页面


if __name__ == '__main__':
    pytest.main(['-v', '-s', '--alluredir=//Users/guan.song/Documents/study/otr-report-bigdata-demo/otr-auto-test/TestGuiResult','test_CreateRwoOrder.py'])







