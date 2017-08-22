from PIL import Image
#char_string = 'abcdefghijklmnopqrstuvwxyz'
#
char_string="人生自古谁无死留取丹心照汗青感统恶鬼争高下不向霸王让寸分"

def rgb2char(r,g,b):
    length=len(char_string)
    gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)

    unit=(256.0+1)/length;

    ##the corresponding char from r,g,b

    index=int(gray/unit)
    return char_string[index]


def preprocess(image_path,delta=100):
    img=Image.open(image_path)
    height,width=img.size

    if height > width:
        max_val=height

    else:
        max_val=width


    scale=max_val/delta

    width, height=int(width/scale), int(height/scale)

    img=img.resize((width,height))


    return img



def img_to_char(img_object, save_path):
    text=""
    width,height=img_object.size


    for i in range(height):
        line=""
        for j in range(width):
            line+=rgb2char(*img_object.getpixel((j,i)))
        text+=line+"\n"


    with open(save_path,"w+",encoding='utf-8') as f:
        f.write(text)


img_object=preprocess("test.jpg")
img_to_char(img_object,"test.txt")
