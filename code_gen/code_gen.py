import sys
from llvmlite import ir
from anytree import PreOrderIter
sys.path.append('/home/eduardo/Dropbox/Universidade/6_Periodo/COMPILERS/T-Compilador/semantic')
from semantic import functions, root
from utils_gen import *
from utils import *
from Generator import Generator
from Function import Function
from llvmlite import binding

generator = Generator(functions)

for node in PreOrderIter(root):
    node_name = get_name(node)
    if node_name == 'declaracao_funcao':
        generator.func_declaration(node)
    elif node_name == 'declaracao_variaveis':
        generator.var_declaration(node)
    elif node_name == 'FIM':
        generator.end(node)
    elif node_name == 'retorna':
        generator.ret(node)
    elif node_name == 'atribuicao':
        generator.assign(node)
    elif node_name == 'se':
        generator.conditional(node)
    elif node_name == 'ENTAO' or node_name == 'SENAO' or node_name == 'ATE':
        generator.change_pos_builder(node)
    elif node_name == 'REPITA':
        generator.repetition()


with open('module.ll', 'w') as out_file:
    out_file.write(str(generator.module))
    out_file.close()

binding.initialize()
binding.initialize_native_target()
binding.initialize_all_asmprinters()

t = binding.Target.from_default_triple()
tm = t.create_target_machine()

bm = binding.parse_assembly("")
eng = binding.create_mcjit_compiler(bm, tm)

mod = binding.parse_assembly(str(generator.module))
mod.verify()

eng.add_module(mod)
eng.finalize_object()
eng.run_static_constructors()

fn_ptr = eng.get_function_address('main')

c_fn = CFUNCTYPE(c_int)(fn_ptr)
res = c_fn()
print 'retorno = ' + str(res)
