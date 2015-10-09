# Cat_Catcher

About:
====
Download a picture about cat with the given size from http://placekitten.com/

There're two ways to use it:
=====

###1.Use command:
3  Arguments:

* The width of the picture &nbsp;<space>&nbsp;<space> # required
* The height of the picture  &nbsp;<space>&nbsp;<space> # required
* The filename of the picture  &nbsp;<space>&nbsp;<space> # optional

If the third argument is not provided, the picture will be download on the current folder.
And the file name will be named with [width]*[height].jpg as default

###&nbsp;<space>Example:
```
python3 dl.py 500 600   
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

Plan:
====
* Enhance the gui
* Download multiple pictures at the same time
