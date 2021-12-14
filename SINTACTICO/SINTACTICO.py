import fileinput
from LEXICO import main

tokenList = main()

print(tokenList)

keywords = {"algoritmo", "borrar", "cadena", "caracter", "como", "con", "de", "definir",
            "dimension", "entero", "entonces", "escribir", "esperar", "falso", "finalgoritmo", "finfuncion",
            "finmientras", "finpara", "finproceso", "finsegun", "finsi", "finsubproceso", "funcion",
            "hacer", "hasta", "identificador", "leer", "limpiar", "logico", "mientras","milisegundos", 
            "modo", "numerico", "numero", "otro", "pantalla", "para", "paso", "proceso", "que",
            "real",  "repetir", "segun", "segundos", "si", "sino", "subproceso", "tecla", "texto", 
            "verdadero"}

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
    '^': "token_pot",
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

def  verifyWord(linea, columna):
    word = ''
    flag = True
    while flag:
        if len(linea) > columna:   
            try: 
                operators[str(linea[columna]).lower()]
                if str(linea[columna]).lower() == 'o' or str(linea[columna]).lower() == 'y':
                    answer = False
                answer = True
            except KeyError:
                answer = False

            if answer:
               flag = False
            else:
                if linea[columna] == ' ' or linea[columna+1] == '\n' or linea[columna+1] == '\r':
                    flag = False
                else: 
                    word= word + linea[columna]
    
    word = str(word).lower()
    for reserved in keywords:
        if reserved == word:
            return ['reservada', word, columna]
    
    if not word == '':
        return ['identificador', word, columna]
    else: 
        return ['noWord',  word, columna]
        

def writeW(linea, fila, columna, word):
    flag = True
    word = str(word).lower()
    for reserved in keywords:
        if reserved == word:
            return nextReserved(linea, fila, columna, word)
    
    return nextId(linea, fila, columna, word, 1)

def case1(linea, fila, columna, word):
    while True :
        if len(linea) > columna:   
            try: 
                operators[str(linea[columna]).lower()]
                if str(linea[columna]).lower() == 'o' or str(linea[columna]).lower() == 'y':
                    answer = False
                answer = True
            except KeyError:
                answer = False

            if answer:
               return writeW(linea, fila, columna, word)
            else:
                if linea[columna] == ' 'or linea[columna+1] == '\n' or linea[columna+1] == '\r':
                    return writeW(linea, fila, columna-1, word)
                else: 
                    word= word + linea[columna]
                    columna = columna + 1
                    
def nextReserved(linea, fila, columna, word):
    if word == 'proceso' or word == 'algoritmo':
        hayProceso = True
        if linea[columna] == ' ':
            return nextId(linea, fila, columna+1, '', 2) 
        elif linea[columna]== '\n':
            print('<'+fila+':'+columna+'> Error sintactico: se encontro: "\n"; se esperaba: "identificador", " ".')
            exit()
        elif linea[columna]== '\r':            
            print('<'+fila+':'+columna+'> Error sintactico: se encontro: "\r"; se esperaba: "identificador", " ".')
            exit()
def nextId(linea, fila, columna, word, case):
    while True: 
        if case == 1:
            if linea[columna+1] == '<' and linea[columna]=='-':
                return nextAsignation(linea, fila, columna)
        
        if case == 2:
            res = verifyWord(linea, fila, columna)
            if res[0] == 'reservada':
                print('<'+fila+':'+columna+'> Error sintactico: se encontro: "'+res[1]+'"; se esperaba: "identificador".')
                exit()
            else:
               if linea[res[2]]== '\n' or linea[res[2]]== '\r':
                  return [linea, fila, res[2]] 
               else:
                    print('<'+fila+':'+res[2]+'> Error sintactico: se encontro: " "; se esperaba: "\r","\n".')
                    exit()
                    
        columna = columna +1
        
    

def nextAsignation (linea, fila, columna):
    return 1

def last(linea, fila, columna, type):
    return 1

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
            elif answer1:
                state = 3
            else: 
                state = 1
        
        if state == 1:
            res = case1(linea, fila, columna, word)
            




"""file = open('caso.txt', 'r')
flag= True
fila = 1
hayProceso = False 

while flag:
    linea = list(file.readline())
    if  len(linea)>0:
        flag = solve(linea, fila, 0)
    else:
        flag=False
    fila += 1 

file.close

for linea in fileinput.input():
    linea = list(linea)
    if  len(linea)>0:
        flag = solve(linea, fila, 0)
        if not flag:
            break
    else:
        break
    fila += 1"""

