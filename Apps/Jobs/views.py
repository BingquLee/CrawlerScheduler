import time

from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from Apps.Jobs import models
from Apps.Jobs.serializers import JobsSerializer
from global_utils import ts2datetime


class Jobs(APIView):

    def get(self, request):
        params = request.query_params.dict()
        page_size = params.get('page_size', 10)
        page_num = params.get('page_num', 1)
        sql = "Select * From jobs ORDER By publish_time DESC LIMIT {}, {}".format((page_num - 1) * page_size, page_size)
        queryset = models.Jobs.objects.raw(
            raw_query=sql
        )
        serializer = JobsSerializer(queryset, many=True)
        data_list = serializer.data

        return Response(data_list, status=status.HTTP_200_OK)

    def post(self, request):
        print(request.query_params.dict())
        params = request.query_params.dict()
        request.data['text'] = params.get('text', '')
        request.data['file_amount'] = params.get('file_amount', 1)
        request.data['status'] = 0
        request.data['update_ts'] = int(time.time())
        request.data['update_dt'] = ts2datetime(request.data['update_ts'])
        serializer = JobsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
            # return render(request, 'Jobs.html')
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
