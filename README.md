# ArduinoComputerStatsDisplay
Show your computer fans' speed, cpu temperature, gpu temperature on an oled display.



Select a gif of an icon preferably.
Seperate the gif on its many images, more than 3 for an animation might be too many. This site can be used for this https://ezgif.com/split
Then convert this image to BMP in this step you can choose the final size of the animation. Use https://cloudconvert.com/
For each image improve the result with an image editor (paint, gimp, etc...) the result should contain only black or white pixels.
With Piskel https://www.piskelapp.com/ create a canvas with the size ok the oled screen import your gif images of for each frame, you must align them so that they show on the same spot.
Any text should be added now too, pixel by pixel. Other tools might by more effective here.
Download each frame image. Use https://javl.github.io/image2cpp/ to transform them to C code.
Place this code on your Arduino file, see file in this repository for an example.

To send information from your computer to the arduino use the Open Hardware Monitor and wmi python package, see the python file for how to handle this information.

Any changes to the payload sent must me updated on the receiver, in this case the arduino code.



