﻿# Binary-Classification-using-CNN

This repository contains a deep learning binary classification model built using TensorFlow for predicting customer churn. The model is designed to classify whether a customer will churn (leave) or not based on various features.

## Dataset

The dataset used for this project is the "Churn_Modelling.csv" dataset. It contains information about bank customers, including features like credit score, geography, gender, age, tenure, balance, etc. The goal is to predict whether a customer will exit the bank (churn) or not.

## Dependencies

Make sure you have the following Python libraries installed:

- TensorFlow
- NumPy
- Pandas
- Matplotlib
- scikit-learn

You can install the required libraries using `pip`:

```bash
pip install tensorflow numpy pandas matplotlib scikit-learn
```

## Data Preprocessing

1. The dataset is loaded using Pandas, and unnecessary columns like "RowNumber," "CustomerId," "Surname," and "Exited" are dropped.

2. Label encoding is performed on the "Geography" and "Gender" columns to convert categorical data into numeric format.

3. One-hot encoding is applied to the "Geography" column to create binary columns for each category.

4. The dataset is split into training and testing sets using scikit-learn's `train_test_split` function.

5. Feature scaling is performed to normalize the data using scikit-learn's `StandardScaler`.

## Model Architecture

The neural network model architecture consists of the following layers:

- Input layer with ReLU activation
- Two hidden layers with ReLU activation
- Output layer with sigmoid activation for binary classification

## Model Compilation

The model is compiled with the following settings:

- Optimizer: Adam
- Loss function: Binary cross-entropy
- Metrics: Accuracy

## Training

The model is trained on the training data with the specified number of epochs and batch size.

## Evaluation

The model is evaluated on the test data, and the test accuracy is calculated.

## Predictions and Confusion Matrix

- Predictions are made on the test data, and a threshold of 0.5 is applied to classify customers as churned or not churned.

- A confusion matrix is generated to evaluate the model's performance further.

## Usage

To train and evaluate the model, run the code in a Python environment. You can adjust hyperparameters, such as the number of epochs, batch size, and model architecture, to optimize the model's performance.

