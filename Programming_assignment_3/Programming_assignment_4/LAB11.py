import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator

from tensorflow.keras.models import Sequential


data_dir = "C:/Users/vansh/OneDrive - Binghamton University/Desktop/GalaxyImages"

train_datagen = ImageDataGenerator(rescale=1./255,
                                   shear_range=0.2,
                                   zoom_range=0.2,
                                   horizontal_flip=True,
                                   validation_split=0.2)

train_generator = train_datagen.flow_from_directory(data_dir,
                                                    target_size=(150, 150),
                                                    batch_size=32,
                                                    classes=["Disk_Edge-on_BoxyBulge",
                                                             "Disk_Edge-on_NoBulge",
                                                             "Disk_Edge-on_RoundedBulge",
                                                             "Disk_Edge-on_LooseSpiral",
                                                             "Disk_Edge-on_MediumSpiral",
                                                             "Disk_Edge-on_No Spiral",
                                                             "Disk_Edge-on_TightSpiral",
                                                             "Smooth_Cigarshaped",
                                                             "Smooth_Completelyround",
                                                             "Smooth_in-betweenround"],
                                                    class_mode='categorical',
                                                    subset='training')

validation_generator = train_datagen.flow_from_directory(data_dir,
                                                         target_size=(150, 150),
                                                         batch_size=32,
                                                         classes=["Disk_Edge-on_BoxyBulge",
                                                                  "Disk_Edge-on_NoBulge",
                                                                  "Disk_Edge-on_RoundedBulge",
                                                                  "Disk_Edge-on_LooseSpiral",
                                                                  "Disk_Edge-on_MediumSpiral",
                                                                  "Disk_Edge-on_No Spiral",
                                                                  "Disk_Edge-on_TightSpiral",
                                                                  "Smooth_Cigarshaped",
                                                                  "Smooth_Completelyround",
                                                                  "Smooth_in-betweenround"],
                                                         class_mode='categorical',
                                                         subset='validation')


model = tf.keras.models.Sequential([
    tf.keras.layers.Conv2D(32, (3, 3), activation='relu', input_shape=(150, 150, 3)),
    tf.keras.layers.MaxPooling2D(2, 2),
    tf.keras.layers.Conv2D(64, (3, 3), activation='relu'),
    tf.keras.layers.MaxPooling2D(2, 2),
    tf.keras.layers.Conv2D(128, (3, 3), activation='relu'),
    tf.keras.layers.MaxPooling2D(2, 2),
    tf.keras.layers.Conv2D(128, (3, 3), activation='relu'),
    tf.keras.layers.MaxPooling2D(2, 2),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(512, activation='relu'),
    tf.keras.layers.Dense(10, activation='softmax')
])


model.compile(loss='categorical_crossentropy',
              optimizer='adam',
              metrics=['accuracy'])


history = model.fit(train_generator,
                    epochs=7,
                    validation_data=validation_generator)