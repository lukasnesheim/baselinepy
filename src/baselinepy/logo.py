# function imports
from baselinepy.theme import load_color, load_style
from PIL import Image, ImageDraw

def add_logo(image_path: str, logo_height: int = 80, logo_width_ratio: float = 0.20):
    try:
        color = load_color()
        style = load_style()["logo"]

        # load the image
        old_image = Image.open(image_path)
        if not old_image:
            raise RuntimeError(f"No image found for the image path: {image_path}")
        
        old_image_width, old_image_height = old_image.size
        
        # set logo size
        logo_width = round(old_image_width * logo_width_ratio)
        
        # create the new image
        new_image = Image.new("RGB", (old_image_width, old_image_height + logo_height), color["background"])

        # add the logo to the new image
        ImageDraw.Draw(new_image).rectangle([0, 0, logo_width, logo_height], fill=style["color"])

        # add the old image to the new image
        new_image.paste(old_image, (0, logo_height))

        # save the new image
        new_image.save(image_path)
        
    except Exception as ex:
        print(f"Failed to add the Baseline logo to an image.\nException: {ex}")