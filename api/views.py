from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

from django.http import HttpResponse

class crop_predict(APIView):
    SAMPLE_CROP_ATTRIBUTES = [
            90,
            40,
            40,
            20,
            80,
            7,
            200
        ]

    def get(self, request):
        return Response({
            'msg': 'success',
            'sample_crop_attributes': self.SAMPLE_CROP_ATTRIBUTES
        })
    
    def post(self, request):
        from controllers.crop_predict import crop_predict

        if not request.data.get('crop_attributes'):
            return Response({
                'msg': 'No crop attributes provided',
                'sample_crop_attributes': self.SAMPLE_CROP_ATTRIBUTES
            }, status=status.HTTP_400_BAD_REQUEST)

        crop_attributes = request.data.get('crop_attributes')

        if len(crop_attributes) != len(self.SAMPLE_CROP_ATTRIBUTES):
            return Response({
                'msg': 'Wrong number of crop attributes provided',
                'sample_crop_attributes': self.SAMPLE_CROP_ATTRIBUTES
            }, status=status.HTTP_400_BAD_REQUEST)

        try:
            return Response({
                'msg': 'success',
                'crop_attributes': crop_attributes,
                'prediction': crop_predict(crop_attributes)[0]
            })
        except:
            return Response({
                'msg': 'Error while processing request',
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)