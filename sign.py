<<<<<<< HEAD
import cv2   #opencv
import time  #time delay between actions
import os    #file path
import uuid  #name image

image_path = "TensorFlow\workspace\images\collectedimages"

labels = ['hello', 'thanks', 'yes', 'no', 'iloveyou']
number_imgs = 15  #number of images, 13 for training, 2 for testing

for label in labels:
    os.makedirs(os.path.join(image_path, label), exist_ok=True)
    cap = cv2.VideoCapture(0)
    print("Collecting images for {}".format(label))
    time.sleep(5)
    for imgname in range(number_imgs):
        ret, frame = cap.read()
        imgname = os.path.join(image_path, label, label +"." + "{}.jpg".format(str(uuid.uuid1())))
        cv2.imwrite(imgname, frame)
        cv2.imshow("frame",frame)
        time.sleep(2)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
=======
import cv2   #opencv
import time  #time delay between actions
import os    #file path
import uuid  #name image

image_path = "TensorFlow\workspace\images\collectedimages"

labels = ['hello', 'thanks', 'yes', 'no', 'iloveyou']
number_imgs = 15  #number of images, 13 for training, 2 for testing

for label in labels:
    os.makedirs(os.path.join(image_path, label), exist_ok=True)
    cap = cv2.VideoCapture(0)
    print("Collecting images for {}".format(label))
    time.sleep(5)
    for imgname in range(number_imgs):
        ret, frame = cap.read()
        imgname = os.path.join(image_path, label, label +"." + "{}.jpg".format(str(uuid.uuid1())))
        cv2.imwrite(imgname, frame)
        cv2.imshow("frame",frame)
        time.sleep(2)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
>>>>>>> 912a429637f41db8ef7c9cc07593ab1c19971a16
