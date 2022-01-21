import os
import imageio

myfiles = os.listdir('Pylearn/Session 8/images')
print(myfiles)
images = []
for i in range(len(myfiles)):
  image = imageio.imread('Pylearn/Session 8/images/' + myfiles[i])
  images.append(image)

imageio.mimsave('imam.gif', images)