from rest_framework import serializers
from .models import Answer, Category, Question, Quiz

# her model için bir serializer kullanılıyor.
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
            "id",
            "name",
            "quiz_count"
        )


class CategoryDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quiz
        fields = (
            "title",
            "question_count",
        )


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:

        model = Answer
        fields = [
            'id',
            'answer_text',
            'is_right',
        ]

# Nested serializer
class QuestionSerializer(serializers.ModelSerializer):
    answer = AnswerSerializer(many=True, read_only=True)
    difficulty = serializers.SerializerMethodField() # altta yazdığım method tan al
    #method ile serialize etmek istendiğinde kullanılır

    class Meta:
        model = Question
        fields = (
            "title",
            "answer",
            "difficulty",
        )

    def get_difficulty(self, obj):
        return obj.get_difficulty_display() # get_field_display fronted te gösterim için.