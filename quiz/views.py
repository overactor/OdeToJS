from django.shortcuts import render

from .models import Expression

def index(request):
    return render(request, 'quiz/index.html')

def expression(request, expression_number):
    try:
        expression = Expression.objects.get(number=expression_number)
    except Expression.DoesNotExist:
        raise Http404("This question does not exist")
    try:
        next_expression = Expression.objects.get(number=int(expression_number) + 1)
        next = int(expression_number) + 1
    except Expression.DoesNotExist:
        next = "end"
    return render(request, 'quiz/expression.html', {'expression': expression, 'next': next})

def end(request):
    return render(request, 'quiz/index.html')