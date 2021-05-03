import face_recognition as f
import cv2 as c
import numpy


i=f.load_image_file("s5.jpg")
i=c.cvtColor(i,c.COLOR_BGR2RGB)
it=f.load_image_file("s4.jpg")
it=c.cvtColor(it,c.COLOR_BGR2RGB)


img=f.face_locations(i)[0]
en=f.face_encodings(i)[0]
c.rectangle(i,(img[3],img[0]),(img[1],img[2]),(255,0,255),2)

imgt=f.face_locations(it)[0]
ent=f.face_encodings(it)[0]
c.rectangle(i,(imgt[3],imgt[0]),(imgt[1],imgt[2]),(255,0,255),2)

r=f.compare_faces([en],ent)
a=f.face_distance([en],ent)
print(r,a)
c.putText(it,f'{r}{a}',(50,50),c.FONT_HERSHEY_COMPLEX,1,(0,0,255),2)

c.imshow("shakira",i)
c.imshow("kiara",it)
c.waitKey(0)
