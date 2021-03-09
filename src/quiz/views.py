from django.shortcuts import render
from rest_framework import generics
import rest_framework
from .models import Category, Quiz, Question
from .serializers import CategorySerializer, CategoryDetailSerializer,QuestionSerializer
# from .pagination import MyPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication, SessionAuthentication



class CategoryList(generics.ListAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    permission_classes = [IsAuthenticated]
    #authentication_classes = [TokenAuthentication,SessionAuthentication] # 2 Katmanlı doğrulama


class CategoryDetail(generics.ListAPIView):
    serializer_class = CategoryDetailSerializer
    permission_classes = [IsAuthenticated]
#  queryset i alamıyoruz. burda seçilen katagorideki quiz leri listemek amaçlanıyor.
# queryset i overwrite ediyoruz. get_queryset ile ediyoruz
    def get_queryset(self):
        queryset = Quiz.objects.all()
        category = self.kwargs["category"]  # backend, frontend
        queryset = queryset.filter(category__name=category)
        # child tan parent ulaşmak için x __y şeklinde yazıyoruz. Quiz den Catagory modeline  ulaşmış oluyoruz
        return queryset
    # Quiz.object.filter(category__name=category) 


class QuizDetail(generics.ListAPIView):
    serializer_class = QuestionSerializer
    permission_classes = [IsAuthenticated]
    # pagination_class= MyPagination

    def get_queryset(self):
        queryset = Question.objects.all()
        title = self.kwargs["title"] # title ı url den akıyoruz.
        queryset = queryset.filter(quiz__title=title)# title (Django, nextjs) göre filtreliyor
        return queryset
        
        
        
    
