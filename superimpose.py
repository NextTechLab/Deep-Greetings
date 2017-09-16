from PIL import Image,ImageDraw,ImageFont
import random
from auto_fest import get_fest
fest=get_fest()
temp=fest+"_"+".txt"
import temp

def superimpose():
    image=Image.open('output.jpg')
    w,h=image.size
    var=random.randint(0, 11)
    draw=ImageDraw.Draw(image)

    text=temp.(dict+var)[1]
    text1=temp.(dict+var)[2]
    text2=temp.(dict+var)[3]
    text3=temp.(dict+var)[4]

    font = ImageFont.truetype("/usr/share/fonts/truetype/freefont/FreeSans.ttf", 30)

    t_w,t_h=draw.textsize(text,font)
    t_w1,t_h1=draw.textsize(text1,font)
    t_w2,t_h2=draw.textsize(text2,font)
    t_w3,t_h3=draw.textsize(text3,font)

    margin=20

    x=w-t_w-margin
    y=h-t_h-margin
    w, h = draw.textsize(text)
    #draw.text(((w-t_w)/2,(h-t_h)/2), text, fill="black")
    draw.text((150,210),text,(255,255,255),font=font)
    draw.text((150+(t_w-t_w1)/2,240),text1,(255,255,255),font=font)
    draw.text((150+(t_w1-t_w2)/2,270),text2,(255,255,255),font=font)
    draw.text((150+(t_w2-t_w3)/2,300),text3,(255,255,255),font=font)
    #draw.text([(x,y)],text,font)

    image.save("./style_text.jpg")
