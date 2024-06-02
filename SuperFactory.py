from FJEFactory import *


class SuperFactory:

    def createFactory(self, factory : str) -> FJEFactory:
        if factory == 'tree':
            return TreeFJEFactory()
        elif factory == 'rect':
            return RectFJEFactory()
        else:
            print('Factory is either "tree" or "rect"!')
            return None
