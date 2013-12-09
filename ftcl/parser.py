__author__ = 'razi'
from ftcl.classes import *

n0 = Node("0")


def nestn(n, st, pr):
    bl = Block()
    while True:
        if n.nexts() == 0:
            prn = pr + n.name
            print(prn)
            bl.add(Instruction(n))
            break
        if n.nexts() == 1:
            prn = pr + n.name
            print(prn)
            bl.add(Instruction(n))
            n = n.getNext()
            continue
        if n.nexts() == 2:
            if n in st:
                #TODO: pętla
                bl.add(Goto(n))
                break
            st.append(n)
            prn = pr + n.name + ":"
            print(prn)
            con = Condition(n)
            con.setTrue(nestn(n.nout[0], st, pr + " +"))
            prn = pr + n.name + "!:"
            print(prn)
            con.setFalse(nestn(n.nout[1], st, pr + " -"))
            bl.add(con)
            st.pop()
        break
    return bl


def nest(n):
    pr = " "
    b = nestn(n, [], pr)
    return opti(b)


def opti(b: Block):
    t = b
    while True:
        for i in range(0, len(b.blocks)):
            block = b.blocks[i]
            if block.isInstruction():
                continue
            if block.isCondition():
                aft = block.opti()
                j = i
                while len(aft) > 0:
                    b.blocks.insert(j+1, aft.pop())
                    j += 1
                continue
        break
    return t










