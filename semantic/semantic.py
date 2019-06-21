# coding=utf-8
from syntax import root, functions_id
from anytree import RenderTree, Walker, LevelOrderIter, PreOrderIter
from utils import *
from Scope import Scope
from Function import Function

from anytree.dotexport import DotExporter

if __name__ == '__main__':
    scope = Scope()
    functions = []
    trim_tree(root)
    DotExporter(root).to_picture('new_tree.png')
    for node in PreOrderIter(root):
        node_name = get_name(node)

        if node_name in scope.generators:
            if get_name(node.children[0]) == 'ID':
                all_scopes_names = [scp['name'] for scp in scope.scopes]
                if get_last_value_name(node.children[0]) in all_scopes_names:
                    raise Exception("Função previamente definida (linha {})"
                                    .format(node.children[0].line))
            elif get_name(node.children[0]) in ('SE', 'REPITA'):
                scope.create_scope(get_name(node.children[0]))
            if node_name == 'cabecalho':
                scope_name = get_last_value_name(node.children[0])
                type_fun = ''
                if get_name(node.parent) == 'declaracao_funcao':
                    type_fun = get_name(node.parent.children[0].children[0])
                    scope.create_scope(scope_name, type_fun, node.children[0].line, is_function=True)
                else:
                    scope.create_scope(scope_name, line_param=node.children[0].line, is_function=True)
                param_list = []
                param_list = get_params(node.children[2], param_list)
                for param in param_list:
                    scope.insert_var(param['name'], param['type'], param['line'], is_param=True)
                fun_id = get_last_value_name(node.children[0])
                functions.append(Function(scope_name, param_list, fun_id, type_fun, node.children[0].line))
                if fun_id == 'principal':
                    functions[len(functions) - 1].used = True

        elif node_name == 'FIM':
            if get_name(node.parent) == 'cabecalho':
                func_name = scope.get_actual_scope()['name']
                func_instance = next(fun for fun in functions if fun.name == func_name)
                validate_function(func_instance, scope.get_actual_scope()['variables'])
            elif get_name(node.parent) == 'SE':
                verify_unused_vars(scope.get_actual_scope()['variables'])
            scp = scope.scopes.pop()

        elif node_name == 'ATE':
            verify_unused_vars(scope.get_actual_scope()['variables'])
            scope.scopes.pop()

        if node_name == 'declaracao_variaveis':
            tipo = get_name(node.children[0].children[0])
            declaration_list_node = node.children[2]
            while get_name(declaration_list_node) != 'var':
                scope.insert_var(get_last_value_name(declaration_list_node.children[2].children[0]), tipo,
                                 declaration_list_node.children[2].children[0].line, is_param=False)
                check_index(declaration_list_node.children[2], scope)
                declaration_list_node = declaration_list_node.children[0]
            scope.insert_var(get_last_value_name(declaration_list_node.children[0]), tipo,
                             declaration_list_node.children[0].line, is_param=False)
            check_index(declaration_list_node, scope)

        elif node_name == 'atribuicao':
            scope.get_var(get_last_value_name(node.children[0].children[0]))['used'] = True
            var_type = get_type(node.children[0].children[0], scope)
            line = node.children[0].children[0].line
            var_walk = node.children[2]
            if get_name(var_walk) == 'fator':
                type_expression = check_factor(var_walk, scope)
                if not type_expression or type_expression != var_type:
                    raise Exception("Atribuição com váriaveis de tipo diferentes (linha {})".format(line))

            elif get_name(var_walk)[:9] == 'expressao':
                type_expression = check_expression(var_walk, scope)
                if not type_expression or type_expression != var_type:
                    raise Exception("Atribuição com váriaveis de tipo diferentes (linha {})".format(line))

            elif get_name(var_walk) == 'var':
                type_expression = get_type(var_walk.children[0], scope)
                if type_expression == 'Not var':
                    raise Exception("Variável '{}' não definida anteriomente (linha {})"
                                    .format(get_last_value_name(var_walk.children[0]), line))
                elif type_expression != var_type:
                    raise Exception("Atribuição com váriaveis de tipo diferentes (linha {})".format(line))
            elif get_name(var_walk) == 'chamada_funcao':
                func = next(fun for fun in functions if fun.name == get_last_value_name(var_walk.children[0]))
                if func.type != var_type:
                    raise Exception("Função retorna {} mas variável é do tipo {} (linha {})"
                                    .format(func.type, var_type, line))
            elif get_name(var_walk) == 'numero':
                type_assign = get_type(var_walk.children[0], scope)
                if type_assign != var_type:
                    raise Exception("Atribuição com valor diferente da variável (linha {})"
                                    .format(line))

        elif node_name == 'retorna':
            var_type = ''
            function_scope = max(fun for index, fun in enumerate(scope.scopes) if fun['is_function'])

            if function_scope['type'] == 'void':
                raise Exception("'retorna' sendo chamado dentro de uma função com retorno vazio (linha {})"
                                .format(node.children[0].line))
            if get_name(node.children[2]) in ('numero', 'var'):
                var_type = get_type(node.children[2].children[0], scope)
            elif get_name(node.children[2]) == 'fator':
                var_type = check_factor(node.children[2], scope)
            elif get_name(node.children[2])[:9] == 'expressao':
                var_type = check_expression(node.children[2], scope)
            if not var_type:
                raise Exception('Expressão ou fator com tipos diferentes (linha {})'
                                .format(node.children[0].line))
            if var_type != function_scope['type']:
                raise Exception("Tipo da função e tipo do retorno diferentes (linha {})".format(node.children[0].line))
            func_instance = next(fun for fun in functions if fun.name == function_scope['name'])
            func_instance.has_return = True

        elif node_name == 'se':
            valid = None
            if get_name(node.children[1]) == 'fator':
                valid = check_factor(node.children[1], scope)
            elif get_name(node.children[1])[:9] == 'expressao':
                valid = check_expression(node.children[1], scope)
            if not valid:
                raise Exception('Fator ou expressão com elementos de tipo diferente (linha {})'
                                .format(node.children[0].line))

        elif node_name == 'repita':
            valid = None
            if get_name(node.children[3]) == 'fator':
                valid = check_factor(node.children[3], scope)
            elif get_name(node.children[3])[:9] == 'expressao':
                valid = check_expression(node.children[3], scope)
            if not valid:
                raise Exception('Fator ou expressão com elementos de tipo diferente (linha {})'
                                .format(node.children[2].line))

        elif node_name == 'chamada_funcao':
            fun_name = get_last_value_name(node.children[0])
            if fun_name == 'principal':
                if scope.get_actual_scope()['name'] == 'principal':
                    print "Atenção: função 'principal' chamada recursivamente (linha {})".format(node.children[0].line)
                else:
                    raise Exception("Função principal sendo chamada (linha {})"
                                    .format(node.children[0].line))
            if fun_name not in functions_id:
                raise Exception("Função '{}' chamada mas não declarada anteriormente (linha {}) "
                                .format(fun_name, node.children[0].line))
            else:
                fun = next(func for func in functions if func.name == fun_name)
                if get_name(node.children[2]) == 'numero':
                    if len(fun.param_list) != 1:
                        raise Exception("Função '{}' espera {} paramêtros mas recebeu apenas 1 (linha {})"
                                        .format(fun_name, len(fun.param_list), node.children[0].line))
                    if get_type(node.children[2].children[0], None) != fun.param_list[0].get('type'):
                        raise Exception("Função espera parâmetro do tipo {} mas foi recebido o tipo {}"
                                        .format(fun.param_list[0].get('type'), get_type(node.children[2].children[0], None)))
                else:
                    arguments_len = count_arguments(node.children[2])
                    if arguments_len != len(fun.param_list):
                        raise Exception("Função '{}' espera {} paramêtros mas recebeu {} paramêtros (linha {})"
                                        .format(fun_name, len(fun.param_list),
                                                arguments_len, node.children[0].line))
                    check_type_arguments(node.children[2], fun.param_list, functions)
                fun.used = True

        elif node_name == 'var':
            if get_name(node.parent) != 'declaracao_variaveis' and get_name(node.parent) != 'lista_variaveis':
                var_name = get_last_value_name(node.children[0])
                if not scope.get_var(var_name)['used']:
                    if not scope.get_var(var_name)['is_param']:
                        if get_name(node.parent) != 'leia':
                            print("Atenção: variável '{}' não icializada e sendo utilizada (linha {})"
                                  .format(var_name, node.children[0].line))
                scope.get_var(var_name)['used'] = True

    verify_haves_main(functions)
    verify_unused_functions(functions)
    verify_unused_vars(scope.scopes[0].get('variables'))
