import argparse
from PIL import Image
import os


def resize_scale_image(path_to_original, scale):

    image_handler = Image.open(path_to_original)
    x_size, y_size = image_handler.size
    x_size = int(x_size * scale)
    y_size = int(y_size * scale)
    return image_handler.resize((x_size, y_size))


def resize_width_height_image(path_to_original, width=None, height=None):

    image_handler = Image.open(path_to_original)
    x_size, y_size = image_handler.size
    if width is not None:
        x_size = width
    if height is not None:
        y_size = height
    return image_handler.resize((x_size, y_size))


def save_image(path_to_original, path_to_result, image_out):

    x_size, y_size = image_out.size
    file_name,  file_extension = os.path.basename(path_to_original).split('.')
    out_file_name = '{}__{}x{}.{}'.format(file_name, x_size, y_size, file_extension)
    image_out.save(os.path.join(path_to_result, out_file_name))


def get_arguments():

    parser = argparse.ArgumentParser(description='Path arguments for resize image')
    parser.add_argument('path', help='Path to the original image')
    parser.add_argument('--output', required=False, default='/', help='Path to the modified image')
    parser.add_argument('--width', type=int, required=False, help='Image width')
    parser.add_argument('--height', type=int, required=False, help='Image height')
    parser.add_argument('--scale', type=float, required=False, help='Magnification factor')
    return parser.parse_args()


def main():
    arguments = get_arguments()

    if arguments.scale and arguments.width or arguments.scale and arguments.height:
        raise Parameters_error('"width", "height" can not be specified together with "scale"')

    if arguments.width is None and arguments.scale is None and arguments.height is None:
        raise Parameters_error('no parameters to resize')

    if arguments.scale:
        image_out = resize_scale_image(
            arguments.path,
            arguments.scale
            )
        save_image(
            arguments.path,
            arguments.output,
            image_out
            )

    if arguments.width or arguments.height:
        image_out = resize_width_height_image(
            arguments.path,
            arguments.width,
            arguments.height
            )
        save_image(
            arguments.path,
            arguments.output,
            image_out
            )


if __name__ == '__main__':

    class Parameters_error(Exception):
        pass

    try:
        main()
    except IOError as error:
        print(' ERROR: {}'.format(error))
    except Parameters_error as error:
        print(' ERROR: {}'.format(error))
