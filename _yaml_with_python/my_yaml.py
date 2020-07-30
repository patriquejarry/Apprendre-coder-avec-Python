import yaml


def read_from_file(filename):
    return yaml.safe_load(open(filename))


def write_to_file(data, filename):
    with open(filename, 'w') as yaml_file:
        yaml.dump(data, yaml_file, default_flow_style=False)


recette = {
    'nom': 'sushi',
    'temps de cuisson': 10,
    'difficulte': 'difficile',
    'ingredients': ['riz', 'vinaigre', 'sucre', 'sel', 'thon', 'saumon']
}

print(write_to_file(recette, "w_to_file.yml"))
print(read_from_file("r_from_file.yml"))
