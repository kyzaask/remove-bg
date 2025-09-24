from rembg import remove
## rembg = remove background, it's a dictionary
## remove is a function which removes the background of a picture.
input_path = "WIN_20250924_20_36_50_Pro.jpg"
## the input format does not matter
output_path = "output.png"
## but the output format must be .png
##The input format doesn’t matter, but the output is usually saved as PNG to keep transparency.

with open(input_path,"rb") as i:
    ## open() used to open a file
    ## rb= read binary because it is a picture
    ## as i = file name is i
    ## Bu satırın sonunda, i artık fotoğraf dosyanın binary verisini temsil ediyor.
    ## At the end of this line, i now represents the binary data of the image file.
    with open(output_path,"wb") as o:
        ## wb = write binary
        input_file =i.read()
        ## i.read() = It reads all the data of the input file (the image).
        output_file = remove(input_file)
        ## we call the remove function first
        ## we give it the raw(ham) data (input file)
        ## remove(input_file) removes the background and returns the result as PNG
        ## this data is saved into the output_file variable
        ## so this is the aı part: the model processes the image
        o.write(output_file)
        ## all the bits and bytes(the image data) in putput_file are taken
        ## They are written exactly into the "o" file
