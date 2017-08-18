
from PIL import Image,ImageDraw,ImageFont
image=Image.open('style.jpg')
w,h=image.size

draw=ImageDraw.Draw(image)

text="As I look around I see the crumbling ruins of a proud civilization strewn like a vast heap of futility. And yet I shall not commit the grievous sin of losing faith in Man. I would rather look forward to the opening of a new chapter in his history after the cataclysm is over and the atmosphere rendered clean with the spirit of service and sacrifice. Perhaps that dawn will come from this horizon, from the East where the sun rises. A day will come when unvanquished Man will retrace his path of conquest, despite all barriers, to win back his lost human heritage"

font=ImageFont.truetype('arial.ttf',14)
t_w,t_h=draw.textsize(text,font)

margin=20

x=w-t_w-margin
y=h-t_h-margin

draw.text((x,y),text,font)

image.save("style_text.jpg")
