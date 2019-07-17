# -*- coding: utf-8 -*-
from ctypes import CFUNCTYPE, c_int
from Scope import Scope
from llvmlite import ir
from utils import *
import collections


def get_const(value_param, type_param):
    return ir.Constant(type_param, value_param)


def get_type_llvm(type_param):
    if type_param == 'INTEIRO':
        return ir.IntType(32)
    elif type_param == 'FLUTUANTE':
        return ir.FloatType()
    elif type_param == '':
        return ir.VoidType()


def get_name_var(blocks):
    name = ''
    for block in blocks:
        name += block.name
        name += '_'
    return name


def alloc_var(var_name, builder, tipo, ir):
    ptr = builder.alloca(get_type_llvm(tipo), name=var_name)
    zero = ir.Constant(get_type_llvm(tipo), 0)
    builder.store(zero, ptr)
    return ptr


def mount_expression(node_param, l):
    node_name = get_name(node_param)
    if node_name == 'numero' or node_name == 'var':
        l.append(get_last_value_name(node_param.children[0]))
        return
    if 'expressao' in node_name:
        op = get_name(node_param.children[1].children[0])
        l.append(mount_expression(node_param.children[0], l))
        l.append(op)
        if 'expressao' not in get_name(node_param.children[2].children[0]):
            l.append(get_last_value_name(node_param.children[2].children[0]))
    if 'expressao' in get_name(node_param.children[2]):
        op = get_name(node_param.children[2].children[1].children[0])
        l.append(mount_expression(node_param.children[2].children[0], l))
        l.append(op)
        l.append(get_last_value_name(node_param.children[2].children[2].children[0]))


def create_operation(a, op, b, all_vars_param, builder):
    exp_type = ''
    if is_constant(a):
        exp_type = 'FLUTUANTE' if a.find('.') > 0 else 'INTEIRO'
    else:
        var = get_var(a, all_vars_param)
        exp_type = 'INTEIRO' if type(var['ptr'].type.pointee) == ir.IntType else 'FLUTUANTE'
    if is_constant(a):
        if exp_type == 'INTEIRO':
            ptr_a = get_const(int(a), get_type_llvm(exp_type))
        else:
            ptr_a = get_const(float(a), get_type_llvm(exp_type))
    else:
        ptr_a = get_var(a, all_vars_param)['ptr']
    if is_constant(b):
        if exp_type == 'INTEIRO':
            ptr_b = get_const(int(b), get_type_llvm(exp_type))
        else:
            ptr_b = get_const(float(b), get_type_llvm(exp_type))
    else:
        ptr_b = get_var(b, all_vars_param)['ptr']

    print ptr_b, ptr_a

    ptr_a = ptr_a if type(ptr_a) == ir.Constant else builder.load(ptr_a)
    ptr_b = ptr_b if type(ptr_b) == ir.Constant else builder.load(ptr_b)
    return_val = None
    if op == 'SUBTRACAO':
        if exp_type == 'INTEIRO':
            return_val = builder.sub(ptr_a, ptr_b)
        else:
            return_val = builder.fsub(ptr_a, ptr_b)
    elif op == 'DIVISAO':
        if exp_type == 'INTEIRO':
            return_val = builder.div(ptr_a, ptr_b)
        else:
            return_val = builder.fdiv(ptr_a, ptr_b)
    elif op == 'MULTIPLICACAO':
        if exp_type == 'INTEIRO':
            return_val = builder.mul(ptr_a, ptr_b)
        else:
            return_val = builder.fmul(ptr_a, ptr_b)
    elif op == 'SOMA':
        if exp_type == 'INTEIRO':
            return_val = builder.add(ptr_a, ptr_b)
        else:
            return_val = builder.fadd(ptr_a, ptr_b)
    return return_val


def get_value(value, all_vars_param):
    if len(value.split('_')) > 1:
        if is_constant(value.split('_')[-1]):
            value = value.split('_')[-1]
            if value.find('.') > 0:
                return get_const(float(value), get_type_llvm('FLUTUANTE'))
            else:
                return get_const(int(value), get_type_llvm('INTEIRO'))
        else:
            return get_var(value, all_vars_param)
    else:
        if is_constant(value):
            if value.find('.') > 0:
                return get_const(float(value), get_type_llvm('FLUTUANTE'))
            else:
                return get_const(int(value), get_type_llvm('INTEIRO'))
        else:
            return get_var(value, all_vars_param)


def get_result_expression(node_param, expression):
    mount_expression(node_param.children[2], expression)
    simplify_expression = [item for item in expression if item is not None]
    return simplify_expression


def get_ptr(id_param, all_vars_param, blocks):
    id_formatted = get_name_var(blocks) + id_param
    for var in all_vars_param[-1]:
        if var['id'] == id_formatted:
            return var['ptr']


def is_constant(value):
    return value.replace('.', '').isnumeric()


def get_var(value, all_vars_param):
    for all_vars in all_vars_param:
        for var in all_vars:
            if var['id'] == value:
                return var
    try:
        values = value.split('_')
        values.pop(-2)
        value = "_".join(values)
        return get_var(value, all_vars_param)
    except Exception:
        pass


def split_exp(exp):
    mult_div_exp = []
    iterator = 0
    for op in exp:
        if op == 'DIVISAO ' or op == 'MULTIPLICACAO':
            if iterator > 1:
                while True:
                    if iterator + 2 < len(exp):
                        mult_div_exp.append(exp[iterator - 1:iterator + 2])
                        try:
                            exp.pop(iterator - 2)
                            exp.pop(iterator - 2)
                            exp.pop(iterator - 2)
                            exp.pop(iterator - 2)
                        except e:
                            pass
                        print exp
                    else:
                        break
            else:
                pass
        iterator += 1
    return [1, 2]
