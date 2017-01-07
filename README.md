# Cat_Catcher

About:
====
Download a picture about cat with the given size from http://placekitten.com/

There're two ways to use it:
=====

###1.Use command:

If the third argument is not provided, the picture will be download on the current folder.
And the file name will be named with [width]\*[height].jpg as default

Usage:
```
usage: dl.py [-h] [--path PATH] [--name NAME] width height

positional arguments:
  width                 an integer indicating the width
  height                an integer indicating the height

optional arguments:
  -h, --help            show this help message and exit
  --path PATH, -p PATH  the path storing the picture
  --name NAME, -n NAME  the picture name
```

###&nbsp;<space>Example:
download a picture with given size in current directory
```
python3 dl.py 500 600
```

download a picture and then name it as "test.jpg"
```
python3 dl.py 500 600 -n test.jpg
```

download the picture at home directory
```
python3 dl.py 500 600 -p ~
```

download a picture at home directory and name it as "test.jpg"
```
python3 dl.py 500 600 -p ~ -n test.jpg
```

###2.Use Simple GUI:
```
python3 ui.py   
```
###&nbsp;<space>Example:
![alt text](http://ww3.sinaimg.cn/bmiddle/e6825b3fgw1ewv41mvrx5j20ax03pgln.jpg) <br>

A picture with the size of 500 * 600 will be downloaded on the chosen folder <br>
![alt text](http://placekitten.com/500/600) <br>
If there're no picture with the given size, a warning will be printed: <br>
```
No such picture with the given size
```
