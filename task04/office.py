from task04.departament import Departament


class Office(Departament):

    def bring_back(self, category, device, warehouse):
        self.storage[category].remove(device)
        warehouse.append(category, device)

    def add_device(self, device):
        super().add_device(device)
        device.set_in_use_status()
