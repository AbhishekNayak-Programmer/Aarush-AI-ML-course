from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

image = Image.open("apple.jpg")

image = image.convert("RGB")

image = image.resize((128, 128))

image_array = np.array(image)

image_array = image_array / 255.0

print(image_array.shape)

plt.imshow(image_array)
plt.axis("off")
# plt.show()

import tensorflow as tf

train_data = tf.keras.utils.image_dataset_from_directory(
    "fruit_dataset/train",
    image_size=(128, 128),
    batch_size=32
)

test_data = tf.keras.utils.image_dataset_from_directory(
    "fruit_dataset/test",
    image_size=(128, 128),
    batch_size=32
)

print(train_data.class_names)


model = tf.keras.Sequential([
    tf.keras.layers.Rescaling(1./255),

    tf.keras.layers.Flatten(),

    tf.keras.layers.Dense(128, activation="relu"),

    tf.keras.layers.Dense(2, activation="softmax")
])

model.compile(
    optimizer="adam",
    loss="sparse_categorical_crossentropy",
    metrics=["accuracy"]
)

model.fit(
    train_data,
    validation_data=test_data,
    epochs=10
)

loss, accuracy = model.evaluate(test_data)

print("Accuracy:", accuracy)


# /////

# ==========================================
# TEST A SINGLE IMAGE
# ==========================================

from PIL import Image
import numpy as np

# Load the image we want to test
image = Image.open("fruit_dataset/test/apple/apple3.jpg")

# Convert image to RGB
image = image.convert("RGB")

# Resize to the same size used during training
image = image.resize((128, 128))

# Convert image to numpy array
image_array = np.array(image)

# Add batch dimension
# (128, 128, 3) -> (1, 128, 128, 3)
image_array = np.expand_dims(image_array, axis=0)

# Predict
prediction = model.predict(image_array)

print("Prediction:", prediction)

# Get the class with the highest probability
predicted_class = np.argmax(prediction[0])

# Get class names
class_names = train_data.class_names

print("Predicted class:", class_names[predicted_class])