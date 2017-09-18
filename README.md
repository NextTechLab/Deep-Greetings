# Deep-Greetings
we generate deep greeting cards for the next major upcomin festival.
We use neural style transfer to generate the cover/background image of our greeting card/postcard and an LSTM model to generate text on the festival. 
We also use Augmented Reality to display a personalized greeting video of your choice on the card.

For neural style tranfers, the various style images we use for the festivals are:
1. Valentines day:
![alt text](style_images/romantic.jpg "Input image")
2. Independace Day:
![alt text](style_images/indian-flag-collage.jpg "Input image")
3.Halloween:
![alt text](style_images/scary.jpg "Input image")
4.Diwali:
![alt text](style_images/diwali.jpg "Input image")
5.Christmas:
![alt text](style_images/christmas.jpg "Input image")

The LSTM model is trained on the following text for the following festivals:
1. Valentines day:love poems
2.Independance Day:Freedom Speeches
3.Halloween: Horror stories and poems
4.Diwali: Diwali greetings
5.Christmas:Christmas Carols

to run the entire program, run main.py

INPUT:
1. path of the content image
2. path of the video

INPUT IMAGE:
![alt text](content_image/ss.png "Input image")
OUTPUT CARD USING HALLOWEEN FILTER:
![alt text](style_text.jpg "Output Image")
