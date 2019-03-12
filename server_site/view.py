from django.shortcuts import render

def notebook(request):
    context = {}
    context['var1'] = 'Hello world!'
    context['var2'] = True
    return render(request, "notebook.html", context)