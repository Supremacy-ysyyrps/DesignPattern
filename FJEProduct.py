from Builder import *


class FunnyJSONExplorer(ABC):

    def __init__(self, icon : tuple):
        self.icon = icon
        self.toDisplay : list[str] = []

    @abstractmethod
    def displayLine(self, component : JSONComponent, prefix : str = ''):
        pass

    @abstractmethod
    def display(self, jsonProduct : JSONProduct):
        pass


class TreeFJE(FunnyJSONExplorer):

    def __init__(self, icon : tuple):
        super().__init__(icon)

    def displayLine(self, component : JSONComponent, prefix : str = ''):
        isLast = component.getIsLast()
        connector = '└─' if isLast else '├─'
        if isinstance(component, JSONComposite):
            self.toDisplay.append(f'{prefix}{connector}{self.icon[0]}{component.getKey()}')
            prefix = f'{prefix}{'   ' if isLast else '│  '}'
            for child in component.getVal():
                self.displayLine(child, prefix)
        elif isinstance(component, JSONLeaf):
            if component.getVal():
                self.toDisplay.append(f'{prefix}{connector}{self.icon[1]}{component.getKey()} : {component.getVal()}')
            else:
                self.toDisplay.append(f'{prefix}{connector}{self.icon[1]}{component.getKey()}')
        else:
            print('Unexpected node!')

    def display(self, jsonProduct : JSONProduct):
        root = jsonProduct.root
        if isinstance(root, JSONComposite):
            for child in root.getVal():
                self.displayLine(child)
        else:
            print('Unexpected node!')
        for line in self.toDisplay:
            print(line)


class RectFJE(FunnyJSONExplorer):

    def __init__(self, icon : tuple):
        super().__init__(icon)

    def displayLine(self, component : JSONComponent, prefix : str = ''):
        # 第一行和最后一行特殊处理
        connector = '├─'
        last = '│'
        if component.getLine() == 1:
            connector = '┌─'
            last = '┐'
        elif component.getLine() == self.totalnum:
            connector = '┴─'
            last = '┘'
            prefix = '└' + '─' * len(prefix[1:])
        if isinstance(component, JSONComposite):
            before = f'{prefix}{connector}{self.icon[0]}{component.getKey()} '
            after = '─' * (40 - len(before)) + last
            self.toDisplay.append(before + after)
            prefix = f'{prefix}│  '
            for child in component.getVal():
                self.displayLine(child, prefix)
        elif isinstance(component, JSONLeaf):
            if component.getVal():
                before = f'{prefix}{connector}{self.icon[1]}{component.getKey()} : {component.getVal()} '
            else:
                before = f'{prefix}{connector}{self.icon[1]}{component.getKey()} '
            after = '─' * (40 - len(before)) + last
            self.toDisplay.append(before + after)
        else:
            print('Unexpected node!')

    def display(self, jsonProduct : JSONProduct):
        root = jsonProduct.root
        self.totalnum = jsonProduct.totLine
        if isinstance(root, JSONComposite):
            for child in root.getVal():
                self.displayLine(child)
        else:
            print('Unexpected node!')
        for line in self.toDisplay:
            print(line)
