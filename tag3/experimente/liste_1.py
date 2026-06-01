l = [ 4711, "a", 12.34, [ 1,2,3] ]

for e in l:
    print(type(e), e)
    if isinstance(e, list):
        for e2 in e:
            print("\t", type(e2), e2)
