import pytest
from config.project_path import *
from core.utils.copy import Copy


def main():
    real_result_path = allure_report_path+'/Result_'+time.strftime('%Y-%m-%d_%H-%M-%S')
    pytest.main(['-v', '-s', '--alluredir='+real_result_path, test_case_path])
    Copy.copy_content(environment_path_properties,real_result_path+'/environment.properties')
    Copy.copy_file(allure_report_tmp,real_result_path)
    Copy.edit_file(real_result_path+'/history/history-trend.json')


if __name__ == '__main__':
    main()
