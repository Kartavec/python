storage = {
            'xerox': [],
            'printer': [],
            'scanner': [],
            'monitor': [],
            'desktop': []
        }


class Departament:
    _instances = []

    def __init__(self, title):
        self.title = title
        self._instances.append(self)
        self.storage = storage

    def __str__(self):
        return self.title

    @classmethod
    def instances(cls):
        return cls._instances

    def gei_device_by_serial(self, serial):
        for category in self.storage:
            for item in self.storage[category]:
                if item.serial_number == serial:
                    return item
        return None

    # @classmethod
    # def _sum_instances(cls, instance):
    #     pass

    def destroy(self):
        self.__class__._instances.remove(self)

    # _instances = []
    #
    # def __init__(self, title):
    #     self.title = title
    #     self._instances.append(self)
    #
    # def __str__(self):
    #     return self.title
    #
    # @classmethod
    # def instances(cls):
    #     return cls._instances
    #
    # @classmethod
    # def _sum_instances(cls, instance):
    #     pass
    #
    # def destroy(self):
    #     self.__class__._instances.remove(self)
