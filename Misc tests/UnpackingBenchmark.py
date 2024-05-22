from timeit import timeit
dict_a = {"a":1,"b":2,"c":3,"d":4,"e":5,"f":6,"g":7}
list_a = [1,2,3,4,5,6,7]
g = globals()
def dict_get(a):
    a,b,c,d,e,f,g = a["a"],a["b"],a["c"],a["d"],a["e"], a["f"], a["g"]
def list_indexing(a):
    a,b,c,d,e,f,g = a[0],a[1],a[2],a[3],a[4],a[5],a[6]
def list_unpacking(a):
    a,b,c,d,e,f,g = a
def dict_key_assignment(a):
    a["a"],a["b"],a["c"],a["d"],a["e"],a["f"],a["g"] = 1,2,3,4,5,6,7
def list_index_assignment(a):
    a[0],a[1],a[2],a[3],a[4],a[5],a[6] = 1,2,3,4,5,6,7
def list_extend_list(a):
    a.extend([1,2,3,4,5,6,7])
def list_extend_tuple(a):
    a.extend((1,2,3,4,5,6,7))

print("dict_get: ", timeit('dict_get(dict_a)', globals = g))
print("list_indexing: ", timeit('list_indexing(list_a)', globals = g))
print("list_unpacking", timeit('list_unpacking(list_a)', globals = g))
print("dict_key_assignment", timeit('dict_key_assignment(dict_a.copy())', globals = g))
print("list_index_assignment", timeit('list_index_assignment(list_a.copy())', globals = g))
print("list_extend_list", timeit('list_extend_list(list_a.copy())', globals = g))
print("list_extend_tuple", timeit('list_extend_tuple(list_a.copy())', globals = g))