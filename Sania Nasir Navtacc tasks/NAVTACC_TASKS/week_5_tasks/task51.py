import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error

# ==========================================
# PART 1: SIMPLE LINEAR REGRESSION
# ==========================================

# Load dataset
df = pd.read_csv("student_scores.csv")

# Display first 5 rows
print(df.head())

# Dataset shape
print("Dataset Shape:", df.shape)

# Exploratory Data Analysis
print(df.describe())
print(df.corr())

# Scatter plot
df.plot.scatter(
    x="Hours",
    y="Scores",
    title="Hours vs Scores"
)
plt.show()

# Separate features and target
X = df["Hours"].values.reshape(-1, 1)
y = df["Scores"].values.reshape(-1, 1)

# Split dataset
SEED = 42

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=SEED
)

# Train model
regressor = LinearRegression()
regressor.fit(X_train, y_train)

# Display intercept and slope
print("Intercept:", regressor.intercept_)
print("Slope:", regressor.coef_)

# Regression equation
print(
    f"Score = {regressor.coef_[0][0]:.2f} * Hours "
    f"+ {regressor.intercept_[0]:.2f}"
)

# Predict score for 5 study hours
score = regressor.predict([[5]])
print("Predicted score for 5 hours:", score[0][0])

# Predict score for 9.5 study hours
score = regressor.predict([[9.5]])
print("Predicted score for 9.5 hours:", score[0][0])

# Predict test data
y_pred = regressor.predict(X_test)

# Compare actual and predicted values
df_preds = pd.DataFrame({
    "Actual": y_test.flatten(),
    "Predicted": y_pred.flatten()
})

print(df_preds)

# Evaluate model
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)

print("Mean Absolute Error:", round(mae, 2))
print("Mean Squared Error:", round(mse, 2))
print("Root Mean Squared Error:", round(rmse, 2))

# R-squared scores
print("Test R2 Score:", regressor.score(X_test, y_test))
print("Train R2 Score:", regressor.score(X_train, y_train))


# ==========================================
# PART 2: MULTIPLE LINEAR REGRESSION
# ==========================================

# Load petrol consumption dataset
df = pd.read_csv("petrol_consumption.csv")

# Display first 5 rows
print(df.head())

# Dataset shape
print("Dataset Shape:", df.shape)

# Descriptive statistics
print(df.describe().round(2).T)

# Independent variables
variables = [
    "Petrol_tax",
    "Average_income",
    "Paved_Highways",
    "Population_Driver_licence(%)"
]

# Regression plots
for var in variables:
    plt.figure()
    sns.regplot(
        x=var,
        y="Petrol_Consumption",
        data=df
    )
    plt.title(f"{var} vs Petrol Consumption")
    plt.show()

# Correlation heatmap
correlations = df.corr()

sns.heatmap(correlations, annot=True)
plt.title("Petrol Consumption Correlations")
plt.show()

# Separate features and target
X = df[
    [
        "Average_income",
        "Paved_Highways",
        "Population_Driver_licence(%)",
        "Petrol_tax"
    ]
]

y = df["Petrol_Consumption"]

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=SEED
)

# Train multiple linear regression model
regressor = LinearRegression()
regressor.fit(X_train, y_train)

# Display intercept and coefficients
print("Intercept:", regressor.intercept_)
print("Coefficients:", regressor.coef_)

# Display coefficients with feature names
coefficients_df = pd.DataFrame(
    data=regressor.coef_,
    index=X.columns,
    columns=["Coefficient Value"]
)

print(coefficients_df)

# Predict test data
y_pred = regressor.predict(X_test)

# Compare actual and predicted values
results = pd.DataFrame({
    "Actual": y_test,
    "Predicted": y_pred
})

print(results)

# Evaluate model
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)

print("Mean Absolute Error:", round(mae, 2))
print("Mean Squared Error:", round(mse, 2))
print("Root Mean Squared Error:", round(rmse, 2))

# Calculate R-squared manually
actual_minus_predicted = np.sum((y_test - y_pred) ** 2)
actual_minus_actual_mean = np.sum((y_test - y_test.mean()) ** 2)

r2 = 1 - (
    actual_minus_predicted / actual_minus_actual_mean
)

print("R2 Score:", r2)

# R-squared using Scikit-Learn
print("Test R2 Score:", regressor.score(X_test, y_test))
print("Train R2 Score:", regressor.score(X_train, y_train))