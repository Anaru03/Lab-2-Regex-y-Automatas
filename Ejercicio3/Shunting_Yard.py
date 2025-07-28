#Refencia del pseudocódigo de: https://gist.github.com/gbrolo/1a80f67f8d0a20d42828fb3fdb7be4de 
#Se utiliza este pseudocódigo por tema de tiempo

def get_precedence(c):
    if c == '(':
        return 1
    if c == '|':
        return 2
    if c == '.':  # concatenación interna
        return 3
    if c in ['?', '*', '+']:
        return 4
    return 5  # operandos


def format_regex(regex):
    res = ""
    operadores = ['|', '?', '+', '*']
    i = 0
    while i < len(regex) - 1:
        c1 = regex[i]
        c2 = regex[i + 1]
        res += c1

        # Si hay escape, saltar siguiente caracter
        if c1 == '\\':
            res += c2
            i += 1
        else:
            # Agregar punto de concatenación si corresponde
            if (c1 != '(' and c2 != ')' and
                c2 not in operadores and
                c1 not in ['|'] and
                c2 != '|'):
                res += '.'

        i += 1
    res += regex[-1]
    return res
