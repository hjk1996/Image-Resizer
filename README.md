# Install

```
git clone https://github.com/hjk1996/instagram-image-crawler.git
```

# Run

The default storage path is a sub-folder of resized_images that is the same as the folder name containing the original image.

--src: The directory of the folder with the image to be resized.

--width: Width of a resized image.

--height: Height of a resized image.

--save_dir(optional): When you enter the storage path, images are stored in the input path. 

--inplace(optional: boolean): Whether to save the images inplace or not.


## Examples
```
python main.py --src ./your/image/folder/path --width 640 --height 640
```
```
python main.py --src ./your/image/folder/path --width 640 --height 640 --inplace True
```
```
python main.py --src ./your/image/folder/path --width 640 --height 640 --save_dir C:\Users
```



