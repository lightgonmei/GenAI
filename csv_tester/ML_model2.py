from sklearn.linear_model import LinearRegression

# Training Data: House sizes (X) and Prices (Y)
X = [[1000], [1500], [2000], [2500], [3000]]
Y = [200000, 250000, 300000, 350000, 400000]

# Create and train model
model = LinearRegression()
model.fit(X, Y)

# Predict price for a 1800 sqft house
prediction = model.predict([[1800]])
print(f"Predicted Price: ${prediction[0]:.2f}")
