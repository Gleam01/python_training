from goto import goto, label

# Problème 3: Q.01. Ecriture de la fonction estPremier(n)
def estPremier(n):
    if n < 2: 
        raise Exception((n, "Positive integer greater or equal to 2 required !")).with_traceback()

    for i in range(2, n // 2 + 1):
        if (n % i) == 0:
            return 0
    else:
        return 1

# Problème 3: Q.02. Ecriture de la fonction petitsPremiers(n). Cette fonction utilise la fonction estPremier(n) de Q.01.
def petitsPremiers(n):
    global premier
    premier = []
    try:
        for i in range(2, n + 1):
            if estPremier(i):
                premier.append(i)
        return len(premier)

    except Exception:
        print('Argument should be greather or equal to 2')


# Problème 3: Q.03. Ecriture de la fonction petitsPremiers2(n). Cette fonction utilise la fonction estPremier2(n) qui utilise le test d'un entier impaire m (3<=m)...
def estPremier2(n):
    if n < 2: 
        raise Exception((n, "Positive integer greater or equal to 2 required !")).with_traceback()
    if n == 2 or n == 3: 
        return 1
    if n % 2 == 0: 
        return 0
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return 0

    return 1

def petitPremiers2(n):
    global premier
    premier = []
    try:
        for i in range(2, n + 1):
            if estPremier2(i):
                premier.append(i)
        return len(premier)
    except Exception:
        print('Argument should be greather or equal to 2')

# Problème 3: Q.04. Ecriture de la fonction petitsPremiers3(n) agissant comme petitsPremiers(n) mais qui utilise le crible d'Érathostène.
def petitPremiers3(n):
    if n < 2: 
        raise Exception((n, "Positive integer greater or equal to 2 required !")).with_traceback()
    global premier
    tableau_n_1_cases = [*range(2, n+1)]
    cailloux = 'C'
    raillure = 'R'
    premier_clone = tableau_n_1_cases[:]
    premier = []
    for i in range(len(premier_clone)):
        if premier_clone[i] != raillure:
            premier_clone[i] = cailloux
            premier.append(tableau_n_1_cases[i])
            for j in range(i, len(premier_clone), tableau_n_1_cases[i]):
                if premier_clone[j] != cailloux:
                    premier_clone[j] = raillure

    return len(premier)

# Problème 3: Q.05 Ecriture de la fonction factoriser(n)
def factoriser(n):
    global facteur
    facteur = []
    m = n
    # Ligne 2 de l'algo dans l'énoncé
    label .line2
    if m == 1: return
    print(premier)
    for i in range(1,len(premier)+1):
        # Ligne 3 de l'algo dans l'énoncé
        label .line3
        if premier[i-1] % i == 0:
            facteur.append(premier[i-1])
            m = m / premier[i-1]
            goto .line3
        else:
            i += 1
            goto .line2

    print(facteur)
    return len(facteur)
