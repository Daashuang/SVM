### Support vector machine
---
Support vector machines (SVMs) are a set of supervised learning methods used for classification, regression and outliers detection.

- Advantages:
1. Effective in high dimensional spaces.
2. Still effective in cases where number of dimensions is greater than the number of samples.
3. Uses a subset of training points in the decision function (called support vectors), so it is also memory efficient.
4. Versatile: different Kernel functions can be specified for the decision function. Common kernels are provided, but it is also possible to specify custom kernels.
- Disadvantages:
1. If the number of features is much greater than the number of samples, avoid over-fitting in choosing Kernel functions and regularization term is crucial.
2. SVMs do not directly provide probability estimates, these are calculated using an expensive five-fold cross-validation.
From [scikit-learn.org](http://scikit-learn.org/stable/modules/svm.html).
Learn more about the SVM: The book has the formulas about SVM.