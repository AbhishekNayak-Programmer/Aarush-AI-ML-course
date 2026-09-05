import tensorflow as tf 

train_data = tf.keras.utils.image_dataset_from_directory(
    "fruit_dataset/train",
    image_size=(256, 256),
    batch_size=32
)

test_data = tf.keras.utils.image_dataset_from_directory(
    "fruit_dataset/test",
    image_size=(256, 256),
    batch_size=32
)

print(train_data.class_names)

model = tf.keras.Sequential([
    tf.keras.layers.Rescaling(1./255),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dense(2, activation='softmax')
])

model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

model.fit(train_data, validation_data=test_data, epochs=10)

loss, accuracy = model.evaluate(test_data)
print("Accuracy: ", accuracy)
print("Loss: ", loss)
