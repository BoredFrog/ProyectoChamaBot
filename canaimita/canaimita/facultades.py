from sklearn import tree
from . import views
clf = tree.DecisionTreeClassifier()
x = [
  [2,1,2,4,4,4], [4,1,2,4,4,4], [2,1,2,1,4,4], [4,1,2,1,4,4], 
[2,1,2,4,2,4], [4,1,2,4,2,4], [2,1,2, 2,4,4], [4,1,2,2,4,4], 
[2,1,2,3,4,4], [4,1,2,3,4,4], [2,1,2,4,3,4], [4,1,2,4,3,4], 
[2,1,2,4,5,4], [4,1,2,4,5,4], 

[4,3,3,2,1, 2], [3,3,3,5,2,3], [4,3,3,2,3,5], [3,4,3,5,4,5], 


[2,1,3,1,5,2], [2,3,2,2,5,2], [2,3,3,3,5,2], [3,1,2,4,5,2], 
[3,3,2,5,2,3], [3,3,3,2,5,3], [4,1,2,2,4,5], [4,3,2,5,5,5], [4,3,3,5,5,2], 

[1,2,1,1,1,1], [1,4,1,2,1,1], [3,2,1,3,1,3 ], [3,4,1,5,1,3],
[1,2,1,2,1,1], [1,4,1,1,1,1], [3,2,1,3,1,3 ], [3,4,1,1,1,1],
[1,2,1,5,1,3], [1,4,1,3,1,3], [3,2,1,5,1,3], [3,4,1,2,1,1],
[1,2,1,3,1,3], [1,4,1,5,1,3], [3,2,1,2,1,1], [3,4,1,3,1,3],
[1,4,4,1,1,1],

[1,1,1,1,2,1], [1,1,2,2,3,2], [1,1,4,3,4,3], [3,1,1,4,5,4],
[3,1,2,5,5,5], [3,1,4,5,4,1],[3,1,1,3,3,3]
]

y = ['Ciencias jurídicas y políticas', 'Ciencias jurídicas y políticas', 
'Ciencias jurídicas y políticas', 'Ciencias jurídicas y políticas', 
'Ciencias jurídicas y políticas', 'Ciencias jurídicas y políticas', 
'Ciencias jurídicas y políticas', 'Ciencias jurídicas y políticas', 
'Ciencias jurídicas y políticas', 'Ciencias jurídicas y políticas', 
'Ciencias jurídicas y políticas', 'Ciencias jurídicas y políticas', 
'Ciencias jurídicas y políticas', 'Ciencias jurídicas y políticas', 

'Ciencias de la información (Diseño gráfico)','Ciencias de la información (Diseño gráfico)',
'Ciencias de la información (Diseño gráfico)','Ciencias de la información (Diseño gráfico)', 

'Humanidades y educación (Comunicación social)','Humanidades y educación (Comunicación social)',
'Humanidades y educación (Comunicación social)','Humanidades y educación (Comunicación social)',
'Humanidades y educación (Comunicación social)','Humanidades y educación (Comunicación social)',
'Humanidades y educación (Comunicación social)','Humanidades y educación (Comunicación social)',
'Humanidades y educación (Comunicación social)',

'Ingeniería','Ingeniería','Ingeniería','Ingeniería', 
'Ingeniería','Ingeniería','Ingeniería','Ingeniería', 
'Ingeniería','Ingeniería','Ingeniería','Ingeniería', 
'Ingeniería','Ingeniería','Ingeniería','Ingeniería', 'Ingeniería', 

'Ciencias administrativas','Ciencias administrativas',
'Ciencias administrativas','Ciencias administrativas',
'Ciencias administrativas','Ciencias administrativas','Ciencias administrativas']

clf = clf.fit(x,y)
#dato1 = [2,1,2,4,4,4] #ABOGADO 
#dato1 = [3,3,3,5,2,3]  #DISENADOR GR.
#dato1 =  [4,1,2,2,4,5]  #Humanidades y educación (Comunicación social)
#dato1 =  [3,1,4,5,4,1]  #Ciencias administrativas
#dato1 =  [1,2,1,1,1,1] #INGENIERIA
#dato1 =  [1,4,4,1,3,1] #ELI MORA
#dato1 =  [2,1,4,2,3,5] #YRALY MORA
#dato1 =  [2,1,3,1,5,2]
dato1 =  [3,1,1,3,3,3]


prediction = clf.predict([dato1])
print(views.respuestasPreguntas)
#print(respuestasPreguntas)
if prediction == 'Ciencias jurídicas y políticas':
  print('Tu personalidad se inclina y manifiesta fuerte interes por las Ciencias jurídicas y políticas, podrias ser un gran abogado!! 👩‍⚖️')

if prediction == 'Ciencias de la información (Diseño gráfico)':
  print('Tu personalidad se inclina y manifiesta fuerte interes por las Ciencias de la información, podrias ser un gran disenador grafico 👩‍🎨')

if prediction == 'Ingeniería':
  print('Tu personalidad es ingeniosa y manifiestas fuerte inter por solventar problemas a traves de las maravillosas matematicas y la tecnologia, podrias ser un gran Ingeniero 👷‍♂️ o informatico 👨‍💻')

if prediction == 'Ciencias administrativas':
  print('Tu personalidad se inclina y manifiesta fuerte interes por las Ciencias administrativas, podrias ser un gran Contador, Administrador o Relacionista Industrial 📈📊')

if prediction == 'Humanidades y educación (Comunicación social)':
  print('Tu personalidad se inclina y manifiesta fuerte interes por las Humanidades y educación, podrias ser un gran Comunicador social 🎤')