from django.views import View
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from djangoapi.serializers import RequestSerializer, ResponseSerializer
from djangoapi.backend_statistics import get_all_statistics
from djangoapi.docs import swagger

class MyAPIView(APIView):
    def get(self, request):
        request_serializer  = RequestSerializer(data=request.query_params)
        request_serializer.is_valid(raise_exception=True)
        data = request_serializer.validated_data
        date_start = data['date_start']
        date_end = data['date_end']
        currency = data['currency']

        response = get_all_statistics(date_start, date_end, currency)

        response = ResponseSerializer(instance = {"document": response}).data
        return Response(response)


def serve_doc(request):
    return render(request, "redoc.html")


@api_view()
def serve_swagger(request):
    return Response(swagger)