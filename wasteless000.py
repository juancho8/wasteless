import matplotlib.pyplot as plt

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
def ahorro(a,b,c):
    count = 0
    for i in range(len(a)):
        if a[i] <= b[i]:
            count += 1
    if count >= 10:
        print("Usted es considerada una persona ahorrativa. Por ende, ingrese un consejo para los otros usuarios, por favor")
        c["consejo de usuario"]=input("Inserte un consejo a compartir: ")
    else:
        print("Lo sentimos, usted no cumple los requisitos para ser considerada ahorrativa. Por ende, no puede agregar un consejo para los otros usuarios; sin embargo, puede recibir un consejo de un profesional")

while True:

# tupla datos media española anuales
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
    print('Bienvenid@ a WASTELESS, para el correcto funcionamiento de esta aplicación, será necesario introducir datos personales, en concreto gastos en diferentes sectores')
    print('\n---------- IMPORTANTE: POR FAVOR, INTRODUCE LOS VALORES CON CARÁCTER ANUAL ----------\n')
    print('>>>>> Si la variabilidad mensual es discontinua, por favor hacer la media e introducir el valor\n>>>>> Ejemplo hipoteca : en el caso de ser 600 euros al mes introduce 7200\n')

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
    Total = 1609.2

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

    consejos = {'hipoteca' : '''Podrías revisar el presupuesto hipotecario con tu banco para saber si se ajusta a tus necesidades: el TAE es un elemento muy variable que afectará a tus gastos.''' , 
            
            'muebles y mantenimiento del hogar' : '''Podemos ahorrar con nuestros gastos en este sector , comprando a mayor escala por ejemplo en el MACRO, en el caso de gastos 
            puntuales en muebles, podemos usar fechas clave de descuentos como BLACK FRIDAY o las ofertas de finales de enero en REBAJAS.''', 

            'vehículos' : '''Los vehículos de segunda mano son una buena opción a la hora de buscar un utilitario para trabajar. 
            Compara el precio de las gasolineras más cercanas a ti. Podrías considerar utilizar más el transporte público o compartir el vehículo con vecinos e incluso la plaza de garaje.''', 

            'material deportivo' : '''Desde siempre se ha recomendado en cuanto a material deportivo comprar en cadenas grandes como DECATHLON, pero tenemos que tener en cuenta que si vamos
             a darle mucho uso al material, es mejor comprar calidad para ahorrar en costes de reparaciones.''', 
            
            'sanidad' : '''Por suerte, en España la sanidad pública es gratuita y de calidad media-alta respecto al resto del mundo. Si queremos reducir gasto podemos quitar los seguros privados 
            y confiar en el sector público.''', 

            'educación' : '''Compra materiales genéricos, normalmente no necesitarás materiales de marcas conocidas. Muchos colegios ofrecen opciones de reutilización de libros o comprarlos de 
            segunda mano. Planificar una lista de lo que vas a comprar de antemano también puede ayudar.''', 

            'transporte' : '''Puedes considerar tarjetas temporales, que en algunos casos pueden reducir el gasto en un 50%. Infórmate de los descuentos. A veces incluso ir en tren o autobús puede ayudar 
            a que desplazamientos puntuales (vacaciones) salgan más económicas.''', 

            'ocio' : '''Hay infinidad de planes que no cuestan dinero como dar un paseo por la montaña o ir a sitios que hace mucho que no visitas de tu localidad, también puedes ahorrar 
            estudiando las ofertas que puedan tener los restaurantes, teatros o cines, como los menús del día o el día del espectador.''', 

            'comida' : '''Evita comprar en exceso, procura comprar lo que te vayas a comer para que no se caduque la comida en la nevera. Hay ciertos alimentos que se pueden comprar más 
            baratos en temporada y que congelándolos pueden durar mucho más tiempo.''', 

            'agua' : '''Pon un cubo en el baño, y en lugar de tirar los papeles en el váter y tirar de la cadena, tiralos allí, ya que se calcula que el 30% del consumo del agua procede de los inodoros. 
            Asegúrate de que tus grifos y cisternas no pierden agua y utilizarla siempre que puedas.''', 

            'electricidad y gas' : '''Puedes cambiar tus bombillas por otras de bajo consumo, pintar las paredes de un color más claro ayudará a que la estancia esté más iluminada durante más tiempo. 
            Instalar un medidor de consumo puede ser una manera útil de ser consciente de tus gastos e incluso programar las horas de encendido y apagado.''', 

            'ropa' : '''Planifica tus compras con antelación y cíñete a la lista. Limpia y reevalúa tu armario, arregla las prendas que lo necesiten, o modifícalas. Échale un vistazo a las tiendas 
            de ropa de segunda mano y la ropa de temporadas anteriores. Fíjate en la calidad de las prendas para que duren más tiempo y compra prendas atemporales centrándote en los básicos. ''', 

            'bebidas alcohólicas y/o tabaco' : '''¿Sabías que si dejas de fumar, de media ahorras una cantidad similar a 1500 euros anuales? Sucede algo parecido al reducir el consumo de bebidas alcohólicas. 
            Hay diversas soluciones que te ayudarán a abandonar estos hábitos como terapias o sustitutos de estos productos.'''}
    print("\n")
    ahorro(listaTotal,list(mediaTotal),consejos)
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
    c = input("¿Es usted un nuevo usuario y desea utilizar el WASTELEES?(Si/No) ").lower()
    if c == "si":
        continue
    elif c == "no":
        print('\nGracias por usar WASTELESS, esperamos que haya sido de utilidad, tenga un buen día')
        break
    else:
        print("Término ingresado inválido. No se ejectuará el programa. Adiós")
        break