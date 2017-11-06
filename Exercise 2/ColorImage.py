import numpy
import cv2
import sys

in1 = cv2.imread(sys.argv[1])

[b,g,r] = cv2.split(in1)

cv2.imwrite('B.png',b)
cv2.imwrite('G.png',g)
cv2.imwrite('R.png',r)

cv2.imshow('B channel',b)
cv2.imshow('G channel',g)
cv2.imshow('R channel',r)

print("BGR :\n",in1[20,25],"\nB: ",b.max(),"to ",b.min(),"\nG: ",g.max(),"to ",g.min(),"\nR: ",r.max(),"to ",r.min())


yin = cv2.cvtColor(in1, cv2.COLOR_BGR2YCR_CB)

[y,cb,cr] = cv2.split(yin)

cv2.imwrite('Y.png',y)
cv2.imwrite('Cb.png',cb)
cv2.imwrite('Cr.png',cr)

cv2.imshow('Y channel',y)
cv2.imshow('Cb channel',cb)
cv2.imshow('Cr channel',cr)

print("YCbCr:\n",yin[20,25],"\nY: ",y.max(),"to ",y.min(),"\nCb: ",cb.max(),"to ",cb.min(),"\nCr: ",cr.max(),"to ",cr.min())

hin = cv2.cvtColor(in1, cv2.COLOR_BGR2HSV)

[h,s,v] = cv2.split(hin)

cv2.imwrite('H.png',h)
cv2.imwrite('S.png',s)
cv2.imwrite('V.png',v)

cv2.imshow('H channel',h)
cv2.imshow('S channel',s)
cv2.imshow('V channel',v)

print("HSV:\n",hin[20,25],"\nY: ",h.max(),"to ",h.min(),"\nS: ",s.max(),"to ",s.min(),"\nV: ",v.max(),"to ",v.min())