from wand.image import Image as wi
from PIL import Image
from PIL import TiffImagePlugin

merged_file_name = "temp.tif"
file_location = "Resources for younglings.pdf"
tiffType = ""
begDoc = 452
Prefix = ["ABC_", "XYZ_"]
type = "single"

def convert_to_multipage_tiffs(merged_file_name):
    with TiffImagePlugin.AppendingTiffWriter(merged_file_name,True) as tf:
        for tiff_in in file_list:
            try:
                im= Image.open(tiff_in)
                im.save(tf)
                tf.newFrame()
                im.close()
                print(tiff_in)
            except:
                print('Error')

def convert_to_single_tiffs(file_location, file_prefix, begin_doc):
    pdf = wi(filename=file_location, resolution=300) # get file to convert
    pdfImage = pdf.convert("tiff") # choose type to convert to
    i = len(str(begin_doc))
    prefix = file_prefix[1]
    j = 7 - i
    file_list = []
    file_numbers = ['0','0','0','0','0','0','0']
    n = 7
    while(j<n):
        n -= 1
        for q in reversed(str(begin_doc)):
            file_numbers[n] = q
            print(file_numbers[n])
            n -= 1
            for img in pdfImage.sequence: # save each page 1by1
                page = wi(image=img)
                page.save(filename=file_prefix + (''.join(file_numbers)) + ".tif")
                file_list.append(file_prefix + (''.join(file_numbers)) + ".tif")

    print(file_list)

if type=="single":
    convert_to_single_tiffs(file_location, Prefix[1], begDoc)
elif type=="multi":
    convert_to_multipage_tiffs(merged_file_name)
