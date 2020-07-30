def symetrise_amis(d, englobe):
    result = {}
    for prenom1 in d:
        for prenom2 in d[prenom1]:
            if prenom1 not in result:
                result[prenom1] = set()
            if prenom2 not in result:
                result[prenom2] = set()
            if englobe:
                result[prenom1].add(prenom2)
                result[prenom2].add(prenom1)
            else:
                if prenom1 in d[prenom2]:
                    result[prenom1].add(prenom2)

    #d.clear()
    #for b in result:
    #    d[b] = result[b]
    d.update(result)


d = {'Thierry': {'Michelle', 'Bernadette'}, 'Michelle': {'Thierry'}, 'Bernadette': set()}
print(symetrise_amis(d, True))
print(d)
# {'Thierry': {'Michelle', 'Bernadette'}, 'Michelle' : {'Thierry'}, 'Bernadette' : {'Thierry'}}

d = {'Thierry': {'Michelle', 'Bernadette'}, 'Michelle': {'Thierry'}, 'Bernadette': set()}
print(symetrise_amis(d, False))
print(d)
# {'Thierry': {'Michelle'}, 'Michelle' : {'Thierry'}, 'Bernadette' : set()}

d = {'Bernadette': {'Ariane'}, 'Pierre': {'Pierre'}, 'Michelle': {'Michelle', 'Thierry'}, 'Thierry': set(), 'Ariane': set()}
print(symetrise_amis(d, True))
print(d)
# None et d doit valoir {'Bernadette': {'Ariane'}, 'Pierre': {'Pierre'}, 'Michelle': {'Michelle', 'Thierry'}, 'Thierry': {'Michelle'}, 'Ariane': {'Bernadette'}}
d = {'Bernadette': {'Ariane'}, 'Pierre': {'Pierre'}, 'Michelle': {'Michelle', 'Thierry'}, 'Thierry': set(), 'Ariane': set()}
print(symetrise_amis(d, False))
print(d)
# None et d doit valoir {'Bernadette': set(), 'Pierre': {'Pierre'}, 'Michelle': {'Michelle'}, 'Thierry': set(), 'Ariane': set()}
d = {'Bernadette': {'Ariane'}, 'Pierre': {'Michelle'}, 'Thierry': {'Bernadette', 'Quidam'}, 'Ariane': set(), 'Michelle': {'Quidam'}, 'Quidam': {'Thierry'}}
print(symetrise_amis(d, True))
print(d)
# None et d doit valoir {'Bernadette': {'Ariane', 'Thierry'}, 'Pierre': {'Michelle'}, 'Thierry': {'Bernadette', 'Quidam'}, 'Ariane': {'Bernadette'}, 'Michelle': {'Pierre', 'Quidam'}, 'Quidam': {'Michelle', 'Thierry'}}
d = {'Bernadette': {'Ariane'}, 'Pierre': {'Michelle'}, 'Thierry': {'Bernadette', 'Quidam'}, 'Ariane': set(), 'Michelle': {'Quidam'}, 'Quidam': {'Thierry'}}
print(symetrise_amis(d, False))
print(d)
# None et d doit valoir {'Bernadette': set(), 'Pierre': set(), 'Thierry': {'Quidam'}, 'Ariane': set(), 'Michelle': set(), 'Quidam': {'Thierry'}}
