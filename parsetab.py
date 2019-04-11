
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'ABRE_CHAVE ABRE_COLCHETE ABRE_PARENTESES ATE ATRIBUICAO COMENTARIO DIFERENTE DIVISAO DOIS_PONTOS E ENTAO ESCREVA FECHA_CHAVE FECHA_COLCHETE FECHA_PARENTESES FIM FLUTUANTE ID IGUAL INTEIRO LEIA MAIOR MAIOR_IGUAL MENOR MENOR_IGUAL MULTIPLICACAO NAO NUM_INTEIRO NUM_PONTO_FLUTUANTE OU REPITA RETORNA SE SENAO SOMA SUBTRACAO VIRGULA programa : lista_declaracoes\n     lista_declaracoes : lista_declaracoes declaracao\n    | declaracao\n     declaracao : declaracao_variaveis\n    | inicializacao_variaveis\n    | declaracao_funcao\n     declaracao_variaveis : tipo DOIS_PONTOS lista_variaveis\n     inicializacao_variaveis : atribuicao\n     lista_variaveis : lista_variaveis VIRGULA var\n    | var\n     var : ID\n    | ID indice\n     indice : indice ABRE_COLCHETE expressao FECHA_COLCHETE\n    | ABRE_COLCHETE expressao FECHA_COLCHETE\n     tipo : INTEIRO\n    | FLUTUANTE\n     declaracao_funcao : tipo cabecalho\n    | cabecalho\n     cabecalho : ID ABRE_PARENTESES lista_parametros FECHA_PARENTESES corpo FIM\n     lista_parametros : lista_parametros VIRGULA lista_parametros\n    | parametro\n    | vazio\n     parametro : tipo DOIS_PONTOS ID\n    | parametro ABRE_COLCHETE FECHA_COLCHETE\n     corpo : corpo acao\n    | vazio\n     acao : expressao\n    | declaracao_variaveis\n    | se\n    | repita\n    | leia\n    | escreva\n    | retorna\n     se : SE expressao ENTAO corpo FIM\n    | SE expressao ENTAO corpo SENAO corpo FIM\n     repita : REPITA corpo ATE expressao\n     atribuicao : var ATRIBUICAO expressao\n     leia : LEIA ABRE_PARENTESES expressao FECHA_PARENTESES\n     escreva : ESCREVA ABRE_PARENTESES expressao FECHA_PARENTESES\n     retorna : RETORNA ABRE_PARENTESES expressao FECHA_PARENTESES\n     expressao : expressao_logica\n    | atribuicao\n     expressao_logica : expressao_simples\n    | expressao_logica operador_logico expressao_simples\n     expressao_simples : expressao_aditiva\n    | expressao_logica operador_relacional expressao_simples\n     expressao_aditiva : expressao_multiplicativa\n    | expressao_aditiva operador_soma expressao_multiplicativa\n     expressao_multiplicativa : expressao_unaria\n    | expressao_multiplicativa operador_multiplicacao expressao_unaria\n     expressao_unaria : fator\n    | operador_soma fator\n    | NAO fator\n     operador_relacional : MENOR\n    | MAIOR\n    | IGUAL\n    | DIFERENTE\n    | MENOR_IGUAL\n    | MAIOR_IGUAL\n     operador_soma : SOMA\n    | SUBTRACAO\n     operador_logico : E\n    | OU\n     operador_negacao : NAO\n     operador_multiplicacao : MULTIPLICACAO\n    | DIVISAO\n     fator : ABRE_PARENTESES expressao FECHA_PARENTESES\n    | var\n    | chamada_funcao\n    | numero\n     numero : NUM_INTEIRO\n    | NUM_PONTO_FLUTUANTE\n     chamada_funcao : ID ABRE_PARENTESES lista_argumentos FECHA_PARENTESES\n     lista_argumentos : lista_argumentos VIRGULA expressao\n    | expressao\n    | vazio\n     vazio : '
    
_lr_action_items = {'NUM_INTEIRO':([18,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,48,51,52,53,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,71,75,76,77,78,82,84,85,87,88,91,92,93,95,96,98,99,100,101,103,105,106,108,110,111,112,113,116,119,120,121,122,123,124,125,126,127,128,],[35,-12,35,-7,-10,-11,-43,-60,35,35,-61,35,-37,-51,-68,-49,-71,-72,-69,-45,-70,-11,-41,-42,-47,35,-52,-68,-53,35,35,-62,-55,35,-56,-57,-54,35,-63,-59,-58,-65,35,-66,-77,-14,-9,-67,-48,-46,-44,-50,-26,35,-13,35,-73,-25,-77,-27,-33,-31,-28,-32,-30,-29,35,35,35,35,35,35,-77,-39,-36,-40,-38,35,-77,-34,35,-35,]),'ATE':([20,22,23,24,25,31,32,33,34,35,36,37,38,39,40,41,42,43,51,52,53,75,76,77,78,82,84,85,87,91,93,95,96,98,99,100,101,103,105,106,111,120,121,122,123,126,128,],[-12,-7,-10,-11,-43,-37,-51,-68,-49,-71,-72,-69,-45,-70,-11,-41,-42,-47,-52,-68,-53,-14,-9,-67,-48,-46,-44,-50,-26,-13,-73,-25,-77,-27,-33,-31,-28,-32,-30,-29,116,-39,-36,-40,-38,-34,-35,]),'ESCREVA':([20,22,23,24,25,31,32,33,34,35,36,37,38,39,40,41,42,43,51,52,53,71,75,76,77,78,82,84,85,87,88,91,93,95,96,98,99,100,101,103,105,106,111,119,120,121,122,123,124,125,126,127,128,],[-12,-7,-10,-11,-43,-37,-51,-68,-49,-71,-72,-69,-45,-70,-11,-41,-42,-47,-52,-68,-53,-77,-14,-9,-67,-48,-46,-44,-50,-26,94,-13,-73,-25,-77,-27,-33,-31,-28,-32,-30,-29,94,-77,-39,-36,-40,-38,94,-77,-34,94,-35,]),'SUBTRACAO':([18,20,21,22,23,24,25,26,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,48,51,52,53,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,71,75,76,77,78,82,84,85,87,88,91,92,93,95,96,98,99,100,101,103,105,106,108,110,111,112,113,116,119,120,121,122,123,124,125,126,127,128,],[29,-12,29,-7,-10,-11,-43,-60,-61,29,-37,-51,-68,-49,-71,-72,-69,29,-70,-11,-41,-42,-47,29,-52,-68,-53,29,29,-62,-55,29,-56,-57,-54,29,-63,-59,-58,-65,29,-66,-77,-14,-9,-67,-48,-46,-44,-50,-26,29,-13,29,-73,-25,-77,-27,-33,-31,-28,-32,-30,-29,29,29,29,29,29,29,-77,-39,-36,-40,-38,29,-77,-34,29,-35,]),'SOMA':([18,20,21,22,23,24,25,26,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,48,51,52,53,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,71,75,76,77,78,82,84,85,87,88,91,92,93,95,96,98,99,100,101,103,105,106,108,110,111,112,113,116,119,120,121,122,123,124,125,126,127,128,],[26,-12,26,-7,-10,-11,-43,-60,-61,26,-37,-51,-68,-49,-71,-72,-69,26,-70,-11,-41,-42,-47,26,-52,-68,-53,26,26,-62,-55,26,-56,-57,-54,26,-63,-59,-58,-65,26,-66,-77,-14,-9,-67,-48,-46,-44,-50,-26,26,-13,26,-73,-25,-77,-27,-33,-31,-28,-32,-30,-29,26,26,26,26,26,26,-77,-39,-36,-40,-38,26,-77,-34,26,-35,]),'NAO':([18,20,21,22,23,24,25,26,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,48,51,52,53,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,71,75,76,77,78,82,84,85,87,88,91,92,93,95,96,98,99,100,101,103,105,106,108,110,111,112,113,116,119,120,121,122,123,124,125,126,127,128,],[28,-12,28,-7,-10,-11,-43,-60,-61,28,-37,-51,-68,-49,-71,-72,-69,-45,-70,-11,-41,-42,-47,28,-52,-68,-53,28,28,-62,-55,28,-56,-57,-54,28,-63,-59,-58,-65,28,-66,-77,-14,-9,-67,-48,-46,-44,-50,-26,28,-13,28,-73,-25,-77,-27,-33,-31,-28,-32,-30,-29,28,28,28,28,28,28,-77,-39,-36,-40,-38,28,-77,-34,28,-35,]),'IGUAL':([20,25,32,33,34,35,36,37,38,39,40,41,43,51,52,53,75,77,78,82,83,84,85,91,93,],[-12,-43,-51,-68,-49,-71,-72,-69,-45,-70,-11,60,-47,-52,-68,-53,-14,-67,-48,-43,60,-43,-50,-13,-73,]),'DIFERENTE':([20,25,32,33,34,35,36,37,38,39,40,41,43,51,52,53,75,77,78,82,83,84,85,91,93,],[-12,-43,-51,-68,-49,-71,-72,-69,-45,-70,-11,61,-47,-52,-68,-53,-14,-67,-48,-43,61,-43,-50,-13,-73,]),'FECHA_COLCHETE':([20,25,31,32,33,34,35,36,37,38,39,40,41,42,43,49,51,52,53,73,74,75,77,78,82,84,85,91,93,],[-12,-43,-37,-51,-68,-49,-71,-72,-69,-45,-70,-11,-41,-42,-47,75,-52,-68,-53,90,91,-14,-67,-48,-46,-44,-50,-13,-73,]),'ABRE_PARENTESES':([11,16,18,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,48,51,52,53,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,71,75,76,77,78,82,84,85,87,88,91,92,93,94,95,96,98,99,100,101,102,103,105,106,107,108,110,111,112,113,116,119,120,121,122,123,124,125,126,127,128,],[19,19,30,-12,30,-7,-10,-11,-43,-60,30,30,-61,30,-37,-51,-68,-49,-71,-72,-69,-45,-70,56,-41,-42,-47,30,-52,-68,-53,30,30,-62,-55,30,-56,-57,-54,30,-63,-59,-58,-65,30,-66,-77,-14,-9,-67,-48,-46,-44,-50,-26,30,-13,30,-73,110,-25,-77,-27,-33,-31,-28,112,-32,-30,-29,113,30,30,30,30,30,30,-77,-39,-36,-40,-38,30,-77,-34,30,-35,]),'VIRGULA':([19,20,22,23,24,25,31,32,33,34,35,36,37,38,39,40,41,42,43,44,46,47,51,52,53,56,70,75,76,77,78,79,80,81,82,84,85,86,89,90,91,93,109,],[-77,-12,50,-10,-11,-43,-37,-51,-68,-49,-71,-72,-69,-45,-70,-11,-41,-42,-47,70,-21,-22,-52,-68,-53,-77,-77,-14,-9,-67,-48,92,-75,-76,-46,-44,-50,70,-23,-24,-13,-73,-74,]),'MAIOR_IGUAL':([20,25,32,33,34,35,36,37,38,39,40,41,43,51,52,53,75,77,78,82,83,84,85,91,93,],[-12,-43,-51,-68,-49,-71,-72,-69,-45,-70,-11,65,-47,-52,-68,-53,-14,-67,-48,-43,65,-43,-50,-13,-73,]),'ATRIBUICAO':([6,11,20,33,40,75,91,],[18,-11,-12,18,-11,-14,-13,]),'MAIOR':([20,25,32,33,34,35,36,37,38,39,40,41,43,51,52,53,75,77,78,82,83,84,85,91,93,],[-12,-43,-51,-68,-49,-71,-72,-69,-45,-70,-11,58,-47,-52,-68,-53,-14,-67,-48,-43,58,-43,-50,-13,-73,]),'MULTIPLICACAO':([20,32,33,34,35,36,37,39,40,43,51,52,53,75,77,78,85,91,93,],[-12,-51,-68,-49,-71,-72,-69,-70,-11,67,-52,-68,-53,-14,-67,67,-50,-13,-73,]),'FLUTUANTE':([0,1,2,4,8,9,10,12,15,17,19,20,22,23,24,25,31,32,33,34,35,36,37,38,39,40,41,42,43,51,52,53,70,71,75,76,77,78,82,84,85,87,88,91,93,95,96,98,99,100,101,103,104,105,106,111,119,120,121,122,123,124,125,126,127,128,],[5,-5,-18,5,-6,-4,-3,-8,-17,-2,5,-12,-7,-10,-11,-43,-37,-51,-68,-49,-71,-72,-69,-45,-70,-11,-41,-42,-47,-52,-68,-53,5,-77,-14,-9,-67,-48,-46,-44,-50,-26,5,-13,-73,-25,-77,-27,-33,-31,-28,-32,-19,-30,-29,5,-77,-39,-36,-40,-38,5,-77,-34,5,-35,]),'MENOR_IGUAL':([20,25,32,33,34,35,36,37,38,39,40,41,43,51,52,53,75,77,78,82,83,84,85,91,93,],[-12,-43,-51,-68,-49,-71,-72,-69,-45,-70,-11,66,-47,-52,-68,-53,-14,-67,-48,-43,66,-43,-50,-13,-73,]),'ABRE_COLCHETE':([11,20,24,40,46,75,89,90,91,],[21,48,21,21,73,-14,-23,-24,-13,]),'$end':([1,2,4,8,9,10,12,13,15,17,20,22,23,24,25,31,32,33,34,35,36,37,38,39,40,41,42,43,51,52,53,75,76,77,78,82,84,85,91,93,104,],[-5,-18,-1,-6,-4,-3,-8,0,-17,-2,-12,-7,-10,-11,-43,-37,-51,-68,-49,-71,-72,-69,-45,-70,-11,-41,-42,-47,-52,-68,-53,-14,-9,-67,-48,-46,-44,-50,-13,-73,-19,]),'E':([20,25,32,33,34,35,36,37,38,39,40,41,43,51,52,53,75,77,78,82,83,84,85,91,93,],[-12,-43,-51,-68,-49,-71,-72,-69,-45,-70,-11,57,-47,-52,-68,-53,-14,-67,-48,-43,57,-43,-50,-13,-73,]),'NUM_PONTO_FLUTUANTE':([18,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,48,51,52,53,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,71,75,76,77,78,82,84,85,87,88,91,92,93,95,96,98,99,100,101,103,105,106,108,110,111,112,113,116,119,120,121,122,123,124,125,126,127,128,],[36,-12,36,-7,-10,-11,-43,-60,36,36,-61,36,-37,-51,-68,-49,-71,-72,-69,-45,-70,-11,-41,-42,-47,36,-52,-68,-53,36,36,-62,-55,36,-56,-57,-54,36,-63,-59,-58,-65,36,-66,-77,-14,-9,-67,-48,-46,-44,-50,-26,36,-13,36,-73,-25,-77,-27,-33,-31,-28,-32,-30,-29,36,36,36,36,36,36,-77,-39,-36,-40,-38,36,-77,-34,36,-35,]),'ENTAO':([20,25,31,32,33,34,35,36,37,38,39,40,41,42,43,51,52,53,75,77,78,82,84,85,91,93,114,],[-12,-43,-37,-51,-68,-49,-71,-72,-69,-45,-70,-11,-41,-42,-47,-52,-68,-53,-14,-67,-48,-46,-44,-50,-13,-73,119,]),'SENAO':([20,22,23,24,25,31,32,33,34,35,36,37,38,39,40,41,42,43,51,52,53,75,76,77,78,82,84,85,87,91,93,95,98,99,100,101,103,105,106,119,120,121,122,123,124,126,128,],[-12,-7,-10,-11,-43,-37,-51,-68,-49,-71,-72,-69,-45,-70,-11,-41,-42,-47,-52,-68,-53,-14,-9,-67,-48,-46,-44,-50,-26,-13,-73,-25,-27,-33,-31,-28,-32,-30,-29,-77,-39,-36,-40,-38,125,-34,-35,]),'MENOR':([20,25,32,33,34,35,36,37,38,39,40,41,43,51,52,53,75,77,78,82,83,84,85,91,93,],[-12,-43,-51,-68,-49,-71,-72,-69,-45,-70,-11,62,-47,-52,-68,-53,-14,-67,-48,-43,62,-43,-50,-13,-73,]),'FECHA_PARENTESES':([19,20,25,31,32,33,34,35,36,37,38,39,40,41,42,43,44,46,47,51,52,53,54,56,70,75,77,78,79,80,81,82,84,85,86,89,90,91,93,109,115,117,118,],[-77,-12,-43,-37,-51,-68,-49,-71,-72,-69,-45,-70,-11,-41,-42,-47,71,-21,-22,-52,-68,-53,77,-77,-77,-14,-67,-48,93,-75,-76,-46,-44,-50,-20,-23,-24,-13,-73,-74,120,122,123,]),'RETORNA':([20,22,23,24,25,31,32,33,34,35,36,37,38,39,40,41,42,43,51,52,53,71,75,76,77,78,82,84,85,87,88,91,93,95,96,98,99,100,101,103,105,106,111,119,120,121,122,123,124,125,126,127,128,],[-12,-7,-10,-11,-43,-37,-51,-68,-49,-71,-72,-69,-45,-70,-11,-41,-42,-47,-52,-68,-53,-77,-14,-9,-67,-48,-46,-44,-50,-26,102,-13,-73,-25,-77,-27,-33,-31,-28,-32,-30,-29,102,-77,-39,-36,-40,-38,102,-77,-34,102,-35,]),'ID':([0,1,2,3,4,5,7,8,9,10,12,14,15,17,18,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,48,50,51,52,53,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,71,72,75,76,77,78,82,84,85,87,88,91,92,93,95,96,98,99,100,101,103,104,105,106,108,110,111,112,113,116,119,120,121,122,123,124,125,126,127,128,],[11,-5,-18,16,11,-16,-15,-6,-4,-3,-8,24,-17,-2,40,-12,40,-7,-10,-11,-43,-60,40,40,-61,40,-37,-51,-68,-49,-71,-72,-69,-45,-70,-11,-41,-42,-47,40,24,-52,-68,-53,40,40,-62,-55,40,-56,-57,-54,40,-63,-59,-58,-65,40,-66,-77,89,-14,-9,-67,-48,-46,-44,-50,-26,40,-13,40,-73,-25,-77,-27,-33,-31,-28,-32,-19,-30,-29,40,40,40,40,40,40,-77,-39,-36,-40,-38,40,-77,-34,40,-35,]),'INTEIRO':([0,1,2,4,8,9,10,12,15,17,19,20,22,23,24,25,31,32,33,34,35,36,37,38,39,40,41,42,43,51,52,53,70,71,75,76,77,78,82,84,85,87,88,91,93,95,96,98,99,100,101,103,104,105,106,111,119,120,121,122,123,124,125,126,127,128,],[7,-5,-18,7,-6,-4,-3,-8,-17,-2,7,-12,-7,-10,-11,-43,-37,-51,-68,-49,-71,-72,-69,-45,-70,-11,-41,-42,-47,-52,-68,-53,7,-77,-14,-9,-67,-48,-46,-44,-50,-26,7,-13,-73,-25,-77,-27,-33,-31,-28,-32,-19,-30,-29,7,-77,-39,-36,-40,-38,7,-77,-34,7,-35,]),'REPITA':([20,22,23,24,25,31,32,33,34,35,36,37,38,39,40,41,42,43,51,52,53,71,75,76,77,78,82,84,85,87,88,91,93,95,96,98,99,100,101,103,105,106,111,119,120,121,122,123,124,125,126,127,128,],[-12,-7,-10,-11,-43,-37,-51,-68,-49,-71,-72,-69,-45,-70,-11,-41,-42,-47,-52,-68,-53,-77,-14,-9,-67,-48,-46,-44,-50,-26,96,-13,-73,-25,-77,-27,-33,-31,-28,-32,-30,-29,96,-77,-39,-36,-40,-38,96,-77,-34,96,-35,]),'FIM':([20,22,23,24,25,31,32,33,34,35,36,37,38,39,40,41,42,43,51,52,53,71,75,76,77,78,82,84,85,87,88,91,93,95,98,99,100,101,103,105,106,119,120,121,122,123,124,125,126,127,128,],[-12,-7,-10,-11,-43,-37,-51,-68,-49,-71,-72,-69,-45,-70,-11,-41,-42,-47,-52,-68,-53,-77,-14,-9,-67,-48,-46,-44,-50,-26,104,-13,-73,-25,-27,-33,-31,-28,-32,-30,-29,-77,-39,-36,-40,-38,126,-77,-34,128,-35,]),'DOIS_PONTOS':([3,5,7,45,97,],[14,-16,-15,72,14,]),'DIVISAO':([20,32,33,34,35,36,37,39,40,43,51,52,53,75,77,78,85,91,93,],[-12,-51,-68,-49,-71,-72,-69,-70,-11,69,-52,-68,-53,-14,-67,69,-50,-13,-73,]),'OU':([20,25,32,33,34,35,36,37,38,39,40,41,43,51,52,53,75,77,78,82,83,84,85,91,93,],[-12,-43,-51,-68,-49,-71,-72,-69,-45,-70,-11,64,-47,-52,-68,-53,-14,-67,-48,-43,64,-43,-50,-13,-73,]),'LEIA':([20,22,23,24,25,31,32,33,34,35,36,37,38,39,40,41,42,43,51,52,53,71,75,76,77,78,82,84,85,87,88,91,93,95,96,98,99,100,101,103,105,106,111,119,120,121,122,123,124,125,126,127,128,],[-12,-7,-10,-11,-43,-37,-51,-68,-49,-71,-72,-69,-45,-70,-11,-41,-42,-47,-52,-68,-53,-77,-14,-9,-67,-48,-46,-44,-50,-26,107,-13,-73,-25,-77,-27,-33,-31,-28,-32,-30,-29,107,-77,-39,-36,-40,-38,107,-77,-34,107,-35,]),'SE':([20,22,23,24,25,31,32,33,34,35,36,37,38,39,40,41,42,43,51,52,53,71,75,76,77,78,82,84,85,87,88,91,93,95,96,98,99,100,101,103,105,106,111,119,120,121,122,123,124,125,126,127,128,],[-12,-7,-10,-11,-43,-37,-51,-68,-49,-71,-72,-69,-45,-70,-11,-41,-42,-47,-52,-68,-53,-77,-14,-9,-67,-48,-46,-44,-50,-26,108,-13,-73,-25,-77,-27,-33,-31,-28,-32,-30,-29,108,-77,-39,-36,-40,-38,108,-77,-34,108,-35,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'indice':([11,24,40,],[20,20,20,]),'expressao_simples':([18,21,30,48,56,59,63,88,92,108,110,111,112,113,116,124,127,],[25,25,25,25,25,82,84,25,25,25,25,25,25,25,25,25,25,]),'numero':([18,21,27,28,30,48,55,56,59,63,68,88,92,108,110,111,112,113,116,124,127,],[39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,]),'operador_soma':([18,21,30,38,48,55,56,59,63,68,88,92,108,110,111,112,113,116,124,127,],[27,27,27,55,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,]),'inicializacao_variaveis':([0,4,],[1,1,]),'cabecalho':([0,3,4,],[2,15,2,]),'corpo':([71,96,119,125,],[88,111,124,127,]),'lista_variaveis':([14,],[22,]),'tipo':([0,4,19,70,88,111,124,127,],[3,3,45,45,97,97,97,97,]),'expressao':([18,21,30,48,56,88,92,108,110,111,112,113,116,124,127,],[31,49,54,74,80,98,109,114,115,98,117,118,121,98,98,]),'fator':([18,21,27,28,30,48,55,56,59,63,68,88,92,108,110,111,112,113,116,124,127,],[32,32,51,53,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,]),'acao':([88,111,124,127,],[95,95,95,95,]),'retorna':([88,111,124,127,],[99,99,99,99,]),'var':([0,4,14,18,21,27,28,30,48,50,55,56,59,63,68,88,92,108,110,111,112,113,116,124,127,],[6,6,23,33,33,52,52,33,33,76,52,33,52,52,52,33,33,33,33,33,33,33,33,33,33,]),'expressao_unaria':([18,21,30,48,55,56,59,63,68,88,92,108,110,111,112,113,116,124,127,],[34,34,34,34,34,34,34,34,85,34,34,34,34,34,34,34,34,34,34,]),'leia':([88,111,124,127,],[100,100,100,100,]),'programa':([0,],[13,]),'declaracao_funcao':([0,4,],[8,8,]),'parametro':([19,70,],[46,46,]),'chamada_funcao':([18,21,27,28,30,48,55,56,59,63,68,88,92,108,110,111,112,113,116,124,127,],[37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,]),'expressao_aditiva':([18,21,30,48,56,59,63,88,92,108,110,111,112,113,116,124,127,],[38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,]),'declaracao_variaveis':([0,4,88,111,124,127,],[9,9,101,101,101,101,]),'operador_logico':([41,83,],[63,63,]),'escreva':([88,111,124,127,],[103,103,103,103,]),'declaracao':([0,4,],[10,17,]),'lista_declaracoes':([0,],[4,]),'repita':([88,111,124,127,],[105,105,105,105,]),'lista_parametros':([19,70,],[44,86,]),'expressao_logica':([18,21,30,48,56,59,63,88,92,108,110,111,112,113,116,124,127,],[41,41,41,41,41,83,83,41,41,41,41,41,41,41,41,41,41,]),'atribuicao':([0,4,18,21,30,48,56,88,92,108,110,111,112,113,116,124,127,],[12,12,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,]),'operador_relacional':([41,83,],[59,59,]),'expressao_multiplicativa':([18,21,30,48,55,56,59,63,88,92,108,110,111,112,113,116,124,127,],[43,43,43,43,78,43,43,43,43,43,43,43,43,43,43,43,43,43,]),'vazio':([19,56,70,71,96,119,125,],[47,81,47,87,87,87,87,]),'lista_argumentos':([56,],[79,]),'operador_multiplicacao':([43,78,],[68,68,]),'se':([88,111,124,127,],[106,106,106,106,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> programa","S'",1,None,None,None),
  ('programa -> lista_declaracoes','programa',1,'p_program','syntax.py',24),
  ('lista_declaracoes -> lista_declaracoes declaracao','lista_declaracoes',2,'p_operation_list','syntax.py',29),
  ('lista_declaracoes -> declaracao','lista_declaracoes',1,'p_operation_list','syntax.py',30),
  ('declaracao -> declaracao_variaveis','declaracao',1,'p_declaration','syntax.py',35),
  ('declaracao -> inicializacao_variaveis','declaracao',1,'p_declaration','syntax.py',36),
  ('declaracao -> declaracao_funcao','declaracao',1,'p_declaration','syntax.py',37),
  ('declaracao_variaveis -> tipo DOIS_PONTOS lista_variaveis','declaracao_variaveis',3,'p_var_declaration','syntax.py',42),
  ('inicializacao_variaveis -> atribuicao','inicializacao_variaveis',1,'p_var_init','syntax.py',47),
  ('lista_variaveis -> lista_variaveis VIRGULA var','lista_variaveis',3,'p_list_var_init','syntax.py',52),
  ('lista_variaveis -> var','lista_variaveis',1,'p_list_var_init','syntax.py',53),
  ('var -> ID','var',1,'p_var','syntax.py',58),
  ('var -> ID indice','var',2,'p_var','syntax.py',59),
  ('indice -> indice ABRE_COLCHETE expressao FECHA_COLCHETE','indice',4,'p_index','syntax.py',64),
  ('indice -> ABRE_COLCHETE expressao FECHA_COLCHETE','indice',3,'p_index','syntax.py',65),
  ('tipo -> INTEIRO','tipo',1,'p_type','syntax.py',70),
  ('tipo -> FLUTUANTE','tipo',1,'p_type','syntax.py',71),
  ('declaracao_funcao -> tipo cabecalho','declaracao_funcao',2,'p_func_declaration','syntax.py',76),
  ('declaracao_funcao -> cabecalho','declaracao_funcao',1,'p_func_declaration','syntax.py',77),
  ('cabecalho -> ID ABRE_PARENTESES lista_parametros FECHA_PARENTESES corpo FIM','cabecalho',6,'p_header','syntax.py',82),
  ('lista_parametros -> lista_parametros VIRGULA lista_parametros','lista_parametros',3,'p_param_list','syntax.py',87),
  ('lista_parametros -> parametro','lista_parametros',1,'p_param_list','syntax.py',88),
  ('lista_parametros -> vazio','lista_parametros',1,'p_param_list','syntax.py',89),
  ('parametro -> tipo DOIS_PONTOS ID','parametro',3,'p_param','syntax.py',94),
  ('parametro -> parametro ABRE_COLCHETE FECHA_COLCHETE','parametro',3,'p_param','syntax.py',95),
  ('corpo -> corpo acao','corpo',2,'p_body','syntax.py',100),
  ('corpo -> vazio','corpo',1,'p_body','syntax.py',101),
  ('acao -> expressao','acao',1,'p_action','syntax.py',106),
  ('acao -> declaracao_variaveis','acao',1,'p_action','syntax.py',107),
  ('acao -> se','acao',1,'p_action','syntax.py',108),
  ('acao -> repita','acao',1,'p_action','syntax.py',109),
  ('acao -> leia','acao',1,'p_action','syntax.py',110),
  ('acao -> escreva','acao',1,'p_action','syntax.py',111),
  ('acao -> retorna','acao',1,'p_action','syntax.py',112),
  ('se -> SE expressao ENTAO corpo FIM','se',5,'p_if','syntax.py',117),
  ('se -> SE expressao ENTAO corpo SENAO corpo FIM','se',7,'p_if','syntax.py',118),
  ('repita -> REPITA corpo ATE expressao','repita',4,'p_while','syntax.py',123),
  ('atribuicao -> var ATRIBUICAO expressao','atribuicao',3,'p_assign','syntax.py',128),
  ('leia -> LEIA ABRE_PARENTESES expressao FECHA_PARENTESES','leia',4,'p_read','syntax.py',133),
  ('escreva -> ESCREVA ABRE_PARENTESES expressao FECHA_PARENTESES','escreva',4,'p_write','syntax.py',138),
  ('retorna -> RETORNA ABRE_PARENTESES expressao FECHA_PARENTESES','retorna',4,'p_return','syntax.py',143),
  ('expressao -> expressao_logica','expressao',1,'p_expression','syntax.py',148),
  ('expressao -> atribuicao','expressao',1,'p_expression','syntax.py',149),
  ('expressao_logica -> expressao_simples','expressao_logica',1,'p_logical_expression','syntax.py',154),
  ('expressao_logica -> expressao_logica operador_logico expressao_simples','expressao_logica',3,'p_logical_expression','syntax.py',155),
  ('expressao_simples -> expressao_aditiva','expressao_simples',1,'p_simple_expression','syntax.py',160),
  ('expressao_simples -> expressao_logica operador_relacional expressao_simples','expressao_simples',3,'p_simple_expression','syntax.py',161),
  ('expressao_aditiva -> expressao_multiplicativa','expressao_aditiva',1,'p_aditive_expression','syntax.py',166),
  ('expressao_aditiva -> expressao_aditiva operador_soma expressao_multiplicativa','expressao_aditiva',3,'p_aditive_expression','syntax.py',167),
  ('expressao_multiplicativa -> expressao_unaria','expressao_multiplicativa',1,'p_times_expression','syntax.py',172),
  ('expressao_multiplicativa -> expressao_multiplicativa operador_multiplicacao expressao_unaria','expressao_multiplicativa',3,'p_times_expression','syntax.py',173),
  ('expressao_unaria -> fator','expressao_unaria',1,'p_unary_expression','syntax.py',179),
  ('expressao_unaria -> operador_soma fator','expressao_unaria',2,'p_unary_expression','syntax.py',180),
  ('expressao_unaria -> NAO fator','expressao_unaria',2,'p_unary_expression','syntax.py',181),
  ('operador_relacional -> MENOR','operador_relacional',1,'p_relational_operator','syntax.py',186),
  ('operador_relacional -> MAIOR','operador_relacional',1,'p_relational_operator','syntax.py',187),
  ('operador_relacional -> IGUAL','operador_relacional',1,'p_relational_operator','syntax.py',188),
  ('operador_relacional -> DIFERENTE','operador_relacional',1,'p_relational_operator','syntax.py',189),
  ('operador_relacional -> MENOR_IGUAL','operador_relacional',1,'p_relational_operator','syntax.py',190),
  ('operador_relacional -> MAIOR_IGUAL','operador_relacional',1,'p_relational_operator','syntax.py',191),
  ('operador_soma -> SOMA','operador_soma',1,'p_sum_operator','syntax.py',196),
  ('operador_soma -> SUBTRACAO','operador_soma',1,'p_sum_operator','syntax.py',197),
  ('operador_logico -> E','operador_logico',1,'p_logical_operator','syntax.py',202),
  ('operador_logico -> OU','operador_logico',1,'p_logical_operator','syntax.py',203),
  ('operador_negacao -> NAO','operador_negacao',1,'p_not_operator','syntax.py',208),
  ('operador_multiplicacao -> MULTIPLICACAO','operador_multiplicacao',1,'p_times_operator','syntax.py',213),
  ('operador_multiplicacao -> DIVISAO','operador_multiplicacao',1,'p_times_operator','syntax.py',214),
  ('fator -> ABRE_PARENTESES expressao FECHA_PARENTESES','fator',3,'p_factor','syntax.py',220),
  ('fator -> var','fator',1,'p_factor','syntax.py',221),
  ('fator -> chamada_funcao','fator',1,'p_factor','syntax.py',222),
  ('fator -> numero','fator',1,'p_factor','syntax.py',223),
  ('numero -> NUM_INTEIRO','numero',1,'p_number','syntax.py',228),
  ('numero -> NUM_PONTO_FLUTUANTE','numero',1,'p_number','syntax.py',229),
  ('chamada_funcao -> ID ABRE_PARENTESES lista_argumentos FECHA_PARENTESES','chamada_funcao',4,'p_function_call','syntax.py',234),
  ('lista_argumentos -> lista_argumentos VIRGULA expressao','lista_argumentos',3,'p_arguments_list','syntax.py',239),
  ('lista_argumentos -> expressao','lista_argumentos',1,'p_arguments_list','syntax.py',240),
  ('lista_argumentos -> vazio','lista_argumentos',1,'p_arguments_list','syntax.py',241),
  ('vazio -> <empty>','vazio',0,'p_empty','syntax.py',246),
]
