from django.shortcuts import render
from .serializers import QuestionSerializer ,QuestionDetailSerializer ,QuestionImageSerializer
from . models import Question
from rest_framework.viewsets import ModelViewSet
from rest_framework import status, parsers
from rest_framework.exceptions import APIException
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.decorators import action

# Create your views here.
class QuestionViewset(ModelViewSet):
    """
    API endpoint that allows Questions to be viewed or edited.
    """
    queryset = Question.objects.all()
    serializer_class = QuestionDetailSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    parser_classes = (parsers.FormParser, parsers.MultiPartParser, parsers.FileUploadParser)

    def get_serializer_class(self):
        if self.action == 'list':
            return QuestionSerializer
        if self.action == 'create':
            return QuestionSerializer
        elif self.action == 'upload_image':
            return QuestionImageSerializer
        return self.serializer_class

    @action(methods=['POST'], detail=True, url_path ='upload-image')
    def upload_image(self, request, pk=None):
        """
        Upload the image of a question.

        Returns a response containing a file of an image.

        Raises:
        - APIException: If an internal server error occurs.
        """

        question_objs = self.get_object()
        serializer = self.get_serializer(question_objs, data=request.data)

        if not serializer.is_valid():
            return Response({
                'status':status.HTTP_400_BAD_REQUEST,
                'errors': serializer.errors,
                'message':'Invalid data'
            })

        serializer.save()
        return Response({
            'status':status.HTTP_201_CREATED,
            'data': serializer.data,
            'message':'Question image added successfully'
        })

    #get all questions
    def list(self, request):
        """
        List all questions.

        Returns a response containing a list of all questions.

        Raises:
        - APIException: If an internal server error occurs.
        """
        try:
            question_objs = Question.objects.all()
            serializer = self.get_serializer(question_objs, many=True)

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

    #add question
    def create(self, request):
        """
        Create a new question.

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
                'messaage':'Question added successfully'
            })

        except Exception as e:
            print(e)
            raise APIException({
                'message':APIException.default_detail,
                'status': APIException.status_code
            })

    # get single question
    def retrieve(self, request, pk=None):
        """
        Retrieve details of a specific question.

        Returns a response containing details of the specified question.

        Raises:
        - APIException: If an internal server error occurs.
        """
        try:
            id = pk
            if id is not None:
                question_objs = self.get_object()
                serializer = self.get_serializer(question_objs)

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

    #update all fields of question
    def update(self, request, pk=None):
        """
        Update all fields of a question.

        Returns a response indicating the success or failure of the operation.

        Raises:
        - APIException: If an internal server error occurs.
        """
        try:
            question_objs = self.get_object()
            serializer = self.get_serializer(question_objs, data=request.data, partial=False)

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
                'messaage':'Question updated successfully'
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
        Update specific fields of a question.

        Returns a response indicating the success or failure of the operation.

        Raises:
        - APIException: If an internal server error occurs.
        """
        try:
            question_objs = self.get_object()
            serializer = self.get_serializer(question_objs, data=request.data, partial=True)

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
                'messaage':'Question updated successfully'
            })

        except Exception as e:
            print(e)
            raise APIException({
                'message':APIException.default_detail,
                'status': APIException.status_code
            })

    def destroy(self, request, pk):
        """
        Delete a question.

        Returns a response indicating the success or failure of the operation.

        Raises:
        - APIException: If an internal server error occurs.
        """
        try:
            id = pk
            question_obj = self.get_object()
            question_obj.delete()
            return Response({
                'status':status.HTTP_200_OK,
                'messaage':'Question deleted successfully'
            })

        except Exception as e:
            print(e)
            raise APIException({
                'message':APIException.default_detail,
                'status': APIException.status_code
            })


