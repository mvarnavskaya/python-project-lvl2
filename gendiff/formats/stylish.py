# -*- coding:utf-8 -*-


def format_stylish(dic):
    diffe = '{\n'
    dicstr = write_dic(dic)
    indent = ' ' * 2
    dicstr = indent + dicstr.replace('\n', '\n' + indent)
    diffe += dicstr
    diffe = diffe[:-3] + diffe[-1]
    return diffe


def write_dic(dic):
    variable = ('changed', 'added', 'deleted', 'unchanged', 'changeddict')
    diffe = ''
    for item in dic.items():
        if isinstance(item[1][1], dict):
            value = format_stylish(item[1][1])
        else:
            value = item[1][1]
        if item[1][0] not in variable:
            diffe += f'  {item[0]}: {item[1]}\n'
            return diffe + '}'
        if item[1][0] == 'changed':
            diffe += f"- {item[0]}: {item[1][1]}\n"
            diffe += f"+ {item[0]}: {item[1][2]}\n"
        if item[1][0] == 'added':
            diffe += f"+ {item[0]}: {value}\n"
        if item[1][0] == 'deleted':
            diffe += f"- {item[0]}: {value}\n"
        if item[1][0] == 'unchanged' or item[1][0] == 'changeddict':
            diffe += f"  {item[0]}: {value}\n"
    return diffe + '}'
