# coding=utf-8
from ast import AST
from ply import yacc
from lexer import tokens
from lexer import symbols_list
from anytree import Node
from anytree.dotexport import DotExporter

count = 0
parent = ''
children = ''
root = None

def counter():
    global count
    count += 1

def create_node(name, parent = None):
    global count
    count+=1
    if(parent):
        return Node(str(count) + '#' + name, parent)
    else:
        return Node(str(count) + '#' + name)

def p_program(t):
    """ programa : lista_declaracoes
    """
    global root
    root = create_node('programa')
    t[0] = root
    t[1].parent = root

def p_program_error(t):
    """ programa : error
    """
    print ("Erro na regra programa")


def p_operation_list(t):
    ''' lista_declaracoes : lista_declaracoes declaracao
    | declaracao
    '''
    father = create_node('lista_declaracoes')
    t[0] = father
    t[1].parent = father
    if len(t) > 2:
        t[2].parent = father


def p_operation_list_error(t):
    ''' lista_declaracoes : error declaracao
    '''
    father = create_node('error')
    t[0] = father
    t[1].parent = father
    if len(t) > 2:
        t[2].parent = father
    print ("Erro na regra lista_declaracoes")

def p_operation_list_error_2(t):
    ''' lista_declaracoes : lista_declaracoes error
    '''
    father = create_node('error')
    t[0] = father
    t[1].parent = father
    if len(t) > 2:
        t[2].parent = father
    print ("Erro na regra lista_declaracoes")

def p_operation_list_error_3(t):
    ''' lista_declaracoes : error
    '''
    father = create_node('error')
    t[0] = father
    t[1].parent = father
    if len(t) > 2:
        t[2].parent = father
    print ("Erro na regra lista_declaracoes")


def p_declaration(t):
    ''' declaracao : declaracao_variaveis
    | inicializacao_variaveis
    | declaracao_funcao
    '''
    father = create_node('declaracao')
    t[0] = father
    t[1].parent = father

def p_declaration_error(t):
    ''' declaracao : error
    '''
    father = create_node('error')
    t[0] = father
    t[1].parent = father
    print ("Erro na regra de declaração")

def p_var_declaration(t):
    ''' declaracao_variaveis : tipo DOIS_PONTOS lista_variaveis
    '''
    father = create_node('declaracao_variaveis')
    t[0] = father
    t[1].parent = father
    t[2] = create_node('DOIS_PONTOS',father)
    t[3].parent = father

def p_var_declaration_error_1(t):
    ''' declaracao_variaveis : error DOIS_PONTOS lista_variaveis
    '''
    father = create_node('error')
    t[0] = father
    t[1].parent = father
    t[2] = create_node('DOIS_PONTOS',father)
    t[3].parent = father
    print ("Erro na regra de declaracao_variaveis")

def p_var_declaration_error_2(t):
    ''' declaracao_variaveis : tipo DOIS_PONTOS error
    '''
    father = create_node('error')
    t[0] = father
    t[1].parent = father
    t[2] = create_node('DOIS_PONTOS',father)
    t[3].parent = father
    print ("Erro na regra de declaracao_variaveis")

def p_var_init(t):
    ''' inicializacao_variaveis : atribuicao
    '''
    father = create_node('inicializacao_variaveis')
    t[0] = father
    t[1].parent = father

def p_var_init_error(t):
    ''' inicializacao_variaveis : error
    '''
    father = create_node('error')
    t[0] = father
    t[1].parent = father
    print ("Erro na regra de inicializacao_variaveis")

def p_list_var_init(t):
    ''' lista_variaveis : lista_variaveis VIRGULA var
    | var
    '''
    father = create_node('lista_variaveis')
    t[0] = father
    t[1].parent = father
    if (len(t)>2):
        t[2] = create_node('VIRGULA', father)
        t[3].parent = father

def p_list_var_init_error_1(t):
    ''' lista_variaveis : error VIRGULA var
    '''
    father = create_node('error')
    t[0] = father
    t[1].parent = father
    if (len(t)>2):
        t[2] = create_node('VIRGULA', father)
        t[3].parent = father
    print ("Erro na regra de lista_variaveis")

def p_list_var_init_error_2(t):
    ''' lista_variaveis : lista_variaveis VIRGULA error
    '''
    father = create_node('error')
    t[0] = father
    t[1].parent = father
    if (len(t)>2):
        t[2] = create_node('VIRGULA', father)
        t[3].parent = father
    print ("Erro na regra de lista_variaveis")

def p_list_var_init_error_3(t):
    ''' lista_variaveis : error
    '''
    father = create_node('error')
    t[0] = father
    t[1].parent = father
    if (len(t)>2):
        t[2] = create_node('VIRGULA', father)
        t[3].parent = father
    print ("Erro na regra de lista_variaveis")

def p_var(t):
    ''' var : ID
    | ID indice
    '''
    father = create_node('var')
    t[0] = father
    create_node('ID', father)
    if len(t)>2:
        t[2].parent = father

def p_var_error(t):
    ''' var : ID error
    '''
    father = create_node('error')
    t[0] = father
    create_node('ID', father)
    if len(t)>2:
        t[2].parent = father
    print ("Erro na regra de var")

def p_index(t):
    ''' indice : indice ABRE_COLCHETE expressao FECHA_COLCHETE
    | ABRE_COLCHETE expressao FECHA_COLCHETE
    '''
    father = create_node('indice')
    t[0] = father
    if len(t) == 4:
        t[1] = create_node('ABRE_COLCHETE', father)
        t[2].parent = father
        t[3] = create_node('FECHA_COLCHETE', father)
    else:
        t[1].parent = father
        t[2] = create_node('ABRE_COLCHETE', father)
        t[3].parent = father
        t[4] = create_node('FECHA_COLCHETE', father)

def p_index_error(t):
    ''' indice : indice ABRE_COLCHETE error FECHA_COLCHETE
    | ABRE_COLCHETE error FECHA_COLCHETE
    | error ABRE_COLCHETE expressao FECHA_COLCHETE
    '''
    father = create_node('error')
    t[0] = father
    if len(t) == 4:
        t[1] = create_node('ABRE_COLCHETE', father)
        t[2].parent = father
        t[3] = create_node('FECHA_COLCHETE', father)
    else:
        t[1].parent = father
        t[2] = create_node('ABRE_COLCHETE', father)
        t[3].parent = father
        t[4] = create_node('FECHA_COLCHETE', father)
    print "Erro na geração da regra indice"

def p_type(t):
    ''' tipo : INTEIRO
    | FLUTUANTE
    '''
    father = create_node('tipo')
    t[0] = father
    t[1] = create_node(t[1].upper(), father)

def p_func_declaration(t):
    ''' declaracao_funcao : tipo cabecalho
    | cabecalho
    '''
    father = create_node('declaracao_funcao')
    t[0] = father
    t[1].parent = father
    if len(t) == 3:
        t[2].parent = father

def p_func_declaration_error(t):
    ''' declaracao_funcao : error cabecalho
    | tipo error
    | error
    '''
    father = create_node('error')
    t[0] = father
    t[1].parent = father
    if len(t) == 3:
        t[2].parent = father
    print "Erro na geração da regra declaracao_funcao"


def p_header(t):
    ''' cabecalho : ID ABRE_PARENTESES lista_parametros FECHA_PARENTESES corpo FIM
    '''
    father = create_node('cabecalho')
    t[0] = father
    t[1] = create_node('ID', father)
    t[2] = create_node('ABRE_PARENTESES', father)
    t[3].parent = father
    t[4] = create_node('FECHA_PARENTESES', father)
    t[5].parent = father
    t[6] = create_node('FIM', father)

def p_header_error(t):
    ''' cabecalho : ID ABRE_PARENTESES error FECHA_PARENTESES corpo FIM
    | ID ABRE_PARENTESES lista_parametros FECHA_PARENTESES error FIM
    '''
    father = create_node('error')
    t[0] = father
    t[1] = create_node('ID', father)
    t[2] = create_node('ABRE_PARENTESES', father)
    t[3].parent = father
    t[4] = create_node('FECHA_PARENTESES', father)
    t[5].parent = father
    t[6] = create_node('FIM', father)
    print "Erro na geração da regra declaracao_funcao"

def p_param_list(t):
    ''' lista_parametros : lista_parametros VIRGULA lista_parametros
    | parametro
    | vazio
    '''
    father = create_node('lista_parametros')
    t[0] = father
    t[1].parent = father
    if len(t) > 2:
        t[2] = create_node('VIRUGLA', father)
        t[3].parent = father

def p_param_list_error(t):
    ''' lista_parametros : error VIRGULA lista_parametros
    | lista_parametros VIRGULA error
    | error
    '''
    father = create_node('error')
    t[0] = father
    t[1].parent = father
    if len(t) > 2:
        t[2] = create_node('VIRUGLA', father)
        t[3].parent = father
    father = create_node('erro')
    t[0] = father
    t[1].parent = father
    if len(t) > 2:
        t[2] = create_node('VIRUGLA', father)
        t[3].parent = father
    print "Erro na geração da regra lista_parametros"


def p_param(t):
    ''' parametro : tipo DOIS_PONTOS ID
    | parametro ABRE_COLCHETE FECHA_COLCHETE
    '''
    father = create_node('parametro')
    t[0] = father
    t[1].parent = father
    if t[2] == ':':
        t[2] = create_node('DOIS_PONTOS', father)
        t[3] = create_node('ID', father)
    else:
        t[2] = create_node('ABRE_COLCHETE', father)
        t[3] = create_node('FECHA_COLCHETE' , father)

def p_param_error(t):
    ''' parametro : error DOIS_PONTOS ID
    | error ABRE_COLCHETE FECHA_COLCHETE
    '''
    father = create_node('error')
    t[0] = father
    t[1].parent = father
    if t[2] == ':':
        t[2] = create_node('DOIS_PONTOS', father)
        t[3] = create_node('ID', father)
    else:
        t[2] = create_node('ABRE_COLCHETE', father)
        t[3] = create_node('FECHA_COLCHETE' , father)
    print "Erro na geração da regra parametro"

def p_body(t):
    ''' corpo : corpo acao
    | vazio
    '''
    father = create_node('corpo')
    t[0] = father
    t[1].parent = father
    if len(t)==3:
        t[2].parent = father

def p_body_error(t):
    ''' corpo : error acao
    | corpo error
    | error
    '''
    father = create_node('error')
    t[0] = father
    t[1].parent = father
    if len(t)==3:
        t[2].parent = father
    print "Erro na geração da regra corpo"


def p_action(t):
    ''' acao : expressao
    | declaracao_variaveis
    | se
    | repita
    | leia
    | escreva
    | retorna
    '''
    father = create_node('acao')
    t[0] = father
    t[1].parent = father

def p_action_error(t):
    ''' acao : error
    '''
    father = create_node('error')
    t[0] = father
    t[1].parent = father
    print "Erro na geração da regra acao"

def p_if(t):
    ''' se : SE expressao ENTAO corpo FIM
    | SE expressao ENTAO corpo SENAO corpo FIM
    '''
    father = create_node('se')
    t[0] = father
    t[1] = create_node('SE', father)
    t[2].parent = father
    t[3] = create_node('ENTAO', father)
    t[4].parent = father
    if len(t) == 8:
        t[5] = create_node('SENAO', father)
        t[6].parent = father
        t[7] = create_node('FIM', father)
    else:
        t[5] = create_node('FIM', father)

def p_if_error(t):
    ''' se : SE error ENTAO corpo FIM
    | SE expressao ENTAO error FIM
    | SE error ENTAO corpo SENAO corpo FIM
    | SE expressao ENTAO error SENAO corpo FIM
    | SE expressao ENTAO corpo SENAO error FIM
    '''
    father = create_node('error')
    t[0] = father
    t[1] = create_node('SE', father)
    t[2].parent = father
    t[3] = create_node('ENTAO', father)
    t[4].parent = father
    if len(t) == 8:
        t[5] = create_node('SENAO', father)
        t[6].parent = father
        t[7] = create_node('FIM', father)
    else:
        t[5] = create_node('FIM', father)
    print "Erro na geração da regra se"


def p_while(t):
    ''' repita : REPITA corpo ATE expressao
    '''
    father = create_node('repita')
    t[0] = father
    t[1] = create_node('REPITA', father)
    t[2].parent = father
    t[3] = create_node('ATE', father)
    t[4].parent = father

def p_while_error(t):
    ''' repita : REPITA corpo ATE error
    | REPITA error ATE expressao
    '''
    father = create_node('error')
    t[0] = father
    t[1] = create_node('REPITA', father)
    t[2].parent = father
    t[3] = create_node('ATE', father)
    t[4].parent = father
    print "Erro na geração da regra repita"

def p_assign(t):
    ''' atribuicao : var ATRIBUICAO expressao
    '''
    father = create_node('atribuicao')
    t[0] = father
    t[1].parent = father
    t[2] = create_node('ATRIBUICAO', father)
    t[3].parent = father

def p_assign_error(t):
    ''' atribuicao : var ATRIBUICAO error
    | error ATRIBUICAO expressao
    '''
    father = create_node('error')
    t[0] = father
    t[1].parent = father
    t[2] = create_node('ATRIBUICAO', father)
    t[3].parent = father

def p_read(t):
    ''' leia : LEIA ABRE_PARENTESES expressao FECHA_PARENTESES
    '''
    father = create_node('leia')
    t[0] = father
    t[1] = create_node('LEIA', father)
    t[2] = create_node('ABRE_PARENTESES', father)
    t[3].parent = father
    t[4] = create_node('FECHA_PARENTESES', father)

def p_read_error(t):
    ''' leia : LEIA ABRE_PARENTESES error FECHA_PARENTESES
    '''
    father = create_node('error')
    t[0] = father
    t[1] = create_node('LEIA', father)
    t[2] = create_node('ABRE_PARENTESES', father)
    t[3].parent = father
    t[4] = create_node('FECHA_PARENTESES', father)
    print "Erro na geração da regra leia"

def p_write(t):
    ''' escreva : ESCREVA ABRE_PARENTESES expressao FECHA_PARENTESES
    '''
    father = create_node('escreva')
    t[0] = father
    t[1] = create_node('ESCREVA', father)
    t[2] = create_node('ABRE_PARENTESES', father)
    t[3].parent = father
    t[4] = create_node('FECHA_PARENTESES', father)

def p_write_error(t):
    ''' escreva : ESCREVA ABRE_PARENTESES error FECHA_PARENTESES
    '''
    father = create_node('error')
    t[0] = father
    t[1] = create_node('ESCREVA', father)
    t[2] = create_node('ABRE_PARENTESES', father)
    t[3].parent = father
    t[4] = create_node('FECHA_PARENTESES', father)
    print "Erro na geração da regra leia"


def p_return(t):
    ''' retorna : RETORNA ABRE_PARENTESES expressao FECHA_PARENTESES
    '''
    father = create_node('retorna')
    t[0] = father
    t[1] = create_node('RETORNA', father)
    t[2] = create_node('ABRE_PARENTESES', father)
    t[3].parent = father
    t[4] = create_node('FECHA_PARENTESES', father)

def p_return_error(t):
    ''' retorna : RETORNA ABRE_PARENTESES error FECHA_PARENTESES
    '''
    father = create_node('error')
    t[0] = father
    t[1] = create_node('RETORNA', father)
    t[2] = create_node('ABRE_PARENTESES', father)
    t[3].parent = father
    t[4] = create_node('FECHA_PARENTESES', father)
    print "Erro na geração da regra retorna"

def p_expression(t):
    ''' expressao : expressao_logica
    | atribuicao
    '''
    father = create_node('expressao')
    t[0] = father
    t[1].parent = father

def p_expression_error(t):
    ''' expressao : error
    '''
    father = create_node('error')
    t[0] = father
    t[1].parent = father
    print "Erro na geração da regra expressao"


def p_logical_expression(t):
    ''' expressao_logica : expressao_simples
    | expressao_logica operador_logico expressao_simples
    '''
    father = create_node('expressao_logica')
    t[0] = father
    t[1].parent = father
    if len(t)>2:
        t[2].parent = father
        t[3].parent = father

def p_logical_expression_error(t):
    ''' expressao_logica : error operador_logico expressao_simples
    | expressao_logica error expressao_simples
    | expressao_logica operador_logico error
    | error
    '''
    father = create_node('error')
    t[0] = father
    t[1].parent = father
    if len(t)>2:
        t[2].parent = father
        t[3].parent = father
    print "Erro na geração da regra expressao_logica"


def p_simple_expression(t):
    ''' expressao_simples : expressao_aditiva
    | expressao_logica operador_relacional expressao_simples
    '''
    father = create_node('expressao_simples')
    t[0] = father
    t[1].parent = father
    if len(t) > 2:
        t[2].parent = father
        t[3].parent = father

def p_simple_expression_error(t):
    ''' expressao_simples : error
    | error operador_relacional expressao_simples
    | expressao_logica error expressao_simples
    | expressao_logica operador_relacional error
    '''
    father = create_node('error')
    t[0] = father
    t[1].parent = father
    if len(t) > 2:
        t[2].parent = father
        t[3].parent = father
    print "Erro na geração da regra expressao_simples"

def p_aditive_expression(t):
    ''' expressao_aditiva : expressao_multiplicativa
    | expressao_aditiva operador_soma expressao_multiplicativa
    '''
    father = create_node('expressao_aditiva')
    t[0] = father
    t[1].parent = father
    if len(t) > 2:
        t[2].parent = father
        t[3].parent = father

def p_aditive_expression_error(t):
    ''' expressao_aditiva : error
    | error operador_soma expressao_multiplicativa
    | expressao_aditiva error expressao_multiplicativa
    | expressao_aditiva operador_soma error
    '''
    father = create_node('error')
    t[0] = father
    t[1].parent = father
    if len(t) > 2:
        t[2].parent = father
        t[3].parent = father
    print "Erro na geração da regra expressao_aditiva"


def p_times_expression(t):
    ''' expressao_multiplicativa : expressao_unaria
    | expressao_multiplicativa operador_multiplicacao expressao_unaria
    '''
    father = create_node('expressao_multiplicativa')
    t[0] = father
    t[1].parent = father
    if len(t) > 2:
        t[2].parent = father
        t[3].parent = father

def p_times_expression_error(t):
    ''' expressao_multiplicativa : error
    | error operador_multiplicacao expressao_unaria
    | expressao_multiplicativa error expressao_unaria
    | expressao_multiplicativa operador_multiplicacao error
    '''
    father = create_node('error')
    t[0] = father
    t[1].parent = father
    if len(t) > 2:
        t[2].parent = father
        t[3].parent = father
    print "Erro na geração da regra expressao_aditiva"



def p_unary_expression(t):
    ''' expressao_unaria : fator
    | operador_soma fator
    | NAO fator
    '''
    father = create_node('expressao_unaria')
    t[0] = father
    if t[1] == '!':
        t[1] = create_node('NAO', father)
    else:
        t[1].parent = father

    if len(t) > 2:
        t[2].parent = father

def p_unary_expression_error(t):
    ''' expressao_unaria : error
    | error fator
    | operador_soma error
    | NAO error
    '''
    father = create_node('error')
    t[0] = father
    if t[1] == '!':
        t[1] = create_node('NAO', father)
    else:
        t[1].parent = father

    if len(t) > 2:
        t[2].parent = father
    print "Erro na geração da regra expressao_aditiva"


def p_relational_operator(t):
    ''' operador_relacional : MENOR
    | MAIOR
    | IGUAL
    | DIFERENTE
    | MENOR_IGUAL
    | MAIOR_IGUAL
    '''
    father = create_node('operador_relacional')
    t[0] = father
    if t[1] == '<':
        t[1] = create_node('MENOR', father)
    elif t[1] == '>':
        t[1] = create_node('MAIOR', father)
    elif t[1] == '=':
        t[1] = create_node('IGUAL', father)
    elif t[1] == '<>':
        t[1] = create_node('DIFERENTE', father)
    elif t[1] == '>=':
        t[1] = create_node('MAIOR_GUAL', father)
    else:
        t[1] = create_node('MENOR_IGUAL', father)


def p_sum_operator(t):
    ''' operador_soma : SOMA
    | SUBTRACAO
    '''
    father = create_node('operador_soma')
    t[0] = father
    if t[1] == '+':
        t[1] = create_node('SOMA', father)
    else:
        t[1] = create_node('SUBTRACAO', father)

def p_logical_operator(t):
    ''' operador_logico : E
    | OU
    '''
    father = create_node('operador_logico')
    t[0] = father
    if t[1] == '&&':
        t[1] = create_node('E', father)
    else:
        t[1] = create_node('OU', father)


def p_not_operator(t):
    ''' operador_negacao : NAO
    '''
    father = create_node('operador_negacao')
    t[0] = father
    t[1] = create_node('NAO', father)


def p_times_operator(t):
    ''' operador_multiplicacao : MULTIPLICACAO
    | DIVISAO
    '''
    father = create_node('operador_multiplicacao')
    t[0] = father
    if t[1] == '*':
        t[1] = create_node('MULTIPLICACAO', father)
    else:
        t[1] = create_node('DIVISAO', father)




def p_factor(t):
    ''' fator : ABRE_PARENTESES expressao FECHA_PARENTESES
    | var
    | chamada_funcao
    | numero
    '''
    father = create_node('operador_soma')
    t[0] = father
    if len(t) > 2:
        t[1] = create_node('ABRE_PARENTESES', father)
        t[2].parent = father
        t[3] = create_node('FECHA_PARENTESES', father)
    else:
        t[1].parent = father

def p_factor_error(t):
    ''' fator : ABRE_PARENTESES error FECHA_PARENTESES
    | error
    '''
    father = create_node('operador_soma')
    t[0] = father
    if len(t) > 2:
        t[1] = create_node('ABRE_PARENTESES', father)
        t[2].parent = father
        t[3] = create_node('FECHA_PARENTESES', father)
    else:
        t[1].parent = father
    print("Erro na geração da regra fator")


def p_number(t):
    ''' numero : NUM_INTEIRO
    | NUM_PONTO_FLUTUANTE
    '''
    father = create_node('numero')
    t[0] = father
    if t[1].find('.') == -1:
        t[1] = create_node('NUM_INTEIRO', father)
    else:
        t[1] = create_node('NUM_PONTO_FLUTUANTE', father)

def p_function_call(t):
    ''' chamada_funcao : ID ABRE_PARENTESES lista_argumentos FECHA_PARENTESES
    '''
    father = create_node('chamada_funcao')
    t[0] = father
    t[1] = create_node('ID', father)
    t[2] = create_node('ABRE_PARENTESES', father)
    t[3].parent = father
    t[4] = create_node('FECHA_PARENTESES', father)

def p_function_call_error(t):
    ''' chamada_funcao : ID ABRE_PARENTESES error FECHA_PARENTESES
    '''
    father = create_node('error')
    t[0] = father
    t[1] = create_node('ID', father)
    t[2] = create_node('ABRE_PARENTESES', father)
    t[3].parent = father
    t[4] = create_node('FECHA_PARENTESES', father)
    print("Erro na geração da regra fator")

def p_arguments_list(t):
    ''' lista_argumentos : lista_argumentos VIRGULA expressao
    | expressao
    | vazio
    '''
    father = create_node('lista_argumentos')
    t[0] = father
    t[1].parent = father
    if len(t) > 2:
        t[2] = create_node('VIRGULA', father)
        t[3].parent = father

def p_arguments_list(t):
    ''' lista_argumentos : error VIRGULA expressao
    | lista_argumentos VIRGULA error
    | error
    '''
    father = create_node('lista_argumentos')
    t[0] = father
    t[1].parent = father
    if len(t) > 2:
        t[2] = create_node('VIRGULA', father)
        t[3].parent = father
    print("Erro na geração da regra fator")

def p_empty(t):
    ' vazio : '
    father = create_node('vazio')
    t[0] = father

def p_error(t):
    if t:
        print "Erro de sintaxe na linha {} no token '{}'".format(t.lineno, t.value)
    else:
        print "Erro no EOF"
        parser.restart()


def parse_tree(code):
    parser = yacc.yacc(debug=True)
    return parser.parse(code)

def main():
    import sys
    parser = yacc.yacc(debug=True)
    code = open(sys.argv[1])
    code_text = code.read()
    parser.parse(code_text.decode('utf-8'))
    if not root:
        raise Exception('Nao foi possivel gerar a árvore')
    DotExporter(root).to_picture('syntatic_tree.png')
    return root

main()



