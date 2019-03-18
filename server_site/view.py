import os
from django.shortcuts import render

global PORT
global TOKEN
global FLAG
global DIR
FLAG = False

def init():
    global PORT
    global TOKEN
    PORT = '8888'
    TOKEN = '531fd582066762d586fef888248f69e31ca63c15277a863d'
    DIR = '/etc/notebooks'

def notebook(request):
    context = {}
    context['msg'] = 'Welcome to the Embedded Jupyter Notebook!'
    return render(request, "notebook.html", context)

def index(request):
    global FLAG
    # Configure Server
    if not FLAG:
        init()
        cmd = ['LANG=zh_CN', 'nohup', 'jupyter', 'notebook', '--port=' + PORT, '--NotebookApp.token=' + TOKEN, '--NotebookApp.notebook_dir=' + DIR, '--allow-root', '&']
        os.system(' '.join(cmd))
    FLAG = True
    return notebook(request)

def jupyter(request, notebook_name):
    init()
    # Connect to Jupyter Notebook Server for opening notebook_name
    context = {}
    context['jupyter_server'] = 'http://192.168.3.80:'+PORT+'/notebooks/'
    context['name'] = notebook_name + '.ipynb'
    context['token'] = TOKEN
    return render(request, "jupyter.html", context)

def page_not_found(request):
    return render_to_response("404.html")
