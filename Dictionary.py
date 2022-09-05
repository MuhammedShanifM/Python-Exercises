d={"tom":95969484635,"rob":893487874234,"joe":438946467478}
print(d)
d["sam"]=4789656957
print(d)
del d["sam"]
print(d)
for key in d:
    print("key",key,"value",d[key])
for k,v in d.items():
    print("key",k,"value",v)

d.clear()
print(d)