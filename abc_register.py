import abc
from abc_base import PluginBase


class RegisteredImplementation(PluginBase):
    def load(self, input):
        return input.read()

    def save(self, output, data):
        return output.write(data)


    def show(self, inputString):
        return inputString



