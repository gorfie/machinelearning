import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

df = pd.read_csv('data.csv')

#separate the other attributes from the predicting attribute
x = df.drop('Price',axis=1)
#separate the predicting attribute into Y for model training 
y = df['Price']

# splitting the data
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state = 42)

# creating an object of LinearRegression class
LR = LinearRegression()
# fitting the training data
LR.fit(x_train,y_train)

# Make predictions using the testing set
y_prediction =  LR.predict(x_test)

# The coefficients
print("Coefficients: \n", LR.coef_)
# The mean squared error
print("Mean squared error: %.2f" % mean_squared_error(y_test, y_prediction))
# The coefficient of determination: 1 is perfect prediction
print("Coefficient of determination: %.2f" % r2_score(y_test, y_prediction))

x_unit = {'Rooms': [2],
                'Bathrooms': [2],
                'Car_Parks': [2],
                'Property_Type': [1],
                'Size': [690],
                'Furnishing': [2]       
                }
x_df = pd.DataFrame(x_unit,columns=['Rooms','Bathrooms','Car_Parks','Property_Type','Size','Furnishing'])
new_y_prediction =  LR.predict(x_df)

print(new_y_prediction)

# Plot outputs
plt.scatter(x_test['Rooms'], y_test, color="black")
plt.plot(x_test['Rooms'], y_prediction, color="blue", linewidth=3)

plt.xticks(())
plt.yticks(())

plt.show()