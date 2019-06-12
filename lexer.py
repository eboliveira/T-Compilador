# -*- coding: UTF-8 -*-
import ply.lex as lex
from ply.lex import TOKEN
import sys
import re

# Dictionary of reserved words
reserved = {
    'se': 'SE',
    'então'.decode('utf-8'): 'ENTAO',
    'senão'.decode('utf-8'): 'SENAO',
    'fim': 'FIM',
    'leia': 'LEIA',
    'escreva': 'ESCREVA',
    'retorna': 'RETORNA',
    'até'.decode('utf-8'): 'ATE',
    'flutuante': 'FLUTUANTE',
    'inteiro': 'INTEIRO',
    'repita': 'REPITA',
}

# List of token names
tokens = [
             # Logicals
             'E', 'OU', 'NAO',

             # Arithmeticals
             'SOMA', 'SUBTRACAO', 'MULTIPLICACAO', 'DIVISAO',

             # Relationals
             'MENOR_IGUAL', 'MAIOR_IGUAL', 'IGUAL', 'DIFERENTE', 'MENOR', 'MAIOR',

             # Types
             'NUM_PONTO_FLUTUANTE', 'NUM_INTEIRO',

             # Symbols
             'VIRGULA', 'ATRIBUICAO', 'ABRE_PARENTESES', 'FECHA_PARENTESES', 'ABRE_COLCHETE', 'FECHA_COLCHETE',
             'ABRE_CHAVE', 'FECHA_CHAVE', 'DOIS_PONTOS',

             # Others
             'ID', 'COMENTARIO'] + \
         list(reserved.values())

# Regular expressions rulers
t_NUM_PONTO_FLUTUANTE = r'((\d+)(\.\d+)(e(\+|-)?(\d+))?|(\d+)e(\+|-)?(\d+))'
t_NUM_INTEIRO = r'\d+'

t_E = r'&&'
t_OU = r'\|'
t_NAO = r'\!'

t_SOMA = r'\+'
t_SUBTRACAO = r'-'
t_MULTIPLICACAO = r'\*'
t_DIVISAO = r'/'

t_VIRGULA = r','
t_ATRIBUICAO = r':='
t_ABRE_PARENTESES = r'\('
t_FECHA_PARENTESES = r'\)'
t_ABRE_COLCHETE = r'\['
t_FECHA_COLCHETE = r'\]'
t_ABRE_CHAVE = r'\{'
t_FECHA_CHAVE = r'\}'
t_DOIS_PONTOS = r':'

t_MENOR_IGUAL = r'<='
t_MAIOR_IGUAL = r'>='
t_IGUAL = r'='
t_DIFERENTE = r'<>'
t_MENOR = r'<'
t_MAIOR = r'>'


def t_ID(t):
    r'[A-Za-zÁ-Ñá-ñ_][\w_]*'
    t.type = reserved.get(t.value, 'ID')
    return t


def t_COMENTARIO(t):
    r'{[^(})]*}'
    lineCount = re.findall('\n', t.value)
    t.lexer.lineno += len(lineCount)


# New lines will be counted
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


# Contains ignore characters as spaces and tabs
t_ignore = ' \t'


# Error handling rule
def t_error(t):
    raise Exception("Caracter ilegal '{}' (linha {})".format(t.value[0], t.lineno))


lexer = lex.lex(optimize=0, reflags=re.UNICODE)

if __name__ == '__main__':
    symbols_list = []
    symbol = {}
    all_tokens = []
    my_token = {}
    code = open(sys.argv[1])
    code_text = code.read()
    lex.input(code_text.decode('utf-8'))
    while True:
        tok = lex.token()
        if not tok:
            break
        my_token['Tipo'] = tok.type
        my_token['Linha'] = tok.lineno
        my_token['Valor'] = tok.value
        all_tokens.append(my_token)
        print my_token
    my_token = {}
