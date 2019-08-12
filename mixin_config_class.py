class DefaultsMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.memory = 4
        self.threads = 2


class Molecule:
    def __init__(self, name):
        self.name = name


class Ligand(DefaultsMixin, Molecule):
    def __init__(self, name):
        super().__init__(name)
        self.atoms = ['C', 'H']


class Protein(DefaultsMixin, Molecule):
    def __init__(self, name):
        super().__init__(name)
        self.atoms = ['O', 'H']


mol1 = Ligand('methane')
mol2 = Protein('heme')
print(mol1.memory)
print(mol2.atoms)
