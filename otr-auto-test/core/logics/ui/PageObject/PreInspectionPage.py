from core.logics.ui.BasePage import BasePage


class PreInspectionPage(BasePage):
    modify_mileage = 'new UiSelector().text("修改")'
    mileage_input = "//android.widget.TextView[@text='km']/parent::android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.EditText"
    #是否要参数化
    oil_full = 'new UiSelector().text("满")'
    mileage_confirm_button = 'new UiSelector().text("确定")'
    normal_inspection = 'new UiSelector().text("标准检查项")'
    alert_confirm = 'new UiSelector().text("确定")'
    mark_all = 'new UiSelector().text("全选标记")'
    air_conditioning_filter = "//android.widget.TextView[@text='空调滤清器(空调系统)*']/parent::android.view.ViewGroup/following-sibling::android.view.ViewGroup[1]/android.widget.ImageView"
    air_conditioning_value = 'new UiSelector().text("空调无异味、出风量正常、且距离上次更换<1.5万公里（10个月）")'
    wiper_blade = "//android.widget.TextView[@text='前后雨刮片*']/parent::android.view.ViewGroup/following-sibling::android.view.ViewGroup[1]/android.widget.ImageView"
    wiper_blade_value = 'new UiSelector().text("无异响、无跳动、无变形，刮水效果正常、更换标记无异常，且距离上次更换<2万公里（1年）")'
    on_board_battery = "//android.widget.TextView[@text='12V车载蓄电池']/parent::android.view.ViewGroup/following-sibling::android.view.ViewGroup[1]/android.widget.ImageView"
    on_board_battery_value = 'new UiSelector().text("距离上次更换<6万公里（4年）")'
    engine_belt = "//android.widget.TextView[@text='发动机皮带/涨紧轮状况']/parent::android.view.ViewGroup/following-sibling::android.view.ViewGroup[1]/android.widget.ImageView"
    engine_belt_value = 'new UiSelector().text("距离上次更换<8万公里（5年）")'

    preinspection_save = 'new UiSelector().text("保存")'
    preinspection_complete = 'new UiSelector().text("完成")'

    air_conditionar = 'new UiSelector().text("空调滤清器(空调系统)*")'
    air_conditionar_check = "//android.widget.TextView[@text='空调滤清器(空调系统)*']/parent::android.view.ViewGroup/following-sibling::android.view.ViewGroup[2]/android.widget.TextView[@text='未检测']"
    wiper_blade_check = "//android.widget.TextView[@text='前后雨刮片*']/parent::android.view.ViewGroup/following-sibling::android.view.ViewGroup[2]/android.widget.TextView[@text='未检测']"
    on_board_battery_check = "//android.widget.TextView[@text='12V车载蓄电池']/parent::android.view.ViewGroup/following-sibling::android.view.ViewGroup[2]/android.widget.TextView[@text='未检测']"
    engine_belt_check = "//android.widget.TextView[@text='发动机皮带/涨紧轮状况']/parent::android.view.ViewGroup/following-sibling::android.view.ViewGroup[2]/android.widget.TextView[@text='未检测']"

    def add_basic_information(self,mileageNumber):
        self.click(self.modify_mileage)
        self.input(self.mileage_input,mileageNumber)
        self.enter()
        self.click(self.mileage_confirm_button)
        self.click(self.oil_full)

    def add_normal_inspection(self):
        self.click(self.mark_all)
        if  self.is_element_existence(self.air_conditionar_check):
            self.click(self.air_conditioning_filter)
            self.click(self.air_conditioning_value)
            self.click(self.preinspection_save)
        self.slide_find_page_ele_text("12V车载蓄电池")
        if  self.is_element_existence(self.wiper_blade_check):
            self.click(self.wiper_blade)
            self.click(self.wiper_blade_value)
            self.click(self.preinspection_save)
        if  self.is_element_existence(self.on_board_battery_check):
            self.click(self.on_board_battery)
            self.click(self.on_board_battery_value)
            self.click(self.preinspection_save)
        if  self.is_element_existence(self.engine_belt_check):
            self.click(self.engine_belt)
            self.click(self.engine_belt_value)
            self.click(self.preinspection_save)
        self.click(self.preinspection_complete)

    def enter_normal_inspection_page(self):
        self.click(self.normal_inspection)
        self.click(self.alert_confirm)
        self.wait(3)

    def normal_inspection_page_loading(self):
        return self.is_element_existence_loop(self.air_conditionar)

    def pre_inspection_page_loading(self):
        return self.is_element_existence_loop(self.modify_mileage)



