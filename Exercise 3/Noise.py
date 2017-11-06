import numpy as np
import cv2
import sys



def add_gaussian_noise(image,mean,sigma):
	gauss = np.random.normal(mean,sigma,image.shape)
	gauss = gauss.reshape(image.shape)
	return np.add(image , gauss,image,casting='unsafe')

def add_salt_pepper(image,pa,pb):
	out=np.copy(image)
	coords = [np.random.randint(0, i - 1, int(pa*image.size))
			for i in image.shape]
	out[coords]=1
	coords = [np.random.randint(0, i - 1, int(pb*image.size))
			for i in image.shape]
	out[coords]=0
	return out


in1 = cv2.imread(sys.argv[1])

cv2.imshow("Original",in1)

n1 = add_gaussian_noise(in1,0,50)
cv2.imshow("Gaussian Noise",n1)


f1 = cv2.blur(np.copy(n1),(3,3))
cv2.imshow("Box filter", f1)
t = np.copy(n1)
f2 = cv2.medianBlur(t,3)
cv2.imshow("Box filter", f2)


f3 = cv2.GaussianBlur(np.copy(n1),(3,3),1.5)
cv2.imshow("Box filter", f3)


n1 = add_salt_pepper(in1,0.01,0.01)

f1 = cv2.blur(np.copy(n1),(3,3))
cv2.imshow("Box filter", f1)


f2 = cv2.medianBlur(np.copy(n1),3)
cv2.imshow("Box filter", f2)


f3 = cv2.GaussianBlur(np.copy(n1),(3,3),1.5)
cv2.imshow("Box filter", f3)

cv2.waitKey(0)












