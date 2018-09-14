from TelaLogin import *



import hashlib
f = b"asdasasd"
g = hashlib.sha256(f).hexdigest()
print(g)

a = janelaLogin()
b = janelaLogin()