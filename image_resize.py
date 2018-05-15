import argparse
from PIL import Image
import os


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


def checking_arguments(scale, width, height):
    parser = argparse.ArgumentParser(description='Errors in parameters')

    if scale and (width or height):
        parser.error('ERROR: scale width height should not be together')

    if not any([scale, width, height]):
        parser.error('ERROR: no parameters in arguments')


def get_resize_by_scale(x_base, y_base, scale):

    x_size = int(x_base * scale)
    y_size = int(y_base * scale)
    return x_size, y_size


def get_resize_by_width_height(width, height):
    return width, height


def save_image_resizing(path_to_original, path_to_result, image_out):

    if os.path.isdir(path_to_result):
        x_size, y_size = image_out.size
        file_fullname = os.path.basename(path_to_original)
        file_name, file_extension = os.path.splitext(file_fullname)
        out_file_name = '{}__{}x{}.{}'.format(
            file_name,
            x_size,
            y_size,
            file_extension
            )
        image_out.save(os.path.join(path_to_result, out_file_name))
    else:
        print('ERROR: not find directory "{}"'.format(path_to_result))


if __name__ == '__main__':
    arguments = get_arguments()
    checking_arguments(arguments.scale, arguments.width, arguments.height)

    try:
        image = Image.open(arguments.path)
        x_size, y_size = image.size

        if arguments.scale:
            x_size, y_size = get_resize_by_scale(
                x_size,
                y_size,
                arguments.scale
                )

        if arguments.width or arguments.height:
            x_size, y_size = get_resize_by_width_height(
                arguments.width,
                arguments.height
                )

        image_out = image.resize((x_size, y_size))

        save_image_resizing(
            arguments.path,
            arguments.output,
            image_out
            )

    except IOError as error:
        print(' ERROR_IOError: {}'.format(error))
