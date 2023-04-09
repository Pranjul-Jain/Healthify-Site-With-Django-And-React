from django.shortcuts import render, redirect
from django.conf import settings
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from .pool import connection
from .serializer import HealthtipsSerializer, adminSerializer
from rest_framework.permissions import IsAuthenticated


def index(request):
    return render(request, "index.html")


class admin_login(APIView):
    serializer_class = adminSerializer

    def post(self, request, *args, **kwargs):
        serializer = adminSerializer(data=request.data)
        serializer.is_valid()

        username = request.data.get("username")
        password = request.data.get("password")

        if settings.ADMIN_PASSWORD == password and settings.ADMIN_USERNAME == username:
            return redirect("healthtips")

        return Response({"message": "not admin"})


class HealthtipsView(APIView):
    serializer_class = HealthtipsSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        serializer = HealthtipsSerializer(data=request.data)
        serializer.is_valid()

        tips = request.data.get('tips')
        tip_description = request.data.get('tip_description')

        db, cmd = connection()

        try:
            query = f'''INSERT INTO HEALTHTIPS(tips,tip_description) VALUES("{tips}","{tip_description}");'''
            cmd.execute(query)
            db.commit()
            db.close()
            return Response({"status": "submitted successfully"})
        except Exception as e:
            db.close()
            print(e)
            return Response({"status": "submit failed"})
