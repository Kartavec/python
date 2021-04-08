

# builtins_types


d = dict(a=1)
t = tuple((1,2,))
l = list('python')
s = set('python')
fs=frozenset('python')
b = bool(1)
by = bytes('python','utf8')
byarr = bytearray((0xFF, 0x01))
n = None
exc = Exception()

builtins_arr = [d,t,l,s, fs,b,by,byarr,n,exc]
[print(elem, type(elem)) for elem in builtins_arr]