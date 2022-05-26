import graphene
from graphene_django import DjangoObjectType
from graphene_django import DjangoListField

from .models import Category, Quizzes, Question, Answer


""" === ObjectTypes === """


class CategoryType(DjangoObjectType):
    class Meta:
        model = Category
        fields = ["id", "name"]


class QuizzesType(DjangoObjectType):
    class Meta:
        model = Quizzes
        fields = ["id", "title", "category", "quiz"]


class QuestionType(DjangoObjectType):
    class Meta:
        model = Question
        fields = ["title", "quiz"]


class AnswerType(DjangoObjectType):
    class Meta:
        model = Answer
        fields = ["question", "answer_text"]


""" === Schema === """


class Query(graphene.ObjectType):
    all_categories = DjangoListField(CategoryType)
    all_quizes = DjangoListField(QuizzesType)

    single_quiz = graphene.Field(QuizzesType, id=graphene.Int())

    def resolve_all_quizes(root, info):
        """This resolve function override default DjangoListField"""
        return Quizzes.objects.all()

    def resolve_single_quiz(root, info, id):
        return Quizzes.objects.get(pk=id)


schema = graphene.Schema(query=Query)
