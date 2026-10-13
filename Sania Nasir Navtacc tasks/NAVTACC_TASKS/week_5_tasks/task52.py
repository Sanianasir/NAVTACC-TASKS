# Five Regression Python Modules

import numpy as np
import matplotlib.pyplot as plt
import scipy as sp
import statsmodels.api as sm
from sklearn import linear_model
import seaborn as sns

# 1. Data
x = np.array([
    56755.72171242, 44178.04737774, 40991.80813814,
    8814.00098681, 43585.51198178, 13574.17183072,
    6175.8760297, 17829.69832237, 53254.85637009,
    17522.23018625, 42784.69836164, 36638.18492916,
    41086.72967373, 18167.77372717, 12706.89121489,
    52564.42917946, 61995.42280258, 35776.79516181,
    30230.22630213, 34524.46986093, 13774.60527391,
    14258.22933451, 101376.49657434, 9616.64500569,
    45175.23189338, 38615.99518491, 74355.51585756,
    12578.49547344, 19242.3664711, 16310.988409,
    20881.76692993, 5734.63362915, 25732.01836475,
    51545.48360953, 82081.59716162, 11006.2497364,
    44974.83187718, 56839.38177423
])

y = np.array([
    7.3, 7.1, 6.9, 6.4, 7.4, 6.5, 6.3, 6.7, 7.6,
    5.7, 7.6, 6.5, 7.0, 5.4, 5.6, 7.5, 7.0, 7.2,
    6.0, 5.9, 5.9, 5.9, 6.9, 6.5, 7.4, 7.3, 7.6,
    6.1, 5.4, 6.2, 5.9, 4.7, 6.3, 7.3, 7.5, 5.5,
    6.8, 6.9
])

# 2. NumPy polyfit
print("\n1. NUMPY POLYFIT")

p = np.poly1d(np.polyfit(x, y, 1))

print("Slope:", p[1])
print("Intercept:", p[0])

x_line = np.linspace(np.amin(x), np.amax(x), 200)

plt.scatter(x, y)
plt.plot(x_line, p(x_line))
plt.xlabel("GDP per capita (USD)")
plt.ylabel("Life Satisfaction")
plt.title("NumPy Linear Regression")
plt.show()


# 3. SciPy linregress
print("\n2. SCIPY LINREGRESS")

regr_results = sp.stats.linregress(x, y)

print(regr_results)


# 4. Statsmodels OLS
print("\n3. STATSMODELS OLS")

X = sm.add_constant(x)

lin_model = sm.OLS(y, X)
ols_results = lin_model.fit()

print("Coefficients:", ols_results.params)
print(ols_results.summary())


# 5. Scikit-learn LinearRegression
print("\n4. SCIKIT-LEARN LINEAR REGRESSION")

X_sklearn = x.reshape(-1, 1)

linmodel = linear_model.LinearRegression(
    fit_intercept=True
)

linmodel.fit(X_sklearn, y)

print("Slope:", linmodel.coef_[0])
print("Intercept:", linmodel.intercept_)
print("R-squared:", linmodel.score(X_sklearn, y))

# Predict a new value
new_gdp = np.array([[50000]])

prediction = linmodel.predict(new_gdp)

print("Predicted life satisfaction:", prediction[0])


# 6. Seaborn regplot
print("\n5. SEABORN REGPLOT")

fig, ax = plt.subplots(figsize=(10, 6))

sns.regplot(
    x=x,
    y=y,
    ci=95,
    order=1,
    seed=1,
    truncate=False,
    ax=ax
)

ax.set_xlabel("GDP per capita 2015 (USD)")
ax.set_ylabel("Life Satisfaction Value")
ax.set_title("Seaborn Regression Plot")

plt.show()