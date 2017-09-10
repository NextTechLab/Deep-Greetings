
from PIL import Image,ImageDraw,ImageFont
image=Image.open('./results/4/5.jpg')
w,h=image.size

draw=ImageDraw.Draw(image)

text="in masks and gowns we haunt the street,"
text1="and knock on doors for trick or treat."
text2="tonight we are the king and queen,"
text3="for oh tonight it's halloween!"

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
