
from ASDI import *

lista_tokens = []
def main():
    ejecutar_prompt()

def ejecutar_prompt():
    global lista_tokens
    while True:
        lista_tokens=[]
        entrada = input(">>> ")
        tokens = list(entrada)
        b = tokens
        estado = 0
        caracter = 0
        lexema = ""
        inicioLexema = 0

        while len(b) > 0:
            if str(b[0]) in simbolos_key or str(b[0]).isdigit() == True or str(b[0]).isalpha() == True or str(b[0]) == '\n' or str(b[0]) == ' ':
                aux = 0
                pass
            else:
                print("Error léxico.")
                print("No se realizará el análisis sintáctico.")
                lista_tokens = []
                break
            if str(b[0]).isalpha() == True:
                b = automataRESIDEN(tokens)
            elif str(b[0]).isspace() == True:
                if len(b) == 1:
                    break
                else:
                    b.pop(0)
                    if str(b[0]).isalpha() == True:
                        b = automataRESIDEN(tokens)
            elif str(b[0]).isalpha() == False and str(b[0]).isnumeric() == False:
                b = automata1CARAC(tokens)


        if len(lista_tokens) > 0:
            nid = {'tipo': 'EOF', 'lexema': ''}
            lista_tokens.append(nid)
            print("Tokens registrados:", lista_tokens)
            analizador = ASDI(lista_tokens)
            analizador.parse()

def automataRESIDEN(lista):
    tama=len(lista)
    state=0
    #print(lista)
    for i in range(tama):
        if state==0 and (str(lista[i]).isalpha()==True):
            #print(lista[i])
            id = str(lista[i])
            state = 13

        if i>0 and state==13 and (str(lista[i]).isalpha()==True or str(lista[i]).isdigit()==True) :
            #print(lista[i])
            id = id + str(lista[i])

        if i>0 and state==13 and str(lista[i]).isalpha()==False and str(lista[i]).isdigit()==False:
            state=14
            id = id + str(lista[i])
            id=list(id)
            id.pop(-1)
            id=''.join(id)

            for token in [id]:
                if token in reservadas_key:
                    print("<" + reservadas[token] + " " + str(id) + ">")
                    nid = {'tipo': reservadas[token], 'lexema': str(id)}
                    lista_tokens.append(nid)
                    id = list(id)
                    ite = len(id)
                    for i in range(ite):
                        lista.remove(id[i])
                    return lista
                else:
                    print("<IDENTIFIER " +id + ">")
                    nid = {'tipo': 'IDENTIFIER', 'lexema': id}
                    lista_tokens.append(nid)
                    id = list(id)
                    ite = len(id)
                    for i in range(ite):
                        lista.remove(id[i])
                    return lista

        if i==tama-1:
            for token in [id]:
                if token in reservadas_key:
                    print("<" + reservadas[token] + " " + str(id) + ">")
                    nid = {'tipo': reservadas[token], 'lexema': str(id)}
                    lista_tokens.append(nid)
                    id = list(id)
                    ite = len(id)
                    for i in range(ite):
                        lista.remove(id[i])
                    return lista
                else:
                    print("<IDENTIFIER " + id + ">")
                    nid = {'tipo': 'IDENTIFIER', 'lexema': id}
                    lista_tokens.append(nid)
                    id = list(id)
                    ite = len(id)
                    for i in range(ite):
                        lista.remove(id[i])
                    return lista

        i = i + 1

def automata1CARAC(lista):
    tama=len(lista)
    state=0
    id=''
    aux=0
    cond=1
    c=0
    #print(lista)
    for i in range(tama):
        if state==0 and str(lista[i]).isdigit()==False and str(lista[i]).isalpha()==False:
            state=1
            id=id + str(lista[i])
            #print(id)
        if i>0 and state==1 and (str(lista[i]).isdigit()==False and str(lista[i]).isalpha()==False):
            state=2
            aux=0
            id = id + str(lista[i])
            aux=automataM1CARAC(id, lista)
            #print(aux)
            if aux!=0:
                return aux
            else:
                id=list(id)
                id.pop(-1)
                id=''.join(id)
                #print(id)
                c=1
                cond=0

        if i==tama-1:
            #id = id + str(lista[i])
            #print(id)
            for token in [id]:
                if token in simbolos_key:
                    print("<" + simbolos[token] + " " + str(id) + ">")
                    nid = {'tipo': simbolos[token], 'lexema': str(id)}
                    lista_tokens.append(nid)
                    id = list(id)
                    ite = len(id)
                    for i in range(ite):
                        lista.remove(id[i])
                    #print(lista)
                    return lista
        if str(lista[i]).isalpha()==True:
            for token in [id]:
                if token in simbolos_key:
                    print("<" + simbolos[token] + " " + str(id) + ">")
                    nid = {'tipo': simbolos[token], 'lexema': str(id)}
                    lista_tokens.append(nid)
                    id = list(id)
                    ite = len(id)
                    for i in range(ite):
                        lista.remove(id[i])
                        #print(lista)
                    return lista
        if cond==0 and str(lista[i-c]).isalpha() == False:
            for token in [id]:
                if token in simbolos_key:
                    print("<" + simbolos[token] + " " + str(id) + ">")
                    nid = {'tipo': simbolos[token], 'lexema': str(id)}
                    lista_tokens.append(nid)
                    id = list(id)
                    ite = len(id)
                    for i in range(ite):
                        lista.remove(id[i])
                        #print(lista)
                    return lista

def automataM1CARAC(id, lista):
    tama=len(lista)
    for token in [id]:
        if token in simbolos_key:
            print("<" + simbolos[token] + " " + str(id) + ">")
            nid = {'tipo': simbolos[token], 'lexema': str(id)}
            lista_tokens.append(nid)
            id = list(id)
            ite = len(id)
            for i in range(ite):
                lista.remove(id[i])
            return lista
        else:
            return 0



reservadas = {'select': 'SELECT', 'from': 'FROM', 'distinct': 'DISTINCT'}
reservadas_key = reservadas.keys()

simbolos = {',': 'COMA', '.': 'PUNTO', '*': 'ASTERISCO'}
simbolos_key = simbolos.keys()

main()


