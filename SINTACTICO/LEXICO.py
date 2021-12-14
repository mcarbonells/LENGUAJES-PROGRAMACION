import fileinput

keywords = {"proceso", "algoritmo", "finproceso", "finalgoritmo", "leer", "escribir",
"definir", "como", "numerico", "numero", "entero", "caracter", "real", "logico", "texto",
"cadena", "verdadero", "falso", "dimension", "mientras", "finsi", "si", "entonces",
"sino", "dimension", "para", "hasta", "con", "paso", "hacer", "finpara", "borrar", "pantalla",
"esperar", "tecla", "segundos", "milisegundos", "segun", "de", "otro", "modo", "finsegun", "finmientras",
"repetir", "que", "subproceso", "finsubproceso", "finfuncion", "funcion", "limpiar", "otro"}

operators={
    '~': "token_neg",
    'no': "token_neg",
    '=':  "token_igual",
    '<-': "token_asig",
    '<>':  "token_dif",
    '<': "token_menor",
    '>': "token_mayor",
    '<=':  "token_menor_igual",
    '>=':  "token_mayor_igual",
    '+': "token_mas",
    '-': "token_menos",
    '/': "token_div",
    '*': "token_mul",
    '%': "token_mod",
    'mod': "token_mod",
    ';': "token_pyc",
    ':': "token_dosp",
    '(': "token_par_izq",
	')': "token_par_der",
	'[': "token_cor_izq",
	']': "token_cor_der",
    '|':  "token_o",
    'o':  "token_o",
	'&':  "token_y",
    'y':  "token_y",
	',': "token_coma",
    '^': "token_pot"
}

simbolos = {
    '"': "comillas",
    "'": "comita",
    "$": "pesos",
    '¿': 'in_izq',
    '?': 'in_der',
    '¡': 'ex_izq',
    '!': 'ex_der',
    'ñ': 'eñe',
    'á': 'a_tilde', 
    'é': 'e_tilde',
    'í': 'i_tilde',
    'ó': 'o_tilde',
    'ú': 'u_tilde',
    'ü': 'u_dierasis',
}

tokenList = []

def writeW(fila, columna, word):
    flag = True
    word = str(word).lower()
    for reserved in keywords:
        if reserved == word:
            tokenList.append('reserved')
            flag = False
    if flag:
        try: 
            operators[word] 
            answer = True      
        except KeyError:
            answer = False
        if answer:
            tokenList.append(operators[word])
        else: 
            tokenList.append('id')

def case1(linea, fila, columna, word): 
    columna1= columna+1
    while True :
        if len(linea) > columna:
            try: 
                operators[str(linea[columna]).lower()]
                answer = True
                if str(linea[columna]).lower() == 'o' or str(linea[columna]).lower() == 'y':
                    answer = False
                    
            except KeyError:
                answer = False
                    
            if answer:
                if linea[columna] == ';' or linea[columna] == ',':
                    writeW(fila, columna1, word)
                    return [linea, fila, columna, 0]
                elif linea[columna] == '+' or linea[columna] == '-' or linea[columna] == '/' or linea[columna] == '*' or linea[columna] == '^' or linea[columna]== '%':
                    writeW(fila, columna1, word)
                    return [linea, fila, columna, 0]
                elif linea[columna] == '<' or linea[columna] == '>' or linea[columna] == '=' or linea[columna] == '>=' or linea[columna] == '<=' or linea[columna]== '<>':
                    writeW(fila, columna1, word)
                    return [linea, fila, columna, 0]
                elif linea[columna] == '&' or linea[columna] == '|' or linea[columna] == '~':
                    writeW(fila, columna1, word)
                    return [linea, fila, columna, 0]
                elif linea[columna] == '(' or linea[columna] == ')' or linea[columna] == '[' or linea[columna] == ']' or linea[columna] == ':':
                    writeW(fila, columna1, word)
                    return [linea, fila, columna, 0]
                else:
                    tokenList.append('Error')
                    return [linea, fila, columna, -2]
            else:
                try: 
                    simbolos[linea[columna]]
                    answer1 = True 
                except KeyError:
                    answer1 = False
                if answer1:
                    if word == '':
                        tokenList.append('Error') 
                        return [linea, fila, columna, -2] 
                    else:
                        writeW(fila, columna1, word)
                        tokenList.append('Error')
                        return [linea, fila, columna, -2] 
                else:
                    if linea[columna] == ' ':
                        writeW(fila, columna1, word)
                        return [linea, fila, columna, 0]
                    elif linea[columna] == '\n' or linea[columna] == '\r':
                        writeW(fila, columna1, word)
                        return [linea, fila, columna, -1]
                    else: 
                        word = word+linea[columna]
                        columna = columna + 1
        else:
            writeW(fila, columna1, word)
            return [linea, fila, columna, -1]
                    

def case2(linea, fila, columna, word, type):
    columna1= columna+1
    while True :
        if len(linea) > columna:
            try: 
                int(linea[columna])
                answer = False
            except ValueError:
                answer = True
            if answer:
                if  type=='token_entero':
                    if linea[columna] == '.' or linea[columna] == ' ' or  linea[columna] == '\n' or linea[columna] == '\r' or linea[columna] == ';' or linea[columna] == ',':
                        if linea[columna] == '\n' or linea[columna] == '\r':
                            tokenList.append(type)
                            return [linea, fila, columna + 1, -1]
                        elif linea[columna] == ' ':
                            tokenList.append(type)
                            return [linea, fila, columna + 1, 0]
                        elif linea[columna] == ';' or linea[columna] == ',':
                            tokenList.append(type)
                            return [linea, fila, columna, 0]
                        else:
                            try: 
                                int(linea[columna+1])
                                answer = True
                            except ValueError:
                                answer = False
                            if answer:
                                word= word+linea[columna] 
                                type = 'token_real'
                                columna = columna + 1
                            else:
                                tokenList.append(type)
                                tokenList.append('Error')
                                return [linea, fila, columna, -2]   
                    elif linea[columna] == '+' or linea[columna] == '-' or linea[columna] == '/' or linea[columna] == '*' or linea[columna] == '^' or linea[columna]== '%':
                        tokenList.append(type)
                        return [linea, fila, columna, 0]
                    elif linea[columna] == '<' or linea[columna] == '>' or linea[columna] == '=' or linea[columna] == '>=' or linea[columna] == '<=' or linea[columna]== '<>':
                        tokenList.append(type)
                        return [linea, fila, columna, 0]
                    elif linea[columna] == '&' or linea[columna] == '|' or linea[columna] == '~':
                        tokenList.append(type)
                        return [linea, fila, columna, 0]
                    elif linea[columna] == '(' or linea[columna] == ')' or linea[columna] == '[' or linea[columna] == ']'   or linea[columna] == '"' or linea[columna] == "'" or linea[columna] == ':':
                        tokenList.append(type)
                        return [linea, fila, columna, 0]
                    else:
                        
                        tokenList.append('Error')
                        return [linea, fila, columna, -2]
                elif linea[columna] == ';' or linea[columna] == ',':
                    tokenList.append(type)
                    return [linea, fila, columna, 0]  
                elif linea[columna] == ' ':
                    tokenList.append(type)
                    return [linea, fila, columna + 1, 0]
                elif linea[columna] == '\n' or linea[columna] == '\r':
                    tokenList.append(type)
                    return [linea, fila, columna + 1, -1]
                elif linea[columna] == '+' or linea[columna] == '-' or linea[columna] == '/' or linea[columna] == '*' or linea[columna] == '^' or linea[columna]== '%':
                    tokenList.append(type)
                    return [linea, fila, columna, 0]
                elif linea[columna] == '<' or linea[columna] == '>' or linea[columna] == '=' or linea[columna] == '>=' or linea[columna] == '<=' or linea[columna]== '<>':
                    tokenList.append(type)
                    return [linea, fila, columna, 0]
                elif linea[columna] == '&' or linea[columna] == '|' or linea[columna] == '~':
                    tokenList.append(type)
                    return [linea, fila, columna, 0]
                elif linea[columna] == '(' or linea[columna] == ')' or linea[columna] == '[' or linea[columna] == ']'   or linea[columna] == '"' or linea[columna] == "'" or linea[columna] == ':':
                    tokenList.append(type)
                    return [linea, fila, columna, 0]
                else:
                    tokenList.append('Error')
                    return [linea, fila, columna, -2]
                
                if linea[columna] == ' ':
                    tokenList.append(type)
                    return [linea, fila, columna + 1, 0]   
            else:
                word=word+linea[columna] 
                columna = columna + 1 
        else: 
            tokenList.append(type)
            return [linea, fila, columna, -1] 
                  

def case3(linea, fila, columna, word):
    columna1= columna+1
    while True :
        if len(linea) > columna:
            if linea[columna]==' ':
                tokenList.append(operators[str(word).lower()])
                return [linea, fila, columna + 1, 0]
            elif linea[columna] == '\n' or linea[columna] == '\r':
                tokenList.append(operators[str(word).lower()])
                return [linea, fila, columna + 1, -1]
            else: 
                try:
                    operators[str(word+linea[columna]).lower()]
                    answer=True
                except KeyError:
                    answer=  False
                
                if answer:
                    word = word + linea[columna]
                    columna = columna + 1 
                else:
                    try: 
                        simbolos[linea[columna]]
                        answer1 = False 
                    except KeyError:
                        answer1 = True
                    if answer1:
                        tokenList.append(operators[str(word).lower()])
                        return [linea, fila, columna, 0] 
                    else:
                        if linea[columna-1] == ';' or linea[columna-1] == ',':
                            tokenList.append(operators[word])
                            return [linea, fila, columna, 0]
                        else: 
                            tokenList.append('Error')
                            return [linea, fila, columna, -2] 
        else:
            tokenList.append(operators[word])
            return [linea, fila, columna + 1, -1] 
                

def case5(linea, fila, columna, word):
    columna1= columna
    while True :
        if len(linea) > columna:
            if linea[columna] == linea[columna] == '"' or linea[columna] == "'":
                tokenList.append('token_cadena')
                return [linea, fila, columna+1, 0]
            else:
                word = word+linea[columna]
                columna = columna + 1
        else:
            
            tokenList.append('Error')
            return [linea, fila, columna, -2]
       


def solve(linea, fila, columna):
    word = ''
    state = 0
    while True:  
        if state == 0:

            if columna >= len(linea):
                return True
            if linea[columna] == '\n' or linea[columna] == '\r':
                return True
            if linea[columna]=='/' and linea[columna+1] =='/':
                return True

            try: 
                int(linea[columna])
                answer = True 
            except ValueError:
                answer = False

            try: 
                operators[str(linea[columna]).lower()]
                answer1 = True
                if str(linea[columna]).lower() == 'o' or str(linea[columna]).lower() == 'y':
                    answer1 = False
                    
            except KeyError:
                answer1 = False
                    
            if answer:
                state = 2 
            elif linea[columna] == '"' or linea[columna] == "'":
                state = 5
            elif answer1:
                state=3
            elif linea[columna] == ' ':
                state = 4
           
            else:
                state = 1

        if state == 1:
            res = case1(linea, fila, columna, word)
            linea   = res[0]
            fila    = res[1]
            columna = res[2]
            state   = res[3]
            
        if state ==2 : 
            res = case2(linea, fila, columna, word, 'token_entero')
            linea   = res[0]
            fila    = res[1]
            columna = res[2]
            state   = res[3]
        
        if state ==3 : 
            res = case3(linea, fila, columna, word)
            linea   = res[0]
            fila    = res[1]
            columna = res[2]
            state   = res[3]
        
        if state == 4:
            columna= columna+1
            state= 0

        if state == 5:
            res = case5(linea, fila, columna+1, word)
            linea   = res[0]
            fila    = res[1]
            columna = res[2]
            state   = res[3] 

        if state == -1:
            return True

        if state == -2:
            return False
        
def main(): 
    file = open('caso.txt', 'r')
    flag= True
    fila = 1

    while flag:
        linea = list(file.readline())
        if  len(linea)>0:
            flag = solve(linea, fila, 0)
        else:
            flag=False
        fila += 1 

    file.close

    """for linea in fileinput.input():
        linea = list(linea)
        if  len(linea)>0:
            flag = solve(linea, fila, 0)
            if not flag:
                break
        else:
            break
        fila += 1"""

