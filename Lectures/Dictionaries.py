# dictionaries are unordered mappings for storing objects, in contrast 
# with lists, which are ordered. Dicts use a key-value pairing instead.
# this key-value pair allows users to quickly grab objects without 
# needing to know an index location

# dictionaries use curly braces and colons to signify the keys and their
# associated values
# {"key1":"value1","key2":"value2"}
# dicts are unordered and cannot be sorted

mydict = {"key1":"value1","key2":"value2"}
print(mydict["key1"])

pricesLookup = {"apple":2.99,"oranges":1.99,"milk":5.80}
print(pricesLookup["apple"])
# nested values
d = {"k1":123,"k2":[0,1,2],"k3":{"insideKey":100}}
print(d["k2"])
print(d["k3"]["insideKey"])
print(d["k2"][2])
# uppercase method on dictionary value
d = {"key1":["a", "b", "c"]}
print(d["key1"][2].upper())
# adding/changing values
d = {"k1":100, "k2": 200}
d["k3"] = 300
d["k1"] = "NEW VALUE"

#list keys
d.keys()
#list values
d.values()
# tuple
d.items()


