import matplotlib.pyplot as plt
from random import randrange
from datetime import timedelta
from datetime import datetime

#Función de fecha y tiempo
def random_date(start, end):
    delta = end - start
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = randrange(int_delta)
    return start + timedelta(seconds=random_second)
d1 = datetime.strptime('1/1/2021 1:30 PM', '%m/%d/%Y %I:%M %p')
d2 = datetime.strptime('12/31/2021 4:50 AM', '%m/%d/%Y %I:%M %p')

print(random_date(d1, d2))

# función para introducir todos los datos
def introducir_inputs(x, y, z):
  print(f'\nGastos {z}:\n')
  a = 0
  while a in range(len(x)):
    keys = x[a]
    values = input(f'Por favor, introduzca el gasto mensual de {x[a]}: ')
    try:
      float(values)
    except:
      print('\nIntroduce un dato válido, vuelve a intentarlo')
      continue
    else:
      values = float(values)
      a +=1
    y[keys] = values 

# función para crear las gráficas
def make_pie(w, x, y, z):
  print('\n')
  explode = (0.05, 0.05, 0.05, 0.05)
  colors = ['#00FFFF','#BFFF00','#FFD700','#eb6123']
  fig = plt.figure()
  ax1 = fig.add_axes([0, 0, .5, .5], aspect=2)
  ax1.pie(x, labels=y, radius = 1.3, colors=colors, autopct='%1.1f%%', textprops={'fontsize': 10}, explode = explode)
  ax2 = fig.add_axes([1, .0, .5, .5], aspect=2)
  ax2.pie(z, labels=y, radius = 1.3, colors= colors, autopct='%1.1f%%', textprops={'fontsize': 10}, explode = explode)
  ax1.set_title(f'Gastos {w}', fontsize=18, pad=32)
  ax2.set_title('Gastos medios', fontsize=18, pad=32)
  plt.show()

# función para crear las gráficas totales
def big_pie(w, x, y, z):
  print('\n\n\n')
  explode = (0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2)
  colors = ['#FF0000', '#4169E1', '#00FF7F', '#FFFF00', '#9ACD32', '#FF00FF', '#00FF00', '#FFFAF0', '#FF8C00', '#9b9b9b', '#DC143C', '#0000FF']
  fig = plt.figure()
  ax1 = fig.add_axes([0, 0, .5, .5], aspect=2)
  ax1.pie(x, labels=y, radius = 2, autopct='%1.1f%%', colors= colors, textprops={'fontsize': 10}, explode = explode)
  ax2 = fig.add_axes([1.5, .0, .5, .5], aspect=2)
  ax2.pie(z, labels=y, radius = 2, autopct='%1.1f%%', colors= colors, textprops={'fontsize': 10}, explode = explode)
  ax1.set_title(f'Gastos {w}', fontsize=28, pad=80)
  ax2.set_title('Gastos medios', fontsize=28, pad=80)
  plt.show()
def ahorro(a,b,c,d):
    count = 0
    for i in range(len(a)):
        if a[i] <= b[i]:
            count += 1
    if count >= 10:
        print("Usted es considerada una persona ahorrativa. Por ende, ingrese un consejo para los otros usuarios, por favor")
        name = "consejo del usuario" + str(d)
        c[name]=input("Inserte un consejo a compartir: ")
    else:
        print("Lo sentimos, usted no cumple los requisitos para ser considerada ahorrativa. Por ende, no puede agregar un consejo para los otros usuarios; sin embargo, puede recibir un consejo de un profesional")
    

def comparacion(m,n,p):
  plt.plot(m, label="Media española")
  plt.plot(n,label ="Gasto del usuario")
  plt.legend()
  plt.xticks(range(0,12),["Ene","Feb","Mar","Abr","May","Jun","Jul","Ago","Set","Oct","Nov","Dic"])
  plt.title(p)
  plt.show()
  # para crear una grafica con los meses , la media española y el Gasto del usuario 



def guardar_datos(d,f,g):
  print("\nPara ",f,":")
  for i in g:
    print("Digite el gasto mensual en ",i,end="")
    d[i] = float(input(": "))

def make_plot_general(m,n,p):
  plt.plot(m, label="Duraderos")
  plt.plot(n,label ="Servicios")
  plt.plot(p,label ="Perecederos")
  plt.legend()
  plt.xticks(range(0,12),["Ene","Feb","Mar","Abr","May","Jun","Jul","Ago","Set","Oct","Nov","Dic"])
  plt.title()
  plt.show()
num = 1
while True:
  print("\tBIENVENID@ A WASTELESS")  
  print("¿Qué desea realizar hoy?\n\t1.Comparar tuss datos con graficas de sectores\n\t2.Guardar tus datos y compararlos con años anteriores ")
  choice = input("Elija una opción: ")
  if choice == "1":
# tupla datos media española mensuales 
    mediaDuraderos = (600, 97.5, 95.8, 25)
    mediaServicios = (83.3, 36.4, 108.3, 141.7)
    mediaPerecederos = (113.3, 150, 115.4, 42.5)
    mediaTotal = (600, 97.5, 95.8, 25, 83.3, 36.4, 108.3, 141.7, 113.3, 150, 115.4, 42.5)


# listas de las diferentes variables
    duraderos = ['hipoteca', 'muebles y mantenimiento del hogar', 'vehículos', 'material deportivo']
    servicios = ['sanidad', 'educación', 'transporte', 'ocio']
    perecederos = ['comida', 'agua, electricidad y gas', 'ropa', 'bebidas alcohólicas y/o tabaco']
    total = ['hipoteca', 'muebles y mantenimiento del hogar', 'vehículos', 'material deportivo','sanidad', 'educación', 'transporte', 'ocio','comida', 'agua, electricidad y gas', 'ropa', 'bebidas alcohólicas y/o tabaco']

# bienvenida app
    print('Para el correcto funcionamiento de esta aplicación, será necesario introducir datos personales, en concreto gastos en diferentes sectores')
    print('\n---------- IMPORTANTE: POR FAVOR, INTRODUCE LOS VALORES CON CARÁCTER MENSUAL ----------\n')

# diccionarios para las variables
    dictDuraderos = {}
    dictServicios = {}
    dictPerecederos = {}

# introducción todos inputs
    introducir_inputs(duraderos, dictDuraderos, 'duraderos')

    introducir_inputs(servicios, dictServicios, 'servicios')

    introducir_inputs(perecederos, dictPerecederos, 'perecederos')

# pasar de diccionario a lista / duraderos
    listaDuraderos = dictDuraderos.values()
    listaDuraderos = list(listaDuraderos)

# pasar de diccionario a lista / servicios
    listaServicios = dictServicios.values()
    listaServicios = list(listaServicios)

# pasar de diccionario a lista / perecederos
    listaPerecederos = dictPerecederos.values()
    listaPerecederos = list(listaPerecederos)
    listaTotal = listaDuraderos + listaServicios + listaPerecederos

# creación gráficas pastel
    make_pie('duraderos', listaDuraderos, duraderos, mediaDuraderos)

    make_pie('servicios', listaServicios, servicios, mediaServicios)

    make_pie('perecederos', listaPerecederos, perecederos, mediaPerecederos)

# gráfica pastel total
    big_pie('totales', listaTotal, total, mediaTotal)
  

#Porcentajes datos de la media española
    Total = 1546

# creación listas porcentajes de la media
    porcentajesD = []
    porcentajesS = [] 
    porcentajesP = []

# introducción porcentajes en las listas de la media española
    for i in mediaDuraderos:
        porcentajesD.append(round((i * 100) / Total,2))

    for i in mediaServicios:
        porcentajesS.append(round((i * 100) / Total,2))

    for i in mediaPerecederos:
        porcentajesP.append(round((i * 100) / Total,2))

# introducción porcentajes datos de la media de usuario
    ResultD = 0
    ResultS = 0
    ResultP = 0

    for i in listaDuraderos:
        ResultD += i

    for i in listaServicios:
        ResultS += i

    for i in listaPerecederos:
        ResultP += i

    UserResult = ResultP + ResultS + ResultD

    porcentajesDUser = []
    porcentajesSUser = []
    porcentajesPUser = []

    for i in listaDuraderos:
        porcentajesDUser.append(round((i * 100) / Total,2))

    for i in listaServicios:
        porcentajesSUser.append(round((i * 100) / Total,2))

    for i in listaPerecederos:
        porcentajesPUser.append(round((i * 100) / Total,2))

#A lista GastoQS se añaden por orden cada categoria, si supera la media se añade el porcentaje sino se añade un 0

    GastoQS = []

    for i in range(0, len(porcentajesDUser)):
        if porcentajesDUser[i]>porcentajesD[i]:
           GastoQS.append(porcentajesDUser[i])
        else:
           GastoQS.append(0)

    for i in range(0, len(porcentajesSUser)):
        if porcentajesSUser[i]>porcentajesS[i]:
            GastoQS.append(porcentajesSUser[i])
        else:
            GastoQS.append(0)
      
    for i in range(0, len(porcentajesPUser)):
        if porcentajesPUser[i]>porcentajesP[i]:
            GastoQS.append(porcentajesPUser[i])
        else:
            GastoQS.append(0)

#Añadimos los nombres de los campos que se han pasado de la media a listaQS e imprimimos dichos campos.

    listaQS = []
    aT = True
    for i in range(len(GastoQS)):
        if GastoQS[i] == 0:
           continue
        else:
           aT = False
           break
    if aT == True:
        print('No superas la media española en ningún sector.\n')
    else:
        print('Superas la media española en:\n')
        for i in range(len(GastoQS)):
            if GastoQS[i] != 0:
               listaQS.append(total[i])
            print(total[i])

# Diccionario con todos los consejos por categorias

    consejos = {'''hipoteca' : De  la mano de la gestión de Gibobs Allbanks, por ejemplo, se puede obtener un ahorro en el total de la hipoteca de más de 38.000€ gracias a sus asesores hipotecarios expertos en negociar por sus clientes con los bancos.

                'muebles y mantenimiento del hogar' : En Perfexya se ofrece un estupendo  servicio para la limpieza de domicilios,donde se llevan a cabo procedimientos de aseo y desinfección  profundos,los cuales pueden ser contratados por la periodicidad  que se ajuste a las necesidades y presupuesto,con resultados garantizados y duraderos.

                'vehículos' : El Fiat Tipo SW, por precio, tiene un aspecto moderno de diseño, el gran espacio del maletero y  su completo equipamiento, resulta ser una de las alternativas más económicas. La oferta mecánica se compone de una opción de gasolina (1.0 GSE de 100 CV) y dos de diésel (1.3 Multijet de 95 CV y el 1.6 Multijet con 130 CV.

                'material deportivo' : Outletic, un interesantísimo outlet online en el que puedes encontrar descuentos muy interesantes en todo lo que se refiere a material deportivo, con unos descuentos realmente interesantes, incluso de un 70.

                'sanidad' : El objetivo  para ahorrar en salud es encontrar la oferta que mejor se adapte a nuestras necesidades y nos resulte más económica. Debemos analizar todas las condiciones del seguro. Si actualmente no tienes un plan de salud y tienes preguntas, AltaMed está  para ayudar a orientarte de manera gratuita acerca de tus opciones.

                'educación' : Las becas escolares son una alternativa excelente.  Las notas van a contar mucho para la obtención de becas,  así que el esfuerzo de cada año cuenta.

                'transporte' : A la hora de utilizar el transporte público es estar bien informado sobre los bonos descuento existentes en esa ciudad y elegir el que mejor se adapte a tus  circunstancias. 

                'ocio' : Empresas como  Offerrum, eltenedor u Oferalia están llenas de propuestas de ocio de todo tipo con descuentos de hasta el 60% si eres capaz de adaptar los días en los que llevas a cabo determinadas actividades como cenar fuera de casa.

                'comida' : es conveniente tener en cuenta los catálogos de los supermercados y señalar las mejores ofertas, tambien seria recomendable guardar la comida que ha sobrado en un tupper y congelarla.

                'agua' :  la mayoría de ayuntamientos disponen de distintas tarifas sociales que te permiten, en caso de que cumplas ciertas condiciones, ahorrar en la factura del agua.

                'electricidad y gas' : Utilizar el calor residual y también ollas a presión que suponen un ahorro del 50%. Cambiar las bombillas convencionales por aquellas de bajo consumo.

                'ropa' : Aplicaciones como Vinted, vende ropa de segunda mano a un buen precio y calidad, no obstante, aprovecha las ofertas que salgan en las tiendas de ropa.

                'bebidas alcohólicas y/o tabaco' : Si lo que quieres es dejar estas adicciones para ahorrar más, la empresa Stopadicciones te puede ayudar a dejarlo.'''}
    print("\n")
    name = input("Digite un nombre de usuario: ")
    ahorro(listaTotal,list(mediaTotal),consejos,name)
# Pedimos al usuario en que quiere reducir gastos y le devolvemos los valores del diccionario
    fin = False
    while fin == False:
        quiereConsejo = input('\n¿Quieres un consejo para reducir gastos? (Si/No) ').title()
        if quiereConsejo == 'No':
            fin = True
            continue
        elif quiereConsejo == 'Si':
            sectorConsejos = input(f'\n¿En qué sector? {total} ')
        if sectorConsejos in consejos:
            print(f'\n{consejos[sectorConsejos]}')
        else:
            print('\nDato incorrecto, por lo que no se ofrecerán recomendaciones')
            fin = True
    c = input("¿Es usted un nuevo usuario y desea utilizar el WASTELESS? o ¿Desea volver a utilizar WASTELESS?(Si/No) ").lower()
    if c == "si":
        continue
    elif c == "no":
        print('\nGracias por usar WASTELESS, esperamos que haya sido de utilidad, tenga un buen día')
        break
    else:
        print("Término ingresado inválido. No se ejectuará el programa. Adiós")
        break


  elif choice == "2":
    total = ['hipoteca', 'muebles y mantenimiento del hogar', 'vehículos', 'material deportivo','sanidad', 'educación', 'transporte', 'ocio','comida', 'agua, electricidad y gas', 'ropa', 'bebidas alcohólicas y/o tabaco']
    enero = {}
    febrero = {}
    marzo = {}
    abril = {}
    mayo = {}
    junio = {}
    julio = {}
    agosto = {}
    setiembre = {}
    octubre = {}
    noviembre = {}
    diciembre = {}
    print("\n")
    guardar_datos(enero,"enero",total)
    print("\n")
    guardar_datos(febrero,"febrero",total)
    print("\n")
    
    
    
    archivo = "archivo"+str(num)+".txt"
    with open(archivo, 'w') as arch:
        arch.write("ENERO:\n")
        for clave,valor in enero.items():
            arch.write(clave)
            arch.write(":")
            arch.write(str(valor))
            arch.write("\n")
    
        
  
    with open(archivo, 'a') as arch:
        arch.write("FEBRERO:\n")
        for clave,valor in febrero.items():
            arch.write(clave)
            arch.write(":")
            arch.write(str(valor))
            arch.write("\n")
     

    with open(archivo, 'a') as arch:
        arch.write("MARZO:\n")
        for clave,valor in marzo.items():
            arch.write(clave)
            arch.write(":")
            arch.write(str(valor))
            arch.write("\n")

    with open(archivo, 'a') as arch:
        arch.write("ABRIL:\n")
        for clave,valor in abril.items():
            arch.write(clave)
            arch.write(":")
            arch.write(str(valor))
            arch.write("\n")

    with open(archivo, 'a') as arch:
        arch.write("MAYO:\n")
        for clave,valor in mayo.items():
            arch.write(clave)
            arch.write(":")
            arch.write(str(valor))
            arch.write("\n")
    with open(archivo, 'a') as arch:
        arch.write("JUNIO:\n")
        for clave,valor in junio.items():
            arch.write(clave)
            arch.write(":")
            arch.write(str(valor))
            arch.write("\n")

    with open(archivo, 'a') as arch:
        arch.write("JULIO:\n")
        for clave,valor in julio.items():
            arch.write(clave)
            arch.write(":")
            arch.write(str(valor))
            arch.write("\n")

    with open(archivo, 'a') as arch:
        arch.write("AGOSTO:\n")
        for clave,valor in agosto.items():
            arch.write(clave)
            arch.write(":")
            arch.write(str(valor))
            arch.write("\n")

    with open(archivo, 'a') as arch:
        arch.write("SETIEMBRE:\n")
        for clave,valor in setiembre.items():
            arch.write(clave)
            arch.write(":")
            arch.write(str(valor))
            arch.write("\n")

    with open(archivo, 'a') as arch:
        arch.write("OCTUBRE:\n")
        for clave,valor in octubre.items():
            arch.write(clave)
            arch.write(":")
            arch.write(str(valor))
            arch.write("\n")

    with open(archivo, 'a') as archivo:
        archivo.write("NOVIEMBRE:\n")
        for clave,valor in noviembre.items():
            archivo.write(clave)
            archivo.write(":")
            archivo.write(str(valor))
            archivo.write("\n")

    with open(archivo, 'a') as archivo:
        archivo.write("DICIEMBRE:\n")
        for clave,valor in diciembre.items():
            archivo.write(clave)
            archivo.write(":")
            archivo.write(str(valor))
            archivo.write("\n")
    arch.close()
    num +=1
    continue
