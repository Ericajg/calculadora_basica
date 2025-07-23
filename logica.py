

digito=''  # variable global para almacenar los digitos ingresados
#---------funcion-----
def tomar_digito(n):
    global digito
    digito += str(n)
    calculo.set(digito)
    
def resultado():
    try:
        global digito
        total = str(eval(digito))
        calculo.set(total)
        digito = ''
    except:
        calculo.set('**ERROR**')

def limpiar_completo():
    global digito
    calculo.set('')
    digito = ''
