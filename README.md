# Cat_Catcher

About:
====
Download a picture about with the given size from http://placekitten.com/

How to use:
====
3  Arguments:

* The width of the picture  # required
* The height of the picture  # required
* The filename of the picture  # optional

If the third argument is not provided, the picture will be download on the current folder.
And the file name will be named with [width]*[height].jpg as default

Example:
====
```
python3 dl.py 500 600   
```
A picture with the size of 500 * 600 will be downloaded on the current folder <br>
![eg.jpg](/screenshots/eg.jpg) <br>
If there're no picture with the given size, a warning will be printed: <br>
```
No such picture with the given size
```

Plan:
====
* Add a gui
* Download multiple pictures at the same time
