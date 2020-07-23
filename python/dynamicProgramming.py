def addto80(n):
    print(addto80.cache)
    if (n in addto80.cache):
        print("with cache")
        return addto80.cache[n]
    else:
        print("without cache")
        addto80.cache[n] = n + 80
        return addto80.cache[n]

addto80.cache = {}

print(addto80(5))
print(addto80(5))
print(addto80(6))
print(addto80(6))
