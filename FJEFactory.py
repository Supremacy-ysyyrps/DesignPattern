from FJEProduct import *


class FJEFactory(ABC):

    @abstractmethod
    def createFJE(self, icon : tuple = (' ', ' ')) -> FunnyJSONExplorer:
        pass


class TreeFJEFactory(FJEFactory):

    def createFJE(self, icon : tuple = (' ', ' ')) -> FunnyJSONExplorer:
        return TreeFJE(icon)


class RectFJEFactory(FJEFactory):

    def createFJE(self, icon : tuple = (' ', ' ')) -> FunnyJSONExplorer:
        return RectFJE(icon)