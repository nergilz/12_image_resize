import argparse
from PIL import Image
import os
import sys


def get_arguments():

    parser = argparse.ArgumentParser(
        description='Path arguments for resize image'
        )
    parser.add_argument(
        'path',
        help='Path to the original image'
        )
    parser.add_argument(
        '--output',
        required=False,
        default='.',
        help='Path to the modified image'
        )
    parser.add_argument(
        '--width',
        type=int,
        required=False,
        help='Image width'
        )
    parser.add_argument(
        '--height',
        type=int,
        required=False,
        help='Image height'
        )
    parser.add_argument(
        '--scale',
        type=float,
        required=False,
        help='Change of scale image'
        )
    return parser.parse_args()


def check_arguments(scale, width, height, output):
    parser = argparse.ArgumentParser(description='Errors in parameters')

    if scale and (width or height):
        parser.error('ERROR: scale width height should not be together')

    if not any([scale, width, height]):
        parser.error('ERROR: no parameters in arguments')

    if not os.path.isdir(output):
        parser.error('ERROR: not find directory {}'.format(output))


def get_new_size(x_size, y_size, scale, width, height):

    if scale:
        x_size = int(x_size * scale)
        y_size = int(y_size * scale)
        return x_size, y_size

    if width and height:
        return width, height

    if width and not height:
        ratio = width / x_size
        height = int(y_size * ratio)
        return width, height

    if height and not width:
        ratio = height / y_size
        width = int(x_size * ratio)
        return width, height


def get_file_name_out(x_size, y_size, path_to_original):

    file_fullname = os.path.basename(path_to_original)
    file_name, file_extension = os.path.splitext(file_fullname)

    return '{}__{}x{}.{}'.format(
        file_name,
        x_size,
        y_size,
        file_extension
        )


if __name__ == '__main__':
    arguments = get_arguments()

    check_arguments(
        arguments.scale,
        arguments.width,
        arguments.height,
        arguments.output
        )
    try:
        image = Image.open(arguments.path)

    except IOError as error:
        print('ERROR: {}'.format(error))
        sys.exit(1)

    x_base, y_base = image.size
    x_new, y_new = get_new_size(
        x_base,
        y_base,
        arguments.scale,
        arguments.width,
        arguments.height
        )
    file_name_out = get_file_name_out(
        x_new,
        y_new,
        arguments.path
        )

    image = image.resize((x_new, y_new), Image.ANTIALIAS)
    image.save(os.path.join(arguments.output, file_name_out))
