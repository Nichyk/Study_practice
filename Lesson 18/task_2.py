# Implement 2 classes, the first one is the Boss and the second one is the Worker.
# Worker has a property 'boss', and its value must be an instance of Boss.
# You can reassign this value, but you should check whether the new value is Boss.
# Each Boss has a list of his own workers. You should implement a method that allows you to add workers to a Boss.
# You're not allowed to add instances of Boss class to workers list directly via access to attribute,
# use getters and setters instead!
# You can refactor the existing code.
# id_ - is just a random unique integer

class Boss:
    def __init__(self, id_: int, name: str, company: str):
        self.id = id_
        self.name = name
        self.company = company
        self.workers = dict()

    def __str__(self):
        return f'{self.id}, {self.name}, {self.company}, {self.workers}'

    def __repr__(self):
        return self.__str__()


class Worker:
    def __init__(self, id_: int, name: str, company: str, boss: Boss):
        self.id = id_
        self.name = name
        self.company = company
        self.boss = boss
        self.boss.workers[self.id] = [self.name, self.company]

    @property
    def get_boss(self):
        return self.boss

    @get_boss.setter
    def get_boss(self, boss):
        if isinstance(boss, Boss):
            self.boss.workers.pop(self.id)
            self.boss = boss
            self.company = self.boss.company
            self.boss.workers[self.id] = [self.name, self.company]
        else:
            raise ValueError('Not a boss')

    def __str__(self):
        return f'Worker {self.id}: {self.name}, {self.company}'

    def __repr__(self):
        return self.__str__()
