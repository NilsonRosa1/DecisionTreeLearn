# DecisionTreeLearn

Creation of input matrix X and output vector y:

X = [[0, 1,0,0], [1, 0,0,0],[1,1,0,0],[0,0,0,0]]
y = ['cat', 'dog', 'parrot', 'fish']

Here, we are defining the input matrix X with 4 samples, 
each with 4 binary values (0 or 1) representing if the animal: 'Barks', 'Meows', 'No Sound', 'Sings'.
In addition, we define the output vector y, indicating if each sample represents: 'Cat', 'Dog', 'Parrot', 'Fish'.

Creation of the model and training:

clf = DecisionTreeClassifier()
clf.fit(X, y)

In this step, I create an instance of the DecisionTreeClassifier class and train the model using the X matrix and y vector.
The created model will be a decision tree that classifies animals as Cats, Dogs, Parrots, and Fish
based on their characteristics.


Adding a Sample for Classification:

new_sample = [[0, 0,0,0]]
result = clf.predict(new_sample)
print(result)

The new_sample variable receives a new list of attributes, which is then passed to the result variable that is receiving the predict function.
This function uses the trained decision tree model to classify the sample based on its attributes and returns the predicted class label.
The decision tree model uses the conditions on its branches to determine which external leaf node the sample belongs to.











pt-br:
Criação da matriz de entrada X e do vetor de saída y:


X = [[0, 1,0,0], [1, 0,0,0],[1,1,0,0],[0,0,0,0]]
y = ['gato', 'cachorro','papagaio','peixe']

Aqui,  defino a matriz de entrada X com 4 amostras, 
cada uma com 4 valores binários (0 ou 1) representando se o animal: 'Latir', 'Miar','Sem Som','Cantar'. Além disso,
definimos o vetor de saída y, indicando se cada amostra representada: 'Gato', 'Cachorro','Papagaio', 'Peixe'.

Criação do modelo e treinamento

clf = DecisionTreeClassifier()
clf.fit(X, y)

Nessa etapa,  crio uma instância da classe DecisionTreeClassifier e treino o modelo utilizando a matriz X e o vetor y. 
O modelo criado será uma árvore de decisão que classifica os animais como Gatos, Cachorros, Papagaios  e Peixe  com base em suas características.



Adicionando Amostra para Classificação:


nova_amostra = [[0, 0,0,0]]
resultado = clf.predict(nova_amostra)
print(resultado)


 Variavel nova_amostra recebe uma nova lista de atributos, que é enviada logo em seguida pela variavel resultado que está recebendo a função predict.
 que nada mais é o modelo treinado em formato de arvore tendo as condições nos ramos que vão classificar em qual folha externa aquela lista se classifica  
