import os
import time

# 项目路径的配置文件
from core.utils.config import ReadConf

project_path_ini = os.path.split(os.path.realpath(__file__))[0] + '/project_path_ini.ini'
# 读取项目的绝对路径
project_path = ReadConf().read_conf(project_path_ini, 'PROJECT_PATH_INI', 'project_path_ini')


# allure报告
allure_report_path = os.path.join(project_path, 'report')
# 生成html报告路径
allure_report_tmp = os.path.join(project_path, 'report', 'allure_report_tmp')
# 每次执行pytest生成的报告（基础数据）路径
report_path = allure_report_path+'/Result_'+time.strftime('%Y-%m-%d_%H-%M-%S')
# 每次报告中要生成的environment.properties
report_environment_path = os.path.join(project_path, 'environment.properties')
# 每次报告中要修改的history-trend.json
report_trend_path = os.path.join(project_path, 'real_report_path+','history/history-trend.json')


# environment配置文件的路径
environment_path_properties = os.path.join(project_path, 'config', 'environment.properties')

# 日志的存放目录
log_path = os.path.join(project_path, 'log')
# log_file = log_path+"/log_"+time.strftime('%Y-%m-%d_%H-%M-%S')+".log"

#截图存放目录
screenshot_path = os.path.join(os.path.abspath(os.path.join(os.getcwd(), "../..")), 'screenshots')

# 用例存放的路径
test_case_path = os.path.join(project_path, 'core', 'TestCases')

# 测试包存放的路径
app_package_path = os.path.join(project_path, 'apk','daimler-otr-hd.apk')






