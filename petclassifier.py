from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import export_graphviz
import graphviz

# Criando a matriz de entrada X e o vetor de saída y
X = [[0, 1,0,0], [1, 0,0,0],[1,1,0,0],[0,0,0,0]]
y = ['gato', 'cachorro','papagaio','peixe']

# Criando uma instância da classe DecisionTreeClassifier
clf = DecisionTreeClassifier()

# Treinando o modelo
clf.fit(X, y)

# Gerando a representação gráfica da árvore de decisão
dot_data = export_graphviz(clf, out_file=None,
                           feature_names=['Latir', 'Miar','Canta','Sem Som'],
                           class_names=['Gato', 'Cachorro','Papagaio', 'Peixe'],
                           filled=True, rounded=True,
                           special_characters=True)
graph = graphviz.Source(dot_data)

# Salvando a imagem da árvore em um arquivo PNG
graph.format = 'png'
graph.render('arvore-decisao')

nova_amostra = [[0, 0,0,0]]
resultado = clf.predict(nova_amostra)
print(resultado)
