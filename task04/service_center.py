from task04.departament import Departament


class ServiceCenter(Departament):

    def repair_device(self, device):
        device.set_repaired_status()
