import os
import cv2

photos_library = input("Input your photos library's name: ")
print("Library's name",photos_library)

if not os.path.exists(photos_library):
    os.mkdir(photos_library)

N = 100                 # number of photos
count = 0     

camera = cv2.VideoCapture(0)            # Read from camera that has id 0

while count < N:
    # Read from camera 
    ret,image = camera.read()

    if ret:
        cv2.imshow("Camera",image)

        count = count + 1
        file_name = "Anh" + str(count) +".png"
        file_path = os.path.join(photos_library,file_name)
        # save photos to library
        cv2.imwrite(file_path,image)
        if cv2.waitKey(1) == ord("o"):
            break

camera.release()
cv2.destroyAllWindows()
