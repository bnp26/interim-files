import os
import sys
import json
import pdb
import jsondiff
import pandas as pd

class Node:
    def __init__(self, key, obj):
        self.key = key
        self.children = list()
        self.required = False
        if isinstance(obj, str):
            return
        else:
            if isinstance(obj, dict):
                for i in obj.keys():
                    self.children.append(Node(i, obj[i]))
            elif isinstance(obj, list):
                for i in obj:
                    self.children.append(Node(self.key, i))
            else:
                self.children.append(Node(self.key, ""))
    
    def to_string(self, level):
        string = "  "*level + self.key
        for i in self.children:
            if isinstance(i, Node) and len(i.children) > 0:
                string = string + "\n" +  i.to_string(level+1)
            elif isinstance(i, Node):
                string = string + "\n" + i.key
        return string


    def __str__(self):
        return self.to_string(0)
        

class PropsObj:

    def __init__(self, string):
        self.json = json.loads(string)
        self.df = pd.read_json(string)
    
    def flattenDict(self, dic=None, result=None):
        d = dic if dic is not None else self.json
        if result is None:
            result = {}
        for key in d:
            value = d[key]
            if isinstance(value, dict):
                value1 = {}
                for keyIn in value:
                    value1[".".join([key,keyIn])]=value[keyIn]
                self.flattenDict(value1, result)
            elif isinstance(value, (list, tuple)):
                for indexB, element in enumerate(value):
                    if isinstance(element, dict):
                        value1 = {}
                        index = 0
                        for keyIn in element:
                            newkey = ".".join([key,keyIn])
                            if ".".join([key, keyIn]) not in value1:
                                value1[".".join([key,keyIn])]=value[indexB][keyIn]
                            index += 1
                        for keyA in value1:
                            self.flattenDict(value1, result)   
            else:
                result[key]=value
        return result	
    
    def to_list(self):
        new_df = pd.io.json.build_table_schema(self.df)
        new_list = list()
        for k, v in new_df['fields'].iteritems():
            new_list.append(k)
        return list(set(new_list))

    def diff(self, new_props):
        list1 = self.flattenDict().keys()
        list2 = new_props.flattenDict().keys()
        changed1 = list1
        changed2 = list2
        for i in list1:
            if i in changed2:
                changed2.remove(i)
                changed1.remove(i)
            
        results = {"removed": changed1, "added": changed2}
        return results
            

def check_payload(old, new):
    oldObj = PropsObj(old)
    newObj = PropsObj(new)
    return oldObj.diff(newObj)
    
str1 = '{ "hello": "Hey!","bye": "Bye Bye"}'
str2 = '{ "hi": "Hey!","bye": "Bye Bye", "hey": "poop"}'

        

def diff(old, new):
    old_props = old
    new_props = new
    N = len(old)
    M = len(new)
    MAX = M + N
    off = MAX + 1
    V = [ 0 for i in range(0, 2 * MAX + 1) ]
    paths = [ [] for i in range(0, 2 * MAX + 1) ]
    no_change = list()
    added = list()
    deleted = list()
    for D in range(0, MAX+1):
        print "Cost: %d" % D
        for k in range(-D, D+1, 2):
            print "Diagonal: %d" % k
            if k == -D or (k != D and V[k-1 + off] < V[k+1 + off]):
                x = V[k + 1 + off]
                path = paths[k + 1 + off][:]
                y = x - k
                if y > len(new_props):
                    pass
                elif y > 0:
                    path.append("+" + new_props[y-1])
                    added.append(new_props[y-1])
            else:
                x = V[k - 1 + off] + 1
                path = paths[k - 1 + off][:]
                if x > len(old_props):
                    pass
                elif x > 0:
                    path.append("-" + old_props[x-1])
                    deleted.append(old_props[x-1])
                print "x: {}".format(x)
            y = x - k

            while x < N and y < M and old_props[x] == new_props[y]:
                path.append(" " + old_props[x])
                no_change.append(old_props[x])
                x += 1
                y += 1
            V[k + off] = x
            paths[k + off] = path
            if x >= N and y >= M:
                print "Solution has cost %d" % D
                return added, deleted, no_change

'''
    diff_list = (0,)*max_len
    diff_list[1] = 0
    for d in range(0, max_len):
        trace = tuple(diff_list)
        for k in range(-d, d, 2):
            x = 0
            if k == -d or (k != d and diff_list[k-1] < diff_list[k+1]
                x = diff_list[k+1]
            else:
                x = diff_list[k-1] + 1
            y = x - k
            while x < n and y < m and a[x] == b[y]:
                x, y = x + 1, y + 1
            diff_list[k] = x
            return trace if x >= n and y >= m

def backtrack(a, b):
    x, y = len(a.iteritems()), len(b.iteritems())
    
    shortest_edit(
'''

def list_diff(list1, list2):
    sorted(list(set(list1)))
    sorted(list(set(list2)))
    merged_set = set(list1)
    added = set()
    removed = set()
    changed1 = set(list1)
    changed2 = set(list2)
    while len(changed1) > 0:
        val = changed1.pop()
        if val in changed2:
            changed2.discard(val)
            merged_set.add(val)
        else:
            removed.add(val)
    while len(changed2) > 0:
        val = changed2.pop()
        added.add(val)
    results = {"removed": list(removed), "added": list(added), "no_change": list(merged_set)}
    return results



file1 = open("menu.json", "r")
file2 = open("edited_menu.json", "r")

str1 = file1.read()
str2 = file2.read()

json1 = json.loads(str1)
json2 = json.loads(str2)

parent = Node("parent", json1)
print parent

props1 = PropsObj(str1)
props2 = PropsObj(str2)

list1 = props1.flattenDict().keys()
list2 = props2.flattenDict().keys()

added, deleted, same = diff(list1, list2)
print set(added)
print set(deleted)
print set(same)

file1.close()
file2.close()
