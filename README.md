# DecisionTree_Vs_RandomForest
As is implied by the names "Tree" and "Forest," the two concepts are similar. A Random Forest is essentially a collection of Decision Trees. A decision tree is built on an entire dataset, using all the features/variables of interest, whereas a random forest randomly selects observations/rows and specific features/variables to build multiple decision trees from and then averages the results.

# When to use to decision tree:

1) When you want your model to be simple and explainable.
2) When you want non parametric model.
3) When you don't want to worry about feature selection or regularization or worry about multi-collinearity.
4) You can overfit the tree and build a model if you are sure of validation or test data set is going to be subset of training data set or    almost overlapping instead of unexpected.

# When to use random forest :  

1) When you don't bother much about interpreting the model but want better accuracy.
2) Random forest will reduce variance part of error rather than bias part, so on a given training data set decision tree may be more          accurate than a random forest. But on an unexpected validation data set, Random forest always wins in terms of accuracy.

# TensorFlow main Classes
* tf.Graph()
* tf.Operation()
* tf.Tensor()
* tf.Session()


# Some Useful funtions:
* tf.get_default_session()
* tf.get_default_graph()
* tf.reset_default_graph()
* ops.reset_default_graph()
* tf.device("/cpu:0")
* tf.name_scope(value)

# TensorFlow Optimizers
* GradientDescentOptimizer
* AdagradOptimizer 
* AdagradOptimizer
* MomentumOptimizer
* AdamOptimizer
* FtrlOptimizer
* RMSPropOptimizer

# Reduction 
* reduce_sum
* reduce_prod
* reduce_min
* reduce_max
* reduce_mean
* reduce_all
* reduce_any
* accumulate_n
* Activation Functins 
* tf.nn?
* relu
* relu6
* elu
* softplus 
* dropsign
* dropout
* bias_add
* sigmoid 
* tanh 
* sigmoid_cross_entropy_with_logits
* softmax
* log_softwax
* softwax_tf.convert_to_tensor(value)



# Skflow main classes
* TensorFlowClassifier
* TensorFlowRegressor
* TensorFlowDNNRegressor
* TensorFlowLinearClassifier
* TensorFlowLinearRegressor
* TensorFlowRNNClassifier
* TensorFlowRNNRegressor
