from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

from django.http import HttpResponse

class crop_predict(APIView):

    def get(self, request):
        from controllers.crop_predict import crop_predict

        sample_crop_attributes = [
            90,
            40,
            40,
            20,
            80,
            7,
            200
        ]

        response = {
            "status": "success",
            "sample_crop_attributes": sample_crop_attributes,
            "prediction": crop_predict(sample_crop_attributes)[0]
        }
        
        return Response(response)