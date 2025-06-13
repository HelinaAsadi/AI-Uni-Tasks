import sys
import numpy as np
from tensorflow.keras.models import load_model

# loading the trained, saved model
model = load_model("F1_trained_model.h5")

# READING INPUTS from PROLOG; circuit , lap , pitstop_number
circuit = int(sys.argv[1])
lap = int(sys.argv[2])
pitstop = int(sys.argv[3])

# PREDICTION
input_data = np.array([[circuit, lap, pitstop]])  # gathering inputs
prediction = model.predict(input_data)            # running them through model
predicted_class = np.argmax(prediction)           # receiving the predicted class

# MAPPING the class to a label
labels = ['BAD TIME TO BOX', 'SO-SO', 'GOOD TIME TO BOX']
print(labels[predicted_class])




