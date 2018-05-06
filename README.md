## Image Resizer

---

### Discription

+ The script takes an input image and puts an image with a new size
+ required argument - is the path to the original image
+ optional parameters: 
    "width" of the resulting image,
    "height" of the resulting image,
    "scale" - how many times to increase (maybe less than 1)
    "output" - path to the resulting file
+ You need a library [pillow](https://pillow.readthedocs.io/en/latest/handbook/index.html) to statr
+ It is recommended to use [virtualenv](https://docs.python.org/3/library/venv.html) 


### How to install pillow

```bash
pip install -r requirements.txt  # or pip3 
```


### Start script example

```bash
python3 image_resize.py image/kode_rev.jpeg --output result --scale 0.5
```
```bash
python3 image_resize.py image/kode_rev.jpeg --output result --width 200 --height 100 
```


### Get help

```bash
python3 image_resize.py --help
```


### Requirements

```bash
Python ver 3.5 (or higher)
```

---

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
