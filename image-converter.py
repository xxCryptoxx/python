from svglib.svglib import svg2rlg
from reportlab.graphics import renderPM
from PIL import Image

choice = input("Conversion type(svg or png): ")

if choice == 'svg':
    svg_file = input('Directory and file with extension: ')

    drawing = svg2rlg(svg_file)

    output_file = input('Save as: ')
    ext = 'png'
    
    renderPM.drawToFile(drawing, output_file+ext, fmt="PNG")

    print('task completed successfully...')

elif choice == 'png':
    file_dir = input('Directory and file with extension: ')

    im1 = Image.open(file_dir)
    output_file = input('Save as(Name + Ext): ')
    im1.save(output_file)

    print('task completed successfully...')
else:
    pass
