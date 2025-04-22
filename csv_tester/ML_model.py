from sklearn.linear_model import LinearRegression
#training Data:     House sizes (x) and Prices (y)
x = [[1000],[1500],[2000],[2500],[3000]]
y = [200000,250000,300000,350000,400000]
#Create and trian model
model = LinearRegression()
model.fit(x,y)
#Pridict the price for a 1900 sqft house:- 
prediction = model.predict([[1900]])
print(f"Predicted Price:- ${prediction[0]:.2f}")

