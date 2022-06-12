class State:

    def __init__(self, name: str, target: str):
        self.population = {'F': [0] * (2021 - 1910), 'M': [0] * (2021 - 1910)}
        self.name = name

        lines = open("namesbystate/" + self.name + '.TXT', 'r').read().split('\n')
        for line in lines[:-1]:
            table = line.split(',')

            if table[3] == target:
                self.population[table[1]][int(table[2]) - 1910] += 1

        for i in range(1, len(self.population['F'])):
            self.population['F'][i] += self.population['F'][i - 1]
            self.population['M'][i] += self.population['M'][i - 1]
            
        return