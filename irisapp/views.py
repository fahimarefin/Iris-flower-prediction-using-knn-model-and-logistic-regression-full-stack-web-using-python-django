from django.shortcuts import render
from joblib import load
model=load(r'C:\Users\Fahim Arefin\Desktop\Ml deployment\djangoMLDeployment\savedModels\knn_model.joblib')

def predictor(request):
  return render(request,'main.html')

def formInfo(request):
    sepal_length = float(request.GET.get('sepal_length', 0.0))
    sepal_width = float(request.GET.get('sepal_width', 0.0))
    petal_length = float(request.GET.get('petal_length', 0.0))
    petal_width = float(request.GET.get('petal_width', 0.0))

    # Now, you can use the numeric values for prediction
    y_pred = model.predict([[sepal_length, sepal_width, petal_length, petal_width]])

    if y_pred[0] == 0:
        y_pred = ''

    return render(request, 'result.html', {'prediction': y_pred})
