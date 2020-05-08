
def welcome(request , template_name='welcome.html'):
  from django import views
  from django.shortcuts import render
  from video.models import Video
  from gallery.models import Image
  data  = {}
  set_image_url ()
  data['gallery'] = Image.objects.all()
  data['videos'] = Video.objects.all()
  
  return render(request ,template_name , data )

def set_image_url():
  url = str(get_bing_Image_url())
  import os 

  path = os.getcwd()
  new_data = None
  with open(path+'/apps/static/welcome.css' , 'r+') as f:
    data = f.read()
    first_part_index = data.find("url") + 4
    second_part_index = first_part_index + data[first_part_index:].find(")")
    new_data = data[:first_part_index] + '"' + url + '"'
    new_data += data[second_part_index:]
  with open(path+'/apps/static/welcome.css' , 'w+') as f:
    f.write(new_data)
  
def get_bing_Image_url():
  import requests;
  import re
  import html
  import html5lib
  import bs4
  from bs4 import BeautifulSoup;
  BingUrl = "https://www.bing.com"

  response = requests.get(BingUrl)

  if  not response.ok :
    print("Bing is out of reach or check Internet connection")
    exit()
  page = BeautifulSoup(response.content , 'html5lib')

  #  ///////////////////print(page.prettify())

  tab = str(page.findAll('div' , attrs={'class' : 'img_cont'}))

  # print("tab = %s" %tab)

  index1 = str(tab).find("url")+4

  tab1 = tab[index1:]

  index2 = str(tab).find("><")-2

  # print("index1 = %s and index2 = %s"%(index1 , index2))

  # print(tab[index1:index2])

  image_url = BingUrl + tab[index1 : index2] ;
 
  # print(image_url)
  return image_url




