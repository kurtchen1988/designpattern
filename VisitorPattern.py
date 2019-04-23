import abc
'''
访问者模式(Visitor)，表示一个作用于某对象结构中的各元素的操作。它使你可以在不改变各元素的类的前提下定义作用于这些元素的新操作。
访问者模式适用于数据结构相对稳定的系统，它把数据结构和作用于结构上的操作之间的耦合解脱开，使得操作集合可以相对自由地演化。
访问者模式的目的是要把处理从数据结构分离出来。如果系统有比较稳定的数据结构，又有易于变化的算法的话，使用访问者模式就是比较合适的，因为访问者
模式使得算法操作的增加变得容易。
'''

class Visitor(metaclass=abc.ABCMeta):
    '''
    visitor类，为该对象结构中ConcreteElement的每一个类声明一个Visit操作
    '''
    @abc.abstractmethod
    def VisitConcreteElementA(self, concreteElementA):
        self.concreteElementA = concreteElementA

    @abc.abstractmethod
    def VisitConcreteElementB(self, concreteElementB):
        self.concreteElementB = concreteElementB


class ConcreteVisitor1(Visitor):
    def VisitConcreteElementA(self, concreteElementA):
        pass

class Element(metaclass=abc.ABCMeta):
    '''
    Element类，定义一个Accept操作，它以一个访问者为参数
    '''
    @abc.abstractmethod
    def Accept(self, Visitor):
        pass

class ConcreteElementA(Element):
    '''
    ConcreteElementA类，具体元素，实现Accept操作
    '''
    def Accept(self, visitor: Visitor):
        # 充分利用双分派技术，实现处理与数据结构的分离
        visitor.VisitConcreteElementA(self)

    def OperationA(self):
        # 其它的相关方法
        pass

class ConcreteElementB(Element):
    '''
    ConcreteElementB类，具体元素，实现Accept操作
    '''
    def Accept(self):
        pass

    def OperationB(self):
        # 其它的相关方法
        pass

class ConcreteVisitor1(Visitor):
    '''
    ConcreteVisiter1和ConcreteVisitor2类具体访问者，实现每个由Visitor声明的操作。每个操作实现算法的一部分，而该算法片段乃是对应于结构
    中对象的类。
    '''
    def VisitConcreteElementA(concreteElementA:ConcreteElementA):
        print("%s被%s访问"%(concreteElementA.__str__(), ConcreteVisitor1.__str__()))


    def VisitConcreteElementB(concreteElementB:ConcreteElementB):
        print("%s被%s访问"%(concreteElementB.__str__(), ConcreteVisitor1.__str__()))

class ConcreteVisitor2(Visitor):
    '''
    ConcreteVisiter1和ConcreteVisitor2类具体访问者，实现每个由Visitor声明的操作。每个操作实现算法的一部分，而该算法片段乃是对应于结构
    中对象的类。
    '''
    def VisitConcreteElementA(concreteElementA:ConcreteElementA):
        print("%s被%s访问"%(concreteElementA.__str__(), ConcreteVisitor1.__str__()))


    def VisitConcreteElementB(concreteElementB:ConcreteElementB):
        print("%s被%s访问"%(concreteElementB.__str__(), ConcreteVisitor1.__str__()))



class ObjectStructure:
    '''
    ObjectStructure类，能枚举它的元素，可以提供一个高层的接口以允许访问者访问它的元素
    '''

    _elements:Element = []

    def Attach(self, element: Element):
        self._elements.append(element)

    def Detach(self, element: Element):
        self._elements.pop(element)

    def Accept(self, visitor: Visitor):
        for e in self._elements:
            e.Accept(visitor)


if __name__=="__main__":
    o = ObjectStructure()
    o.Attach(ConcreteElementA())
    o.Attach(ConcreteElementB())

    v1 = ConcreteVisitor1()
    v2 = ConcreteVisitor2()

    o.Accept(v1)
    o.Accept(v2)
