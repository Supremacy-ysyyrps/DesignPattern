from SuperFactory import *
from config import *
import argparse
import json


class Demo:

    def __init__(self, args):
        self.superFactory = SuperFactory()
        self.director = Director(JSONBuilder())
        self.icon = icon
        self.args = args

    def demo(self, data):
        fjeFactory = self.superFactory.createFactory(args['style'])
        fje = fjeFactory.createFJE(icon[args['icon_family']])
        components = self.director.construct(data)
        fje.display(components)


if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='命令行参数')

    parser.add_argument('-f',
                        '--file',
                        type = str,
                        help = '选择 json 文件')

    parser.add_argument('-s',
                        '--style',
                        type = str,
                        choices = ['tree', 'rect'],
                        default = 'tree',
                        help = '选择风格')

    parser.add_argument('-i',
                        '--icon_family',
                        type = str,
                        choices = ['default', 'fruit', 'animal', 'sports'],
                        default = 'default',
                        help = '选择图标族')

    args = vars(parser.parse_args())

    with open(args['file'], 'r') as f:
        json_string = f.read()

    data = json.loads(json_string)

    demo = Demo(args)
    demo.demo(data)