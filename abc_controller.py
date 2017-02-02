from abc_base import PluginBase
from abc_register import RegisteredImplementation



if __name__ == '__main__':

    interface = RegisteredImplementation()

    interface2 = RegisteredImplementation()
    PluginBase.register(RegisteredImplementation)

    print 'Subclass:', issubclass(RegisteredImplementation, PluginBase)
    print 'Instance:', isinstance(RegisteredImplementation(), PluginBase)


    for sc in PluginBase.__subclasses__():
        print sc.__name__

    print interface.show("hallo von Plugin Methode")
    print interface2.show("hallo von Plugin2 Methode")