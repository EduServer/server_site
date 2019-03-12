from django.shortcuts import render

def notebook(request):
    context = {}
    context['msg'] = 'Welcome to the Embedded Jupyter Notebook!'
    return render(request, "notebook.html", context)

def index(request):
    return notebook(request)

def jupyter(request, notebook_name):
    # Connect to Jupyter Notebook Server for opening notebook_name
    context = {}
    context['jupyter_server'] = 'http://127.0.0.1:8888/notebooks/'
    context['name'] = notebook_name + '.ipynb'
    return render(request, "jupyter.html", context)

def page_not_found(request):
    return render_to_response("404.html")