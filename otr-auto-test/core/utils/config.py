# 读取配置文件的信息
import configparser


class ReadConf:
    @staticmethod
    def read_conf(file_path, section, option):
        cf = configparser.ConfigParser()
        cf.read(file_path, encoding="utf-8-sig")
        config = cf.get(section, option)
        return config


if __name__ == '__main__':
    print(ReadConf().read_conf("../config/project_path_ini.ini", "PROJECT_PATH_INI", "project_path_ini"))