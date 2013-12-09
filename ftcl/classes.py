__author__ = 'razi'


class Node:
    def __init__(self, name):
        self.nin = []
        self.nout = []
        self.back = set()
        self.forward = set()
        self.name = name

    def nexts(self):
        return len(self.nout)

    def hasNext(self):
        return len(self.nout) > 0

    def getNext(self):
        return self.nout[0]

    def conTo(self, node):
        self.nout.append(node)
        node.nin.append(self)

    def fillBack(self, node):
        self.back.add(node)
        for n in node.nin:
            self.fillBack(n)

    def fillForward(self, node):
        self.forward.add(node)
        for n in node.nout:
            self.fillForward(n)

    def prnt(self):
        s = ""
        for n in self.back:
            s += n.name + ":"
        s += self.name
        s += "\t\t\t"
        for n in self.forward:
            s += ":" + n.name
        print(s)

    def explore(self, lvl):
        s = ""
        for i in range(0, lvl):
            s += "  "
        print(s + self.name)
        for n in self.nout:
            n.explore(lvl + 1)


class Block:
    def __init__(self):
        self.blocks = []
        self.name = None

    def add(self, b):
        self.blocks.append(b)

    def isEnding(self):
        return False

    def getName(self):
        return self.getString("")

    def getString(self, p):
        s = ""
        for b in self.blocks:
            s += b.getString(p+" ")
        return s

    def isInstruction(self):
        return False

    def isCondition(self):
        return False

    def equal(self, b):
        return False
    pass


class Instruction(Block):
    def __init__(self, n: Node):
        self.name = n.name
        self.block = n

    def set(self, n: Block):
        self.block = n


    def isInstruction(self):
        return True

    def getString(self, p):
        s = p
        s += self.block.name
        return s+"\n"

    def equal(self, n: Block):
        if not isinstance(n, Instruction):
            return False
        return self.name == n.name and n.name != None
        pass


class Condition(Block):
    def __init__(self, b: Node):
        self.name = b.name
        self.true = Block()
        self.false = Block

    def setTrue(self, b: Block):
        self.true = b
        pass

    def setFalse(self, b: Block):
        self.false = b
        pass

    def opti(self):
        app = []
        #opti(self.true)
        #opti(self.false)
        while self.true != None and self.false != None:
            t = self.true.blocks[-1]
            f = self.false.blocks[-1]
            if t.equal(f):
                app.append(t)
                self.true.blocks.pop()
                if len(self.true.blocks)==0:
                    self.true = None
                self.false.blocks.pop()
                if len(self.false.blocks)==0:
                    self.false = None
                continue
            break
        return app


    def getFor(self, con):
        if con:
            return self.true.blocks
        return self.false.blocks

    def isCondition(self):
        return True

    def isEnding(self):
        return self.true.isEnding() and self.false.isEnding()

    def getString(self, p):
        if self.true != None:
            s = p + "if " + self.name+":\n"
            s += self.true.getString(p+"| ")
            if self.false != None:
                s += p + "else: \n"
                s += self.false.getString(p+"| ")
        else:
            s = p + "if not " + self.name+":\n"
            s += self.false.getString(p+"| ")
        return s

    def compareLast(self):
        pass


class Ending(Block):
    def isEnding(self):
        return True


class Goto(Ending):
    def __init__(self, b):
        self.goto = b

    def getString(self, p):
        return p+"goto "+self.goto.name
    pass


class Return(Ending):
    pass
