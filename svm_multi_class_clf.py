from sklearn import svm

X = [[0,1],[1,0],[0,0]]
y = [1,2,3]
clf = svm.SVC()  #SVC:C-Support Vector Classification.
f = clf.fit(X,y)
p = clf.predict([[0.1,0.1]]) #this is predicted by the fit classification
v = clf.support_vectors_
s = clf.support_
n = clf.n_support_

X = [[0],[1],[2],[3]]
Y = [0,1,2,3]
clf = svm.SVC(decision_function_shape='ovo')
f2 = clf.fit(X,Y)
dec = clf.decision_function([[1]])
s2 = dec.shape[1]
clf.decision_function_shape = "ovr"
dec = clf.decision_function([[1]])
s3 = dec.shape[1]
lin_clf = svm.LinearSVC()
f3 = lin_clf.fit(X,Y)
dec = lin_clf.decision_function([[1]])
s4 = dec.shape[1]
print()