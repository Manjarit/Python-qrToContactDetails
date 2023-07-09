'''
#Lets pass our details and build our own bcard
#save in the image format
'''

from segno import helpers


qr = helpers.make_mecard(name = "Manjari Thiru",
                         email = "manjaridecember@gmail.com",
                         phone = "+91 70119453144")

qr.save("myqr.png",scale = 10)
