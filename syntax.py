from ast import AST
from ply import yacc
from lexer import tokens
from lexer import symbols_list


def p_program(t):
    ''' programa : lista_declaracoes 
    '''

def p_operation_list(t):
    ''' lista_declaracoes : lista_declaracoes declaracao
    | declaracao
    '''
    
def p_declaration(t):
    ''' declaracao : declaracao_variaveis
    | inicializacao_variaveis
    | declaracao_funcao
    '''
    
def p_var_declaration(t):
    ''' declaracao_variaveis : tipo DOIS_PONTOS lista_variaveis
    '''

def p_var_init(t):
    ''' inicializacao_variaveis : atribuicao
    '''

def p_list_var_init(t):
    ''' lista_variaveis : lista_variaveis VIRGULA var
    | var
    '''

def p_var(t):
    ''' var : ID
    | ID indice
    '''
    
def p_index(t):
    ''' indice : indice ABRE_COLCHETE expressao FECHA_COLCHETE
    | ABRE_COLCHETE expressao FECHA_COLCHETE
    '''

def p_type(t):
    ''' tipo : INTEIRO
    | FLUTUANTE
    '''

def p_func_declaration(t):
    ''' declaracao_funcao : tipo cabecalho
    | cabecalho
    '''

def p_header(t):
    ''' cabecalho : ID ABRE_PARENTESES lista_parametros FECHA_PARENTESES corpo FIM
    '''

def p_param_list(t):
    ''' lista_parametros : lista_parametros VIRGULA lista_parametros
    | parametro
    | vazio
    '''

def p_param(t):
    ''' parametro : tipo DOIS_PONTOS ID
    | parametro ABRE_COLCHETE FECHA_COLCHETE
    '''

def p_body(t):
    ''' corpo : corpo acao
    | vazio
    '''
    
def p_action(t):
    ''' acao : expressao
    | declaracao_variaveis
    | se
    | repita
    | leia
    | escreva
    | retorna
    '''

def p_if(t):
    ''' se : SE expressao ENTAO corpo FIM
    | SE expressao ENTAO corpo SENAO corpo FIM
    '''

def p_while(t):
    ''' repita : REPITA corpo ATE expressao
    '''

def p_assign(t):
    ''' atribuicao : var ATRIBUICAO expressao
    '''

def p_read(t):
    ''' leia : LEIA ABRE_PARENTESES expressao FECHA_PARENTESES
    '''

def p_write(t):
    ''' escreva : ESCREVA ABRE_PARENTESES expressao FECHA_PARENTESES
    '''

def p_return(t):
    ''' retorna : RETORNA ABRE_PARENTESES expressao FECHA_PARENTESES
    '''

def p_expression(t):
    ''' expressao : expressao_logica
    | atribuicao
    '''

def p_logical_expression(t):
    ''' expressao_logica : expressao_simples
    | expressao_logica operador_logico expressao_simples
    '''

def p_simple_expression(t):
    ''' expressao_simples : expressao_aditiva
    | expressao_logica operador_relacional expressao_simples
    '''

def p_aditive_expression(t):
    ''' expressao_aditiva : expressao_multiplicativa
    | expressao_aditiva operador_soma expressao_multiplicativa
    '''

def p_times_expression(t):
    ''' expressao_multiplicativa : expressao_unaria
    | expressao_multiplicativa operador_multiplicacao expressao_unaria
    '''


def p_unary_expression(t):
    ''' expressao_unaria : fator
    | operador_soma fator
    | NAO fator
    '''

def p_relational_operator(t):
    ''' operador_relacional : MENOR
    | MAIOR
    | IGUAL
    | DIFERENTE
    | MENOR_IGUAL
    | MAIOR_IGUAL
    '''

def p_sum_operator(t):
    ''' operador_soma : SOMA
    | SUBTRACAO
    '''

def p_logical_operator(t):
    ''' operador_logico : E
    | OU
    '''

def p_not_operator(t):
    ''' operador_negacao : NAO
    '''

def p_times_operator(t):
    ''' operador_multiplicacao : MULTIPLICACAO
    | DIVISAO
    '''

def p_factor(t):
    ''' fator : ABRE_PARENTESES expressao FECHA_PARENTESES
    | var
    | chamada_funcao
    | numero
    '''

def p_number(t):
    ''' numero : NUM_INTEIRO
    | NUM_PONTO_FLUTUANTE
    '''

def p_function_call(t):
    ''' chamada_funcao : ID ABRE_PARENTESES lista_argumentos FECHA_PARENTESES
    '''

def p_arguments_list(t):
    ''' lista_argumentos : lista_argumentos VIRGULA expressao
    | expressao
    | vazio
    '''

def p_empty(t):
    ' vazio : '

def p_error(t):
    if t:
        print "Syntax error: '%s' Line %d" % (t.value, t.lineno)
    else:
        parser.restart()
        print "Syntax error"

def parse_tree(code):
    parser = yacc.yacc(debug=True)
    return parser.parse(code)

if __name__ == "__main__":
    import sys
    parser = yacc.yacc(debug=True)
    code = open(sys.argv[1])
    code_text = code.read()
    parser.parse(code_text.decode('utf-8'))
