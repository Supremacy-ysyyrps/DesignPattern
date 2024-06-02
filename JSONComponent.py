from abc import ABC, abstractmethod


class JSONComponent(ABC):

    def __init__(self, key : str, line : int):
        self.key = key
        self.line = line            # 节点应该显示在第几行
        self.isLast : bool = True   # 是否是父节点的最后一个子节点

    def getKey(self) -> str:
        return self.key

    def getLine(self) -> int:
        return self.line

    def getIsLast(self) -> bool:
        return self.isLast

    def setIsLast(self, isLast : bool) -> None:
        self.isLast = isLast

    @abstractmethod
    def getVal(self):
        pass


class JSONComposite(JSONComponent):

    def __init__(self, key : str, line : int):
        super().__init__(key, line)
        self.val : list[JSONComponent] = []

    def add(self, component : JSONComponent):
        if len(self.val) > 0:
            self.val[-1].setIsLast(False)
        self.val.append(component)

    def getVal(self):
        return self.val


class JSONLeaf(JSONComponent):

    def __init__(self, key : str, line : int, val):
        super().__init__(key, line)
        self.val = val

    def getVal(self):
        return self.val
