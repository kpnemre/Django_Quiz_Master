from django.db import models
from django.utils import timezone


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Category Name")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Categories"

    @property
    #  method u field olarak kullanmak için koyuyoruz,
    # koymaz isek de çalışır.attribute olarak kullandığımız belirtmek için kullanıuoruz. best practice
    def quiz_count(self):
        return self.quiz_set.count()
    #model in adını_set parametresi  parent tan child a ulaşıyoruz. Quiz de kaç obje olduğunu döner
    # model in altını method olarak yazıp field olarak kullanabiliyoruz.
    
    
    
class Quiz(models.Model):
    title = models.CharField(max_length=100, verbose_name="Quiz Title")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    date_created = models.DateTimeField(auto_now_add=True)

    # def save(self, *args, **kwargs):
    #     if not self.id:
    #         self.date_created = timezone.now()
    #     self.date_modified=timezone.now()
    #     return super(Quiz, self).save(*args,**kwargs)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Quizzes"

    @property
    def question_count(self):
        return self.question_set.count()
    # herbir quiz deki soru sayısı nı verecek. parent tan child a 


class Update(models.Model):
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        # DB ye kaydedilmemesi için abstract Model inheritance . tekrarı önelemek için


class Question(Update):

    SCALE = (
        (0, "Beginner"),
        (1, "Intermediate"),
        (2, "Advanced")
    )

    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    title = models.CharField(max_length=300, verbose_name="question")
    difficulty = models.IntegerField(choices=SCALE)
    date_created = models.DateTimeField(auto_now_add=True)
    # updated= models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title


class Answer(Update):
    # question = models.ForeignKey(Question, on_delete=models.CASCADE)
    question = models.ForeignKey(
        Question, on_delete=models.CASCADE, related_name='answer')
    answer_text = models.CharField(max_length=250)
    is_right = models.BooleanField(default=False)
    
    def __str__(self):
        return self.answer_text


# Absratct Model inheritance