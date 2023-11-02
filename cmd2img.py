##Please install ansi2html for your os try "pip install ansi2html,sudo apt install wkhtmltopdf"
##Please install pdfcrowd and Pillow in your python "sudo pip install pdfkit && sudo pip install pillow && sudo pip install pdf2image"
##additonal install for windows WKHTMLTOPDF and http://blog.alivate.com.au/poppler-windows/ install and then copy the bin path put into system env variable
##additonal install for windows pip install ansi2html
##python install older version 3.5
import os;
from PIL import Image, ImageChops;
import pdfkit;
from pdf2image import convert_from_path;

def trim(im):
	bg = Image.new(im.mode, im.size, im.getpixel((0,0)))
	diff = ImageChops.difference(im, bg)
	diff = ImageChops.add(diff, diff, 2.0 , -100)
	bbox = diff.getbbox()
	a,b,c,d = bbox
	bbox =(a-10,b-10,c+20,d+20)
	if bbox:
 		return im.crop(bbox)
	else:
		return im 

def cmd2img(cmd,filename):
	#cmd = str(input("Enter the Command : "))
	#filename = str(input("Enter the File Name : "))
	filename = filename+".png"
	cmd+=" | ansi2html > temp.html"

	os.system(cmd)
	print("Command Execute Successfully\n")

	pdfkit.from_file('temp.html','temp.pdf')
	print("PDF Converted Successfully\n")

	pages = convert_from_path('temp.pdf')
	count = 1
	for page in pages:
		page.save(str(count)+"_"+filename)

		print("Image Converted Successfully\n")
		print("Output Original Image : "+str(count)+"_"+filename)

		im = Image.open(str(count)+"_"+filename)
		im =trim(im)
		im.save(str(count)+"_"+'Trim_'+filename)

		print("Image Trimed Successfully\n")
		print("Output Trimed Image : "+str(count)+"_"+'Trim_'+filename)
		count = count+1;

	#os.system("rm temp.*")
	
#except Exception as ex:
	#print(ex)
