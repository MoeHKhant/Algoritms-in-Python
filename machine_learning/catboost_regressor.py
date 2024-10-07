"""
CatBoost Regressor Example.

This script demonstrates the usage of the CatBoost Regressor for a simple regression task.
CatBoost is a powerful gradient boosting library that handles categorical features automatically
and is highly efficient.

Make sure to install CatBoost using:
    pip install catboost

Contributed by: @AHuzail
"""

import numpy as np
from sklearn.datasets import load_boston
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from catboost import CatBoostRegressor


def data_handling() -> tuple:
    """
    Loads and handles the dataset, splitting it into features and targets.

    The Boston dataset is used as a regression example.

    Returns:
        tuple: A tuple of (features, target), where both are numpy arrays.

    Example:
    >>> features, target = data_handling()
    >>> features.shape
    (506, 13)
    >>> target.shape
    (506,)
    """
    # Load Boston dataset (note: this dataset may be deprecated, replace if needed)
    boston = load_boston()
    features = boston.data
    target = boston.target
    return features, target


def catboost_regressor(features: np.ndarray, target: np.ndarray) -> CatBoostRegressor:
    """
    Trains a CatBoostRegressor using the provided features and target values.

    Args:
        features (np.ndarray): The input features for the regression model.
        target (np.ndarray): The target values for the regression model.

    Returns:
        CatBoostRegressor: A trained CatBoost regressor model.

    Example:
    >>> features, target = data_handling()
    >>> model = catboost_regressor(features, target)
    >>> isinstance(model, CatBoostRegressor)
    True
    """
    regressor = CatBoostRegressor(iterations=100, learning_rate=0.1, depth=6, verbose=0)
    regressor.fit(features, target)
    return regressor


def main() -> None:
    """
    Main function to run the CatBoost Regressor example.

    It loads the data, splits it into training and testing sets,
    trains the regressor on the training data, and evaluates its performance
    on the test data.
    """
    # Load and split the dataset
    features, target = data_handling()
    x_train, x_test, y_train, y_test = train_test_split(
        features, target, test_size=0.25, random_state=42
    )

    # Train CatBoost Regressor
    regressor = catboost_regressor(x_train, y_train)

    # Predict on the test set
    predictions = regressor.predict(x_test)

    # Evaluate the performance using Mean Squared Error
    mse = mean_squared_error(y_test, predictions)
    print(f"Mean Squared Error on Test Set: {mse:.4f}")


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
    main()
