from sklearn import metrics


def accuracy(model, x_test, y_test):
    # Predict the response for test dataset
    y_pred = model.predict(x_test)

    # Model Accuracy, how often is the classifier correct?
    print('Accuracy: {0:.4f}%'.format(100 * (metrics.accuracy_score(y_test, y_pred))))
