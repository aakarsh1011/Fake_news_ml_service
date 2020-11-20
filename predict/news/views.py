from django.shortcuts import render
from django.http import JsonResponse
import pandas as pd

# Create your views here.
def news(request):
	return render(request, 'predict.html')


def predict_chances(request):


	#to check request is a html
	if request.POST.get('action') == 'post':

		#receive data from client
		news_text = str(request.POST.get(news))



		# unpacking model
		model = pd.read_pickle(r"E:/fake_news_ml_service/models/fake_detect_model.pkl")

		# make prediction
		result = model.predict([news_text])

		classification = result



		return JsonResponse({'result': classification,'news': news}, safe = False)

