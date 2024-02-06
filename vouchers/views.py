from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Voucher
from .serializers import VoucherSeriaizer
from rest_framework import status 
from rest_framework.exceptions import APIException 
from rest_framework.response import Response 
from rest_framework import permissions
from rest_framework_simplejwt.authentication import JWTAuthentication

class VoucherViewSet(ModelViewSet):
    queryset = Voucher.objects.all()
    serializer_class = VoucherSeriaizer
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_serializer_class(self):
        """
        Returns the serializer class to be used for this view set.
        """
        return self.serializer_class
    
    def list(self, request):
        """
        List all voucher codes.

        Returns a response containing a list of all voucher codes.

        Raises:
        - APIException: If an internal server error occurs.
        """
        try:
            voucher_objs = Voucher.objects.all()
            serializer = self.get_serializer(voucher_objs, many = True) 

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
        Create a new voucher code.

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
                'message': 'Voucher code added successfully'
            })
        except Exception as e:
            print(e)
            raise APIException({
                'message': APIException.default_detail,
                'status': APIException.status_code
            })

    def retrieve(self, request, pk=None):
        """
        Retrieve details of a specific voucher code.

        Returns a response containing details of the specified voucher code.

        Raises:
        - APIException: If an internal server error occurs.
        """
        try:
            id = pk
            if id is not None:
                voucher_obj = self.get_object()
                serializer = self.get_serializer(voucher_obj)

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

    def update(self, request, pk=None):
        """
        Update all fields of a voucher code.

        Returns a response indicating the success or failure of the operation.

        Raises:
        - APIException: If an internal server error occurs.
        """
        try:
            voucher_obj = self.get_object()
            serializer = self.get_serializer(voucher_obj, data = request.data, partial = False)

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
                'message': 'Voucher code updated successfully'
            })

        except Exception as e:
            print(e)
            raise APIException({
                'message': APIException.default_detail,
                'status': APIException.status_code
            })

    def partial_update(self, request, pk = None):
        """
        Update specific fields of a voucher code.

        Returns a response indicating the success or failure of the operation.

        Raises:
        - APIException: If an internal server error occurs.
        """
        try:
            voucher_obj = self.get_object()
            serializer = self.get_serializer(voucher_obj, data = request.data, partial = True)

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
                'message': 'Voucher code updated successfully'
            })

        except Exception as e:
            print(e)
            raise APIException({
                'message': APIException.default_detail,
                'status': APIException.status_code
            })

    def destroy(self, request, pk):
        """
        Delete a voucher code.

        Returns a response indicating the success or failure of the operation.

        Raises:
        - APIException: If an internal server error occurs.
        """
        try:
            id = pk
            voucher_obj = self.get_object()
            voucher_obj.delete()
            return Response({
                'status': status.HTTP_204_NO_CONTENT,
                'message': 'Voucher code deleted successfully'
            })

        except Exception as e:
            print(e)
            raise APIException({
                'message': APIException.default_detail,
                'status': APIException.status_code
            })
