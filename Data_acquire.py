### D A T A     A C Q U I R I N G  ###
'''
acquire fake_news data set from kaggle with url
URL: "https://www.kaggle.com/c/fake-news/data?select=test.csv"

The script will download the dataset in zipfile and extract it 
automatically in the working directory.

'''

# importing necessary libraries
import os							#to run commands in cmd
from zipfile import ZipFile 		#to handle zipped file

#change this for downloading another data
data_api_name = 'fake-news'
def get_data():
	# Downloading data
	print("Downloading data.....\n")
	os.system("kaggle competitions download -c {}".format(data_api_name))
	print("Zip file downloaded\n")

	# handling zip file
	#creating folder
	os.system("mkdir {}".format(data_api_name))

	#creating zipfile object
	with ZipFile ('fake-news.zip','r') as zipObj:
		#extract all the contents of zip file in current directory
		zipObj.extractall(data_api_name)

	print('File extracted in the {} directory'.format(data_api_name))

get_data()