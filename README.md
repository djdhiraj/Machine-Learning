# DecisionTree_Vs_RandomForest
As is implied by the names "Tree" and "Forest," the two concepts are similar. A Random Forest is essentially a collection of Decision Trees. A decision tree is built on an entire dataset, using all the features/variables of interest, whereas a random forest randomly selects observations/rows and specific features/variables to build multiple decision trees from and then averages the results.

When to use to decision tree:

1) When you want your model to be simple and explainable.
2) When you want non parametric model.
3) When you don't want to worry about feature selection or regularization or worry about multi-collinearity.
4) You can overfit the tree and build a model if you are sure of validation or test data set is going to be subset of training data set or    almost overlapping instead of unexpected.

When to use random forest :  

1) When you don't bother much about interpreting the model but want better accuracy.
2) Random forest will reduce variance part of error rather than bias part, so on a given training data set decision tree may be more          accurate than a random forest. But on an unexpected validation data set, Random forest always wins in terms of accuracy.
