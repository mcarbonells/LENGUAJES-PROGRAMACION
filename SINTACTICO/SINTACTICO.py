import fileinput
from LEXICO import main

tokenList = main()

print('Tokens: ')
print (tokenList)

keywords = {"algoritmo", "borrar", "cadena", "caracter", "como", "con", "de", "definir",
            "dimension", "entero", "entonces", "escribir", "esperar", "falso", "finalgoritmo", "finfuncion",
            "finmientras", "finpara", "finproceso", "finsegun", "finsi", "finsubproceso", "funcion",
            "hacer", "hasta", "identificador", "leer", "limpiar", "logico", "mientras","milisegundos", 
            "modo", "numerico", "numero", "otro", "pantalla", "para", "paso", "proceso", "que",
            "real",  "repetir", "segun", "segundos", "si", "sino", "subproceso", "tecla", "texto", 
            "verdadero"}
exepciones = {
    "algoritmo", "como", "con", "entero", "entonces",  "falso", "funcion", "hacer", "hasta",
    "logico", "milisegundos", "modo", "numerico", "numero", "otro", "paso", "proceso", "que",
    "real", "segundos", "texto", "verdadero"
}

exepciones1 = {"algoritmo", "borrar", "definir",
            "dimension", "escribir", "esperar", "finalgoritmo", "finfuncion",
            "finmientras", "finpara", "finproceso", "finsegun", "finsi", "finsubproceso", "funcion",
            "identificador", "leer", "limpiar", "mientras", 
            "pantalla", "para", "proceso", "repetir", "segun", "si", "sino", "subproceso", "tecla", "caso", "de"
}

tokens={
    "token_asig":        '<-',
    "token_cadena":      'valor_cadena',
    "token_coma":        ',' ,
    "token_cor_der":     ']' ,
    "token_cor_izq":     '[' ,
	"token_dif":          '<>',
    "token_div":         '/' ,
    "token_dosp":        ':' ,
    "token_entero":      'valor_entero',
    "token_igual":       '=',
    "token_mas":         '+',
    "token_mayor":       '>',
    "token_mayor_igual": '>=',
    "token_menor":       '<',
    "token_menor_igual": '<=',
    "token_menos":       '-' ,
    "token_mod":         '%',
    "token_mul":         '*' ,
    "token_neg":         '~',
    "token_o":           '|',
    "token_par_der":     ')',
    "token_par_izq":     '(',
    "token_pot":         '^', 
    "token_pyc":         ';',
    "token_real":        'valor_real',
	"token_y":           '&',
}

comparacion={
    "token_mayor", "token_mayor_igual", "token_menor", "token_menor_igual", "token_dif"
} 

def verify(prioridad, token):
    cadena = ''
    flag = True
    entre = False
    entre2 = False
    c = 0
    
    f=True
    
    if len(prioridad) == 0:
        c = 2
    
    if tokenList[token][0] == 'finsi':
        entre2 = True
        for p in prioridad:
            if p == 'si':
               entre = True 
        if len(prioridad)>0:
            if prioridad[len(prioridad)-1] == 'si':
                cadena = 'si'
            elif prioridad[len(prioridad)-2] == 'si':
                cadena = 'si'
                if 'fin'+prioridad[len(prioridad)-2]=='repetir':
                    b = 'hasta'
                    try: 
                        a = tokens[tokenList[token][0]]
                        answer = True

                    except KeyError:
                        answer = False
                    if answer: 
                        print('<'+str(tokenList[token][1])+','+str(tokenList[token][2])+'> Error sintactico: se encontro: "'+a+'"; se esperaba: "borrar", "definir", "dimension", "escribir", "esperar", "identificador", "'+b+'", "leer", "limpiar", "mientras", "para", "repetir", "segun", "si".')
                        flag = False
                    else:
                        print('<'+str(tokenList[token][1])+','+str(tokenList[token][2])+'> Error sintactico: se encontro: "'+tokenList[token][0]+'"; se esperaba: "borrar", "definir", "dimension", "escribir", "esperar", "identificador", "'+b+'", "leer", "limpiar", "mientras", "para", "repetir", "segun", "si".')
                        flag = False
                else:
                    b = 'fin'+prioridad[len(prioridad)-2]
                    try: 
                        a = tokens[tokenList[token][0]]
                        answer = True

                    except KeyError:
                        answer = False
                    if answer: 
                        print('<'+str(tokenList[token][1])+','+str(tokenList[token][2])+'> Error sintactico: se encontro: "'+a+'"; se esperaba: "borrar", "definir", "dimension", "escribir", "esperar", "'+b+'", "identificador", "leer", "limpiar", "mientras", "para", "repetir", "segun", "si".')
                        flag = False
                    else:
                        print('<'+str(tokenList[token][1])+','+str(tokenList[token][2])+'> Error sintactico: se encontro: "'+tokenList[token][0]+'"; se esperaba: "borrar", "definir", "dimension", "escribir", "esperar", "'+b+'", "identificador", "leer", "limpiar", "mientras", "para", "repetir", "segun", "si".')
                        flag = False           
    elif tokenList[token][0] == 'finpara':
        entre2 = True
        for p in prioridad:
            if p == 'para':
               entre = True 
        if len(prioridad)>0:
            if prioridad[len(prioridad)-1] == 'para':
                cadena = 'para'
            elif prioridad[len(prioridad)-2] == 'para':
                cadena = 'para'
                if 'fin'+prioridad[len(prioridad)-2]=='repetir':
                    b = 'hasta'
                    try: 
                        a = tokens[tokenList[token][0]]
                        answer = True

                    except KeyError:
                        answer = False
                    if answer: 
                        print('<'+str(tokenList[token][1])+','+str(tokenList[token][2])+'> Error sintactico: se encontro: "'+a+'"; se esperaba: "borrar", "definir", "dimension", "escribir", "esperar", "identificador", "'+b+'", "leer", "limpiar", "mientras", "para", "repetir", "segun", "si".')
                        flag = False
                    else:
                        print('<'+str(tokenList[token][1])+','+str(tokenList[token][2])+'> Error sintactico: se encontro: "'+tokenList[token][0]+'"; se esperaba: "borrar", "definir", "dimension", "escribir", "esperar", "identificador", "'+b+'", "leer", "limpiar", "mientras", "para", "repetir", "segun", "si".')
                        flag = False
                else:
                    b = 'fin'+prioridad[len(prioridad)-2]
                    try: 
                        a = tokens[tokenList[token][0]]
                        answer = True

                    except KeyError:
                        answer = False
                    if answer: 
                        print('<'+str(tokenList[token][1])+','+str(tokenList[token][2])+'> Error sintactico: se encontro: "'+a+'"; se esperaba: "borrar", "definir", "dimension", "escribir", "esperar", "'+b+'", "identificador", "leer", "limpiar", "mientras", "para", "repetir", "segun", "si".')
                        flag = False
                    else:
                        print('<'+str(tokenList[token][1])+','+str(tokenList[token][2])+'> Error sintactico: se encontro: "'+tokenList[token][0]+'"; se esperaba: "borrar", "definir", "dimension", "escribir", "esperar", "'+b+'", "identificador", "leer", "limpiar", "mientras", "para", "repetir", "segun", "si".')
                        flag = False
    elif tokenList[token][0] == 'finmientras':
        entre2 = True
        for p in prioridad:
            if p == 'mientras':
               entre = True 
        if len(prioridad)>0:
            if prioridad[len(prioridad)-1] == 'mientras':
                cadena = 'mientras'
            elif prioridad[len(prioridad)-2] == 'mientras':
                cadena = 'mientras'
                if 'fin'+prioridad[len(prioridad)-2]=='repetir':
                    b = 'hasta'
                    try: 
                        a = tokens[tokenList[token][0]]
                        answer = True

                    except KeyError:
                        answer = False
                    if answer: 
                        print('<'+str(tokenList[token][1])+','+str(tokenList[token][2])+'> Error sintactico: se encontro: "'+a+'"; se esperaba: "borrar", "definir", "dimension", "escribir", "esperar", "identificador", "'+b+'", "leer", "limpiar", "mientras", "para", "repetir", "segun", "si".')
                        flag = False
                    else:
                        print('<'+str(tokenList[token][1])+','+str(tokenList[token][2])+'> Error sintactico: se encontro: "'+tokenList[token][0]+'"; se esperaba: "borrar", "definir", "dimension", "escribir", "esperar", "identificador", "'+b+'", "leer", "limpiar", "mientras", "para", "repetir", "segun", "si".')
                        flag = False
                else:
                    b = 'fin'+prioridad[len(prioridad)-2]
                    try: 
                        a = tokens[tokenList[token][0]]
                        answer = True

                    except KeyError:
                        answer = False
                    if answer: 
                        print('<'+str(tokenList[token][1])+','+str(tokenList[token][2])+'> Error sintactico: se encontro: "'+a+'"; se esperaba: "borrar", "definir", "dimension", "escribir", "esperar", "'+b+'", "identificador", "leer", "limpiar", "mientras", "para", "repetir", "segun", "si".')
                        flag = False
                    else:
                        print('<'+str(tokenList[token][1])+','+str(tokenList[token][2])+'> Error sintactico: se encontro: "'+tokenList[token][0]+'"; se esperaba: "borrar", "definir", "dimension", "escribir", "esperar", "'+b+'", "identificador", "leer", "limpiar", "mientras", "para", "repetir", "segun", "si".')
                        flag = False
    elif tokenList[token][0] == 'hasta':
        if tokenList[token+1][0] == 'que':
            res = verifyI(token)
            token2 = res[0]
            flag = res[1]
            if flag:
                entre2 = True
                for p in prioridad:
                    if p == 'hasta':
                        entre = True 
                if len(prioridad)>0:
                    if prioridad[len(prioridad)-1] == 'hasta':
                        cadena = 'hasta'
                    elif prioridad[len(prioridad)-2] == 'hasta':
                        cadena = 'hasta'
                        if 'fin'+prioridad[len(prioridad)-2]=='repetir':
                            b = 'hasta'
                            try: 
                                a = tokens[tokenList[token][0]]
                                answer = True

                            except KeyError:
                                answer = False
                            if answer: 
                                print('<'+str(tokenList[token][1])+','+str(tokenList[token][2])+'> Error sintactico: se encontro: "'+a+'"; se esperaba: "borrar", "definir", "dimension", "escribir", "esperar", "identificador", "'+b+'", "leer", "limpiar", "mientras", "para", "repetir", "segun", "si".')
                                flag = False
                            else:
                                print('<'+str(tokenList[token][1])+','+str(tokenList[token][2])+'> Error sintactico: se encontro: "'+tokenList[token][0]+'"; se esperaba: "borrar", "definir", "dimension", "escribir", "esperar", "identificador", "'+b+'", "leer", "limpiar", "mientras", "para", "repetir", "segun", "si".')
                                flag = False
                        else:
                            b = 'fin'+prioridad[len(prioridad)-2]
                            try: 
                                a = tokens[tokenList[token][0]]
                                answer = True

                            except KeyError:
                                answer = False
                            if answer: 
                                print('<'+str(tokenList[token][1])+','+str(tokenList[token][2])+'> Error sintactico: se encontro: "'+a+'"; se esperaba: "borrar", "definir", "dimension", "escribir", "esperar", "'+b+'", "identificador", "leer", "limpiar", "mientras", "para", "repetir", "segun", "si".')
                                flag = False
                            else:
                                print('<'+str(tokenList[token][1])+','+str(tokenList[token][2])+'> Error sintactico: se encontro: "'+tokenList[token][0]+'"; se esperaba: "borrar", "definir", "dimension", "escribir", "esperar", "'+b+'", "identificador", "leer", "limpiar", "mientras", "para", "repetir", "segun", "si".')
                                flag = False 
    elif tokenList[token][0] == 'finsegun':
        entre2 = True
        for p in prioridad:
            if p == 'segun':
               entre = True 
        if len(prioridad)>0:
            if prioridad[len(prioridad)-1] == 'segun':
                cadena = 'segun'
            elif prioridad[len(prioridad)-2] == 'segun':
                cadena = 'segun'
                if 'fin'+prioridad[len(prioridad)-2]=='repetir':
                    b = 'hasta'
                    try: 
                        a = tokens[tokenList[token][0]]
                        answer = True

                    except KeyError:
                        answer = False
                    if answer: 
                        print('<'+str(tokenList[token][1])+','+str(tokenList[token][2])+'> Error sintactico: se encontro: "'+a+'"; se esperaba: "borrar", "definir", "dimension", "escribir", "esperar", "identificador", "'+b+'", "leer", "limpiar", "mientras", "para", "repetir", "segun", "si".')
                        flag = False
                    else:
                        print('<'+str(tokenList[token][1])+','+str(tokenList[token][2])+'> Error sintactico: se encontro: "'+tokenList[token][0]+'"; se esperaba: "borrar", "definir", "dimension", "escribir", "esperar", "identificador", "'+b+'", "leer", "limpiar", "mientras", "para", "repetir", "segun", "si".')
                        flag = False
                else:
                    b = 'fin'+prioridad[len(prioridad)-2]
                    try: 
                        a = tokens[tokenList[token][0]]
                        answer = True

                    except KeyError:
                        answer = False
                    if answer: 
                        print('<'+str(tokenList[token][1])+','+str(tokenList[token][2])+'> Error sintactico: se encontro: "'+a+'"; se esperaba: "borrar", "definir", "dimension", "escribir", "esperar", "'+b+'", "identificador", "leer", "limpiar", "mientras", "para", "repetir", "segun", "si".')
                        flag = False
                    else:
                        print('<'+str(tokenList[token][1])+','+str(tokenList[token][2])+'> Error sintactico: se encontro: "'+tokenList[token][0]+'"; se esperaba: "borrar", "definir", "dimension", "escribir", "esperar", "'+b+'", "identificador", "leer", "limpiar", "mientras", "para", "repetir", "segun", "si".')
                        flag = False
    else:
        f=False
    
               
    if c == 2 or not entre:
        if tokenList[token][0]=='finsi':
            print('<'+str(tokenList[token][1])+','+str(tokenList[token][2])+'> Error sintactico: se encontro: "'+tokenList[token][0]+'"; se esperaba: "borrar", "definir", "dimension", "escribir", "esperar", "identificador", "leer", "limpiar", "mientras", "para", "repetir", "segun", "si".')
            flag = False
        if tokenList[token][0]=='finpara':
            print('<'+str(tokenList[token][1])+','+str(tokenList[token][2])+'> Error sintactico: se encontro: "'+tokenList[token][0]+'"; se esperaba: "borrar", "definir", "dimension", "escribir", "esperar", "identificador", "leer", "limpiar", "mientras", "para", "repetir", "segun", "si".')
            flag = False
        if tokenList[token][0]=='finmientras':
            print('<'+str(tokenList[token][1])+','+str(tokenList[token][2])+'> Error sintactico: se encontro: "'+tokenList[token][0]+'"; se esperaba: "borrar", "definir", "dimension", "escribir", "esperar", "identificador", "leer", "limpiar", "mientras", "para", "repetir", "segun", "si".')
            flag = False
        if tokenList[token][0]=='hasta':
            print('<'+str(tokenList[token][1])+','+str(tokenList[token][2])+'> Error sintactico: se encontro: "'+tokenList[token][0]+'"; se esperaba: "borrar", "definir", "dimension", "escribir", "esperar", "identificador", "leer", "limpiar", "mientras", "para", "repetir", "segun", "si".')
            flag = False
        if tokenList[token][0]=='finsegun':
            print('<'+str(tokenList[token][1])+','+str(tokenList[token][2])+'> Error sintactico: se encontro: "'+tokenList[token][0]+'"; se esperaba: "borrar", "definir", "dimension", "escribir", "esperar", "identificador", "leer", "limpiar", "mientras", "para", "repetir", "segun", "si".')
            flag = False
    newPrioridad = []
    
    if len(prioridad)>0:    
        if not entre2:
            if prioridad[len(prioridad)-1] == 'si':
                print('<'+str(tokenList[token][1])+','+str(tokenList[token][2])+'> Error sintactico: se encontro: "'+tokenList[token][0]+'"; se esperaba: "borrar", "definir", "dimension", "escribir", "esperar", "finsi", "identificador", "leer", "limpiar", "mientras", "para", "repetir", "segun", "si".')
                flag = False
            if prioridad[len(prioridad)-1] == 'para':
                print('<'+str(tokenList[token][1])+','+str(tokenList[token][2])+'> Error sintactico: se encontro: "'+tokenList[token][0]+'"; se esperaba: "borrar", "definir", "dimension", "escribir", "esperar", "finpara", "identificador", "leer", "limpiar", "mientras", "para", "repetir", "segun", "si".')
                flag = False
            if prioridad[len(prioridad)-1] == 'mientras':
                print('<'+str(tokenList[token][1])+','+str(tokenList[token][2])+'> Error sintactico: se encontro: "'+tokenList[token][0]+'"; se esperaba: "borrar", "definir", "dimension", "escribir", "esperar", "finmientras", "identificador", "leer", "limpiar", "mientras", "para", "repetir", "segun", "si".')
                flag = False
            if prioridad[len(prioridad)-1] == 'hasta':
                print('<'+str(tokenList[token][1])+','+str(tokenList[token][2])+'> Error sintactico: se encontro: "'+tokenList[token][0]+'"; se esperaba: "borrar", "definir", "dimension", "escribir", "esperar", "finmientras", "identificador", "leer", "limpiar", "mientras", "para", "repetir", "segun", "si".')
                flag = False
            if prioridad[len(prioridad)-1] == 'segun':
                print('<'+str(tokenList[token][1])+','+str(tokenList[token][2])+'> Error sintactico: se encontro: "'+tokenList[token][0]+'"; se esperaba: "borrar", "definir", "dimension", "escribir", "esperar", "finmientras", "identificador", "leer", "limpiar", "mientras", "para", "repetir", "segun", "si".')
                flag = False
            
        
        f = False
        for p in range(0, len(prioridad)-1):
            if prioridad[p] == cadena:
                f = True
        
            if f:
                newPrioridad.insert(p, prioridad[p]) 
            elif not prioridad[p] == cadena:
                if f:
                    newPrioridad.insert(p, prioridad[p]) 
                else:
                    newPrioridad.insert(p-1, prioridad[p])
        
    if f:
        token = token +1
    return [newPrioridad, flag, token]

def verifyI(token):
    flag = True
    flag2 = True
    while flag2: 
        if tokenList[token][0] == 'token_entero' or tokenList[token][0] == 'token_real' or tokenList[token][0] == 'identificador' or tokenList[token][0] == 'token_menos' or tokenList[token][0] == 'token_par_izq':
            d = token
            compa = ''
            falg3 = True
            while falg3:
                if d < len(tokenList): 
                    for com in comparacion:
                        if tokenList[d][0] == com:
                            compa = com
                            falg3=False
                            break
                    d=d+1
                              
            if compa != '':
                res = verifyEx(compa, token)
                token = res[0]+1
                flag = res[1]
            else:
                flag3=True
                if compa =='':
                    while falg3:
                        if d < len(tokenList): 
                            for exp in exepciones1:
                                if tokenList[d][0] == exp:
                                    compa = exp
                                    falg3=False
                                    break
                            d=d+1
                if compa != '':
                    res = verifyEx(compa, token)
                    token = res[0]
                    flag = res[1]
                    state = 3
                else:
                    state =3
                    flag = False
                    token = len(tokenList)   
                            
        elif tokenList[token][0] == 'token_cadena' or tokenList[token][0] == 'verdadero' or tokenList[token][0] == 'falso':
                si = False
                for com in comparacion:
                    if tokenList[token+1][0] == com:
                        si = True
                        break 
                    
                if si:
                    token = token +1
                else:
                    compa=''
                    flag3=True
                    while falg3:
                        if d < len(tokenList): 
                            for exp in exepciones1:
                                if tokenList[d][0] == exp:
                                    compa = exp
                                    falg3=False
                                    break
                                d=d+1
                    if compa != '':
                        state = 3
                        flag2 = False 
                        token = token +1
                    else: 
                        state =3
                        flag = False
                        token = len(tokenList) 
        else:
            try: 
                a = tokens[tokenList[token][0]]
                answer = True
            except KeyError:
                answer = False
            if answer: 
                print('<'+str(tokenList[token][1])+','+str(tokenList[token][2])+'> Error sintactico: se encontro: "algoritmo", "borrar", "definir", "dimension", "escribir", "esperar", "finalgoritmo", "finfuncion","finmientras", "finpara", "finproceso", "finsegun", "finsi", "finsubproceso", "funcion","identificador", "leer", "limpiar", "mientras", "pantalla", "para", "proceso", "repetir", "segun", "si", "sino", "subproceso", "<>", "=", ">", ">=", "<", "<=".')
                flag = False
                flag2 = False
            else:
                print('<'+str(tokenList[token][1])+','+str(tokenList[token][2])+'> Error sintactico: se encontro: "algoritmo", "borrar", "definir", "dimension", "escribir", "esperar", "finalgoritmo", "finfuncion","finmientras", "finpara", "finproceso", "finsegun", "finsi", "finsubproceso", "funcion","identificador", "leer", "limpiar", "mientras", "pantalla", "para", "proceso", "repetir", "segun", "si", "sino", "subproceso", "<>", "=", ">", ">=", "<", "<=".')
                flag = False 
                flag2 = False
    return [token, flag]        

def verifyFun(token):
    flag = True
    flag2 = True
    
    while flag2: 
        if tokenList[token][0] == 'token_par_der':
            flag2=False
        elif tokenList[token][0] == 'token_entero' or tokenList[token][0] == 'token_real' or tokenList[token][0] == 'identificador' or tokenList[token][0] == 'token_menos' or tokenList[token][0] == 'token_par_izq' or tokenList[token][0] == 'token_par_der':
            flag4=False
            if tokenList[token][0] == 'token_par_der':
                token = token
                flag4 = True
            if not flag4:
                b= False
                c = False
                d = token
                flag3= True
                
                while flag3:
                    d=d+1 
                    if d<len(tokenList):  
                        for key in keywords:
                            if tokenList[d][0] == key:
                                flag3 = False
                    else:
                        d= len(tokenList)
                        flag3 = False
                    
                for i in range(token, d):
                    if tokenList[i][0] == 'token_coma':
                        b = True
                        break
                    if tokenList[i][0] == 'token_par_der':
                        c = True
                        break
                
                if b:
                    res = verifyEx('token_coma', token)
                    token = res[0]+1
                    flag = res[1] 
                elif c:
                    res = verifyEx('token_par_der', token)
                    token = res[0]
                    flag = res[1]
                else:
                    res = verifyEx('token_coma', token)
                    token = res[0]
                    flag = res[1]
                    flag2 = False
        elif tokenList[token][0] == 'token_cadena' or tokenList[token][0] == 'verdadero' or tokenList[token][0] == 'falso':
            if tokenList[token+1][0] == 'token_coma' or tokenList[token+1][0] == 'token_par_der':
                if tokenList[token+1][0] == 'token_par_der':
                    token = token + 1
                    flag2 = False
                else: 
                    token = token + 2
            else:
                try: 
                    a = tokens[tokenList[token+1][0]]
                    answer = True
                except KeyError:
                    answer = False
                if answer: 
                    print('<'+str(tokenList[token+1][1])+','+str(tokenList[token+1][2])+'> Error sintactico: se encontro: "'+a+'"; se esperaba: ",", ")".')
                    flag = False
                    flag2 = False
                else:
                    print('<'+str(tokenList[token+1][1])+','+str(tokenList[token+1][2])+'> Error sintactico: se encontro: "'+tokenList[token+1][0]+'"; se esperaba: ",", ")".')
                    flag = False 
                    flag2 = False
        else:
            try: 
                a = tokens[tokenList[token+1][0]]
                answer = True
            except KeyError:
                answer = False
            if answer: 
                print('<'+str(tokenList[token+1][1])+','+str(tokenList[token+1][2])+'> Error sintactico: se encontro: "'+a+'"; se esperaba: "falso", "identificador", "valor_cadena", "valor_entero", "-", "(", "valor_real", "verdadero".')
                flag = False
                flag2 = False
            else:
                print('<'+str(tokenList[token+1][1])+','+str(tokenList[token+1][2])+'> Error sintactico: se encontro: "'+tokenList[token+1][0]+'"; se esperaba: "falso", "identificador", "valor_cadena", "valor_entero", "-", "(", "valor_real", "verdadero".')
                flag = False  
                flag2 = False
         
    return [token, flag]

def verifyAr(token):
    flag = True
    return [token, flag]

def verifyEx (palabra, token):
    flag = True
    flag2 = True
    while flag2:
        if tokenList[token][0] == 'token_entero' or tokenList[token][0] == 'token_real' or tokenList[token][0] == 'identificador':
            if tokenList[token][0] == 'identificador':    
                if tokenList[token+1][0] == 'token_par_izq':
                    res = verifyFun(token+2)
                    token = res[0]
                    flag = res[1]
                elif tokenList[token+1][0] == 'token_cor_izq':
                    res = verifyAr(token+2)
                    token = res[0]
                    flag = res[1]
            if tokenList[token+1][0] == 'token_mas' or tokenList[token+1][0] == 'token_menos' or tokenList[token+1][0] == 'token_div' or tokenList[token+1][0] == 'token_mul' or tokenList[token+1][0] == 'token_mod' or tokenList[token+1][0] == 'token_pot': 
                if tokenList[token+2][0] == 'token_entero' or tokenList[token+2][0] == 'token_real' or tokenList[token+2][0] == 'identificador' or tokenList[token+2][0] == 'token_par_izq':
                    token = token +2
                else: 
                    try: 
                        a = tokens[tokenList[token+2][0]]
                        answer = True

                    except KeyError:
                        answer = False
                    if answer: 
                        print('<'+str(tokenList[token+2][1])+','+str(tokenList[token+2][2])+'> Error sintactico: se encontro: "'+a+'"; se esperaba: "identificador", "valor_entero", "(", "valor_real".')
                        flag = False
                        flag2 = False
                    else:
                        print('<'+str(tokenList[token+2][1])+','+str(tokenList[token+2][2])+'> Error sintactico: se encontro: "'+tokenList[token+2][0]+'"; se esperaba: "identificador", "valor_entero", "(", "valor_real".')
                        flag = False
                        flag2 = False  
            elif tokenList[token+1][0] == palabra:
                flag2 = False
                token = token+1             
            elif  tokenList[token+1][0] == 'token_par_der':
                if tokenList[token+2][0] == 'token_mas' or tokenList[token+2][0] == 'token_menos' or tokenList[token+2][0] == 'token_div' or tokenList[token+2][0] == 'token_mul' or tokenList[token+2][0] == 'token_mod' or tokenList[token+2][0] == 'token_pot':
                    if tokenList[token+3][0] == 'token_entero' or tokenList[token+3][0] == 'token_real' or tokenList[token+3][0] == 'identificador' or tokenList[token+3][0] == 'token_par_izq':
                        token = token +3
                    else: 
                        try: 
                            a = tokens[tokenList[token+3][0]]
                            answer = True

                        except KeyError:
                            answer = False
                        if answer: 
                            print('<'+str(tokenList[token+3][1])+','+str(tokenList[token+3][2])+'> Error sintactico: se encontro: "'+a+'"; se esperaba: "identificador", "valor_entero", "(", "valor_real".')
                            flag = False
                            flag2 = False
                        else:
                            print('<'+str(tokenList[token+3][1])+','+str(tokenList[token+3][2])+'> Error sintactico: se encontro: "'+tokenList[token+3][0]+'"; se esperaba: "identificador", "valor_entero", "(", "valor_real".')
                            flag = False
                            flag2 = False      
                elif tokenList[token+2][0] == 'token_par_der':
                    token = token + 3
                elif tokenList[token+2][0] == palabra:
                    flag2 = False
                    token = token+2
                else:
                    try: 
                        a = tokens[tokenList[token+2][0]]
                        answer = True

                    except KeyError:
                        answer = False
                    if answer: 
                        print('<'+str(tokenList[token+2][1])+','+str(tokenList[token+2][2])+'> Error sintactico: se encontro: "'+a+'"; se esperaba: "'+palabra+'", "/", "+", "-", "%", "*", ")", "^".')
                        flag = False
                        flag2 = False
                    else:
                        print('<'+str(tokenList[token+2][1])+','+str(tokenList[token+2][2])+'> Error sintactico: se encontro: "'+tokenList[token+2][0]+'"; se esperaba: "'+palabra+'", "/", "+", "-", "%", "*", ")", "^".')
                        flag = False
                        flag2 = False
            else:
                try: 
                    a = tokens[tokenList[token+1][0]]
                    answer = True

                except KeyError:
                    answer = False
                if answer: 
                    print('<'+str(tokenList[token+1][1])+','+str(tokenList[token+1][2])+'> Error sintactico: se encontro: "'+a+'"; se esperaba: "'+palabra+'", "/", "+", "-", "%", "*", ")", "^".')
                    flag = False
                    flag2 = False 
                else:
                    print('<'+str(tokenList[token+1][1])+','+str(tokenList[token+1][2])+'> Error sintactico: se encontro: "'+tokenList[token+1][0]+'"; se esperaba: "'+palabra+'", "/", "+", "-", "%", "*", ")", "^".')
                    flag = False
                    flag2 = False                
        elif tokenList[token][0] == 'token_par_izq':
            if tokenList[token+1][0] == 'identificador' or tokenList[token+1][0] == 'token_entero' or tokenList[token+1][0] == 'token_real' or tokenList[token+1][0] == 'token_menos' or tokenList[token+1][0] == 'token_par_izq':
                token = token + 1
            else:
                try: 
                    a = tokens[tokenList[token+1][0]]
                    answer = True

                except KeyError:
                    answer = False
                if answer: 
                    print('<'+str(tokenList[token+1][1])+','+str(tokenList[token+1][2])+'> Error sintactico: se encontro: "'+a+'"; se esperaba:"identificador", "valor_entero", "-", "(", "valor_real".')
                    flag = False
                    flag2 = False 
                else:
                    print('<'+str(tokenList[token+1][1])+','+str(tokenList[token+1][2])+'> Error sintactico: se encontro: "'+tokenList[token+1][0]+'"; se esperaba:"identificador", "valor_entero", "-", "(", "valor_real".')
                    flag = False
                    flag2 = False        
        elif tokenList[token][0] == 'token_menos':
            if tokenList[token+1][0] == 'identificador' or tokenList[token+1][0] == 'token_entero' or tokenList[token+1][0] == 'token_real' or tokenList[token+1][0] == 'token_par_izq':
                token = token + 1
            else:
                try: 
                    a = tokens[tokenList[token+1][0]]
                    answer = True

                except KeyError:
                    answer = False
                if answer: 
                    print('<'+str(tokenList[token+1][1])+','+str(tokenList[token+1][2])+'> Error sintactico: se encontro: "'+a+'"; se esperaba:"identificador", "valor_entero", "(", "valor_real".')
                    flag = False
                    flag2 = False 
                else:
                    print('<'+str(tokenList[token+1][1])+','+str(tokenList[token+1][2])+'> Error sintactico: se encontro: "'+tokenList[token+1][0]+'"; se esperaba:"identificador", "valor_entero", "(", "valor_real".')
                    flag = False
                    flag2 = False  
        else:
            try: 
                a = tokens[tokenList[token][0]]
                answer = True

            except KeyError:
                answer = False
            if answer: 
                print('<'+str(tokenList[token][1])+','+str(tokenList[token][2])+'> Error sintactico: se encontro: "'+a+'"; se esperaba: "'+palabra+'", "identificador", "valor_entero", "-", "(", "valor_real".')
                flag = False
                flag2 = False 
            else:
                print('<'+str(tokenList[token][1])+','+str(tokenList[token][2])+'> Error sintactico: se encontro: "'+tokenList[token][0]+'"; se esperaba: "'+palabra+'", "identificador",  "valor_entero", "-", "(", "valor_real".')
                flag = False
                flag2 = False
    
    return [token, flag]

def verifyEx1 (token):
    flag = True
    flag2 = True
    while flag2:
        if tokenList[token][0] == 'token_entero' or tokenList[token][0] == 'token_real' or tokenList[token][0] == 'identificador':
            if tokenList[token+1][0] == 'token_mas' or tokenList[token+1][0] == 'token_menos' or tokenList[token+1][0] == 'token_div' or tokenList[token+1][0] == 'token_mul' or tokenList[token+1][0] == 'token_mod' or tokenList[token+1][0] == 'token_pot': 
                if tokenList[token+2][0] == 'token_entero' or tokenList[token+2][0] == 'token_real' or tokenList[token+2][0] == 'identificador' or tokenList[token+2][0] == 'token_par_izq':
                    token = token +2
                else: 
                    try: 
                        a = tokens[tokenList[token+2][0]]
                        answer = True

                    except KeyError:
                        answer = False
                    if answer: 
                        print('<'+str(tokenList[token+2][1])+','+str(tokenList[token+2][2])+'> Error sintactico: se encontro: "'+a+'"; se esperaba: "identificador", "valor_entero", "(", "valor_real".')
                        flag = False
                        flag2 = False
                    else:
                        print('<'+str(tokenList[token+2][1])+','+str(tokenList[token+2][2])+'> Error sintactico: se encontro: "'+tokenList[token+2][0]+'"; se esperaba: "identificador", "valor_entero", "(", "valor_real".')
                        flag = False
                        flag2 = False              
            elif  tokenList[token+1][0] == 'token_par_der':
                if tokenList[token+2][0] == 'token_mas' or tokenList[token+2][0] == 'token_menos' or tokenList[token+2][0] == 'token_div' or tokenList[token+2][0] == 'token_mul' or tokenList[token+2][0] == 'token_mod' or tokenList[token+2][0] == 'token_pot':
                    if tokenList[token+3][0] == 'token_entero' or tokenList[token+3][0] == 'token_real' or tokenList[token+3][0] == 'identificador' or tokenList[token+3][0] == 'token_par_izq':
                        token = token +3
                    else: 
                        try: 
                            a = tokens[tokenList[token+3][0]]
                            answer = True

                        except KeyError:
                            answer = False
                        if answer: 
                            print('<'+str(tokenList[token+3][1])+','+str(tokenList[token+3][2])+'> Error sintactico: se encontro: "'+a+'"; se esperaba: "identificador", "valor_entero", "(", "valor_real".')
                            flag = False
                            flag2 = False
                        else:
                            print('<'+str(tokenList[token+3][1])+','+str(tokenList[token+3][2])+'> Error sintactico: se encontro: "'+tokenList[token+3][0]+'"; se esperaba: "identificador", "valor_entero", "(", "valor_real".')
                            flag = False
                            flag2 = False      
                elif tokenList[token+2][0] == 'token_par_der':
                    token = token + 3
                else:
                    try: 
                        a = tokens[tokenList[token+2][0]]
                        answer = True

                    except KeyError:
                        answer = False
                    if answer: 
                        print('<'+str(tokenList[token+2][1])+','+str(tokenList[token+2][2])+'> Error sintactico: se encontro: "'+a+'"; se esperaba: "hacer", "<>", "/", "=", "+", ">", ">=", "<", "<=", "-", "%", "*", ")", "^".')
                        flag = False
                        flag2 = False
                    else:
                        print('<'+str(tokenList[token+2][1])+','+str(tokenList[token+2][2])+'> Error sintactico: se encontro: "hacer", "<>", "/", "=", "+", ">", ">=", "<", "<=", "-", "%", "*", ")", "^".')
                        flag = False
                        flag2 = False
            else:
                try: 
                    a = tokens[tokenList[token+1][0]]
                    answer = True

                except KeyError:
                    answer = False
                if answer: 
                    print('<'+str(tokenList[token+1][1])+','+str(tokenList[token+1][2])+'> Error sintactico: se encontro: "'+a+'"; se esperaba: "hacer", "<>", "/", "=", "+", ">", ">=", "<", "<=", "-", "%", "*", ")", "^".')
                    flag = False
                    flag2 = False 
                else:
                    print('<'+str(tokenList[token+1][1])+','+str(tokenList[token+1][2])+'> Error sintactico: se encontro: "'+tokenList[token+1][0]+'"; se esperaba: "hacer", "<>", "/", "=", "+", ">", ">=", "<", "<=", "-", "%", "*", ")", "^".')
                    flag = False
                    flag2 = False                
        elif tokenList[token][0] == 'token_par_izq':
            if tokenList[token+1][0] == 'identificador' or tokenList[token+1][0] == 'token_entero' or tokenList[token+1][0] == 'token_real' or tokenList[token+1][0] == 'token_menos' or tokenList[token+1][0] == 'token_par_izq':
                token = token + 1
            else:
                try: 
                    a = tokens[tokenList[token+1][0]]
                    answer = True

                except KeyError:
                    answer = False
                if answer: 
                    print('<'+str(tokenList[token+1][1])+','+str(tokenList[token+1][2])+'> Error sintactico: se encontro: "'+a+'"; se esperaba:"identificador", "valor_entero", "-", "(", "valor_real".')
                    flag = False
                    flag2 = False 
                else:
                    print('<'+str(tokenList[token+1][1])+','+str(tokenList[token+1][2])+'> Error sintactico: se encontro: "'+tokenList[token+1][0]+'"; se esperaba:"identificador", "valor_entero", "-", "(", "valor_real".')
                    flag = False
                    flag2 = False        
        elif tokenList[token][0] == 'token_menos':
            if tokenList[token+1][0] == 'identificador' or tokenList[token+1][0] == 'token_entero' or tokenList[token+1][0] == 'token_real' or tokenList[token+1][0] == 'token_par_izq':
                token = token + 1
            else:
                try: 
                    a = tokens[tokenList[token+1][0]]
                    answer = True

                except KeyError:
                    answer = False
                if answer: 
                    print('<'+str(tokenList[token+1][1])+','+str(tokenList[token+1][2])+'> Error sintactico: se encontro: "'+a+'"; se esperaba:"identificador", "valor_entero", "(", "valor_real".')
                    flag = False
                    flag2 = False 
                else:
                    print('<'+str(tokenList[token+1][1])+','+str(tokenList[token+1][2])+'> Error sintactico: se encontro: "'+tokenList[token+1][0]+'"; se esperaba:"identificador", "valor_entero", "(", "valor_real".')
                    flag = False
                    flag2 = False  
        else:
            try: 
                a = tokens[tokenList[token][0]]
                answer = True

            except KeyError:
                answer = False
            if answer: 
                print('<'+str(tokenList[token][1])+','+str(tokenList[token][2])+'> Error sintactico: se encontro: "'+a+'"; se esperaba: "hacer", "identificador", "valor_entero", "<>", "/", "=", "+", ">", ">=", "<", "<=", "-", "%", "*", ")", "^", "-", "(", "valor_real".')
                flag = False
                flag2 = False 
            else:
                print('<'+str(tokenList[token][1])+','+str(tokenList[token][2])+'> Error sintactico: se encontro: "'+tokenList[token][0]+'"; se esperaba: "hacer", "identificador",  "valor_entero", "-", "<>", "/", "=", "+", ">", ">=", "<", "<=", "-", "%", "*", ")", "^", "(", "valor_real".')
                flag = False
                flag2 = False
    
    return [token, flag]
        
def grammar():
    state = 0
    token = 0
    entre = False
    entre1= False
    prioridad = []
    hayProceso = False
    flag = True
    while flag:
        if state == 0:   
            if len(tokenList) > token:
                if tokenList[token][0] == 'subproceso' or tokenList[token][0] == 'funcion':
                    state= 2
                    token = token + 1
                    entre1= True 
                    
                elif tokenList[token][0] == 'proceso' or tokenList[token][0] == 'algoritmo':
                    entre = True
                    hayProceso = True
                    state = 1
                    token = token + 1
                else:
                    try: 
                        a = tokens[tokenList[token][0]]
                        answer = True

                    except KeyError:
                        answer = False
                    if answer: 
                        print('<'+str(tokenList[token][1])+','+str(tokenList[token][2])+'> Error sintactico: se encontro: "'+a+'"; se esperaba: "algoritmo", "funcion", "proceso", "subproceso".')
                        flag = False
                    else:
                        print('<'+str(tokenList[token][1])+','+str(tokenList[token][2])+'> Error sintactico: se encontro: "'+tokenList[token][0]+'"; se esperaba: "algoritmo", "funcion", "proceso", "subproceso".')
                        flag = False
            else:
                if not hayProceso:
                        print ('Error sintactico: falta proceso.')
                        flag = False
                        
        if state == 1:
            if tokenList[token][0] == 'identificador':
                state = 3
                token = token + 1
            else:
                try: 
                    a = tokens[tokenList[token][0]]
                    answer = True

                except KeyError:
                    answer = False
                if answer: 
                    print('<'+str(tokenList[token][1])+','+str(tokenList[token][2])+'> Error sintactico: se encontro: "'+a+'"; se esperaba: "identificador".')
                    flag = False
                else:
                    print('<'+str(tokenList[token][1])+','+str(tokenList[token][2])+'> Error sintactico: se encontro: "'+tokenList[token][0]+'"; se esperaba: "identificador".')
                    flag = False
                    
        if state == 2:
            if tokenList[token][0] == 'identificador':
                state = 9
                token = token + 1
            else:
                try: 
                    a = tokens[tokenList[token][0]]
                    answer = True

                except KeyError:
                    answer = False
                if answer: 
                    print('<'+str(tokenList[token][1])+','+str(tokenList[token][2])+'> Error sintactico: se encontro: "'+a+'"; se esperaba: "identificador".')
                    flag = False
                else:
                    print('<'+str(tokenList[token][1])+','+str(tokenList[token][2])+'> Error sintactico: se encontro: "'+tokenList[token][0]+'"; se esperaba: "identificador".')
                    flag = False 
        
        if state == 3: 
            if len(tokenList) > token: 
                try: 
                    b = tokens[tokenList[token][0]]
                    answer = True

                except KeyError:
                    answer = False
                
                answer1 = False
                for ex in exepciones:
                    if tokenList[token][0] == ex:
                        answer1= True 
                if tokenList[token][0]== 'definir':
                    state = 4
                    token = token + 1
                    
                elif tokenList[token][0] == 'leer':
                    state = 5
                    token = token + 1
                
                elif tokenList[token][0] == 'escribir':
                    state = 6
                    token = token + 1
                    
                elif tokenList[token][0] == 'identificador':
                    state = 7
                    token = token + 1
                elif tokenList[token][0] == 'dimension':
                    state = 12
                    token = token + 1
                elif tokenList[token][0] == 'si':
                    
                    state = 14
                    res = verify(prioridad, token)
                    token = res[2]+1
                    flag = res[1]
                    prioridad = res[0]
                    
                    prioridad.append('si')
                elif tokenList[token][0] == 'sino':
                    a = False
                    for p in prioridad:
                        if p == 'si':
                            a = True
                    if a:
                        state = 3
                        token = token + 1
                    else:
                        print('<'+str(tokenList[token][1])+','+str(tokenList[token][2])+'> Error sintactico: se encontro: "'+tokenList[token][0]+'"; se esperaba: "borrar", "definir", "dimension", "escribir", "esperar", "identificador", "leer", "limpiar", "mientras", "para", "repetir", "segun", "si".')
                        flag = False
                elif tokenList[token][0] == 'para':
                    state = 15
                    res = verify(prioridad, token)
                    token = res[2]+1
                    flag = res[1]
                    prioridad = res[0]
                    
                    prioridad.append('para') 
                elif tokenList[token][0] == 'mientras':
                    state = 16
                    res = verify(prioridad, token)
                    token = res[2]+1
                    flag = res[1]
                    prioridad = res[0]
                    prioridad.append('mientras') 
                elif tokenList[token][0] == 'repetir':
                    state = 3
                    res = verify(prioridad, token)
                    token = res[2]+1
                    flag = res[1]
                    prioridad = res[0]
                    prioridad.append('repetir')
                elif tokenList[token][0] == 'segun':
                    state = 17
                    res = verify(prioridad, token)
                    token = res[2]+1
                    flag = res[1]
                    prioridad = res[0]
                    prioridad.append('segun')
                elif tokenList[token][0] == 'caso':
                    a = False
                    for p in prioridad:
                        if p == 'segun':
                            a = True
                    if a:
                        state = 18
                        token = token + 1
                    else:
                        print('<'+str(tokenList[token][1])+','+str(tokenList[token][2])+'> Error sintactico: se encontro: "'+tokenList[token][0]+'"; se esperaba: "borrar", "definir", "dimension", "escribir", "esperar", "identificador", "leer", "limpiar", "mientras", "para", "repetir", "segun", "si".')
                        flag = False
                elif tokenList[token][0] == 'de':
                    if tokenList[token+1][0] == 'otro':
                        if tokenList[token+2][0] == 'modo':
                            if tokenList[token+3][0] == 'token_dosp':
                                token = token + 4
                                state = 3
                            else:
                                try: 
                                    a = tokens[tokenList[token][0]]
                                    answer = True
                                except KeyError:
                                    answer = False
                                if answer: 
                                    print('<'+str(tokenList[token][1])+','+str(tokenList[token][2])+'> Error sintactico: se encontro: ":".')
                                    flag = False
                                else:
                                    print('<'+str(tokenList[token][1])+','+str(tokenList[token][2])+'> Error sintactico: se encontro: ":".')
                                    flag = False 
                        else:
                            try: 
                                a = tokens[tokenList[token][0]]
                                answer = True
                            except KeyError:
                                answer = False
                            if answer: 
                                print('<'+str(tokenList[token][1])+','+str(tokenList[token][2])+'> Error sintactico: se encontro: "modo".')
                                flag = False
                            else:
                                print('<'+str(tokenList[token][1])+','+str(tokenList[token][2])+'> Error sintactico: se encontro: "modo".')
                                flag = False 
                    else:
                        try: 
                            a = tokens[tokenList[token][0]]
                            answer = True
                        except KeyError:
                            answer = False
                        if answer: 
                            print('<'+str(tokenList[token][1])+','+str(tokenList[token][2])+'> Error sintactico: se encontro: "otro".')
                            flag = False
                        else:
                            print('<'+str(tokenList[token][1])+','+str(tokenList[token][2])+'> Error sintactico: se encontro: "otro".')
                            flag = False 
                elif answer:
                    print('<'+str(tokenList[token][1])+','+str(tokenList[token][2])+'> Error sintactico: se encontro: "'+b+'"; se esperaba: "borrar", "definir", "dimension", "escribir", "esperar", "identificador", "leer", "limpiar", "mientras", "para", "repetir", "segun", "si".')
                    flag = False
                elif answer1:
                    if entre1:
                        print('<'+str(tokenList[token][1])+','+str(tokenList[token][2])+'> Error sintactico: se encontro: "'+tokenList[token][0]+'"; se esperaba: "borrar", "definir", "dimension", "escribir", "esperar", "finalgoritmo", "finproceso", "identificador", "leer", "limpiar", "mientras", "para", "repetir", "segun", "si".')
                        flag = False
                    else:
                        print('<'+str(tokenList[token][1])+','+str(tokenList[token][2])+'> Error sintactico: se encontro: "'+tokenList[token][0]+'"; se esperaba: "borrar", "definir", "dimension", "escribir", "esperar", "identificador", "leer", "limpiar", "mientras", "para", "repetir", "segun", "si".')
                        flag = False
                else:
                    res = verify(prioridad, token)
                    token = res[2]
                    flag = res[1]
                    prioridad = res[0]
                    state = 3
                    if flag:
                        if tokenList[token][0]=='finproceso' or tokenList[token][0]=='finalgoritmo':
                            entre = False
                            if hayProceso:
                                print ('El analisis sintactico ha finalizado exitosamente.')
                            else:
                                print ('Error sintactico: falta proceso.')
                            flag =False
                        if tokenList[token][0]=='finsubproceso' or tokenList[token][0]=='finfuncion':
                            entre1 = False
                            state = 0
                            token = token +1
                        if entre1 and tokenList[token][0]=='proceso':
                            try: 
                                a = tokens[tokenList[token][0]]
                                answer = True

                            except KeyError:
                                answer = False
                            if answer: 
                                print('<'+str(tokenList[token][1])+','+str(tokenList[token][2])+'> Error sintactico: se encontro: "'+a+'"; se esperaba: "borrar", "definir", "dimension", "escribir", "esperar", "finfuncion", "finsubproceso", "identificador", "leer", "limpiar", "mientras", "para", "repetir", "segun", "si".')
                                flag = False
                            else:
                                print('<'+str(tokenList[token][1])+','+str(tokenList[token][2])+'> Error sintactico: se encontro: "'+tokenList[token][0]+'"; se esperaba: "borrar", "definir", "dimension", "escribir", "esperar", "finfuncion", "finsubproceso", "identificador", "leer", "limpiar", "mientras", "para", "repetir", "segun", "si".')
                                flag = False
                        elif entre and len(tokenList)-1 == token:
                            print('<'+str(tokenList[token][1])+','+str(tokenList[token][2])+'> Error sintactico: se encontro: "EOF"; se esperaba:"borrar", "definir", "dimension", "escribir", "esperar", "finalgoritmo", "finproceso", "identificador", "leer", "limpiar", "mientras", "para", "repetir", "segun", "si".')
                            flag = False
                    
            else:
                if entre1:
                    try: 
                        a = tokens[tokenList[token][0]]
                        answer = True

                    except KeyError:
                        answer = False
                    if answer: 
                        print('<'+str(tokenList[token-1][1])+','+str(tokenList[token-1][2])+'> Error sintactico: se encontro: "'+a+'"; se esperaba: "borrar", "definir", "dimension", "escribir", "esperar", "finfuncion", "finsubproceso", "identificador", "leer", "limpiar", "mientras", "para", "repetir", "segun", "si".')
                        flag = False
                    else:
                        print('<'+str(tokenList[token-1][1])+','+str(tokenList[token-1][2])+'> Error sintactico: se encontro: "'+tokenList[token-1][0]+'"; se esperaba: "borrar", "definir", "dimension", "escribir", "esperar", "finfuncion", "finsubproceso", "identificador", "leer", "limpiar", "mientras", "para", "repetir", "segun", "si".')
                        flag = False
                elif entre:
                    print('<'+str(tokenList[token-1][1])+','+str(tokenList[token-1][2])+'> Error sintactico: se encontro: "EOF"; se esperaba:"borrar", "definir", "dimension", "escribir", "esperar", "finalgoritmo", "finproceso", "identificador", "leer", "limpiar", "mientras", "para", "repetir", "segun", "si".')
                    flag = False
                elif hayProceso:
                    print ('El analisis sintactico ha finalizado exitosamente.')
                else:
                    print ('Error sintactico: falta proceso.')
                    
        if state == 4:
            flagDef = True
            while flagDef:
                if tokenList[token][0] == 'real' or tokenList[token][0] == 'entero' or tokenList[token][0] == 'texto' or tokenList[token][0] == 'numerico' or tokenList[token][0] == 'caracter' or tokenList[token][0] == 'logico' or tokenList[token][0] == 'numero' or tokenList[token][0] == 'cadena':
                    if tokenList[token+1][0] == 'token_pyc':
                        state = 3
                        token = token + 2
                        flagDef = False
                    else:
                        try: 
                            a = tokens[tokenList[token+1][0]]
                            answer = True

                        except KeyError:
                            answer = False
                        if answer: 
                            print('<'+str(tokenList[token+1][1])+','+str(tokenList[token+1][2])+'> Error sintactico: se encontro: "'+a+'"; se esperaba: ";".')
                            flag = False
                            flagDef = False
                        else:
                            print('<'+str(tokenList[token+1][1])+','+str(tokenList[token+1][2])+'> Error sintactico: se encontro: "'+tokenList[token+1][0]+'"; se esperaba: ";".')
                            flag = False
                            flagDef = False
                elif tokenList[token][0] == 'identificador':
                    if tokenList[token+1][0] == 'token_coma':
                        token = token + 2
                    elif tokenList[token+1][0]== 'como':
                        token = token + 2
                    else:
                        try: 
                            a = tokens[tokenList[token+1][0]]
                            answer = True

                        except KeyError:
                            answer = False
                        if answer: 
                            print('<'+str(tokenList[token+1][1])+','+str(tokenList[token+1][2])+'> Error sintactico: se encontro: "'+a+'"; se esperaba: "como", ",".')
                            print('error')
                            flag = False
                            flagDef = False
                        else:
                            print('<'+str(tokenList[token+1][1])+','+str(tokenList[token+1][2])+'> Error sintactico: se encontro: "'+tokenList[token+1][0]+'"; se esperaba: "como", ",".')
                            flag = False
                            flagDef = False
                else:
                    try: 
                        a = tokens[tokenList[token][0]]
                        answer = True

                    except KeyError:
                        answer = False
                    if answer: 
                        print('<'+str(tokenList[token][1])+','+str(tokenList[token][2])+'> Error sintactico: se encontro: "'+a+'"; se esperaba: "identificador".')
                        flag = False
                        flagDef = False
                    else:
                        print('<'+str(tokenList[token][1])+','+str(tokenList[token][2])+'> Error sintactico: se encontro: "'+tokenList[token][0]+'"; se esperaba: "identificador".')
                        flag = False
                        flagDef = False
        
        if state == 5:
            flagLe = True
            while flagLe:
                if tokenList[token][0] == 'identificador':
                    if tokenList[token+1][0] == 'token_coma':
                        token = token + 2
                    elif tokenList[token+1][0]== 'token_pyc':
                        token = token + 2
                        state = 3
                        flagLe= False
                    else:
                        try: 
                            a = tokens[tokenList[token+1][0]]
                            answer = True

                        except KeyError:
                            answer = False
                        if answer: 
                            print('<'+str(tokenList[token+1][1])+','+str(tokenList[token+1][2])+'> Error sintactico: se encontro: "'+a+'"; se esperaba: ",", ";".')
                            print('error')
                            flag = False
                            flagLe = False
                        else:
                            print('<'+str(tokenList[token+1][1])+','+str(tokenList[token+1][2])+'> Error sintactico: se encontro: "'+tokenList[token+1][0]+'"; se esperaba: ",", ";".')
                            flag = False
                            flagLe = False
                else:
                    try: 
                        a = tokens[tokenList[token][0]]
                        answer = True

                    except KeyError:
                        answer = False
                    if answer: 
                        print('<'+str(tokenList[token][1])+','+str(tokenList[token][2])+'> Error sintactico: se encontro: "'+a+'"; se esperaba: "identificador".')
                        flag = False
                        flagLe = False
                    else:
                        print('<'+str(tokenList[token][1])+','+str(tokenList[token][2])+'> Error sintactico: se encontro: "'+tokenList[token][0]+'"; se esperaba: "identificador".')
                        flag = False
                        flagLe = False
        
        if state == 6:
            flag2 = True
            while flag2: 
                if tokenList[token][0] == 'token_pyc':
                    flag2=False
                    token = token +1
                    state = 3
                elif tokenList[token][0] == 'token_entero' or tokenList[token][0] == 'token_real' or tokenList[token][0] == 'identificador' or tokenList[token][0] == 'token_menos' or tokenList[token][0] == 'token_par_izq':
                    b= False
                    c = False
                    d = token
                    flag3= True
                    
                    while flag3:   
                        for key in keywords:
                            if tokenList[d][0] == key:
                                flag3 = False
                        if d> len(tokenList):
                            d= len(tokenList)
                            flag3 = False
                        d=d+1
                    
                    for i in range(token, d):
                        if tokenList[i][0] == 'token_coma':
                            b = True
                            break
                        if tokenList[i][0] == 'token_pyc':
                            c = True
                            break
                    
                    if b:
                        res = verifyEx('token_coma', token)
                        token = res[0]+1
                        flag = res[1] 
                    elif c:
                        res = verifyEx('token_pyc', token)
                        token = res[0]
                        flag = res[1]
                    else:
                        res = verifyEx('token_pyc', token)
                        token = res[0]
                        flag = res[1]
                        flag2 = False
                elif tokenList[token][0] == 'token_cadena' or tokenList[token][0] == 'verdadero' or tokenList[token][0] == 'falso':
                    if tokenList[token+1][0] == 'token_coma' or tokenList[token+1][0] == 'token_pyc':
                        if tokenList[token+1][0] == 'token_pyc':
                            token = token + 2
                            flag2 = False
                            state = 3
                        else:
                            token = token + 2
                    else:
                        try: 
                            a = tokens[tokenList[token+1][0]]
                            answer = True
                        except KeyError:
                            answer = False
                        if answer: 
                            print('<'+str(tokenList[token+1][1])+','+str(tokenList[token+1][2])+'> Error sintactico: se encontro: "'+a+'"; se esperaba: ",", ";".')
                            flag = False
                            flag2 = False
                        else:
                            print('<'+str(tokenList[token+1][1])+','+str(tokenList[token+1][2])+'> Error sintactico: se encontro: "'+tokenList[token+1][0]+'"; se esperaba: ",", ";".')
                            flag = False 
                            flag2 = False
                else:
                    try: 
                        a = tokens[tokenList[token+1][0]]
                        answer = True
                    except KeyError:
                        answer = False
                    if answer: 
                        print('<'+str(tokenList[token+1][1])+','+str(tokenList[token+1][2])+'> Error sintactico: se encontro: "'+a+'"; se esperaba: "falso", "identificador", "valor_cadena", "valor_entero", "-", "(", "valor_real", "verdadero".')
                        flag = False
                        flag2 = False
                    else:
                        print('<'+str(tokenList[token+1][1])+','+str(tokenList[token+1][2])+'> Error sintactico: se encontro: "'+tokenList[token+1][0]+'"; se esperaba: "falso", "identificador", "valor_cadena", "valor_entero", "-", "(", "valor_real", "verdadero".')
                        flag = False  
                        flag2 = False
         
        if state == 7:
            if tokenList[token][0]== 'token_asig':
                if tokenList[token+1][0] == 'token_entero' or tokenList[token+1][0] == 'token_real' or tokenList[token+1][0] == 'identificador' or tokenList[token+1][0] == 'token_menos' or tokenList[token+1][0] == 'token_par_izq':
                    res = verifyEx('token_pyc', token+1)
                    token = res[0]+1
                    flag = res[1]
                    state = 3
                elif tokenList[token+1][0] == 'token_cadena' or tokenList[token+1][0] == 'verdadero' or tokenList[token+1][0] == 'falso':
                    if tokenList[token+2][0] == 'token_pyc':
                        token = token +3
                        state = 3
                    else:
                        try: 
                            a = tokens[tokenList[token+2][0]]
                            answer = True
                        except KeyError:
                            answer = False
                        if answer: 
                            print('<'+str(tokenList[token+2][1])+','+str(tokenList[token+2][2])+'> Error sintactico: se encontro: "'+a+'"; se esperaba: ";".')
                            flag = False
                        else:
                            print('<'+str(tokenList[token+2][1])+','+str(tokenList[token+2][2])+'> Error sintactico: se encontro: "'+tokenList[token+2][0]+'"; se esperaba: ";".')
                            flag = False 
                else: 
                    try: 
                        a = tokens[tokenList[token+1][0]]
                        answer = True

                    except KeyError:
                        answer = False
                    if answer: 
                        print('<'+str(tokenList[token+1][1])+','+str(tokenList[token+1][2])+'> Error sintactico: se encontro: "'+a+'"; se esperaba: "falso", "identificador", "valor_cadena", "valor_entero", "-", "(", "valor_real", "verdadero".')
                        flag = False
                    else:
                        print('<'+str(tokenList[token+1][1])+','+str(tokenList[token+1][2])+'> Error sintactico: se encontro: "'+tokenList[token+1][0]+'"; se esperaba: "falso", "identificador", "valor_cadena", "valor_entero", "-", "(", "valor_real", "verdadero".')
                        flag = False 
            elif tokenList[token][0]== 'token_par_izq':  
                res = verifyFun(token+1) 
                token = res[0]+1
                flag= res[1]
                if tokenList[token][0] == 'token_pyc':
                    state =3
                    token = token+1
                else: 
                    try: 
                        a = tokens[tokenList[token][0]]
                        answer = True

                    except KeyError:
                        answer = False
                    if answer: 
                        print('<'+str(tokenList[token][1])+','+str(tokenList[token][2])+'> Error sintactico: se encontro: "'+a+'"; se esperaba: ";".')
                        flag = False
                    else:
                        print('<'+str(tokenList[token][1])+','+str(tokenList[token][2])+'> Error sintactico: se encontro: "'+tokenList[token][0]+'"; se esperaba: ";".')
                        flag = False
            else:
                try: 
                    a = tokens[tokenList[token][0]]
                    answer = True

                except KeyError:
                    answer = False
                if answer: 
                    print('<'+str(tokenList[token][1])+','+str(tokenList[token][2])+'> Error sintactico: se encontro: "'+a+'"; se esperaba: "<-", "(".')
                    flag = False
                else:
                    print('<'+str(tokenList[token][1])+','+str(tokenList[token][2])+'> Error sintactico: se encontro: "'+tokenList[token][0]+'"; se esperaba: "<-", "(".')
                    flag = False

        if state == 9:    
            if tokenList[token][0]== 'token_asig':
                if tokenList[token+1][0] == 'identificador':
                    if tokenList[token+2][0] == 'token_par_izq':
                        flagsub = True
                        token = token +3
                        while flagsub:
                            if tokenList[token][0] == 'identificador':
                                if tokenList[token+1][0] == 'token_coma':
                                    token = token + 2
                                elif tokenList[token+1][0] == 'token_par_der':
                                    token = token + 2
                                    state = 3
                                    flagsub =False
                                else:
                                    try: 
                                        a = tokens[tokenList[token+1][0]]
                                        answer = True

                                    except KeyError:
                                        answer = False
                                    if answer: 
                                        print('<'+str(tokenList[token+1][1])+','+str(tokenList[token+1][2])+'> Error sintactico: se encontro: "'+a+'"; se esperaba: ",", ")".')
                                        print('error')
                                        flag = False
                                        flagsub = False
                                    else:
                                        print('<'+str(tokenList[token+1][1])+','+str(tokenList[token+1][2])+'> Error sintactico: se encontro: "'+tokenList[token+1][0]+'"; se esperaba: ",", ")".')
                                        flag = False
                                        flagsub = False
                            else:
                                try: 
                                    a = tokens[tokenList[token][0]]
                                    answer = True

                                except KeyError:
                                    answer = False
                                if answer: 
                                    print('<'+str(tokenList[token][1])+','+str(tokenList[token][2])+'> Error sintactico: se encontro: "'+a+'"; se esperaba: "identificador".')
                                    flag = False
                                    flagsub = False
                                else:
                                    print('<'+str(tokenList[token][1])+','+str(tokenList[token][2])+'> Error sintactico: se encontro: "'+tokenList[token][0]+'"; se esperaba: "identificador".')
                                    flag = False
                                    flagsub = False
                    else:
                        try: 
                            a = tokens[tokenList[token+2][0]]
                            answer = True

                        except KeyError:
                            answer = False
                        if answer: 
                            print('<'+str(tokenList[token+2][1])+','+str(tokenList[token+2][2])+'> Error sintactico: se encontro: "'+a+'"; se esperaba: "(".')
                            flag = False
                        else:
                            print('<'+str(tokenList[token+2][1])+','+str(tokenList[token+2][2])+'> Error sintactico: se encontro: "'+tokenList[token+2][0]+'"; se esperaba: "(".')
                            flag = False    
                else:
                    try: 
                        a = tokens[tokenList[token+1][0]]
                        answer = True

                    except KeyError:
                        answer = False
                    if answer: 
                        print('<'+str(tokenList[token+1][1])+','+str(tokenList[token+1][2])+'> Error sintactico: se encontro: "'+a+'"; se esperaba: "identificador".')
                        flag = False
                    else:
                        print('<'+str(tokenList[token+1][1])+','+str(tokenList[token+1][2])+'> Error sintactico: se encontro: "'+tokenList[token+1][0]+'"; se esperaba: "identificador".')
                        flag = False
            else:
                token = token +1
                state = 3
        
        if state == 12:
            if tokenList[token][0] == 'identificador':
                if tokenList[token+1][0] == 'token_cor_izq':
                    flagDef = True
                    token = token + 2
                    while flagDef:
                        if tokenList[token][0] == 'token_entero' or tokenList[token][0] == 'token_real' or tokenList[token][0] == 'identificador':
                            if tokenList[token+1][0] == 'token_coma':
                                token = token +2
                            elif tokenList[token+1][0] == 'token_cor_der':
                                if tokenList[token+2][0] == 'token_pyc':
                                    token = token+3
                                    flagDef = False 
                                    state = 3
                                elif tokenList[token+2][0] == 'token_coma':
                                    token = token+3
                                    flagDef = False 
                                    state = 12
                                else: 
                                    try: 
                                        a = tokens[tokenList[token][0]]
                                        answer = True

                                    except KeyError:
                                        answer = False
                                    if answer: 
                                        print('<'+str(tokenList[token+2][1])+','+str(tokenList[token+2][2])+'> Error sintactico: se encontro: "'+a+'"; se esperaba: ",", ";".')
                                        flag = False
                                        flagDef = False
                                    else:
                                        print('<'+str(tokenList[token+2][1])+','+str(tokenList[token+2][2])+'> Error sintactico: se encontro: "'+tokenList[token+2][0]+'"; se esperaba: ",", ";".')
                                        flag = False
                                        flagDef = False        
                            elif tokenList[token+1][0] == 'token_mas' or tokenList[token+1][0] == 'token_menos' or tokenList[token+1][0] == 'token_div' or tokenList[token+1][0] == 'token_mul' or tokenList[token+1][0] == 'token_mod' or tokenList[token+1][0] == 'token_pot':
                                state = 13
                                flagDef = False
                                
                            else: 
                                try: 
                                    a = tokens[tokenList[token][0]]
                                    answer = True

                                except KeyError:
                                    answer = False
                                if answer: 
                                    print('<'+str(tokenList[token+1][1])+','+str(tokenList[token+1][2])+'> Error sintactico: se encontro: "'+a+'"; se esperaba: ",", "[".')
                                    flag = False
                                    flagDef = False
                                else:
                                    print('<'+str(tokenList[token+1][1])+','+str(tokenList[token+1][2])+'> Error sintactico: se encontro: "'+tokenList[token+1][0]+'"; se esperaba: ",", "[".')
                                    flag = False
                                    flagDef = False
                        else: 
                            
                            try: 
                                a = tokens[tokenList[token][0]]
                                answer = True
                            except KeyError:
                                answer = False
                            if answer: 
                                print('<'+str(tokenList[token][1])+','+str(tokenList[token][2])+'> Error sintactico: se encontro: "'+a+'"; se esperaba: "identificador", "valor_entero", "valor_real".')
                                flag = False
                                flagDef = False
                            else:
                                print('<'+str(tokenList[token][1])+','+str(tokenList[token][2])+'> Error sintactico: se encontro: "'+tokenList[token][0]+'"; se esperaba: "identificador", "valor_entero", "valor_real".')
                                flag = False
                                flagDef = False         
                else:
                    try: 
                        a = tokens[tokenList[token][0]]
                        answer = True

                    except KeyError:
                        answer = False
                    if answer: 
                        print('<'+str(tokenList[token+1][1])+','+str(tokenList[token+1][2])+'> Error sintactico: se encontro: "'+a+'"; se esperaba: "[".')
                        flag = False
                    else:
                        print('<'+str(tokenList[token+1][1])+','+str(tokenList[token+1][2])+'> Error sintactico: se encontro: "'+tokenList[token+1][0]+'"; se esperaba: "[".')
                        flag = False
            else: 
                try: 
                    a = tokens[tokenList[token][0]]
                    answer = True
                except KeyError:
                    answer = False
                if answer: 
                    print('<'+str(tokenList[token][1])+','+str(tokenList[token][2])+'> Error sintactico: se encontro: "'+a+'"; se esperaba: "identificador".')
                    flag = False
                else:
                    print('<'+str(tokenList[token][1])+','+str(tokenList[token][2])+'> Error sintactico: se encontro: "'+tokenList[token][0]+'"; se esperaba: "identificador".')
                    flag = False
        
        if state ==13:
            flag2 = True
            while flag2:
                if tokenList[token][0] == 'token_coma':
                    flag2 = False
                    token = token +1
                elif tokenList[token][0] == 'token_cor_der':
                    if tokenList[token+1][0] == 'token_pyc':
                        token = token+2
                        flag2 = False 
                        state = 3
                    elif tokenList[token+1][0] == 'token_coma':
                        token = token+2
                        flag2 = False 
                        state = 12
                elif tokenList[token][0] == 'token_entero' or tokenList[token][0] == 'token_real' or tokenList[token][0] == 'identificador':
                    if tokenList[token+1][0] == 'token_mas' or tokenList[token+1][0] == 'token_menos' or tokenList[token+1][0] == 'token_div' or tokenList[token+1][0] == 'token_mul' or tokenList[token+1][0] == 'token_mod' or tokenList[token+1][0] == 'token_pot': 
                        if tokenList[token+2][0] == 'token_mas' or tokenList[token+2][0] == 'token_menos' or tokenList[token+2][0] == 'token_div' or tokenList[token+2][0] == 'token_mul' or tokenList[token+2][0] == 'token_mod' or tokenList[token+2][0] == 'token_pot':
                            print('<'+str(tokenList[token+2][1])+','+str(tokenList[token+2][2])+'> Error sintactico: se encontro: "'+token[tokenList[token+2][0]]+'"; se esperaba: "falso", "identificador", "valor_cadena", "valor_entero", "(", "valor_real", "verdadero".')
                            flag = False
                            flag2 = False 
                        else: 
                            token = token + 2 
                    elif tokenList[token+1][0] == 'token_par_der':
                        if tokenList[token+2][0] == 'token_mas' or tokenList[token+2][0] == 'token_menos' or tokenList[token+2][0] == 'token_div' or tokenList[token+2][0] == 'token_mul' or tokenList[token+2][0] == 'token_mod' or tokenList[token+2][0] == 'token_pot':
                            if tokenList[token+3][0] == 'token_mas' or tokenList[token+3][0] == 'token_menos' or tokenList[token+3][0] == 'token_div' or tokenList[token+3][0] == 'token_mul' or tokenList[token+3][0] == 'token_mod' or tokenList[token+3][0] == 'token_pot':
                                print('<'+str(tokenList[token+3][1])+','+str(tokenList[token+3][2])+'> Error sintactico: se encontro: "'+token[tokenList[token+3][0]]+'"; se esperaba: "falso", "identificador", "valor_cadena", "valor_entero", "(", "valor_real", "verdadero".')
                                flag = False
                                flag2 = False 
                            else: 
                                token = token + 3 
                        
                        elif tokenList[token+2][0] == 'token_coma':
                            flag2 = False
                            token = token +3
                        elif tokenList[token+2][0] == 'token_cor_der':
                            if tokenList[token+3][0] == 'token_pyc':
                                token = token+4
                                flag2 = False 
                                state = 3
                            elif tokenList[token+3][0] == 'token_coma':
                                token = token+4
                                flag2 = False 
                                state = 12
                        else:
                            try: 
                                a = tokens[tokenList[token+2][0]]
                                answer = True

                            except KeyError:
                                answer = False
                            if answer: 
                                print('<'+str(tokenList[token+2][1])+','+str(tokenList[token+2][2])+'> Error sintactico: se encontro: "'+a+'"; se esperaba: "/", "+", "-", "%", "*", "^".')
                                flag = False
                                flag2 = False
                            else:
                                print('<'+str(tokenList[token+2][1])+','+str(tokenList[token+2][2])+'> Error sintactico: se encontro: "'+tokenList[token+2][0]+'"; se esperaba: "/", "+", "-", "%", "*", "^".')
                                flag = False
                                flag2 = False
                    elif tokenList[token+1][0] == 'token_coma':
                            flag2 = False
                            token = token + 2
                    elif tokenList[token+1][0] == 'token_cor_der':
                        if tokenList[token+2][0] == 'token_pyc':
                            token = token+3
                            flag2 = False 
                            state = 3
                        elif tokenList[token+2][0] == 'token_coma':
                            token = token+3
                            flag2 = False 
                            state = 12
                    else:
                        try: 
                            a = tokens[tokenList[token+1][0]]
                            answer = True

                        except KeyError:
                            answer = False
                        if answer: 
                            print('<'+str(tokenList[token+1][1])+','+str(tokenList[token+1][2])+'> Error sintactico: se encontro: "'+a+'"; se esperaba: "/", "+", "-", "%", "*", ")", "^".')
                            flag = False
                            flag2 = False 
                        else:
                            print('<'+str(tokenList[token+1][1])+','+str(tokenList[token+1][2])+'> Error sintactico: se encontro: "'+tokenList[token][0]+'"; se esperaba: "/", "+", "-", "%", "*", ")", "^".')
                            flag = False
                            flag2 = False 
                        
                elif tokenList[token][0] == 'token_par_izq' or tokenList[token][0] == 'token_menos':
                    if tokenList[token+1][0] == 'identificador' or tokenList[token+1][0] == 'token_entero' or tokenList[token+1][0] == 'token_real':
                        token = token + 1
                    else:
                        try: 
                            a = tokens[tokenList[token+1][0]]
                            answer = True

                        except KeyError:
                            answer = False
                        if answer: 
                            print('<'+str(tokenList[token+1][1])+','+str(tokenList[token+1][2])+'> Error sintactico: se encontro: "'+a+'"; se esperaba:"identificador", "valor_entero", "valor_real".')
                            flag = False
                            flag2 = False 
                        else:
                            print('<'+str(tokenList[token+1][1])+','+str(tokenList[token+1][2])+'> Error sintactico: se encontro: "'+tokenList[token][0]+'"; se esperaba:"identificador", "valor_entero", "valor_real".')
                            flag = False
                            flag2 = False  
                else:
                    try: 
                        a = tokens[tokenList[token][0]]
                        answer = True

                    except KeyError:
                        answer = False
                    if answer: 
                        print('<'+str(tokenList[token][1])+','+str(tokenList[token][2])+'> Error sintactico: se encontro: "'+a+'"; se esperaba: "falso", "identificador", "valor_cadena", "valor_entero", "-", "(", "valor_real", "verdadero".')
                        flag = False
                        flag2 = False 
                    else:
                        print('<'+str(tokenList[token][1])+','+str(tokenList[token][2])+'> Error sintactico: se encontro: "'+tokenList[token][0]+'"; se esperaba: "falso", "identificador", "valor_cadena", "valor_entero", "-", "(", "valor_real", "verdadero".')
                        flag = False
                        flag2 = False            
        
        if state ==14:
            if tokenList[token][0] == 'token_par_izq': 
                if tokenList[token+1][0] == 'identificador':
                    if tokenList[token+2][0] == 'token_dif' or tokenList[token+1][0] == 'token_mayor' or tokenList[token+1][0] == 'token_mayor_igual' or tokenList[token+1][0] == 'token_menor' or tokenList[token+1][0] == 'token_menor_igual' or tokenList[token+1][0] == 'token_igual':
                        if tokenList[token+3][0] == 'identificador':
                            if tokenList[token+4][0] == 'token_par_izq':
                                if tokenList[token+5][0] == 'entonces':
                                    state = 3
                                    token = token +6
                                else: 
                                    try: 
                                        a = tokens[tokenList[token+5][0]]
                                        answer = True

                                    except KeyError:
                                        answer = False
                                    if answer: 
                                        print('<'+str(tokenList[token+5][1])+','+str(tokenList[token+5][2])+'> Error sintactico: se encontro: "'+a+'"; se esperaba: "entonces".')
                                        flag = False
                                    else:
                                        print('<'+str(tokenList[token+5][1])+','+str(tokenList[token+5][2])+'> Error sintactico: se encontro: "'+tokenList[token+5][0]+'"; se esperaba: "entonces".')
                                        flag = False
                            else:
                                try: 
                                    a = tokens[tokenList[token+4][0]]
                                    answer = True

                                except KeyError:
                                    answer = False
                                if answer: 
                                    print('<'+str(tokenList[token+4][1])+','+str(tokenList[token+4][2])+'> Error sintactico: se encontro: "'+a+'"; se esperaba: ")".')
                                    flag = False
                                else:
                                    print('<'+str(tokenList[token+4][1])+','+str(tokenList[token+4][2])+'> Error sintactico: se encontro: "'+tokenList[token+4][0]+'"; se esperaba: ")".')
                                    flag = False
                        else: 
                            try: 
                                a = tokens[tokenList[token+3][0]]
                                answer = True

                            except KeyError:
                                answer = False
                            if answer: 
                                print('<'+str(tokenList[token+3][1])+','+str(tokenList[token+3][2])+'> Error sintactico: se encontro: "'+a+'"; se esperaba: "identificador".')
                                flag = False
                            else:
                                print('<'+str(tokenList[token+3][1])+','+str(tokenList[token+3][2])+'> Error sintactico: se encontro: "'+tokenList[token+3][0]+'"; se esperaba: "identificador".')
                                flag = False
                    else: 
                        try: 
                            a = tokens[tokenList[token+2][0]]
                            answer = True

                        except KeyError:
                            answer = False
                        if answer: 
                            print('<'+str(tokenList[token+2][1])+','+str(tokenList[token+2][2])+'> Error sintactico: se encontro: "'+a+'"; se esperaba: "<>", "=", ">", ">=", "<", "<=".')
                            flag = False
                        else:
                            print('<'+str(tokenList[token+2][1])+','+str(tokenList[token+2][2])+'> Error sintactico: se encontro: "'+tokenList[token+2][0]+'"; se esperaba: "<>", "=", ">", ">=", "<", "<=".')
                            flag = False
                else: 
                    try: 
                        a = tokens[tokenList[token+1][0]]
                        answer = True

                    except KeyError:
                        answer = False
                    if answer: 
                        print('<'+str(tokenList[token+1][1])+','+str(tokenList[token+1][2])+'> Error sintactico: se encontro: "'+a+'"; se esperaba: "identificador".')
                        flag = False
                    else:
                        print('<'+str(tokenList[token+1][1])+','+str(tokenList[token+1][2])+'> Error sintactico: se encontro: "'+tokenList[token+1][0]+'"; se esperaba: "identificador".')
                        flag = False
            elif tokenList[token][0] == 'identificador':
                if tokenList[token+1][0] == 'token_dif' or tokenList[token+1][0] == 'token_mayor' or tokenList[token+1][0] == 'token_mayor_igual' or tokenList[token+1][0] == 'token_menor' or tokenList[token+1][0] == 'token_menor_igual' or tokenList[token+1][0] == 'token_igual':
                    if tokenList[token+2][0] == 'identificador':
                        if tokenList[token+3][0] == 'entonces':
                            state = 3
                            token = token +4
                        else: 
                            try: 
                                a = tokens[tokenList[token+3][0]]
                                answer = True

                            except KeyError:
                                answer = False
                            if answer: 
                                print('<'+str(tokenList[token+3][1])+','+str(tokenList[token+3][2])+'> Error sintactico: se encontro: "'+a+'"; se esperaba: "entonces".')
                                flag = False
                            else:
                                print('<'+str(tokenList[token+3][1])+','+str(tokenList[token+3][2])+'> Error sintactico: se encontro: "'+tokenList[token+3][0]+'"; se esperaba: "entonces".')
                                flag = False
                    else: 
                        try: 
                            a = tokens[tokenList[token+2][0]]
                            answer = True

                        except KeyError:
                            answer = False
                        if answer: 
                            print('<'+str(tokenList[token+2][1])+','+str(tokenList[token+2][2])+'> Error sintactico: se encontro: "'+a+'"; se esperaba: "identificador".')
                            flag = False
                        else:
                            print('<'+str(tokenList[token+2][1])+','+str(tokenList[token+2][2])+'> Error sintactico: se encontro: "'+tokenList[token+2][0]+'"; se esperaba: "identificador".')
                            flag = False
                else: 
                    try: 
                        a = tokens[tokenList[token+1][0]]
                        answer = True

                    except KeyError:
                        answer = False
                    if answer: 
                        print('<'+str(tokenList[token+1][1])+','+str(tokenList[token+1][2])+'> Error sintactico: se encontro: "'+a+'"; se esperaba: "<>", "=", ">", ">=", "<", "<=".')
                        flag = False
                    else:
                        print('<'+str(tokenList[token+1][1])+','+str(tokenList[token+1][2])+'> Error sintactico: se encontro: "'+tokenList[token+1][0]+'"; se esperaba: "<>", "=", ">", ">=", "<", "<=".')
                        flag = False
            else:
                try: 
                    a = tokens[tokenList[token][0]]
                    answer = True

                except KeyError:
                    answer = False
                if answer: 
                    print('<'+str(tokenList[token][1])+','+str(tokenList[token][2])+'> Error sintactico: se encontro: "'+a+'"; se esperaba: "identificador", "(".')
                    flag = False
                else:
                    print('<'+str(tokenList[token][1])+','+str(tokenList[token][2])+'> Error sintactico: se encontro: "'+tokenList[token][0]+'"; se esperaba: "identificador", "(".')
                    flag = False

        if state ==15:
            if tokenList[token][0] == 'identificador':
                if tokenList[token+1][0] == 'token_asig':
                    state = 16
                    token= token +2 
                    res = verifyEx('hasta', token)
                    token = res[0]
                    flag = res[1]
                    
                    if flag:
                        b= False
                        c = False
                        d = token
                        flag3= True
                        
                        while flag3:   
                            for exp in exepciones1:
                                if tokenList[d][0] == exp:
                                    flag3 = False
                            if d> len(tokenList):
                                d= len(tokenList)
                                flag3 = False
                            d=d+1
                                
                        
                        for i in range(token+1, d):
                            if tokenList[i][0] == 'hacer':
                                b = True
                                break
                            if tokenList[i][0] == 'con':
                                c = True
                                break
                            
                        if b:
                            res = verifyEx('hacer', token+1)
                            token = res[0]+1
                            flag = res[1]
                            state = 3
                        elif c:
                            res = verifyEx('con', token+1)
                            token = res[0]
                            flag = res[1]
                                    
                            if flag:
                                if tokenList[token+1][0] == 'paso': 
                                    res = verifyEx('hacer', token+2)
                                    token = res[0]+1
                                    flag = res[1]
                                    state = 3
                        else:
                            res = verifyEx('hacer", "con', token+1)
                            token = res[0]
                            flag = res[1]    
                else:
                    try: 
                        a = tokens[tokenList[token][0]]
                        answer = True

                    except KeyError:
                        answer = False
                    if answer: 
                        print('<'+str(tokenList[token+1][1])+','+str(tokenList[token+1][2])+'> Error sintactico: se encontro: "'+a+'"; se esperaba: "<-".')
                        flag = False
                    else:
                        print('<'+str(tokenList[token+1][1])+','+str(tokenList[token+1][2])+'> Error sintactico: se encontro: "'+tokenList[token+1][0]+'"; se esperaba: "<-".')
                        flag = False
            else:
                try: 
                    a = tokens[tokenList[token][0]]
                    answer = True

                except KeyError:
                    answer = False
                if answer: 
                    print('<'+str(tokenList[token][1])+','+str(tokenList[token][2])+'> Error sintactico: se encontro: "'+a+'"; se esperaba: "identificador".')
                    flag = False
                else:
                    print('<'+str(tokenList[token][1])+','+str(tokenList[token][2])+'> Error sintactico: se encontro: "'+tokenList[token][0]+'"; se esperaba: "identificador".')
                    flag = False
        
        if state == 16:
            flag2 = True
            while flag2: 
                if tokenList[token][0] == 'token_entero' or tokenList[token][0] == 'token_real' or tokenList[token][0] == 'identificador' or tokenList[token][0] == 'token_menos' or tokenList[token][0] == 'token_par_izq':
                    d = token
                    compa = ''
                    falg3 = True
                    while falg3:
                        if d < len(tokenList): 
                            for com in comparacion:
                                if tokenList[d][0] == com:
                                    compa = com
                                    falg3=False
                                    break
                                elif tokenList[d][0] == 'hacer':
                                    compa = 'hacer'
                                    falg3=False
                                    break
                            
                            d=d+1
                    if compa != '':
                        res = verifyEx(compa, token)
                        token = res[0]+1
                        flag = res[1]
                        if compa == 'hacer':
                            state = 3
                            flag2 = False
                    else:
                        verifyEx1 (token) 
                        token = res[0]
                        flag = res[1]
                        flag2 = False
                elif tokenList[token][0] == 'token_cadena' or tokenList[token][0] == 'verdadero' or tokenList[token][0] == 'falso':
                    
                    si = False
                    for com in comparacion:
                        if tokenList[token+1][0] == com:
                            si = True
                            break 
                    
                    if si:
                        token = token +1
                    else:
                        if tokenList[token+1][0] == 'hacer':
                            state = 3
                            flag2 = False 
                            token = token +2
                        else: 
                            try: 
                                a = tokens[tokenList[token+1][0]]
                                answer = True
                            except KeyError:
                                answer = False
                            if answer: 
                                print('<'+str(tokenList[token+1][1])+','+str(tokenList[token+1][2])+'> Error sintactico: se encontro: "hacer", "<>", "=", ">", ">=", "<", "<=".')
                                flag = False
                                flag2 = False
                            else:
                                print('<'+str(tokenList[token+1][1])+','+str(tokenList[token+1][2])+'> Error sintactico: se encontro: "hacer", "<>", "=", ">", ">=", "<", "<=".')
                                flag = False 
                                flag2 = False
                else:
                    try: 
                        a = tokens[tokenList[token][0]]
                        answer = True
                    except KeyError:
                        answer = False
                    if answer: 
                        print('<'+str(tokenList[token][1])+','+str(tokenList[token][2])+'> Error sintactico: se encontro: "falso", "identificador", "valor_cadena", "valor_entero", "-", "(", "valor_real", "verdadero".')
                        flag = False
                        flag2 = False
                    else:
                        print('<'+str(tokenList[token][1])+','+str(tokenList[token][2])+'> Error sintactico: se encontro: "falso", "identificador", "valor_cadena", "valor_entero", "-", "(", "valor_real", "verdadero"..')
                        flag = False 
                        flag2 = False
            
        if state == 17:
            if tokenList[token][0] == 'token_entero' or tokenList[token][0] == 'token_real' or tokenList[token][0] == 'identificador' or tokenList[token][0] == 'token_menos' or tokenList[token][0] == 'token_par_izq':
                res = verifyEx('hacer', token)
                token = res[0]+1
                flag = res[1] 
                state = 3            
            else: 
                try: 
                    a = tokens[tokenList[token][0]]
                    answer = True
                except KeyError:
                    answer = False
                if answer: 
                    print('<'+str(tokenList[token][1])+','+str(tokenList[token][2])+'> Error sintactico: se encontro: "identificador", "valor_entero", "-", "(", "valor_real".')
                    flag = False
                else:
                    print('<'+str(tokenList[token][1])+','+str(tokenList[token][2])+'> Error sintactico: se encontro: "identificador", "valor_entero", "-", "(", "valor_real".')
                    flag = False  
        
        if state ==18: 
            if tokenList[token][0] == 'token_entero' or tokenList[token][0] == 'token_real' or tokenList[token][0] == 'identificador' or tokenList[token][0] == 'token_menos' or tokenList[token][0] == 'token_par_izq':
                res = verifyEx('token_dosp', token)
                token = res[0]+1
                flag = res[1] 
                state = 3            
            else: 
                try: 
                    a = tokens[tokenList[token][0]]
                    answer = True
                except KeyError:
                    answer = False
                if answer: 
                    print('<'+str(tokenList[token][1])+','+str(tokenList[token][2])+'> Error sintactico: se encontro: "identificador", "valor_entero", "-", "(", "valor_real".')
                    flag = False
                else:
                    print('<'+str(tokenList[token][1])+','+str(tokenList[token][2])+'> Error sintactico: se encontro: "identificador", "valor_entero", "-", "(", "valor_real".')
                    flag = False       
                
                        
 
grammar()

