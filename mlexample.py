from sklearn

#[height, weight, shoe size]
X = [[181,80,44], [177,70,43], [160,60,38], [154,54,37],
     [166,65,40],[190,90,47],[177,64,39],[159,87,50],
     [171,75,43],[181,85,43]]

Y = ['male','female','female','female','male','male','male','female','male','female']

clf = tree.DecisionTreeClassifier()
clf = clf.fit(X,Y)
prediction = clf.predict([[190,70,43]])
print('Decision Tree:')
print(prediction)

clf = neighbors.KNeighborsClassifier(n_neighbors=3)
clf = clf.fit(X,Y)
prediction = clf.predict([[190,70,43]])
print('KNeighbors:')
print(prediction)

clf = ensemble.RandomForestClassifier()
clf = clf.fit(X,Y)
prediction = clf.predict([[190,70,43]])
print('RFC:')
print(prediction)

clf = naive_bayes.GaussianNB()
clf = clf.fit(X,Y)
prediction = clf.predict([[190,70,43]])
print('GaussianNB')
print(prediction)
