import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.utils import to_categorical

# Load the cleaned data
df = pd.read_csv('pitstop_learning_data.csv')

# Features and labels
X = df[['Circuit', 'Lap', 'PitstopNumber']].values
y = df['Label'].values

# Normalize features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# One-hot encode the labels (for 3 output classes)
y_categorical = to_categorical(y, num_classes=3)

# Split into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y_categorical, test_size=0.2, random_state=42)

# Define the neural network
from tensorflow.keras import Input

model = Sequential([
    Input(shape=(3,)),
    Dense(16, activation='relu'),
    Dense(8, activation='relu'),
    Dense(3, activation='softmax')
])# 3 output classes

'''model = Sequential([
    Dense(16, input_shape=(3,), activation='relu'),
    Dense(8, activation='relu'),
    Dense(3, activation='softmax')  # 3 output classes
])
'''

# Compile the model
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# Train the model
model.fit(X_train, y_train, epochs=50, batch_size=8, validation_data=(X_test, y_test))


model.save("pitstop_model.h5")


# to predict for queries
import numpy as np
