import os
import yaml
from config import BASE_PATH


def read_yaml(filename):
    filepath = BASE_PATH + os.sep + 'data' + os.sep + filename
    arr = []
    with open(filepath, 'r', encoding='utf-8') as f:
        for datas in yaml.safe_load(f).values():
            arr.append(tuple(datas.values()))
    return arr


if __name__ == '__main__':
    print('read:', read_yaml('mp_login.yaml'))
    print(type(read_yaml('mp_login.yaml')))
