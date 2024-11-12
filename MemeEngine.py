"""This is meme engine module."""
import random
import textwrap

from PIL import Image, ImageDraw


class MemeEngine():
    """Edit photos."""

    def __init__(self, output_dir):
        """Initialize class with path out file."""
        self.output_dir = output_dir

    def make_meme(self, img_path, text, author, width=500) -> str:
        """Create a imgage with a text greeting.

        Arguments:
            img_path {str} -- the file location for the input image
            text {str} -- the text to be placed on the image
            author {str} -- the author of the meme
            width {int} -- the width of image
        Returns:
            str -- the file path to the output imgage.
        """
        img = Image.open(img_path)

        ratio = width/float(img.size[0])
        height = int(ratio*float(img.size[1]))
        img = img.resize((width, height), Image.NEAREST)

        cmwidth = round(width / 37.79527559055, 0)
        cmheight = round(height / 37.79527559055, 0)
        contain = text
        if text is not None:
            draw = ImageDraw.Draw(img)

            if len(text) > cmwidth:
                wrapper = textwrap.TextWrapper(width=int(cmwidth) * 2)
                contain_wrapper = wrapper.wrap(text=text)
                contain = ''
                for str in contain_wrapper:
                    contain = f'{contain} \n {str}'

            draw.text((random.uniform(0, cmwidth * 2),
                       random.uniform(0, cmheight * 10)),
                      f'{contain}\n - {author}', fill='white', font_size=30)

        out_path = img_path.split('/')[-1]
        img.save(f'{self.output_dir}/{out_path}')
        return f'{self.output_dir}/{out_path}'
