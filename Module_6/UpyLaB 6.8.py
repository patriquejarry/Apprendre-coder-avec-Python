def store_email(liste_mails):
    """ La fonction qui reçoit en paramètre une liste d’adresses e-mail
    et qui renvoie un dictionnaire avec comme clés les domaines des adresses e-mail
    et comme valeurs les listes d’utilisateurs correspondantes, triées par ordre croissant (UTF-8)."""

    result = {}
    for mail in liste_mails:
        user, domain = mail.split('@')
        if domain not in result:
            result[domain] = [user]
        else:
            result[domain].append(user)
            result[domain] = sorted(result[domain])

    return result


print(store_email(["ludo@prof.ur", "andre.colon@stud.ulb", "thierry@profs.ulb", "sébastien@prof.ur", "eric.ramzi@stud.ur", "bernard@profs.ulb", "jean@profs.ulb" ]))
# { 'prof.ur' : ['ludo', 'sébastien'], 'stud.ulb' : ['andre.colon'], 'profs.ulb' : ['bernard', 'jean', 'thierry'], 'stud.ur' : ['eric.ramzi'] }