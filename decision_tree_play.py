from sklearn.tree import DecisionTreeClassifier, export_text
from sklearn.preprocessing import LabelEncoder
import pandas as pd

# criar o DataFrame a partir dos dados
df = pd.DataFrame({
    
    'Tempo':   ['Chuvoso','Quente','Nublado','Chuvoso'],
    'Humidade':['86°', '45°', '60°','44°'],
    'Jogar':   ['Não','Sim', 'Sim','Não']
})
# Limpa a coluna 'Humidade'
df['Humidade'] = df['Humidade'].str.replace('°', '').astype(int)
# exibir o DataFrame
print(df)
print('='*40)


# Convertendo as variáveis categóricas em numéricas
df['Tempo'] = df['Tempo'].map({'Chuvoso': 0, 'Nublado': 0.1, 'Quente': 0.2})
df['Jogar'] = df['Jogar'].map({'Não': 0, 'Sim': 1})

print(df)
print('='*40)

# Separando a matriz de recursos X e o vetor de destino y
X = df.drop('Jogar', axis=1)
y = df['Jogar']

# Instanciando o modelo de classificação de árvore de decisão
clf = DecisionTreeClassifier()

# Treinando o modelo
clf.fit(X, y)

# Testando Modelo:
print('Chuvoso: 0, Nublado: 0.1,Quente: 0.2})')
nova_amostra = [[float(input('Tempo:')),float(input('Humidade:'))]]
resultado = clf.predict(nova_amostra)
print(''*15)
if resultado == 0:
    print('Vai jogar?: Não')
    print('='*40)
else:
    print('Vai jogar?: Sim')
    print('='*40)
