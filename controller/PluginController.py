from services.IPluginBaseService import IPluginBaseService
from implementation.IPluginBaseImplemention import IPluginBaseImplementation


class Controller:
    def __init__(self):
        print 'subclass:', issubclass(IPluginBaseImplementation, IPluginBaseService)
        print 'Instance:', isinstance(IPluginBaseImplementation(), IPluginBaseService)

        for sc in IPluginBaseService.__subclasses__():
            print sc.__name__

        self.interface = IPluginBaseImplementation()

    def check(self):
        print self.interface.show("hallo von Plugin Methode")



if __name__ == '__main__':

    ctl = Controller()
    ctl.check()
