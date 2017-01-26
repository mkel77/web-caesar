def encrypt(letter, rot):
    new_list = list(letter)
    newer_list = []
    for item in new_list:
        new_elem = rotate_character(item, rot)
        newer_list.append(new_elem)

    glue = ';'
    s = glue.join(newer_list)
    return ("".join(newer_list))


def alphabet_position(letter):
    #receives a letter (ex.a,Z) and returns a number (ex.0,25)
    alpha = ['a','b','c','d','e','f','g','h','i','j','k','l',
               'm','n','o','p','q','r','s','t','u','v','w','x','y','z']
    num = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16,
               17, 18, 19, 20, 21, 22, 23, 24, 25]

    for i in range (len(alpha)):
        newletter = letter.lower()
        if alpha[i] == newletter:
            newnum = num[i]
            return newnum

def rotate_character(char, rot):
    #receives a letter (ex.a, Z) and rot (ex. 1, 1) and returns
    #a letter by rot (ex.b, A)
    alpha = ['a','b','c','d','e','f','g','h','i','j','k','l',
               'm','n','o','p','q','r','s','t','u','v','w','x','y','z']
    num = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16,
    17, 18, 19, 20, 21, 22, 23, 24, 25]

    if str.isalpha(char):
        a = alphabet_position(char)
        a = a + rot

        while a > 25:
            a = a - 26

        if char.isupper():
             return alpha[a].upper()

        return alpha[a]

    else:
        return char
    
