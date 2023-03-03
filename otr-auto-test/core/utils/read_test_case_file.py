import os

import yaml


def read_testcase_yaml(yaml_name, filter):
    with open(os.getcwd()+'/'+yaml_name) as f:
        data = yaml.load(stream=f, Loader=yaml.FullLoader)
        test_data = []
        for index in range(len(data)):
            if filter in data[index]['case_name']:
                test_data.append(data[index])
        return test_data
