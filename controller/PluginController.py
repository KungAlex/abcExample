from services.IPluginBaseService import IPluginBaseService
from implementation.IPluginBaseImplemention import IPluginBaseImplementation


if __name__ == '__main__':
    print 'subclass:', issubclass(IPluginBaseImplementation, IPluginBaseService)
    print 'Instance:', isinstance(IPluginBaseImplementation(), IPluginBaseService)

    for sc in IPluginBaseService.__subclasses__():
        print sc.__name__
