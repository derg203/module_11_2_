import pprint
import inspect
import requests
import pandas as pd
import pprint
class Class1():
    def __init__(self):
        self.attribute_1 = 2
    def some_class_method(self, value):
        self.attribute_1 = value
        print(self.attribute_1)
def introspection_info(obj = None):
    print (f'элемент {obj}')
    info_obj : info = {}
    info_obj['type'] = type(obj)
    info_obj['attributes'] = [a for a in dir(obj) if not callable(getattr(obj, a))]
    info_obj['methods'] = [a for a in dir(obj) if  callable(getattr(obj, a))]
    info_obj['module'] = (__name__)

    for key in info_obj:
        print(key,info_obj[key])




if __name__ == "__main__":

    info = introspection_info(42)
    print()
    pprint.pprint(info)

    info = introspection_info('Hello')
    print()
    pprint.pprint(info)

    info = introspection_info(introspection_info)
    print()
    pprint.pprint(info)

    info = introspection_info(Class1)
    print()
    pprint.pprint(info)

    obj_class1 = Class1()
    info = introspection_info(obj_class1)
    print()
    pprint.pprint(info)

    info = introspection_info()
    print()
    pprint.pprint(info)

#Вывод на консоль:
#{'type': 'int', 'attributes': [...], 'methods': ['__abs__', '__add__', ...], 'module': '__main__'}