import pandas as pd
from sklearn.datasets import fetch_california_housing
from sklearn.ensemble import RandomForestRegressor
import pickle

housing = fetch_california_housing(as_frame=True)

X = housing.data[['MedInc', 'HouseAge', 'AveRooms', 'AveBedrms', 'Population']]

y = housing.target 
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X, y)

print("3. Model save ho raha hai...")
with open('model.pkl', 'wb') as file:
    pickle.dump(model, file)
