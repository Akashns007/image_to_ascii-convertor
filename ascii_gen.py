from PIL import Image, ImageDraw, ImageFont, ImageEnhance

import math

#s = "`.-':_,^=;><+!rc*/z?sLTv)J7(|Fi{\C}fI31tlu[neoZ5Yxjya]2ESwqkP6h9d4VpOGbUAKXHm8RD#$Bg0MNWQ%&@"
#chars = s[::-1]
chars = "#Wo- "[::-1]
#chars = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{\}[]?-_+~<>i!lI;:,\"^`'."
#chars = "!\"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~"
#chars = ".-:;+=oO*#%@$0123456789"


charArray = list(chars)
charLength = len(charArray)
interval = charLength/256

ScaleFactor = 0.2 #adjust scale

#brightness_factor = 0.4  # Adjust brightness here(reducing the factor increases brightness)

oneCharWidth = 8
oneCharHeight = 18


def getchar(h):
    return charArray[math.floor(h*interval)]

text_file = open("output.txt","w")

img = Image.open(input("give the image name: "))
 
fnt = ImageFont.truetype('c:\\Windows\\Fonts\\lucon.ttf', 15)
 

width, height = img.size
img = img.resize((int(ScaleFactor*width), int(ScaleFactor*height*(oneCharWidth/oneCharHeight))), Image.NEAREST)
width, height = img.size
pix = img.load()

print(width,height)


outputImage = Image.new('RGB', (oneCharWidth* width, oneCharHeight* height), color=(0,0,0))
d = ImageDraw.Draw(outputImage)

for i in range(height):
    for j in range(width):
        r,g,b = pix[j, i] #rgb values
        h = int(r/3 + g/3 + b/3) #mean_value
        #h = min(255, int(h * brightness_factor))  # Adjust brightness
        pix[j,i] = (h,h,h) #filling grey color
        text_file.write(getchar(h))
        d.text((j*oneCharWidth, i*oneCharHeight), getchar(h), font = fnt, fill = (r,g,b))
        
    text_file.write('\n')
        
#outputImage.save('output.png')


brightness_factor = 3  # Adjust brightness factor here

# Create an ImageEnhance object with the output image
enhancer = ImageEnhance.Brightness(outputImage)

# Apply brightness enhancement
brightened_image = enhancer.enhance(brightness_factor)

# Save or display the brightened image
brightened_image.save('output.png')


        
        