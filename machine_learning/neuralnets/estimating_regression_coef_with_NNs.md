
# Estimating regression coefficients using a Neural Network (from scratch)

**Link:** https://lcgodoy.me/post/2021/06/lmnnet/


## Intro

NNs are sick.


## Neural Network regression

A NN is a highly parameterized model that can approx any functional relationship between a set of *features* **x** and a responce variable **y**, provided enough data. Many NN structures, but will focus on *feed-forward* NNs. This is pretty much the bog standard NN. Connections from left o right, representing information flow (hence *feed-forward*). Each unit is computed by:
1. Giving weights to each input
2. Calc dot product between weights & inputs
3. Adding a constant, or *bias*
4. Applying an element-wise *activation* function **f(.)** to it, to establish *non-linear* relationships between units.

The # of hidden layers & units associated with each layer can be regarded as *tuning* parameters. With single hidden layer NNs Efron & Hastie (https://lcgodoy.me/post/2021/06/lmnnet/#ref-efron2016computer) suggest that it is better to consider several units for the hidden layer & some kind of regularisation, akin to lasso/ridge penalties.

NNs are *pure prediction algs*, ie they are focused mostly on prediction, neglecting estimation. Strategy consists of searching for high predictive accuracy. So they make no assumption of the probability distribution of the data and one consequence of this is to make it impossible to make interval predictions or to calc confidence intervals for the "estimated" parameters.


## Single Neuron Feed-Forward Networks

No hidden layer, resemble more standard stat models ie linear & logistic regression. Taking the identity as the *activation function*, the functional relationship between **x** & **y** considered by the NN is equivalent to one for a general linera model. Considering the same representation, if we take

**f(x) = logit(x)** (*sigmoid* function in NN literature), where **y ∈ {0,1}**.

Although the functional relationship between **x** and **y** assumed by single layer NNs coincides with some statistical models we cannot promptly claim an equivalence between models because the way the NNs **learn**, that is estimates, the weights, which can lead to diffferent solutions dependening on the **loss** and **cost** functions selected.


## Activation functions
