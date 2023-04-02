from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import export_graphviz
import graphviz

#Creating the input matrix X and output vector y
X = [[0, 1,0,0], [1, 0,0,0],[1,1,0,0],[0,0,0,0]]
y = ['cat', 'dog','parrot','fish']

#Creating an instance of the DecisionTreeClassifier class
clf = DecisionTreeClassifier()

#Training the model
clf.fit(X, y)

#Generating the graphical representation of the decision tree
dot_data = export_graphviz(clf, out_file=None,
feature_names=['Bark', 'Meow','Silent','Sing'],
class_names=['Cat', 'Dog','Parrot', 'Fish'],
filled=True, rounded=True,
special_characters=True)
graph = graphviz.Source(dot_data)

#Saving the tree image to a PNG file
graph.format = 'png'
graph.render('decision-tree')

#To add a new sample to be classified
new_sample = [[0, 0,0,0]]
result = clf.predict(new_sample)
print(result)
