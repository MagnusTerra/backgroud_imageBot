from rembg import remove
from rembg import *

def backgroud_image(image: str=None):
    name = '\n'.join(image.split('/')[-1].rsplit('.', 1)[:-1])

    #Leemos imagen input y Python procede a generarte una nueva imagen sin fondo en output
    with open(image, 'rb') as i:
        with open(f'{name}_backgroupless.png', 'wb') as o:
            input = i.read()
            model_name = "isnet-general-use"
            session = new_session(model_name)
            output = remove(input, session=session)

            o.write(output)
    
    return f'{name}_backgroupless.png'