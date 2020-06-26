cache = {}

def addto80(n):
    if (n in cache):
        print("with cache")
        return cache[n]
    else:
        print("without cache")
        cache[n] = n + 80
        return cache[n]

print(addto80(5))
print(addto80(5))
print(addto80(6))
print(addto80(6))
print(cache)
