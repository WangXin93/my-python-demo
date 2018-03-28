import tensorflow as tf

import iris_data

def main():
    tf.logging.set_verbosity(tf.logging.INFO)

    batch_size = 100
    train_steps = 1000

    (train_x, train_y), (test_x, test_y) = iris_data.load_data()

    my_feature_columns = []
    for key in train_x.keys():
        my_feature_columns.append(tf.feature_column.numeric_column(key=key))

    classifier = tf.estimator.DNNClassifier(
        feature_columns=my_feature_columns,
        hidden_units=[10,10],
        n_classes=3)

    # Train
    classifier.train(input_fn=lambda:iris_data.train_input_fn(train_x, train_y, batch_size), steps=1000)

    # Evaluate
    eval_result = classifier.evaluate(input_fn=lambda:iris_data.eval_input_fn(test_x, test_y, 100))
    print('\nTest set accuracy: {accuracy:0.3f}\n'.format(**eval_result))

    # Predict
    expected = ['Setosa', 'Versicolor', 'Virginica']
    predict_x = {
        'SepalLength': [5.1, 5.9, 6.9],
        'SepalWidth': [3.3, 3.0, 3.1],
        'PetalLength': [1.7, 4.2, 5.4],
        'PetalWidth': [0.5, 1.5, 2.1],
    }
    predictions = classifier.predict(input_fn=lambda:iris_data.eval_input_fn(predict_x,
                                                                             labels=None,
                                                                             batch_size=batch_size))
    template = ('\nPrediction is "{}" ({:.1f}%), expected "{}"')
    for pred_dict, expec in zip(predictions, expected):
        class_id = pred_dict['class_ids'][0]
        probability = pred_dict['probabilities'][class_id]
        print(template.format(iris_data.SPECIES[class_id], 100 * probability, expec))

if __name__ == "__main__": 
    main()
