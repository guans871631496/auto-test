from core.logics.ui.BasePage import BasePage


class MainPage(BasePage):
    create_rwo_order_icon = 'new UiSelector().text("创建订单")'
    processing_order_list = 'new UiSelector().text("处理中")'

    # def __init__(self, driver):
    #     self.driver = driver

    def enter_create_order_input_car_plate_number_page(self):
        #self.driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value=self.create_rwo_order_icon).click()
        self.click(self.create_rwo_order_icon)

    def seach_processing_order(self):
        self.click(self.processing_order_list)
