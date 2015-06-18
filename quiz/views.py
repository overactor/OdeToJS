"""
    Views for OdeToJS
    Copyright (C) 2015  Rik de Graaff

    This program is free software; you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation; either version 2 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License along
    with this program; if not, write to the Free Software Foundation, Inc.,
    51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
"""

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