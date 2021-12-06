from docutils.nodes import classifier
from keras import models
from keras.preprocessing.image import ImageDataGenerator
from keras.models import Sequential
from keras.layers import Conv2D
from keras.layers import MaxPooling2D
from keras.layers import Flatten
from keras.layers import Dense

base_dir = 'E:/Experiment/2021.03.LungSound/0.data'
train_dir = base_dir + '/' + 'ALL/train'
test_dir = base_dir + '/' + 'ALL/test'

train_generator = ImageDataGenerator(rescale=1./255, shear_range=0.5, zoom_range=0.5, horizontal_flip=True)
test_generator = ImageDataGenerator(rescale=1./255)
train_set = train_generator.flow_from_directory(train_dir, target_size=(64, 64), batch_size=32, class_mode='categorical')
test_set = test_generator.flow_from_directory(test_dir, target_size=(64, 64), batch_size=32, class_mode='categorical')

model = models.Sequential()
model.add(Conv2D(32, (3, 3), input_shape=(64, 64, 3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Conv2D(32, (3, 3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Flatten())
model.add(Dense(128, activation='relu'))
model.add(Dense(4, activation='softmax'))
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

model.fit_generator(train_set, steps_per_epoch=10, epochs=30, validation_data=test_set, validation_steps=5)
scores = model.evaluate_generator(test_set, steps=5)
acc = round(scores[1]*100, 1)
print('accuracy : ' + str(acc))
