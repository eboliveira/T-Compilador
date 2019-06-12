# coding:utf-8
from anytree import LevelOrderIter
from lexer import t_NUM_INTEIRO
from lexer import t_NUM_PONTO_FLUTUANTE
import re


def trim_tree(root_param):
    for node_iter in LevelOrderIter(root_param):
        if len(node_iter.children) == 1:
            if node_iter.children[0].children:
                nod_name = get_name(node_iter)
                if nod_name != 'programa':
                    children = node_iter.children
                    parent = node_iter.parent
                    node_iter.children[0].parent = node_iter.parent
                    parent.children = tuple(list(parent.children)[0:len(parent.children) - 1])
                    list_children = list(node_iter.parent.children)
                    for i in range(len(list_children)):
                        if list_children[i] == node_iter:
                            list_children[i] = children[0]
                    node_iter.parent.children = tuple(list_children)
                    trim_tree(root_param)
                    break


def create_var(id_param=None, type_param=None, line_param=None, is_param=None):
    var = {'id': id_param, 'type': type_param, 'line': line_param, 'value': None, 'used': False, 'is_param': is_param}
    return var


def is_id_exists(name, scop):
    if name in scop:
        return True
    else:
        return False


def get_name(node_param):
    node_param_name = re.search('#(.)*', node_param.name).group(0)
    node_param_name = node_param_name[1:len(node_param_name)]
    haves_id = re.search('(.)*-', node_param_name)
    if haves_id:
        node_param_name = haves_id.group(0)
        node_param_name = node_param_name[:len(node_param_name) - 1]
    return node_param_name


def get_last_value_name(node_param):
    return re.search('-(.)*', node_param.name).group(0)[1:len(node_param.name) + 1]


def is_float(node_param):
    if not re.search('^' + t_NUM_PONTO_FLUTUANTE + '$', get_last_value_name(node_param.children[2].children[0])):
        raise Exception("Esperando receber valor inteiro, mas foi recebido um valor diferente (linha {})."
                        .format(node_param.children[0].children[0].line))


def is_integer(node_param):
    if not re.search('^' + t_NUM_INTEIRO + '$', get_last_value_name(node_param.children[2].children[0])):
        raise Exception("Esperando receber valor inteiro, mas foi recebido um valor diferente (linha {})."
                        .format(node_param.children[0].children[0].line))


def get_type(nod, scop, function_list=None):
    if get_name(nod) == 'ID':
        if get_name(nod.parent) == 'chamada_funcao':
            fun_name = get_last_value_name(nod)
            return next(fun.type for fun in function_list if fun.name == fun_name)
        else:
            var_compare = scop.get_var(get_last_value_name(nod))
            if not var_compare:
                raise Exception(
                    "Variável '{}' não foi definida previamente (linha {})"
                        .format(get_last_value_name(nod), nod.line))
            return var_compare['type']
    else:
        nod_type = get_name(nod)
        nod_type = re.search('_[^_]*$', nod_type)
        if not nod_type:
            return
        nod_type = nod_type.group(0)
        nod_type = nod_type[1:len(nod_type)]
        return nod_type


def check_expression(expression_param, scope_param):
    children1 = expression_param.children[0]
    children2 = expression_param.children[2]
    children1_type = ''
    children2_type = ''
    if get_name(children1) in ('var', 'numero'):
        children1_type = get_type(children1.children[0], scope_param)

    elif get_name(children1)[:9] == 'expressao':
        children1_type = check_expression(children1, scope_param)

    elif get_name(children1) == 'fator':
        children1_type = check_factor(children1, scope_param)

    if get_name(children2) in ('var', 'numero'):
        children2_type = get_type(children2.children[0], scope_param)

    elif get_name(children2) == 'fator':
        children2_type = check_factor(children2, scope_param)

    elif get_name(children2)[:9] == 'expressao':
        children2_type = check_expression(children2, scope_param)

    if children1_type != children2_type:
        return False
    else:
        return children1_type


def check_factor(factor_param, scope_param):
    if get_name(factor_param.children[1])[:9] == 'expressao':
        return check_expression(factor_param.children[1], scope_param)
    elif get_name(factor_param.children[1]) == 'fator':
        return check_factor(factor_param.children[1], scope_param)
    elif get_name(factor_param.children[1]) in ('var', 'numero'):
        return get_type(factor_param.children[1].children[0], scope_param)


def get_params(param_list_node, param_list):
    if get_name(param_list_node) == 'lista_parametros':
        if get_name(param_list_node.children[0]) == 'vazio':
            return param_list
        param_list.append({'type': get_name(param_list_node.children[0].children[0].children[0]),
                           'name': get_last_value_name(param_list_node.children[0].children[2]),
                           'line': param_list_node.children[0].children[2].line})

        if get_name(param_list_node.children[2]) == 'lista_parametros':
            get_params(param_list_node.children[2], param_list)
            return param_list

        elif get_name(param_list_node.children[2]) == 'parametro':
            param_list.append({'type': get_name(param_list_node.children[2].children[0].children[0]),
                               'name': get_last_value_name(param_list_node.children[2].children[2]),
                               'line': param_list_node.children[2].children[2].line})
            return param_list
    elif get_name(param_list_node) == 'parametro':
        param_list.append({'type': get_name(param_list_node.children[0].children[0]),
                           'name': get_last_value_name(param_list_node.children[2]),
                           'line': param_list_node.children[2].line})
        return param_list


def validate_function(fun, variables):
    if fun.type != '':
        if not fun.has_return:
            raise Exception(
                "Função '{}' com o tipo {} declarada mas sem retorno (linha {})".format(fun.name, fun.type,
                                                                                        fun.line))
    verify_unused_vars(variables)


def verify_unused_vars(variables):
    non_used_variables = []
    for variable in variables:
        if not variable['used']:
            non_used_variables.append(variable)
    for var in non_used_variables:
        if var['is_param']:
            print("Atenção: parâmetro '{}' declarado na linha {} e não utilizado".format(var['id'], var['line']))
        else:
            print("Atenção: variável '{}' declarada na linha {} e não utilizada".format(var['id'], var['line']))


def verify_haves_main(functions_list):
    haves_main = [fun for fun in functions_list if fun.name == 'principal']
    if len(haves_main) == 0:
        raise Exception("Função principal não foi declarada")
    elif len(haves_main) > 1:
        raise Exception("Função principal declarada mais de uma vez")


def verify_unused_functions(functions_list):
    for fun in functions_list:
        if not fun.used:
            print("Função '{}' declarada mas não utilizada (linha {})"
                  .format(fun.name, fun.line))


def check_index(var_node, scope_param):
    if len(var_node.children) > 1:
        index_node = var_node.children[1]
        if get_name(index_node.children[1])[:9] == 'expressao':  # se for indice
            if (check_expression(index_node.children[1], scope_param)) in ('FLUTUANTE', False):
                raise Exception("Número flutuante usado como índice de vetor linha {}"
                                .format(var_node.children[0].line))
        elif get_name(index_node.children[1]) in ('numero', 'var'):
            if get_type(index_node.children[1].children[0], scope_param) == 'FLUTUANTE':
                raise Exception("Número flutuante usado como índice de vetor linha {}"
                                .format(var_node.children[0].line))


def count_arguments(argument_list_node):
    count = 0
    if get_name(argument_list_node.children[0]) == 'vazio':
        return count
    count = 2
    node_walk = argument_list_node.children[0]
    while get_name(node_walk) == 'lista_argumentos':
        count += 1
        node_walk = node_walk.children[0]
    return count


def check_type_arguments(argument_list_node, param_list, functions_list):
    node_walk = argument_list_node
    i = len(param_list) - 1
    while get_name(node_walk) != 'numero':
        print node_walk
        if get_name(node_walk) == 'chamada_funcao':
            fun_name = get_last_value_name(node_walk.children[0])
            fun_instance = next(func for func in functions_list if func.name == fun_name)
            if fun_instance.type != param_list[i].get('type'):
                raise Exception("Argumento '{}' deve ser do tipo {} (linha {})"
                                .format(param_list[i].get('name'),
                                        param_list[i].get('type'),
                                        argument_list_node.parent.children[0].line))
            node_walk = node_walk.children[2]
        else:
            if get_type(node_walk.children[2].children[0], None, functions_list) != param_list[i].get('type'):
                raise Exception("Argumento '{}' deve ser do tipo {} (linha {})"
                                .format(param_list[i].get('name'),
                                        param_list[i].get('type'),
                                        argument_list_node.parent.children[0].line))
            node_walk = node_walk.children[0]
        i -= 1
    if get_type(node_walk.children[0], None) != param_list[i].get('type'):
        raise Exception("Argumento '{}' deve ser do tipo {} (linha {})"
                        .format(param_list[i].get('name'),
                                param_list[i].get('type'),
                                argument_list_node.parent.children[0].line))


def get_function_by_name(name, functions_list):
    return next(func for func in functions_list if func.name == name)
