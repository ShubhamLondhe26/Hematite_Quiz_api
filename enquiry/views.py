from django.shortcuts import render
from .serializers import EnquirySerializer
from .models import Enquiry
from rest_framework.viewsets import ModelViewSet
from rest_framework import status
from rest_framework.exceptions import APIException
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework_simplejwt.authentication import JWTAuthentication

# Create your views here.
class EnquiryViewset(ModelViewSet):
    """
    API endpoint that allows Enquiry to be viewed or edited.
    """
    queryset = Enquiry.objects.all()
    serializer_class = EnquirySerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_serializer_class(self):
        return self.serializer_class

    #get all enquiry details
    def list(self,request):
        """
        List all enquiries.

        Returns a response containing a list of all enquiries.

        Raises:
        - APIException: If an internal server error occurs.
        """
        try:
            enquiry_objs = Enquiry.objects.all()
            serializer = self.get_serializer(enquiry_objs, many = True)

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

    #add enquiry detail
    def create(self,request):
        """
        Create a new enquiry.

        Returns a response indicating the success or failure of the operation.

        Raises:
        - APIException: If an internal server error occurs.
        """
        try:
            serializer =self.get_serializer(data=request.data)

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
                'messaage':'Enquiry detail added successfully'
            })

        except Exception as e:
            print(e)
            raise APIException({
                'message':APIException.default_detail,
                'status': APIException.status_code
            })

    # get single enquiry detail
    def retrieve(self,request,pk=None):
        """
        Retrieve details of a specific enquiry.

        Returns a response containing details of the specified enquiry.

        Raises:
        - APIException: If an internal server error occurs.
        """
        try:
            id = pk
            if id is not None:
                enquiry_obj = self.get_object()
                serializer = self.get_serializer(enquiry_obj)

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

    #update all fields of enquiry detail
    def update(self,request,pk=None):
        """
        Update all fields of an enquiry.

        Returns a response indicating the success or failure of the operation.

        Raises:
        - APIException: If an internal server error occurs.
        """
        try:
            enquiry_objs = self.get_object()
            serializer = self.get_serializer(enquiry_objs, data=request.data, partial=False)

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
                'messaage':'Enquiry detail updated successfully'
            })

        except Exception as e:
            print(e)
            raise APIException({
                'message':APIException.default_detail,
                'status': APIException.status_code
            })

    #update specific fields
    def partial_update(self,request, pk=None):
        """
        Update specific fields of an enquiry.

        Returns a response indicating the success or failure of the operation.

        Raises:
        - APIException: If an internal server error occurs.
        """
        try:
            enquiry_obj = self.get_object()
            serializer = self.get_serializer(enquiry_obj, data=request.data, partial = True)

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
                'messaage':'Enquiry detail updated successfully'
            })

        except Exception as e:
            print(e)
            raise APIException({
                'message':APIException.default_detail,
                'status': APIException.status_code
            })

    # delete enquiry detail
    def destroy(self,request,pk):
        """
        Delete an enquiry.

        Returns a response indicating the success or failure of the operation.

        Raises:
        - APIException: If an internal server error occurs.
        """
        try:
            id = pk
            enquiry_obj = self.get_object()
            enquiry_obj.delete()
            return Response({
                'status':status.HTTP_200_OK,
                'messaage':'Enquiry detail deleted successfully'
            })

        except Exception as e:
            print(e)
            raise APIException({
                'message':APIException.default_detail,
                'status': APIException.status_code
            })


