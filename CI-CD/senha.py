import re

def verifica_forca_senha(senha):
    rexes = ('[A-Z]', '[a-z]', '[0-9]', '[!@#$%^&*+=:?]')
    #rexes = ('[A-Z]', '[a-z]', '[0-9]')
    if len(senha) >= 8 and all(re.search(r, senha) for r in rexes):
        return True
    else:
        return False
