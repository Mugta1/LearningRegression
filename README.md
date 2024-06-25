# Linear Regression with Gradient Descent

This repository contains Python code for implementing linear regression using gradient descent. Regards to Andrew NG for his course on machine learning 

## Overview

Linear regression is a powerful statistical method that models the relationship between a dependent variable and one or more independent variables. It's widely used in various fields such as economics, finance, and machine learning for tasks like predicting house prices, stock prices, and more.

This code implements linear regression and gradient descent from scratch using NumPy, a popular library for numerical computing in Python. The implementation includes functions to calculate the cost, gradients, and update weights and biases using gradient descent.
 
## How it Works

1. **Input Data**: Provide training data `x_train` and corresponding labels `y_train`. These represent the features (independent variables) and target variable (dependent variable) respectively.
2. **Set Parameters**: Set initial values for weights `w` and bias `b`, learning rate `a`, and number of iterations `itr`.
3. **Run Code**: Execute the `finalfunc` function with the provided inputs. This function applies gradient descent to find the optimal parameters for the linear regression model.
4. **Prediction**: Input the area of a house to predict its selling price. The model will output the predicted selling price based on the learned parameters.

## Files

- `linear_regression.py`: Python script containing the implementation of linear regression and gradient descent.
- `README.md`: This file providing an overview of the repository and instructions for usage.

## Usage

To use this code, follow these steps:

1. Clone the repository to your local machine.
2. Install the required dependencies (Python 3 and NumPy).
3. Open `linear_regression.py` and provide your training data (`x_train` and `y_train`).
4. Set the initial values for weights `w` and bias `b`, learning rate `a`, and number of iterations `itr`.
5. Run the script and observe the output.
6. Use the `finalfunc` function to make predictions for new data.

## Requirements

- Python 3
- NumPy

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- This implementation was inspired by Andrew Ng's Machine Learning course on Coursera.
- Special thanks to the open-source community for their contributions to NumPy and other libraries used in this project.
