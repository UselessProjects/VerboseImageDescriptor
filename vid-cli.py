# ========================================================================
#                       VERBOSE IMAGE DESCRIPTOR
# ========================================================================
#   Version     :   0.1
#   Author      :   Argann Bonneau
#   Last Update :   06 april 2017
# ========================================================================
# Copyright 2017 argann bonneau
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ========================================================================
# If you want to know how to use this script,
# please go to https://github.com/UselessProjects/VerboseImageDescriptor
# ========================================================================
from PIL import Image
import sys
if __name__ == "__main__":
    if sys.argv[1] == "vid":
        im = Image.open(sys.argv[2])
        lineSize = im.size[0]
        descriptor = "This image got "+str(lineSize)+" pixel line length and got "+str(im.size[1])+" pixel column height.\n"
        indice = 0
        for pixel in im.getdata():
            descriptor += "In the pixel number "+str(indice)+", there is an amount of red of "+str(pixel[0])+" , an amount of green of "+str(pixel[1])+" and an amount of blue of "+str(pixel[2])+" .\n"
            indice += 1
        file = open(sys.argv[2]+".vid", 'w')
        file.write(descriptor)
        file.close()
    elif sys.argv[1] == "unvid":
        xSize, ySize = 0, 0
        file = open(sys.argv[2], 'r')
        go = True
        currentLine = 0
        for line in file:
            if go:
                xSize, ySize = [int(s) for s in line.split() if s.isdigit()]
                im = Image.new("RGB", (xSize, ySize))
                go = False
            else:
                red, green, blue = [int(s) for s in line.split() if s.isdigit()]
                print((currentLine % xSize, int(currentLine / xSize)))
                im.putpixel((currentLine % xSize, int(currentLine / xSize)), (red, green, blue))
                currentLine += 1
        im.save("YOLO.png")
