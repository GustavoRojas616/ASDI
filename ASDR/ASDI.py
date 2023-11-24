from collections import deque
class TipoToken:
    IDENTIFIER = 'IDENTIFIER'

    #Palabras reservadas
    SELECT = 'SELECT'
    FROM = 'FROM'
    DISTINCT = 'DISTINCT'

    #Caracteres
    COMA = 'COMA'
    PUNTO = 'PUNTO'
    ASTERISCO = 'ASTERISCO'

    EOF = 'EOF'

class ASDI:

    def __init__(self, tokens):
        self.i = 0
        self.hayErrores = False
        self.tokens = tokens
        print(len(self.tokens))
        self.preanalisis = self.tokens[self.i]

    def parse(self):
        pila = deque()
        pila.append("$")
        pila.append("Q")
        while self.i < len(self.tokens)-1:
            if self.hayErrores:
                print("Se encontraron errores")
                return True
            if self.preanalisis['tipo'] == TipoToken.SELECT:
                if pila[-1] == "Q":
                    pila.pop()
                    pila.append("T")
                    pila.append("from")
                    pila.append("D")
                    pila.append("select")
                else:
                    if pila[-1] == "select":
                        pila.pop()
                        self.siguiente()
                    else:
                        self.hayErrores = True
            if self.preanalisis['tipo'] == TipoToken.DISTINCT:
                if pila[-1] == "D":
                    pila.pop()
                    pila.append("P")
                    pila.append("distinct")
                else:
                    if pila[-1] == "distinct":
                        pila.pop()
                        self.siguiente()
                    else:
                        self.hayErrores = True
            if self.preanalisis['tipo'] == TipoToken.FROM:
                if pila[-1] == "A1":
                    pila.pop()
                else:
                    if pila[-1] == "A3":
                        pila.pop()
                    else:
                        if pila[-1] == "from":
                            pila.pop()
                            self.siguiente()
                        else:
                            self.hayErrores = True
            if self.preanalisis['tipo'] == TipoToken.ASTERISCO:
                if pila[-1] == "D":
                    pila.pop()
                    pila.append("P")
                else:
                    if pila[-1] == "P":
                        pila.pop()
                        pila.append("*")
                    else:
                        if pila[-1] == "*":
                            pila.pop()
                            self.siguiente()
                        else:
                            self.hayErrores = True
            if self.preanalisis['tipo'] == TipoToken.COMA:
                if pila[-1] == "A1":
                    pila.pop()
                    pila.append("A")
                    pila.append(",")
                else:
                    if pila[-1] == "T1":
                        pila.pop()
                        pila.append("T")
                        pila.append(",")
                    else:
                        if pila[-1] == ",":
                            pila.pop()
                            self.siguiente()
                        else:
                            if pila[-1] == "A3":
                                pila.pop()
                            else:
                                if pila[-1] == "T3":
                                    pila.pop()
                                else:
                                    self.hayErrores = True
            if self.preanalisis['tipo'] == TipoToken.PUNTO:
                if pila[-1] == "A3":
                    pila.pop()
                    pila.append("id")
                    pila.append(".")
                else:
                    if pila[-1] == ".":
                        pila.pop()
                        self.siguiente()
                    else:
                        self.hayErrores = True
            if self.preanalisis['tipo'] == TipoToken.IDENTIFIER:
                if pila[-1] == "A":
                    pila.pop()
                    pila.append("A1")
                    pila.append("A2")
                else:
                    if pila[-1] == "A2":
                        pila.pop()
                        pila.append("A3")
                        pila.append("id")
                    else:
                        if pila[-1] == "T":
                            pila.pop()
                            pila.append("T1")
                            pila.append("T2")
                        else:
                            if pila[-1] == "T2":
                                pila.pop()
                                pila.append("T3")
                                pila.append("id")
                            else:
                                if pila[-1] == "D":
                                    pila.pop()
                                    pila.append("P")
                                else:
                                    if pila[-1] == "P":
                                        pila.pop()
                                        pila.append("A")
                                    else:
                                        if pila[-1] == "T3":
                                            pila.pop()
                                            pila.append("id")
                                        else:
                                            if pila[-1] == "id":
                                                pila.pop()
                                                self.siguiente()
                                            else:
                                                self.hayErrores = True
        while len(pila) > 0:
            if self.hayErrores:
                print("Se encontraron errores")
                return True
            if pila[-1] == "T1":
                pila.pop()
            else:
                if pila[-1] == "T3":
                    pila.pop()
                else:
                    if pila[-1] == "$":
                        print("Consulta correcta.")
                        return False
                    else:
                        self.hayErrores = True
        return True
    def siguiente(self):
        self.i = self.i + 1
        self.preanalisis = self.tokens[self.i]