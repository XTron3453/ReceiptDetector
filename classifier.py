import numpy as np
import matplotlib.pyplot as plt
import pprint
import os
from PIL import Image
from sklearn.tree import DecisionTreeClassifier
from sklearn import datasets, svm, metrics
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
import random

#11
divisor = 11

tar_path = r"C:\Users\theyo\Documents\PythonProjects\FridgeStash\Target Receipts"
wal_path = r"C:\Users\theyo\Documents\PythonProjects\FridgeStash\Walmart Receipts"
#Can make these paths dynamic when later integrated with the application

tar_imgs = list()
wal_imgs = list()
all_imgs = list()

def get_pics(used_path, used_list):
	for image_path in os.listdir(used_path):
		input_path = os.path.join(used_path, image_path)
		im = Image.open(input_path, 'r').convert("L")
		used_list.append(im)
		all_imgs.append(im)

def get_pic_av(new_av=(0, 0), counter=0):
	width, height = all_imgs[counter].size
	if counter == (len(all_imgs) - 1):
		return (int(new_av[0] / len(all_imgs)), int(new_av[1] / len(all_imgs)))
	else:
		return get_pic_av(new_av=(new_av[0] + width, new_av[1] + height), counter=counter + 1)

get_pics(tar_path, tar_imgs)
get_pics(wal_path, wal_imgs)

width, height = get_pic_av()

random.sample(range(len(all_imgs)), len(all_imgs))

all_imgs = list(map(lambda img : img.resize((width // divisor, height // divisor), Image.ANTIALIAS).getdata(), all_imgs))

x = np.array(all_imgs)
tar_y = [[0] for tar in tar_imgs]
wal_y = [[1] for wal in wal_imgs]
tar_y.extend(wal_y)
y = np.array(tar_y)

clf = DecisionTreeClassifier()
svc = svm.SVC(gamma=0.001)

X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.33, random_state=32)

print("Fed\n")

clf.fit(X_train, y_train)
svc.fit(X_train, y_train)

predict_img = Image.open("06.2.jpg", 'r').convert("L")

prediction = np.array(predict_img.resize((width // divisor, height // divisor), Image.ANTIALIAS).getdata())

print("\n Size = \n", divisor)
print(clf.score(X_test, y_test))
print(svm.SVC.score(svc, X_test, y_test))

#print(clf.predict(prediction.reshape(1, -1)))
#print(clf.predict_log_proba(prediction.reshape(1, -1)))
#print(clf.predict_proba(prediction.reshape(1, -1)))

#print("\n SVM \n")

#print(clf.predict(prediction.reshape(1, -1)))
#print(clf.predict_log_proba(prediction.reshape(1, -1)))
#print(clf.predict_proba(prediction.reshape(1, -1)))