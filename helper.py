import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import seaborn as sns

from sklearn.metrics import precision_score, recall_score, accuracy_score, f1_score
from sklearn.metrics import roc_curve, plot_roc_curve, auc, roc_auc_score
from sklearn.metrics import plot_confusion_matrix
from sklearn.metrics import confusion_matrix

def binary_classification_evaluation(estimator, X_train, X_test, y_train, y_test, name_of_estimator='unnamed', cm_labels=[0,1],                                                  is_ANN=False):
    """This function will make predictions and evaluate a classifier using a variety of metrics:
    
       COPY THIS 
       
       import pandas as pd
       import numpy as np
       import matplotlib.pyplot as plt
       import matplotlib.ticker as mtick
       %matplotlib inline
       import seaborn as sns

       from sklearn.metrics import precision_score, recall_score, accuracy_score, f1_score
       from sklearn.metrics import roc_curve, plot_roc_curve, auc, roc_auc_score
       from sklearn.metrics import plot_confusion_matrix
       from sklearn.metrics import confusion_matrix"""
    
    # make predictions on train and test sets
    # round so that neural network outputs 0's and 1's rather than values between 0 and 1
    y_hat_train = np.round(estimator.predict(X_train))
    y_hat_test = np.round(estimator.predict(X_test))
    
    # evaluate classifier on training set
    
    print("TRAINING SET METRICS")
    print("--------------------------------------------------------------------------------------")
    
    # basic metrics
    print("{} Classifier Training Data Scores".format(name_of_estimator))
    print("")
    print("Recall Score: {}%".format(round(100*recall_score(y_train, y_hat_train),3)))
    print("Precision Score: {}%".format(round(100*precision_score(y_train, y_hat_train),3)))
    print("Accuracy Score: {}%".format(round(100*accuracy_score(y_train, y_hat_train),3)))
    print("F1 Score: {}".format(round(f1_score(y_train, y_hat_train),5)))
    print("ROC AUC Score: {}".format(round(roc_auc_score(y_train, y_hat_train),5)))
    print("")
    
    # check if classifier is ANN
    if is_ANN==False:
    
        # confusion matrix
        print("Train Data Confusion Matrix")
        print("---------------------------------------------------------------------------------------")
        fig, ax = plt.subplots()
        fig.set_figheight(8)
        fig.set_figwidth(8)
        plot_confusion_matrix(estimator, X_train, y_train,
                              display_labels=cm_labels,
                              cmap=plt.cm.Blues,
                              normalize=None, ax=ax)
        plt.title("{} Train Data Confusion Matrix".format(name_of_estimator))
        plt.show()
        print("")

        # ROC Curve
        print("Train Data ROC Curve")
        print("---------------------------------------------------------------------------------------")
        # set style
        sns.set_style('darkgrid') 
        sns.set_context('talk') 

        # initialize plot and size
        fig, ax = plt.subplots()
        fig.set_figheight(10)
        fig.set_figwidth(15)

        # plot curve and label
        plot_roc_curve(estimator, X_train, y_train, ax=ax)
        plt.title("{} Train Data ROC Curve".format(name_of_estimator))
        plt.show()
        print("")
    
    # evaluate classifier on testing set
    
    print("TESTING SET METRICS")
    print("--------------------------------------------------------------------------------------")
    
    # basic metrics
    print("{} Classifier Testing Data Scores".format(name_of_estimator))
    print("")
    print("Recall Score: {}%".format(round(100*recall_score(y_test, y_hat_test),3)))
    print("Precision Score: {}%".format(round(100*precision_score(y_test, y_hat_test),3)))
    print("Accuracy Score: {}%".format(round(100*accuracy_score(y_test, y_hat_test),3)))
    print("F1 Score: {}".format(round(f1_score(y_test, y_hat_test),5)))
    print("ROC AUC Score: {}".format(round(roc_auc_score(y_test, y_hat_test),5)))
    print("")
    
    # check if classifier is ANN
    if is_ANN==False:
   
        # confusion matrix
        print("Test Data Confusion Matrix")
        print("---------------------------------------------------------------------------------------")
        fig, ax = plt.subplots()
        fig.set_figheight(8)
        fig.set_figwidth(8)
        plot_confusion_matrix(estimator, X_test, y_test,
                              display_labels=cm_labels,
                              cmap=plt.cm.Blues,
                              normalize=None, ax=ax)
        plt.title("{} Test Data Confusion Matrix".format(name_of_estimator))
        plt.show()
        print("")

        # ROC Curve
        print("Test Data ROC Curve")
        print("---------------------------------------------------------------------------------------")
        # set style
        sns.set_style('darkgrid') 
        sns.set_context('talk') 

        # initialize plot and size
        fig, ax = plt.subplots()
        fig.set_figheight(10)
        fig.set_figwidth(15)

        # plot curve and label
        plot_roc_curve(estimator, X_test, y_test, ax=ax)
        plt.title("{} Test Data ROC Curve".format(name_of_estimator))
        plt.show()
    