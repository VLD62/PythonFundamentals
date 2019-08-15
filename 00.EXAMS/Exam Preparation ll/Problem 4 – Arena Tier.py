class Gladiator:
    def __init__(self, name, technique):
        self.name = name
        self.technique = technique
        self.total_skill = self.get_total_skill()

    def get_total_skill(self):
        return sum(self.technique.values())


if __name__ == "__main__":
    input_data = input()
    gladiators = []

    while not input_data == 'Ave Cesar':

        input_data = input_data.split(' -> ')

        if len(input_data) > 1:
            gladiator_name, technique, skill = input_data[0], input_data[1], int(
                input_data[2])
            skill_dict = {technique: skill}

            if gladiator_name not in [gladiator.name for gladiator in gladiators]:
                new_gladiator = Gladiator(
                    name=gladiator_name, technique=skill_dict)
                gladiators.append(new_gladiator)
            else:
                for gladiator in gladiators:
                    if gladiator.name == gladiator_name:
                        if technique not in gladiator.technique.keys():
                            gladiator.technique[technique] = skill
                            gladiator.total_skill = gladiator.get_total_skill()

                        else:
                            if gladiator.technique[technique] < skill:
                                gladiator.technique[technique] = skill
                                gladiator.total_skill = gladiator.get_total_skill()
        else:
            gladiator11, gladiator21 = input_data[0].split(" vs ")

            if (gladiator11 in [gladiator.name for gladiator in gladiators] and gladiator21 in [gladiator.name for gladiator in gladiators]):

                for gladiator1 in gladiators:
                    for gladiator2 in gladiators:
                        if gladiator1.name == gladiator11 and gladiator2.name == gladiator21:
                            for key, value in gladiator1.technique.items():
                                for key1, value1 in gladiator2.technique.items():
                                    if key == key1:
                                        if gladiator1.total_skill > gladiator2.total_skill:
                                            for gladiator in gladiators:
                                                if gladiator.name == gladiator21:
                                                    gladiators.remove(gladiator)
                                        else:
                                            for gladiator in gladiators:
                                                if gladiator.name == gladiator11:
                                                    gladiators.remove(gladiator)

        input_data = input()

    for gladiator in sorted(gladiators, key=lambda x: (-x.total_skill, x.name)):
        print(f'{gladiator.name}: {gladiator.total_skill} skill')
        for k, v in sorted(gladiator.technique.items(), key=lambda kvp: kvp[1], reverse=True):
            print(f'- {k} <!> {v}')
