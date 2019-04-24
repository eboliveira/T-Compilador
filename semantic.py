from syntax import main

from anytree import Node
from anytree.dotexport import DotExporter

if __name__=='__main__':
    root = main()
    DotExporter(root).to_picture('teste.png')