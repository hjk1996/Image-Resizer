from PIL import Image
import multiprocessing
import os
from glob import glob
from typing import List, Tuple
from functools import partial


def open_image(img_path: str) -> Image.Image:
    return Image.open(img_path)


def open_images(folder_dir: str) -> Tuple[List[Image.Image], List[str], str, List[str]]:
    folder_name = folder_dir.split("\\")[-1]
    formats = ["*.jpg", "*.png", "*.jpeg"]
    file_list = []
    for format in formats:
        file_list.extend(glob(os.path.join(folder_dir, format)))
    image_names = [file_path.split("\\")[-1] for file_path in file_list]

    pool = multiprocessing.Pool()
    results = pool.map(open_image, file_list)
    return results, image_names, folder_name, file_list


def resize_image(image: Image.Image, w: int, h: int) -> Image:
    return image.resize((w, h))


def resize_images(images: List[Image.Image], w: int, h: int) -> List[Image.Image]:
    resize_func = partial(resize_image, w=w, h=h)
    pool = multiprocessing.Pool()
    results = pool.map(resize_func, images)
    return results


def save_image(image: Image.Image, image_name: str) -> None:
    image.save(image_name)


def save_images(
    images: List[Image.Image], image_names: List[str], folder_name: str, save_dir=None
) -> None:

    if save_dir is not None:
        if not os.path.exists(save_dir):
            os.makedirs(save_dir)
        image_names = [os.path.join(save_dir, image_name) for image_name in image_names]

    else:
        save_dir = os.path.join("resized_images", folder_name)
        if not os.path.exists(save_dir):
            os.mkdir(save_dir)
        image_names = [os.path.join(save_dir, image_name) for image_name in image_names]

    pool = multiprocessing.Pool()
    _ = pool.starmap(save_image, zip(images, image_names))


def inplace_save_images(images: List[Image.Image], file_list: List[str]) -> None:
    pool = multiprocessing.Pool()
    _ = pool.starmap(save_image, zip(images, file_list))
