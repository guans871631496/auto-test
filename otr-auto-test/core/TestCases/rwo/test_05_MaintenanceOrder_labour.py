import time

import pytest
import allure

from core.logics.ui.PageObject.InputCarPlateNumberPage import InputCarPlateNumberPage
from core.logics.ui.PageObject.LoginPage import LoginPage
from core.logics.ui.PageObject.MainPage import MainPage
from core.logics.ui.PageObject.OrderMainPage import OrderMainPage
from core.logics.ui.PageObject.PreInspectionPage import PreInspectionPage
from core.logics.ui.PageObject.VccPage import VccPage
from core.logics.ui.app import App
from core.utils.read_test_case_file import read_testcase_yaml
from core.utils.log import logger


@allure.story("维修订单（含工时）-story")
@allure.suite("维修订单（含工时）-suite")
class Test05MaintenanceOrderLabour:

    def setup_class(self):
        self.driver = App.start(self)
        self.orderMain = OrderMainPage(self.driver)

    # @pytest.fixture(scope='function', params= read_testcase_yaml("maintenanceOrderLabour_case.yaml", "登录"))
    # def f_function(self, request):
    #     print("fixture部分:{}".format(request.param))
    #     return request.param

    @allure.sub_suite("登录-sub_suite")
    @allure.title("登录-title")
    @pytest.mark.parametrize("caseInfo",read_testcase_yaml("maintenanceOrderLabour_case.yaml", "登录"))
    def test_login(self, caseInfo):
        logger.info("=====开始测试登录=====")
        # user_name = 'K6ASM3'
        # LoginPage(self.driver).login(request.param, '789@Test')  # 登录
        # assert LoginPage(self.driver).get_user_name() == user_name  # 验证登录成功
        LoginPage(self.driver).login(caseInfo['parameter']['username'], caseInfo['parameter']['password'])  # 登录
        assert LoginPage(self.driver).get_user_name() == caseInfo['validata'] # 验证登录成功


    @allure.sub_suite("查询车牌号-sub_suite")
    @allure.title("查询车牌号-title")
    @pytest.mark.parametrize("caseInfo",read_testcase_yaml("maintenanceOrderLabour_case.yaml", "车牌号"))
    def test_search_car_plate_number(self,caseInfo):
        logger.info("=====开始测试查询车牌号=====")
        MainPage(self.driver).enter_create_order_input_car_plate_number_page()  # 创建订单
        InputCarPlateNumberPage(self.driver).input_car_plate_number(caseInfo['parameter']['car_plate_number'])  # 输入车牌号
        assert InputCarPlateNumberPage(self.driver).find_car_plate_page_text(['parameter']['validata']) == True

    @allure.sub_suite("添加车主信息-sub_suite")
    @allure.title("添加车主信息-title")
    def test_add_owner_information(self):
        self.orderMain.enter_vcc_page()  # 进入vcc
        Vcc = VccPage(self.driver)
       # Vcc.vcc_repair_person_same_with_car_owner()  # 添加与车主相同信息
        Vcc.vcc_add_repair_person_and_car_owner_information()
        repair_person = Vcc.get_repair_person_name()
        Vcc.back_order_main_page()  # 返回订单主页面
        assert repair_person == self.OrderMain.get_vcc_repair_person()  # 验证送修人信息添加成功
        time.sleep(5)

    # @allure.sub_suite("添加预检信息-sub_suite")
    # @allure.title("添加预检信息-title")
    # def test_add_preinspection_information(self):
    #     self.orderMain.enter_preinspection_page()  # 进入预检页面
    #     preinspection = PreInspectionPage(self.driver)
    #     preinspection.add_basic_information(200)  # 车辆公里数修改
    #     loading_pre_inspection_page = preinspection.pre_inspection_page_loading()
    #     if loading_pre_inspection_page:
    #         logger.info("车辆预检页面加载成功")
    #     else:
    #         logger.info("车辆预检页面加载失败")
    #     assert loading_pre_inspection_page == True
    #     preinspection.enter_normal_inspection_page()
    #     loading_normal_inspection_page = preinspection.normal_inspection_page_loading()
    #     if loading_normal_inspection_page:
    #         logger.info("标准检查项页面加载成功")
    #     else:
    #         logger.info("标准检查项页面加载成功")
    #     assert loading_normal_inspection_page == True
    #     preinspection.add_normal_inspection()  # 标准检查项
    #     assert self.orderMain.find_page_text("查看车辆预检结果") ==True





if __name__ == '__main__':
    pytest.main(['-v', '-s', '--alluredir=//Users/guan.song/Documents/study/otr-report-bigdata-demo/otr-auto-test/TestGuiResult','test_CreateRwoOrder.py'])




