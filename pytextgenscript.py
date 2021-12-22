"""
Python interpreter for TextGen Script

TextGen Script docs - https://janvarev.ru/TGen
"""

import sexpdata
from sexpdata import Symbol
import random

variables = dict()

def sexpToPlTxt(obj, gen_text):
    if (isinstance(obj, list)):
        if len(obj)==0:
            return ""
        else:
            cur_sym = obj[0]
            if isinstance(cur_sym, Symbol):
                cur_sym_value = cur_sym.value()
                if cur_sym == Symbol('#r'):
                    return sexpToPlTxt(random.choice(obj[1:]), gen_text)
                elif cur_sym_value == '#varSet':
                    variables[obj[1]]=sexpToPlTxt(obj[2], gen_text)
                    #variables[cur_sym[1]]=cur_sym[2]
                    #return sexpToPlTxt() #по идее, ничего возвращать не должна
                    #return sexpToPlTxt(obj[2], gen_text)
                    return ""
                elif cur_sym.value() == '#ifVarEq':
                    if (len(variables)) and (variables[obj[1]]==obj[2]):
                        return sexpToPlTxt(obj[3], gen_text)
                    else:
                        return sexpToPlTxt(obj[4], gen_text)
                elif cur_sym.value()[0] == '@':
                    #print(variables[cur_sym.value()[1:]])
                    var1 = variables[cur_sym.value()[1:]] #sexpToPlTxt(obj[0], gen_text)
                    return var1 + sexpToPlTxt(obj[1:], gen_text + var1)
                elif cur_sym_value == '#nl': # new line
                    var1 = "\r\n"
                    return var1 + sexpToPlTxt(obj[1:], gen_text + var1)
                else:
                    return '\n Error not found symbol: '+str(cur_sym)
            else:
                var1 = sexpToPlTxt(obj[0], gen_text)
                return var1 + sexpToPlTxt(obj[1:], gen_text+var1)
    else:
        return obj


# ------ Util functions ------

def s_to_sobj(s):
    return sexpdata.loads(s)

def run(sobj, def_vars = {}):
    global variables
    variables = def_vars.copy()
    return sexpToPlTxt(sobj,"")

def run_s(s, def_vars = {}):
    sobj = s_to_sobj(s)
    return run(sobj, def_vars)
