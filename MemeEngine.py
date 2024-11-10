from PIL import Image, ImageDraw, ImageFont

class MemeEngine():

    def __init__(self, output_dir):
        self.output_dir = output_dir
        
    def make_meme(self, img_path, text, author, width=500) -> str:
        """ create a imgage with a text greeting
        
        Arguments:
            img_path {str} -- the file location for the input image
            text {str} -- the text to be placed on the image
            author {str} -- the author of the meme
            width {int} -- the width of image 
        Returns:
            str -- the file path to the output imgage
        """
        img = Image.open(img_path)
        
        ratio = width/float(img.size[0])
        height = int(ratio*float(img.size[1]))
        img = img.resize((width, height), Image.NEAREST)

        if text is not None:
            draw = ImageDraw.Draw(img)
            draw.text((10, 10), f'{text} \n - {author}', fill='white', font_size=40)
        
        out_path = img_path.split('/')[-1]
        img.save(f'{self.output_dir}/{out_path}')
        return f'{self.output_dir}/{out_path}'

