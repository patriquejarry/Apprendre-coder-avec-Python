import yaml


class Personne(yaml.YAMLObject):

    yaml_tag = '!personne'

    def __init__(self, nom, age):
        self.nom = nom
        self.age = age

    def __repr__(self):
        return "%s(nom=%r, age=%r)" % \
               (self.__class__.__name__, self.nom, self.age)


# from object to yaml
print(yaml.dump(Personne('Robert', 25), default_flow_style=False))


# from yaml to object
p = yaml.load("""
!personne
nom: Roberto
age: 26
""", Loader=yaml.FullLoader)
print("p", p)
