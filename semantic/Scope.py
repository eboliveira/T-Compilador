# coding: utf-8
from utils import create_var


class Scope:
    scopes = []
    generators = ['repita', 'se', 'cabecalho']

    def __init__(self):
        self.create_scope('global')

    def get_actual_scope(self):
        return self.scopes[len(self.scopes)-1]

    def create_scope(self, name, type_param='void', line_param=None, is_function=False):
        actual_scope = dict(name=name, type=type_param, line=line_param, is_function=is_function, variables=[])
        self.scopes.append(actual_scope)
        return actual_scope

    def insert_var(self, id_param, type_param, line_param, is_param):
        lexeme = create_var(id_param, type_param, line_param, is_param)
        for var in self.get_actual_scope().get('variables'):
            if var['id'] == lexeme['id']:
                raise (
                    Exception('Variável "{}" já definida anteriormente na linha {}'
                              .format(lexeme['id'], var['line'])))
        self.get_actual_scope().get('variables').append(lexeme)

    def get_var(self, id_param):
        for scp in reversed(self.scopes):
            for var in scp['variables']:
                if var['id'] == id_param:
                    return var
        return None
