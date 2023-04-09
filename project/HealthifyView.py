from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_protect
from django.conf import settings
from .pool import connection
import pickle as pk
import json
from warnings import filterwarnings

filterwarnings("ignore")

with open(settings.BASE_DIR / "media/Models/MentalDisorder/heatlhify_mental_disorder.pickle", 'rb') as Disorder_modal:
    mental_disorder_model = pk.load(Disorder_modal)

with open(settings.BASE_DIR / "media/Models/MentalDisorder/disease_class_encoder.pickle", 'rb') as Disorder_encoder:
    mental_disorder_encoder = pk.load(Disorder_encoder)


@api_view(["GET"])
def HealthtipData(request):
    try:
        db, cmd = connection()
        query = "select tips,tip_description from healthtips"

        cmd.execute(query)
        data = cmd.fetchall()
        db.close()

        return Response(data)
    except:
        return Response([])


@csrf_protect
@api_view(["POST"])
def predictDisorder(request):
    try:
        features = request.data['features']['current']
        disorder = mental_disorder_encoder.inverse_transform(
            mental_disorder_model.predict([features]))[0]
        return Response({"disorder": disorder})
    except Exception as e:
        print(e)
        return Response({"disorder": None})
