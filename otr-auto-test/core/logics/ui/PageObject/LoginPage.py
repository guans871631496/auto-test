from core.logics.ui.BasePage import BasePage


class LoginPage(BasePage):
    # 手机号码 输入框
    #login_username = 'new UiSelector().text("用户名")'
    # 密码 输入框
   # login_passwd_xpath = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup[2]/android.widget.EditText'
    #login_passwd_xpath="//android.widget.TextView[@text='登 录']/parent::*/parent::android.view.ViewGroup/android.view.ViewGroup[2]/android.widget.EditText"
    #login_passwd_xpath3="//android.widget.TextView[@text='登 录']/parent::*/preceding-sibling::android.view.ViewGroup[1]/android.widget.EditText"

    login_username = 'new UiSelector().text("用户名")'
    #密码
    login_passwd_xpath="//android.widget.TextView[@text='登 录']/parent::*/parent::android.view.ViewGroup/android.view.ViewGroup[2]/android.widget.EditText"
    # 登录 按钮
    login_button_text = 'new UiSelector().text("登 录")'

   #validata_username = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[9]/android.widget.TextView'
    validata_username = "//android.widget.TextView[@text='创建订单']/parent::android.view.ViewGroup/following-sibling::android.view.ViewGroup[6]/android.widget.TextView"


    # 登录功能
    def login(self,username,passwd):
        # username = 'K6ASM3'
        # passwd = "789@Test"
        # self.driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value='new UiSelector().text("CONTINUE")').click()
        # self.driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value='new UiSelector().text("OK")').click()

        # # time.sleep(10)
        # driver.find_element(by=AppiumBy.XPATH, value=self.login_passwd_xpath).send_keys(passwd)
        # driver.find_element(by=AppiumBy.XPATH, value=self.login_passwd_xpath2).send_keys(passwd)
        #self.driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value=self.login_username).send_keys(username)
        #self.driver.find_element(by=AppiumBy.XPATH, value=self.login_passwd_xpath).send_keys(passwd)
        #self.driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value=self.login_button_text).click()
        self.input(self.login_username, username)
        self.input(self.login_passwd_xpath, passwd)
        self.click(self.login_button_text)

    def get_user_name(self):
        return self.get_text(self.validata_username)

    def screenshot_save(self):
        self.get_windows_img()

    def is_element_exist(self):
        return self.is_element_existence_loop(self.login_username)

