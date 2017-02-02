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
