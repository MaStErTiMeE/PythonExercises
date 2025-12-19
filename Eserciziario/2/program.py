
def es2(ls,ftesto):

    '''
    Si definisca la  funzione es4(ls,ftesto) che,
    - riceve una lista ls contenente stringhe di caratteri  e l'indirizzo di  un file di 
    testo 'ftesto' contenente almeno due stringhe di caratteri separate da spazi e/o  virgole e/o
    andate a capo.
    -  cancella in modo distruttivo da ls le stringhe che e' possibile ottenere concatenando due
       stringhe consecutive lette dal file
    - restituisce il numero di stringhe cancellate da ls.
    ESEMPIO: 
    se  ls=['b', 'abba', 'babc','ccc', 'bba', 'bb' ] e il  file di testo e' 
    "b, \n\n\n ab  ba, b \nc c cc" 
    la funzione restituisce il numero 2
    e la lista ls risultera' modificata come ['b',  'babc', 'bba', 'bb' ]
    Infatti il file contiene in sequenza le parole 
    'b', 'ab', 'ba', 'b', 'c' 'c' 'cc'
    e le parole di ls che possono ottenersi come concatenazione di due  parole che compaiono 
    una di seguito all'altra  nel file di testo 
    sono:
    'abba' = 'ab' +'ba'
    'ccc'= 'c' + 'cc'
    '''
    testo = pulisciTesto(ftesto)
    for i in range(len(ls)) :
        for j in range(len(testo_pulito)) :
            tempStr = testo_pulito[j] + testo_pulito[j+1]
            if ls[i] == tempStr :
                ls.remove(i)
    return ls


def pulisciTesto(filename) :
    with open(filename=filename,encoding="utf-8") as file :
        testo = file.read()
        for lettera in testo :
            if lettera is notalpha() :
                lettera.replace(',',' ')
        testo_pulito = testo.strip().split()
    return testo_pulito

#print(es2(['b', 'abba', 'babc','ccc', 'bba', 'bb' ],'/Users/lucian/Documents/GitHub/UniExercises/PythonExercises/Eserciziario/2/ft1.txt'))
#print(es2([ 'bab', 'abba','bc', 'cc', 'ccc' ],'/Users/lucian/Documents/GitHub/UniExercises/PythonExercises/Eserciziario/2/ft1.txt'))
