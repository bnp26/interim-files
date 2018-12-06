import json
import pdb

class KeyObj:
    
    def __init__(self, key, scope, parent=None):
        self.json = scope
        self.key = key
        # pdb.set_trace()
        if parent is not None and key != "root":
            if isinstance(scope, list):
                self.type = "list"
            elif isinstance(scope, dict):
                self.type = "dict"
            else:
                self.type = "basic"
        else:
            self.type = "root"
            self.name = "obj"
        self.children = list()
        self.parent = parent

    def __str__(self):
        tabs = 0
        string = "KeyObj\n"
        string += self.to_string(tabs)
        return string
    
    def to_string(self, tabs):
        string = "\t"*tabs + self.name + "\n"
        if len(self.children) > 0:
            for i in self.children:
                if not isinstance(i, KeyObj):
                    string += "\t"*(tabs+1) + i + "\n"
                else:
                    pdb.set_trace()
                    string += i.to_string(tabs+1)
        return string
    def get_scope(self, path):
        '''
        assumes path is a string seperated by .
        '''
        path_array = path.split(".")
        context = self
        for i in path_array:
            if i in context.children and len(context.children) > 0:
                if context.type == "list":
                    path_array.remove(context.name)
                    context = context[i][0]
                else:
                    path_array.remove(context.name)
                    context = context[i]
            else:
                raise Exception("could not reach scope, incorrect scope: {}".format(path))
        return context
            
def generate_key_objs(scope, name=None, path=None, root=None, parent=None):
    # pdb.set_trace()
    print "name: {}, path: {}, root: {}, parent: {}".format(scope, name, path, root, parent)
    obj = None
    if isinstance(scope, str):
        if parent is None:
            scope = json.loads(string)
        else:
            return scope

    # currently, json is our scope
    path = list() if path is None else path
    if parent == None:
        keys = scope.keys()
        for key in keys:
            obj = KeyObj("root", scope, parent={})
        root = obj
        parent = root
        path.append("root")
        root.children.append(generate_key_objs(scope, path=path, parent=parent))
    elif isinstance(scope, dict):
        for x in scope.keys():
            obj = KeyObj(x, scope[x], parent)
            new_scope = scope[x]
            path.append(x)
            obj.children.append(generate_key_objs(new_scope, str(x), path=path, root, obj))
    elif isinstance(scope, list):
        obj = parent
        for i in range(0, len(scope)):
            # pdb.set_trace()
            # ======================================================
            # ===============         WARNING        ===============
            # ======================================================
            # This is going to go through each entry in a given list
            obj.children.append(generate_key_objs(scope[i], i, path, root, parent))  
    else:
        if name is not None:
            # pdb.set_trace()
           return name

        else:
            return scope
    return obj 

file1 = open("menu.json", "r+")
load = file1.read()
file1.close()

json_for_test = json.loads(load)

root = generate_key_objs(json.loads(load))
print str(root)
