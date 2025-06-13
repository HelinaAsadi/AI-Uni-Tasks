import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.utils import to_categorical

# Loading the clean data ready to train the model from
df = pd.read_csv('ready_data.csv')

# features
X = df[['Circuit', 'Lap', 'TotalPitStops']].values
y = df['Label'].values

# normalizing
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# nne-hot encode the labels (for 3 output classes of good , so-so , bad )
y_categorical = to_categorical(y, num_classes=3)

# splitting into training sets and testing sets
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y_categorical, test_size=0.2, random_state=42)

# NN
from tensorflow.keras import Input

model = Sequential([
    Input(shape=(3,)),
    Dense(16, activation='relu'),
    Dense(8, activation='relu'),
    Dense(3, activation='softmax')    # for the 3 output classes
])

# COMPILING
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# TRAINING
model.fit(X_train, y_train, epochs=50, batch_size=8, validation_data=(X_test, y_test))

# SAVING; to be used by the prolog system
model.save("F1_trained_model.h5")


