from PIL        import Image
from os         import listdir
from os.path    import isfile, join
from optparse   import OptionParser
import operator

sup_exts    = ['jpg','png']  # supported images extensions
img_rbound  = (1280,1920)    # default boundary of image resize
wmark_per   = 5              # default percentage of image taken up by watermark
wmark_ver   = 0.9            # default vertical position of watermark on image
wmark_hor   = 0.9            # default horizontal position of watermark on image
if __name__ == '__main__':
    optparser = OptionParser()
    optparser.add_option( "-x", dest="resboundx", type="int"
                          help = "set x resize boundary", metavar = "size")
    optparser.add_option( "-y", dest="resboundy", type="int"
                          help = "set y resize boundary", metavar = "size")
    optparser.add_option( "-a", dest="wmark_per", type="int"
                          help = "set percent of image area taken up by watermark (default = " + wmark_per + ")"  metavar="PERCENTAGE")
    optparser.add_option( "-v", dest="wmark_pos", 
                          help = "set vertical position of watermark (default = " + 
    optparser.add_option( "-w", dest="wmark_file", 
                          help = "set watermark file", metavar="FILE" )
    optparser.add_option( "-h", help="prints this help message" )
    

imgs = [ f for f in listdir('.') if isfile(join('.',f)) and f.split('.')[-1].lower() in sup_exts ]

wmark_file = ''
for img_file in imgs:
    if img_file.split('.')[0] == 'watermark' :
        wmark_file = img_file
        break

if wmark_file:
    try:
        wmark = Image.open(join('.',wmark_file))
    except IOError:
        print "cannot open watermark file: ", wmark_file
        
    for img_file in imgs :
        try:
            img = Image.open(join('.',img_file))
        except IOError:
            print "cannot open image file: ", img_file

        img_area = reduce( operator.mul, img.size )
        print img_file, img_area

        #img.paste(watermark.resize( ),
else:
    print 'no watermark found'
    

