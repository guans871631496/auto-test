import requests
import os
from core.utils.log import logger

class DownloadApp:
    @staticmethod
    def download_app(app_package_path):
        try:
            os.remove(app_package_path)
        except FileNotFoundError:
            pass
        r = requests.get("https://uat.otrplus.mercedes-benz.com.cn/hd/download/daimler-otr-hd.apk",headers={"Sec-Fetch-Dest":"document",
                                                                                                            "sec-ch-ua-platform":"macOS",
                                                                                                           "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36" })
        if r.status_code != 200:
            logger.error("工作时间再来测试吧")
        else:
            # 存储
            with open(app_package_path, 'wb') as output:
                output.write(r.content)


if __name__ == '__main__':
    DownloadApp.download_app(app_package_path="/Users/peichen/Documents/p_7report/otr-report-bigdata-demo/otr-auto-test/apk/daimler-otr-hd.apk")
