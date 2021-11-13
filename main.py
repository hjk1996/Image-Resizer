from resizer import *
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--src",
        type=str,
        required=True,
        help="The directory of the folder with the image to be resized.",
    )
    parser.add_argument(
        "--width", type=int, required=True, help="Width of a resized image"
    )
    parser.add_argument(
        "--height", type=int, required=True, help="Height of a resized image"
    )
    parser.add_argument(
        "--save_dir",
        type=str,
        required=False,
        default=None,
        help="A directory to store images.",
    )
    parser.add_argument(
        "--inplace",
        type=bool,
        required=False,
        default=False,
        help="Whether to save the images inplace or not.",
    )
    args = parser.parse_args()
    images, image_names, folder_name, file_list = open_images(args.src)
    images = resize_images(images, args.width, args.height)

    if args.inplace:
        inplace_save_images(images, file_list)
    elif args.save_dir is not None:
        save_images(images, image_names, folder_name, args.save_dir)
    else:
        save_images(images, image_names, folder_name)

    print("Done")
