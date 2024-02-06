from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Feedback
from .serializers import FeedbacksSerializer
from rest_framework import status
from rest_framework.exceptions import APIException
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework_simplejwt.authentication import JWTAuthentication

# Create your views here.
class FeedbacksViewSet(ModelViewSet):
    """
    API endpoint that allows Feedback to be viewed or edited.
    """
    queryset = Feedback.objects.all()
    serializer_class = FeedbacksSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_serializer_class(self):
        return self.serializer_class

    #get all feedback
    def list(self, request):
        """
        List all feedbacks.

        Returns a response containing a list of all feedbacks.

        Raises:
        - APIException: If an internal server error occurs.
        """
        try:
            feedbacks_objs = Feedback.objects.all()
            serializer = self.get_serializer(feedbacks_objs, many = True)

            return Response({
                'status':status.HTTP_200_OK,
                'data': serializer.data
            })

        except Exception as e:
            print(e)
            raise APIException({
                'message':APIException.default_detail,
                'status': APIException.status_code
            })

    #add feedback
    def create(self, request):
        """
        Create a new feedback.

        Returns a response indicating the success or failure of the operation.

        Raises:
        - APIException: If an internal server error occurs.
        """
        try:
            serializer = self.get_serializer(data=request.data)

            if not serializer.is_valid():
                print(serializer.errors)
                return Response({
                    'status':status.HTTP_400_BAD_REQUEST,
                    'data': serializer.errors,
                    'message':'Invalid data'
                })
            serializer.save()

            return Response({
                'status':status.HTTP_201_CREATED,
                'data': serializer.data,
                'messaage':'Feedback added successfully'
            })

        except Exception as e:
            print(e)
            raise APIException({
                'message':APIException.default_detail,
                'status': APIException.status_code
            })

    # get single feedback
    def retrieve(self, request, pk = None):
        """
        Retrieve details of a specific feedback.

        Returns a response containing details of the specified feedback.

        Raises:
        - APIException: If an internal server error occurs.
        """
        try:
            id = pk
            if id is not None:
                feedbacks_obj = self.get_object()
                serializer = self.get_serializer(feedbacks_obj)

            return Response({
                'status':status.HTTP_200_OK,
                'data': serializer.data
            })

        except Exception as e:
            print(e)
            raise APIException({
                'message':APIException.default_detail,
                'status': APIException.status_code
            })

    #update all fields of feedback
    def update(self, request, pk=None):
        """
        Update all fields of a feedback.

        Returns a response indicating the success or failure of the operation.

        Raises:
        - APIException: If an internal server error occurs.
        """
        try:
            
            feedbacks_obj = self.get_object()
            serializer = self.get_serializer(feedbacks_obj, data=request.data, partial=False)

            if not serializer.is_valid():
                print(serializer.errors)
                return Response({
                    'status':status.HTTP_400_BAD_REQUEST,
                    'data': serializer.errors,
                    'message':'Invalid data'
                })
            serializer.save()

            return Response({
                'status':status.HTTP_200_OK,
                'data': serializer.data,
                'messaage':'Feedback updated successfully'
            })

        except Exception as e:
            print(e)
            raise APIException({
                'message':APIException.default_detail,
                'status': APIException.status_code
            })

    #update specific fields
    def partial_update(self, request, pk=None):
        """
        Update specific fields of a feedback.

        Returns a response indicating the success or failure of the operation.

        Raises:
        - APIException: If an internal server error occurs.
        """
        try:
            
            feedbacks_objs = self.get_object()
            serializer = self.get_serializer(feedbacks_objs, data=request.data, partial = True)

            if not serializer.is_valid():
                print(serializer.errors)
                return Response({
                    'status':status.HTTP_400_BAD_REQUEST,
                    'data': serializer.errors,
                    'message':'Invalid data'
                })
            serializer.save()

            return Response({
                'status':status.HTTP_200_OK,
                'data': serializer.data,
                'messaage':'Feedback updated successfully'
            })

        except Exception as e:
            print(e)
            raise APIException({
                'message':APIException.default_detail,
                'status': APIException.status_code
            })

    # delete feedback
    def destroy(self, request, pk):
        """
        Delete a feedback.

        Returns a response indicating the success or failure of the operation.

        Raises:
        - APIException: If an internal server error occurs.
        """
        try:
            id = pk
            feedbacks_obj = self.get_object()
            feedbacks_obj.delete()
            return Response({
                'status':status.HTTP_200_OK,
                'messaage':'Feedback deleted successfully'
            })

        except Exception as e:
            print(e)
            raise APIException({
                'message':APIException.default_detail,
                'status': APIException.status_code
            })
