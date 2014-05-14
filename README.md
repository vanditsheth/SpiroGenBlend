SpiroGenBlend
=============

Generates a spirograph (shape can be changed) and blends it with given image

The code first generates a spirograph image using the equation for it and then stores the image as RandomImage.png (PNG format is kept for transparency in image) as well as RandomImage.jpg using readPixels. The colors for the lines here are taken from palette.txt file having 200 (presently, random) colors in RGB format. The image is then blended with the Design.png file, of 400*400 resolution, using Alpha:1-Alpha blending and then 17 different filters are applied to it, namely: Black and White, Min, Max, Median, Mode, Invert, Blur, Gaussian Blur, Edge Enhance, Edge Enhance More, Emboss, Find Edges, Smooth, Smooth More, Sharpen, Contour and Detail. While the Design.png file is being opened, it is checked if the file exists and it is cropped to 400*400 pixels resolution to fit the spirograph, if it does. Each of the filtered images is stored as Blended_<FilterName>.jpg in the same folder as the code. The resolution used for all images is 400*400 pixels. 

The necessary files for the code are: 1)palette.txt. This file contains 200 randomly generated colors (using hardware randomisation), which are used for line colors. This file can be changed to have different colors 2)Design.png. This file contains an image, having resolution 400*400 pixels. This is blended with the generated spirograph and the filters are applied to thi blended image.

The code has only one module, display, but it can be read in independent sub-parts: Image Creation, Image Blending and Image Filters (in the same order)
