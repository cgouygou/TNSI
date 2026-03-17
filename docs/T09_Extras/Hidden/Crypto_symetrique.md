# Corrections du travail en autonomie sur la cryptographie

{{ initexo(0) }}

Only for you, Cécile :wink:


!!! example "{{ exercice() }}: chiffre de César"
    1. Il existe 26 clés, ou plutôt 25 (si on exclut la clé 0 qui ne crée aucun décalage).
    2. On déchiffre avec la clé $26-10=16$.
    2. On obtient un message lisible avec une clé égale à 13:

        ```python linenums='1'
        def decale(lettre:str, cle:int) -> str:
            '''
            Décale une lettre majuscule de cle rangs dans l'alphabet.
            '''
            rang = ord(lettre) - ord('A')
            rang = (rang + cle) % 26 + ord('A')
            return chr(rang)
        
        assert decale('A', 3) == 'D'
        assert decale('X', 5) == 'C'

        def chiffre_cesar(phrase:str, cle:int) -> str:
            '''
            Chiffre le texte phrase avec la clé cle et renvoie le texte chiffré
            '''
            texte_chiffre = ""
            for lettre in phrase:
                texte_chiffre += decale(lettre, cle)
            return texte_chiffre

        assert chiffre_cesar('NSI', 12) == 'ZEU'

        msg_chiffre = 'PRZRFFNTRARPBAGVRAGEVRAQVAGRERFFNAGZNVFVYRFGFHSSVFNZRAGYBATCBHEDHRPRFBVGCRAVOYRQRYRQRPUVSSERENYNZNVA'

        for cle in range(1, 26):
            print(cle, chiffre_cesar(msg_chiffre, cle))
        ```


!!! example "{{ exercice() }}: analyse de fréquences"
    ```python linenums='1'
    message_chiffre = '''DRZJMFLJJRMVQDFZAVEVTIFZJGRJHLZCPRZKUVSFEEVFLUVDRLMRZJVJZKLRKZFEDFZJZAVUVMRZJIJLDVIDRMZVRLAFLIUYLZRMVTMFLJAVUZIRZJHLVTVJKURSFIUUVJIVETFEKIVJUVJXVEJHLZDFEKKVEULCRDRZEGVLKKIVLEDFDVEKFAVEVGFLMRZJGRJFAKRZJJVLCTYVQDFZVKTVJKRJJVQTLIZVLOUVJVUZIVHLVCVJYRJRIUJCVJIVETFEKIVJWFIXVEKLEVUVJKZEVGRITVHLVHLREUFERCVXFKUVCRTYFJVHLREUFERCVXFKUVCRTYFJVSZVEWRZKVCVSVRLXVJKVGRIWFZJFEEVKIFLMVGRJCZEKVICFTLKVLIVEWRTVAVUZIRZJCVDZIFZIHLZMFLJRZUVRMRETVIRCFIJTVEVJKGRJDFETRJTFDDVAVCVUZJRZJCGLZJHLVDFZRLTFEKIRZIVARZGLVKAVUZJDVITZCRMZVAVCLZUZJDVITZAVTYREKVCRMZVAVUREJVCRMZVAVEVJLZJHLRDFLIVKWZERCVDVEKHLREUSVRLTFLGUVXVEJRLAFLIUYLZDVUZJVEKDRZJTFDDVEKWRZJKLGFLIRMFZITVKKVYLDREZKVYSVEAVCVLIIGFEUJKIJJZDGCVDVEKAVCVLIUZJHLVTVJKTVXFKUVCRDFLITVXFKUFETHLZDRGFLJJRLAFLIUYLZVEKIVGIVEUIVLEVTFEJKILTKZFEDTREZHLVDRZJUVDRZEHLZJRZKGVLKKIVJVLCVDVEKDVDVKKIVRLJVIMZTVUVCRTFDDLERLKWRZIVCVUFECVUFEUVJFZ'''

    dico_occurences = {}
    for caractere in message_chiffre:
        if caractere in dico_occurences:
            dico_occurences[caractere] += 1
        else:
            dico_occurences[caractere] = 1

    occurence_max = 0
    for caractere in dico_occurences:
        if dico_occurences[caractere] > occurence_max:
            occurence_max = dico_occurences[caractere]
            caractere_max = caractere
    
    cle = ord(caractere_max) - ord('E')

    print(chiffre_cesar(message_chiffre, 26-cle))

    ```



!!! example "{{ exercice() }}: masque jetable ou chiffre de Vernam"
    La clé est `#!py 'NSI'` ...

    ```python
    >>> masque_jetable(\"\x0c!(8<en\x12%/=i\x1a&;'=.n ,<2 :s/'6;n7,n%&; h\", \"NSI\")
    'Bravo, Alan Turing serait fier de vous!'
    ```



!!! example "{{ exercice() }}: chiffrement affine"
    ```python linenums='1'
    # 1.
    import math

    def affine(msg:str, a:int, b:int) -> str:
        '''
        Renvoie le texte msg chiffré avec la méthode du chiffrement affine avec a, b comme clé.
        '''
        msg_chiffre = ''
        for caractere in msg:
            rang = ord(caractere) - 65
            rang_chiffre = (a*rang + b) % 26
            caractere_chiffre = chr(rang_chiffre + 65)
            msg_chiffre += caractere_chiffre
        return msg_chiffre

    # 2.
    def trouve_cle(msg:str, mot:str) -> tuple:
        '''
        Renvoie la clé a, b si le mot chiffré est dans le message msg.
        '''
        for a in range(1, 21):
            for b in range(21):
                if math.gcd(a, 26) == 1:
                    mot_chiffre = affine(mot, a, b)
                    if mot_chiffre in msg:
                        return a, b

    def dico_dechiffrement(a:int, b:int):
        '''
        Construit un dictionnaire de déchiffrement dont les clés sont les lettres
        chiffrées et les valeurs les lettres claires.
        '''
        dico = {}
        for k in range(26):
            caractere = chr(65 + k)
            dico[affine(caractere, a, b)] = caractere
        return dico

    def dechiffre_affine(msg:str, mot:str) -> str:
        '''
        Déchiffre un message chiffré msg connaissant un mot du texte clair.
        '''
        a, b = trouve_cle(msg, mot)
        msg_clair = ''
        d = dico_dechiffrement(a, b)
        for caractere in msg:
            msg_clair += d[caractere]
        return msg_clair

    print(dechiffre_affine('UCGXLODCMOXPMFMSRJCFQOGTCRSUSXC', 'TRAVAIL'))
    ```



