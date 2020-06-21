class Departament:
    _instances = []

    def __init__(self, title):
        self.title = title
        self._instances.append(self)
        self.storage = {
            'xerox': [],
            'printer': [],
            'scanner': [],
            'monitor': [],
            'desktop': []
        }

    def __str__(self):
        return self.title

    @classmethod
    def instances(cls):
        return cls._instances

    def add_device(self, device):
        category = device.type
        self.storage[category].append(device)

    def sent_device(self, departament, device):
        category = device.type
        self.storage[category].remove(device)
        departament.add_device(device)

    def get_device_by_serial(self, serial):
        for category in self.storage:
            for item in self.storage[category]:
                if item.serial_number == serial:
                    return item
        return None

    def destroy(self):
        self.__class__._instances.remove(self)

    def get_devices_count(self):
        result = 0
        for category in self.storage:
            result += len(self.storage[category])
        return result

    def get_all_devices(self):
        return self.storage

    def get_devices_by_category(self, category):
        if category in self.storage:
            return {
                category: self.storage[category]
            }
        return f'No category with name "{category}"'

    def get_printers_low_ink(self):
        return [printer for printer in self.storage['printer'] if printer.ink_status == 'LOW']

    def get_printers_empty_ink(self):
        return [printer for printer in self.storage['printer'] if printer.ink_status == 'EMPTY']

    def remove_device(self, category, device):
        self.storage[category].remove(device)

