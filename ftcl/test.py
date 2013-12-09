__author__ = 'razi'
from ftcl.parser import *


a = Node("A")
b = Node("B")
c = Node("C")
d = Node("D")
e = Node("E")
f = Node("F")
g = Node("G")

a.conTo(b)
b.conTo(c)
b.conTo(d)
c.conTo(d)
d.conTo(e)

a.fillBack(a)
b.fillBack(b)
c.fillBack(c)
d.fillBack(d)
e.fillBack(e)

a.fillForward(a)
b.fillForward(b)
c.fillForward(c)
d.fillForward(d)
e.fillForward(e)

a.explore(0)

if False:
    a.prnt()
    b.prnt()
    c.prnt()
    d.prnt()
    e.prnt()

n = nest(a)
print("\n\n")
print(n.getString(""))

#o = opti(n)
#print("\n\n")
#print(o.getString(""))