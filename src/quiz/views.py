from django.shortcuts import render
from rest_framework import generics
from .models import Category, Quiz, Question
from .serializers import CategorySerializer, CategoryDetailSerializer,QuestionSerializer
from .pagination import MyPagination

class CategoryList(generics.ListAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class CategoryDetail(generics.ListAPIView):
    serializer_class = CategoryDetailSerializer
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

    def get_queryset(self):
        queryset = Question.objects.all()
        title = self.kwargs["title"]
        queryset = queryset.filter(quiz__title=title)# title (Django, nextjs) göre filtreliyor
        return queryset
        
        
        
    
