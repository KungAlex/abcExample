import abc


class IPluginBaseService(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def load(self, input):
        """load"""
        return

    @abc.abstractmethod
    def save(self, output, data):
        """save"""
        return

    @abc.abstractmethod
    def show(self, input):
        """Show data from the input source and return an object."""
        return
