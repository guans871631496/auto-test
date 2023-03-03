import os
import yaml


def read_userdata_yaml():
    with open(os.getcwd()+"/account.yaml") as f:
        value = yaml.load(stream=f, Loader=yaml.FullLoader)
        return value

def write_extract_yaml(data):
    with open(os.getcwd() + "/extract.yaml", mode='a', encoding='utf-8') as f:
        yaml.dump(data=data, stream=f, allow_unicode=True)

def clear_extract_yaml():
    with open(os.getcwd() + "/extract.yaml", mode='w', encoding='utf-8') as f:
        f.truncate()

def read_testcase_path_yaml(yaml_name):
    with open(os.path.abspath(os.path.dirname(os.path.dirname(__file__)))+'/'+yaml_name) as f:
        data = yaml.load(stream=f, Loader=yaml.FullLoader)
        return data

def read_testcase_yaml(yaml_name,filter):
    with open(os.getcwd()+'/'+yaml_name) as f:
        data = yaml.load(stream=f, Loader=yaml.FullLoader)
        test_data = []
        for index in range(len(data)):
            if filter in data[index]['case_name']:
                test_data.append(data[index])
        return test_data

# def read_testcase_yaml1(yaml_name):
#     with open(os.getcwd()+'/'+yaml_name) as f:
#         data = yaml.load(stream=f, Loader=yaml.FullLoader)
#         return data






