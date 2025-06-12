import sys
import numpy as np
from tensorflow.keras.models import load_model

# Load trained model
model = load_model("pitstop_model.h5")

# Input args: circuit lap pitstop_num
circuit = int(sys.argv[1])
lap = int(sys.argv[2])
pitstop = int(sys.argv[3])

# Predict
input_data = np.array([[circuit, lap, pitstop]])
prediction = model.predict(input_data)
predicted_class = np.argmax(prediction)

# Map to label
labels = ['Bad', 'So-So', 'Good']
print(labels[predicted_class])

#print(f"Based on the model, this is a {labels[predicted_class]}", flush=True)
