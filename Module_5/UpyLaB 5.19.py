def acrostiche(file):
    acro = ''
    for ligne in open(file, encoding="UTF-8"):
        acro += ligne.strip()[0] if len(ligne.strip()) > 0 else ' '
    return acro


print(acrostiche('files/acro1.txt'))  # VIVE PYTHON
print(acrostiche('files/acro2.txt'))  # MARIA
print(acrostiche('files/acro3.txt'))  # ISABELLE SEBASTIEN THIERRY
