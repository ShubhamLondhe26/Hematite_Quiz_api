from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import EnquiryModel
from .serializers import EnquirySeriaizers
from rest_framework import status 
from rest_framework.exceptions import APIException 
from rest_framework.response import Response 
from rest_framework import permissions
from rest_framework_simplejwt.authentication import JWTAuthentication

# Create your views here.

class EnquiryViewSet(ModelViewSet):
    """
    API endpoint that allows Enquiries to be viewed or edited.
    """
    queryset = EnquiryModel.objects.all()
    serializer_class = EnquirySeriaizers
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    
    def get_serializer_class(self):
        """
        Returns the serializer class to be used for this view set.
        """
        return self.serializer_class
    
    def list(self, request):
        """
        List all enquiries.

        Returns a response containing a list of all enquiries.

        Raises:
        - APIException: If an internal server error occurs.
        """
        try:
            enquiry_objs = EnquiryModel.objects.all()
            serializer = self.get_serializer(enquiry_objs, many = True) 

            return Response({
                'status': status.HTTP_200_OK,
                'data': serializer.data
            })
        except Exception as e:
            print(e)
            raise APIException({
                'message': APIException.default_detail,
                'status': APIException.status_code
            })
        
    def create(self, request):
        """
        Create a new enquiry.

        Returns a response indicating the success or failure of the operation.

        Raises:
        - APIException: If an internal server error occurs.
        """
        try:
            serializer = self.get_serializer(data = request.data)
            if not serializer.is_valid():
                print(serializer.errors)
                return Response({
                    'status': status.HTTP_400_BAD_REQUEST,
                    'data': serializer.errors,
                    'message': 'Invalid Data'
                })
            serializer.save()
            return Response({
                'status': status.HTTP_201_CREATED,
                'data': serializer.data,
                'message': 'Enquiry added successfully'
            })
        except Exception as e:
            print(e)
            raise APIException({
                'message': APIException.default_detail,
                'status': APIException.status_code
            })

    def retrieve(self, request, pk=None):
        """
        Retrieve details of a specific enquiry.

        Returns a response containing details of the specified enquiry.

        Raises:
        - APIException: If an internal server error occurs.
        """
        try:
            id = pk
            if id is not None:
                enquiry_objs = self.get_object()
                serializer = self.get_serializer(enquiry_objs)

            return Response({
                'status': status.HTTP_200_OK,
                'data': serializer.data
            })

        except Exception as e:
            print(e)
            raise APIException({
                'message': APIException.default_detail,
                'status': APIException.status_code
            })

    def update(self, request, pk = None):
        """
        Update all fields of an enquiry.

        Returns a response indicating the success or failure of the operation.

        Raises:
        - APIException: If an internal server error occurs.
        """
        try:
            enquiry_objs = self.get_object()
            serializer = self.get_serializer(enquiry_objs, data = request.data, partial = False)

            if not serializer.is_valid():
                print(serializer.errors)
                return Response({
                    'status': status.HTTP_400_BAD_REQUEST,
                    'data': serializer.errors,
                    'message': 'Invalid data'
                })
            serializer.save()

            return Response({
                'status': status.HTTP_200_OK,
                'data': serializer.data,
                'message': 'Enquiry updated successfully'
            })

        except Exception as e:
            print(e)
            raise APIException({
                'message': APIException.default_detail,
                'status': APIException.status_code
            })

    def partial_update(self, request, pk = None):
        """
        Update specific fields of an enquiry.

        Returns a response indicating the success or failure of the operation.

        Raises:
        - APIException: If an internal server error occurs.
        """
        try:
            enquiry_obj = self.get_object()
            serializer = self.get_serializer(enquiry_obj, data = request.data, partial = True)

            if not serializer.is_valid():
                print(serializer.errors)
                return Response({
                    'status': status.HTTP_400_BAD_REQUEST,
                    'data': serializer.errors,
                    'message': 'Invalid data'
                })
            serializer.save()

            return Response({
                'status': status.HTTP_200_OK,
                'data': serializer.data,
                'message': 'Enquiry updated successfully'
            })

        except Exception as e:
            print(e)
            raise APIException({
                'message': APIException.default_detail,
                'status': APIException.status_code
            })

    def destroy(self, request, pk):
        """
        Delete an enquiry.

        Returns a response indicating the success or failure of the operation.

        Raises:
        - APIException: If an internal server error occurs.
        """
        try:
            id = pk
            enquiry_objs = self.get_object()
            enquiry_objs.delete()
            return Response({
                'status': status.HTTP_204_NO_CONTENT,
                'message': 'Enquiry deleted successfully'
            })

        except Exception as e:
            print(e)
            raise APIException({
                'message': APIException.default_detail,
                'status': APIException.status_code
            })