from Log.Page import BasePage


class AddWorkPage(BasePage):
    #参数化
    work_value = 'new UiScrollable(new UiSelector().className("android.widget.ScrollView")).scrollIntoView(new UiSelector().text("1154"))'
    search = "//android.widget.TextView[@text='1154']/following-sibling::android.view.ViewGroup[2]/android.view.ViewGroup"
    add_work_complete = 'new UiSelector().text("完成")'
