from io import BytesIO

from PIL import Image, ImageEnhance, ImageFilter


def generate_thumbnail(django_image_field):
    output = BytesIO()

    with Image.open(fp=django_image_field) as original:
        original.load()

    if original.height / original.width != 0.5625:
        thumb_w = 800
        thumb_h = 450
        original.thumbnail(size=(thumb_w, thumb_h), resample=Image.Resampling.LANCZOS)

        # Check if thumbnail scaled properly:
        if original.width != thumb_w and original.height != thumb_h:
            diff_w = abs(thumb_w - original.width)
            diff_h = abs(thumb_h - original.height)

            if diff_w < diff_h:
                original = original.resize(size=(thumb_w, original.height))
            else:
                original = original.resize(size=(original.width, thumb_h))

        background = Image.new(mode='RGB', size=(800, 450), color=(52, 58, 64))

        pos = (
            (background.width - original.width) // 2,
            (background.height - original.height) // 2
        )

        background.paste(im=original, box=pos)
        original = background

    else:
        original.thumbnail(size=(800, 450), resample=Image.Resampling.LANCZOS)

    original.save(output, format='PNG')

    output.seek(0)
    return output
