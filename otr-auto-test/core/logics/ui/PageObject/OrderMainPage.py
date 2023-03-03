from core.logics.ui.BasePage import BasePage
from core.utils.log import logger


class OrderMainPage(BasePage):
    car_vcc = 'new UiSelector().text("客户/车辆信息 *")'
    preinspection = 'new UiSelector().text("车辆预检 *")'
    back_to_main= 'new UiSelector().text("返回")'
    input_preinspection_finding = 'new UiSelector().text("请输入预检发现")'
    input_preinspection_suggestions = 'new UiSelector().text("请输入预检建议")'
    select_service_type = 'new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().text("   选择服务类型").instance(0))'
    # 需参数化
    service_type_value = 'new UiSelector().text("保养")'
    save = 'new UiSelector().text("保存")'
    delivery_time = 'new UiSelector().text("请选择预计交车时间")'
    #参数化 默认交车时间
    default_delivery_time = 'new UiSelector().text("完成")'
    hour_library = 'new UiSelector().text("工时库")'
    assign_work_items = "//android.widget.TextView[@text='登记进厂']/parent::android.view.ViewGroup/parent::android.view.ViewGroup/preceding-sibling::android.view.ViewGroup[1]"
    assign_to_workshop = 'new UiSelector().text("分配到车间")'
    register_to_enter_factory = 'new UiSelector().text("登记进厂")'
    determine = 'new UiSelector().text("确认")'

    def enter_vcc_page(self):
        #self.driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value=self.car_vcc).click()
        self.click(self.car_vcc)


    def enter_preinspection_page(self):
        if self.slide_find_page_ele_text("车辆预检 *"):
            self.click(self.preinspection)
        else:
            logger.info("车辆预检已完成")

    def find_page_text(self,text):
        return self.slide_find_page_ele_text(text)

    def order_page_required_data(self,finding_information,suggestions_information,service_type):
        #预检发现/建议信息
        self.input(self.input_preinspection_finding,finding_information)
        self.input(self.input_preinspection_suggestions,suggestions_information)
        #选择服务类型
        self.click(self.select_service_type)
        self.click('new UiSelector().text("'+service_type+'")')
        #选择默认交车时间
        self.click(self.delivery_time)
        self.click(self.default_delivery_time)

    def enter_work_page(self):
        self.click(self.hour_library)

    def assign_work_items(self):
        self.click(self.assign_work_items)
        self.click(self.assign_to_workshop)

    def register_to_enter_factory(self):
        self.click(self.register_to_enter_factory)
        self.click(self.determine)

    def order_main_page_loading(self):
        return self.is_element_existence_loop(self.car_vcc)

    def get_order_number(self):
        pass
