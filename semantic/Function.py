class Function:
    def __init__(self, name, param_list, id, type, line):
        self.name = name
        self.param_list = param_list
        self.id = id
        self.has_return = False
        self.type = type
        self.line = line
        self.used = False
