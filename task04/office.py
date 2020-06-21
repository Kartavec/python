from task04.departament import Departament


class Office(Departament):

    def bring_back(self, office_equipment):
        pass

    def append(self, category, item):
        self.storage[category].append(item)
