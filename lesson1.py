class Profile:
    def __init__(self, name, family_name, age, weight):
        self.name = name
        self.family_name = family_name
        self.age = age
        self.weight = weight

    @staticmethod
    def enter_data():
        name = input("Введите имя - ")
        family_name = input("Введите фамилию - ")
        age = int(input("Введите возраст - "))
        weight = int(input("Введите вес - "))
        return Profile(name, family_name, age, weight)

    @staticmethod
    def print_result():
        profile = Profile.enter_data()
        result = "{0} {1}, {2} год, вес {3} - ".format(profile.name, profile.family_name, profile.age, profile.weight)
        if profile.age < 30 and 50 < profile.weight < 120:
            print(result + "хорошее состояние")
        elif profile.age > 30 and (profile.weight < 50 or profile.weight > 120):
            print(result + "следует заняться собой")
        elif profile.age > 40 and (profile.weight < 50 or profile.weight > 120):
            print(result + "следует обратится к врачу!")


Profile.print_result()
