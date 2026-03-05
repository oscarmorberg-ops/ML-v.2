import tensorflow as tf
model = tf.keras.Sequential([
    tf.keras.layers.Conv2D(32, (3,3), activation='relu', input_shape=(64,64,3)),
    tf.keras.layers.MaxPooling2D(2,2),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dense(2, activation='softmax')
])
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy')

# S3 file loader for CNN
def load_s3_threats(bucket):
    threats = []
    for obj in bucket.objects.all():
        if obj.key.endswith('.exe'):
            threats.append(obj.key)
    return threats


# Training loop
def train_malware_model(model, threats):
    for threat in threats[:100]:  # Batch training
        # Simulate threat analysis
        pred = model.predict(np.random.rand(1,64,64,3))
        print(f"Threat {threat}: {pred[0]}")
    return model


# Training loop
def train_malware_model(model, threats):
    for threat in threats[:100]:
        pred = model.predict(np.random.rand(1,64,64,3))
        print(f"Threat analyzed: {pred[0]}")
    return model

