# Neural Network optimization with SGD and Adam

In this assignment you are asked to study the behavior of Adam and compare with SGD. You will be replicating the results of section 6 from the paper [Adam: A Method for Stochastic Optimization](https://arxiv.org/abs/1412.6980) by Diederik P. Kingma and Jimmy Ba.

You can watch this video to learn about the variations of SGD and Adam. 

```{eval-rst}
.. youtube:: jDkePF7nUWk
   :width: 560
   :height: 315
   :align: center
```


## Datasets

You will use the [IMDB dataset](https://www.tensorflow.org/api_docs/python/tf/keras/datasets/imdb) and [CFAR10](https://www.tensorflow.org/api_docs/python/tf/keras/datasets/cifar10) datasets and MNIST datasets. The IMDB dataset is a set of 50,000 highly polarized reviews from the Internet Movie Database. They are split into 25,000 reviews for training and 25,000 reviews for testing. The CFAR10 dataset consists of 60,000 32x32 color images in 10 classes, with 6,000 images per class. There are 50,000 training images and 10,000 test images.

## Create the BoW feature vectors  (10 points)

Create the word vectors using Bag of Words (BoW) representation. You can use the following code to get the BoW representation of the dataset. You can read more about BoW [here](https://www.freecodecamp.org/news/an-introduction-to-bag-of-words-and-how-to-code-it-in-python-for-nlp-282e87a9da04/)

## Implement the models (10 points)

You need to implement Logistioc Regression, MLP and CNN models. 


## SGD and Adam optimizers (20 points)

Use SGD and Adam optimizers with Optuna to find the best hyperparameters for the models. You can read more about Optuna [here](https://optuna.readthedocs.io/en/stable/).

## Compare the results (10 points)

Comment on whether the results of the paper have been replicated and on the relative merits of Adam vs SGD.  Consider though the statements made on page 24 of [this reference](https://arxiv.org/pdf/1912.08957.pdf) and comment on how hyperparameter optimization may make the empirical results of the paper less relevant.

