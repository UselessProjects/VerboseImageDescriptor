# Verbose Image Descriptor
A Python Script that convert an image to the VerboseImageDescriptor format.
## What is Verbose Image Descriptor ?

The **Verbose Image Descriptor** format is a lossless format for images. It's absolutely not optimized.

An .verboseimagedescriptor file is basically a text file, where every pixel is describe with a sentence like this one :

> In the pixel number 42042, there is an amount of red of 35 , an amount of green of 119 and an amount of blue of 219 .

At the beginning of the file, there is a line that tell the dimensions of the image :

> This image got 300 pixel line length and got 300 pixel column height.

I'm sure you understand why this is (a bit) useless.

## Usage

If you want to convert an image to the VerboseImageDescriptor format, you must use the `vid` option :

`python vid-cli.py vid myimage.png`

> I don't lie to you, it may be _very_ long.

It will create a file called `myimage.png.vid` that is basically your image converted.

You can open this new file with your favorite text editor if you want to have fun.

If you want to convert a `vid` file into an image, simply use the `unvid` option :

`python vid-cli.py unvid myvidfile.vid myoutputimage.png`

The script will detect the format you want to use as output. 

> If you want to know what format is supported, you can go here : http://effbot.org/imagingbook/formats.htm
