import yaml


class Personne(object):

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
!!python/object:__main__.Personne
nom: Roberto
age: 26
""", Loader=yaml.FullLoader)
print("p", p)
