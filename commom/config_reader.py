import configparser
import os

def get_config(section,key):
    config = configparser.ConfigParser()
    #构建绝对路径
    config_path = os.path.join(os.path.dirname(__file__),'..','config','configs.ini')
    print(f"正在尝试读取配置文件路径：{os.path.abspath(config_path)}")

    config.read(config_path,encoding='utf-8')
    return config.get(section,key)