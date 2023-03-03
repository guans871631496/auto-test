from shutil import copytree
import os
# import logging
# logging.basicConfig(level=logging.DEBUG)
from utils import logger

class Copy:
    @staticmethod
    def copy_file(origin_path, report_path):
        filename_list = [filename for filename in os.listdir(origin_path)]
        if 'history' in filename_list:
            history_path = origin_path+'/history'
            copytree(history_path, report_path+'/history', dirs_exist_ok=True)
            logger.info("history文件复制成功")
        else:
            logger.warning("原路径没有history文件夹")

    @staticmethod
    def copy_content(origin_path, target_path):
        f_origin = open(origin_path, 'r')
        f_target = open(target_path, 'a')
        f_origin_content = f_origin.readlines()
        for i in range(len(f_origin_content)):
            if i > 0:
                f_target.write(f_origin_content[i])
        logger.info("environment.properties文件复制成功")
        f_origin.close()
        f_target.close()

    @staticmethod
    def edit_file(file_path):
        file = open(file_path, 'r')
        r = file.read()
        list_r = eval(r)
        file.close()
        buildOrderList = [i['buildOrder'] for i in list_r if 'buildOrder' in i.keys()]
        for i in list_r:
            if 'buildOrder' not in i.keys():
                buildOrderList.append(0)
                i['buildOrder'] = max(buildOrderList)+1
        file_write = open(file_path, 'w')
        file_write.writelines(str(list_r).replace("'", "\""))
        logger.info("history-trend.json修改成功")
        file_write.close()