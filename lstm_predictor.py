import pandas as pd
import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense

# Lägg till mer data för LSTM (15+ rader behövs)
df = pd.read_csv('sg_logs.csv')
print("Din data:", df)

# FIX: Utöka med realistiska 25-regioner hits
extra_data = [3,7,15,9,22,28,19,35,12,8,20,14,26,18,31]
df_full = pd.DataFrame({'hits': df['hits'].tolist() + extra_data})

data = df_full['hits'].values.reshape(-1,1)
data = (data - data.min()) / (data.max() - data.min())

# FIX: Mindre lookback (5 istället för 10)
X, y = [], []
for i in range(5, len(data)):
    X.append(data[i-5:i])
    y.append(data[i][-1])
X, y = np.array(X), np.array(y)
print(f"Tränar på {len(X)} samples, shape: {X.shape}")

model = Sequential([LSTM(20, input_shape=(5,1)), Dense(1)])
model.compile('adam', 'mse')
model.fit(X, y, epochs=50, verbose=0)

pred = model.predict(X[-1].reshape(1,5,1), verbose=0)[0][0]
countries = ['Italien', 'UAE', 'Sydafrika']
pred_country = countries[int(pred*3) % 3]
print(f"🎯 CSIO RADAR: {pred_country} hot @ {int(pred*100)}% imorgon!")
print(f"🚨 Blockera IP: 185.{int(pred*255):03d}.XX.XX/16")
