# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def is_palindrome(n):
    '''
    Functie care verifica daca numarul este palindrom
    :param n: int
    :return: bool, true daca numarul este palindrom, false altfel
    '''
    inv = 0
    aux = n
    while aux!=0:
        inv=inv*10+aux%10
        aux=int(aux/10)
    if n==inv:
        return True
    else:
        return False

def test_is_palindrome():
    '''Functie care testeaza functia is_palindrome '''
    nr=121
    assert (is_palindrome(nr)==True)
    nr=35
    assert (is_palindrome(nr) == False)
    assert (is_palindrome(100)==False)

def prim(nr):
    '''Functie care verifica daca un numar este prim
    :param nr: int
    :return: bool, true daca numarul este prim, false altfel
    '''
    if nr<2:
        return False
    if (nr%2==0) & (nr!=2):
        return False
    i=3
    while i*i<=nr:
        if nr%i==0:
            return False
        i+=2
    return True

def test_prim():
    '''Functie care verifica functia prim'''
    assert (prim(1)==False)
    assert (prim(2)==True)
    assert (prim(666013)==True)

def is_superprime(n):
    '''
    Functie care verifica daca un numar este superprim
    :param n: int
    :return: bool, true daca numarul este superprim, false altfel
    '''
    while n!=0:
        if prim(n)==False:
            return False
        n= int(n/10)
    return True

def test_is_superprime():
    '''
    Functie care verifica functia is_superprim
    '''
    assert(is_superprime(233)==True)
    assert (is_superprime(521)==False)
    assert (is_superprime(101)==False)

def is_antipalindrome(n):
    '''
    Functie care determina daca un numar este antipalindrom
    :param n: int
    :return: bool, true daca numarul este antipalindrom, false altfel
    '''
    clona_n = n
    invers_n = 0
    nr_cifre = 0
    while clona_n:
        invers_n = invers_n*10+clona_n % 10
        clona_n = int(clona_n/10)
        nr_cifre += 1
        if nr_cifre % 2 == 1:
            ok = 0
        else:
            ok = 1

    while invers_n:
        if invers_n % 10 == n % 10:
            ok = ok+1
        if ok == 2:
            return False
        invers_n = int(invers_n/10)
        n /= 10
    return True

def test_is_antipalindrome():
    '''Functie care testeaza functia antipalindrom'''
    assert (is_antipalindrome(1234) == True)
    assert (is_antipalindrome(2783) == True)
    assert (is_antipalindrome(2772) == False)


def main():
    test_is_palindrome()
    test_prim()
    test_is_superprime()
    test_is_antipalindrome()
    print("Meniu\n 1.Palindrom \n 2. Superprim \n 3.Antipalindrom \n 4.Exit \n")
    optiune=0
    while optiune!=4:
        optiune=int(input("alegeti o optiune din meniu: "))
        if optiune==1:
            nr1=int(input("Introdu numarul: "))
            if is_palindrome(nr1)==True:
                print("Numarul este palindrom.\n")
            else:
                print("Numarul nu este palindrom.\n")
        elif optiune==2:
            nr2=int(input("Introdu numarul: "))
            if is_superprime(nr2)==True:
                print("Numarul este superprim. \n")
            else:
                print("Numarul nu este superprim. \n")
        elif optiune==3:
            nr3=int(input("Introdu numarul: "))
            if is_antipalindrome(nr3)==True:
                print("Numarul este antipalindrom. \n")
            else:
                print("Numarul nu este antipalindrom. \n")
        elif optiune==4:
            print("aplicatia s-a inchis")
            break
main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
