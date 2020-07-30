def construction_dict_amis(amis):

    result = {}
    for prenom1, prenom2 in amis:
        if prenom1 not in result:
            result[prenom1] = set()
        if prenom2 not in result:
            result[prenom2] = set()
        result[prenom1].add(prenom2)
    return result


print(construction_dict_amis([('Quidam', 'Pierre'), ('Thierry', 'Michelle'), ('Thierry', 'Pierre')]))
# {'Quidam' : {'Pierre'}, 'Pierre' : set(), 'Thierry' : {'Michelle', 'Pierre'}, 'Michelle' : set()}


print(construction_dict_amis([('Thierry', 'Pierre'), ('Thierry', 'Ariane'), ('Quidam', 'Pierre')]))
# {'Thierry': {'Pierre', 'Ariane'}, 'Ariane': set(), 'Pierre': set(), 'Quidam': {'Pierre'}}
print(construction_dict_amis([('Bernadette', 'Michelle'), ('Pierre', 'Quidam'), ('Bernadette', 'Pierre'), ('Quidam', 'Bernadette'), ('Michelle', 'Bernadette')]))
# {'Michelle': {'Bernadette'}, 'Bernadette': {'Michelle', 'Pierre'}, 'Quidam': {'Bernadette'}, 'Pierre': {'Quidam'}}
print(construction_dict_amis([('Ariane', 'Pierre'), ('Quidam', 'Thierry'), ('Quidam', 'Quidam'), ('Quidam', 'Michelle'), ('Bernadette', 'Thierry'), ('Ariane', 'Thierry'), ('Thierry', 'Michelle'), ('Michelle', 'Ariane')]))
# {'Thierry': {'Michelle'}, 'Bernadette': {'Thierry'}, 'Ariane': {'Thierry', 'Pierre'}, 'Michelle': {'Ariane'}, 'Quidam': {'Michelle', 'Thierry', 'Quidam'}, 'Pierre': set()}
print(construction_dict_amis([('Pierre', 'Michelle'), ('Quidam', 'Quidam'), ('Quidam', 'Pierre'), ('Bernadette', 'Bernadette'), ('Quidam', 'Pierre'), ('Bernadette', 'Pierre'), ('Michelle', 'Ariane'), ('Thierry', 'Michelle'), ('Pierre', 'Bernadette'), ('Bernadette', 'Pierre'), ('Bernadette', 'Thierry'), ('Pierre', 'Michelle'), ('Pierre', 'Thierry')]))
# {'Thierry': {'Michelle'}, 'Bernadette': {'Thierry', 'Bernadette', 'Pierre'}, 'Pierre': {'Thierry', 'Michelle', 'Bernadette'}, 'Michelle': {'Ariane'}, 'Quidam': {'Quidam', 'Pierre'}, 'Ariane': set()}
print(construction_dict_amis([('Quidam', 'Ariane'), ('Michelle', 'Pierre'), ('Pierre', 'Thierry'), ('Ariane', 'Thierry'), ('Ariane', 'Ariane'), ('Quidam', 'Thierry'), ('Thierry', 'Pierre'), ('Pierre', 'Ariane'), ('Thierry', 'Pierre'), ('Thierry', 'Quidam'), ('Thierry', 'Michelle'), ('Quidam', 'Michelle'), ('Quidam', 'Bernadette')]))
# {'Thierry': {'Michelle', 'Quidam', 'Pierre'}, 'Bernadette': set(), 'Ariane': {'Thierry', 'Ariane'}, 'Michelle': {'Pierre'}, 'Quidam': {'Michelle', 'Thierry', 'Bernadette', 'Ariane'}, 'Pierre': {'Thierry', 'Ariane'}}
print(construction_dict_amis([('Bernadette', 'Michelle'), ('Pierre', 'Ariane'), ('Quidam', 'Bernadette'), ('Michelle', 'Ariane'), ('Ariane', 'Michelle'), ('Ariane', 'Pierre'), ('Michelle', 'Thierry'), ('Michelle', 'Thierry'), ('Pierre', 'Bernadette'), ('Quidam', 'Thierry'), ('Pierre', 'Pierre'), ('Pierre', 'Pierre')]))
# {'Thierry': set(), 'Bernadette': {'Michelle'}, 'Pierre': {'Bernadette', 'Pierre', 'Ariane'}, 'Michelle': {'Thierry', 'Ariane'}, 'Quidam': {'Thierry', 'Bernadette'}, 'Ariane': {'Michelle', 'Pierre'}}
print(construction_dict_amis([('Thierry', 'Pierre'), ('Ariane', 'Thierry'), ('Ariane', 'Bernadette'), ('Michelle', 'Michelle'), ('Michelle', 'Bernadette'), ('Quidam', 'Pierre'), ('Pierre', 'Michelle'), ('Bernadette', 'Ariane'), ('Ariane', 'Ariane'), ('Ariane', 'Michelle'), ('Ariane', 'Michelle'), ('Pierre', 'Michelle'), ('Ariane', 'Michelle'), ('Quidam', 'Thierry'), ('Thierry', 'Quidam')]))
# {'Thierry': {'Quidam', 'Pierre'}, 'Bernadette': {'Ariane'}, 'Pierre': {'Michelle'}, 'Michelle': {'Michelle', 'Bernadette'}, 'Quidam': {'Thierry', 'Pierre'}, 'Ariane': {'Michelle', 'Thierry', 'Bernadette', 'Ariane'}}
