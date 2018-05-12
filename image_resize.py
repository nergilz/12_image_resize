import argparse
from PIL import Image
import os


def get_image_resize_to_scale(image_handler, scale):

    x_size, y_size = image_handler.size
    x_size = int(x_size * scale)
    y_size = int(y_size * scale)
    return image_handler.resize((x_size, y_size))


def get_image_resize_to_width_height(image_handler, width=None, height=None):

    x_size, y_size = image_handler.size
    if width is not None:
        x_size = width
    if height is not None:
        y_size = height
    return image_handler.resize((x_size, y_size))


def save_image_resizing(path_to_original, path_to_result, image_out):

    x_size, y_size = image_out.size
    file_name_with_path, file_extension = os.path.splitext(path_to_original)
    file_name = os.path.split(file_name_with_path)[1]
    out_file_name = '{}__{}x{}.{}'.format(
        file_name,
        x_size,
        y_size,
        file_extension
        )
    image_out.save(os.path.join(path_to_result, out_file_name))


def open_origin_image(path_to_original):
    return Image.open(path_to_original)


def checking_arguments(scale, width, height):
    parser_error = argparse.ArgumentParser(description='errors in parameters')

    if scale and (width or height):
        raise parser_error.error('ERROR: scale width height - together')

    if not any([scale, width, height]):
        raise parser_error.error('ERROR: no parameters in arguments')


def get_arguments():

    parser = argparse.ArgumentParser(
        description='Path arguments for resize image'
        )
    parser.add_argument('path',
                        help='Path to the original image')
    parser.add_argument('--output',
                        required=False,
                        default='.',
                        help='Path to the modified image')
    parser.add_argument('--width',
                        type=int,
                        required=False,
                        help='Image width')
    parser.add_argument('--height',
                        type=int,
                        required=False,
                        help='Image height')
    parser.add_argument('--scale',
                        type=float,
                        required=False,
                        help='Magnification factor')
    return parser.parse_args()


if __name__ == '__main__':
    arguments = get_arguments()

    try:
        checking_arguments(arguments.scale, arguments.width, arguments.height)
        image_handler = open_origin_image(arguments.path)

        if arguments.scale:
            image_out = get_image_resize_to_scale(
                image_handler,
                arguments.scale
                )
            save_image_resizing(
                arguments.path,
                arguments.output,
                image_out
                )

        if arguments.width or arguments.height:
            image_out = get_image_resize_to_width_height(
                image_handler,
                arguments.width,
                arguments.height
                )
            save_image_resizing(
                arguments.path,
                arguments.output,
                image_out
                )

    except IOError as error:
        print(' ERROR: {}'.format(error))
