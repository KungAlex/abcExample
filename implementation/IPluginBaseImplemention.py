import abc
from services.IPluginBaseService import IPluginBaseService


class IPluginBaseImplementation(IPluginBaseService):

    def load(self, input):
        return input.read()

    def save(self, output, data):
        return output.write(data)


if __name__ == '__main__':
    print 'subclass:', issubclass(IPluginBaseImplementation, IPluginBaseService)
    print 'Instance:', isinstance(IPluginBaseImplementation(), IPluginBaseService)

    for sc in IPluginBaseService.__subclasses__():
        print sc.__name__
