from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from snippets.models import Snippet #Snippetモデルをインポート

# Create your views here.
def top(request):
    #実践Django Pythonによる本格Webアプリケーション開発
    #return render(request, "snippets/top.html")
    #return HttpResponse(b"Hello World")
    #実践Django Pythonによる本格Webアプリケーション開発(p.93)
    snippets = Snippet.objects.all()
    context = {"snippets": snippets}    #テンプレートエンジンに与えるPythonオブジェクト
    return render(request, "snippets/top.html", context)

def snippet_new(request):
    return HttpResponse('スニペットの登録')

def snippet_edit(request, snippet_id):
    return HttpResponse('スニペットの編集')

def snippet_detail(request, snippet_id):
    return HttpResponse('スニペットの詳細閲覧')

#実践Django Pythonによる本格Webアプリケーション開発(p.102)
def snippet_detail(request, snippet_id):
    snippet = get_object_or_404(Snippet, pk=snippet_id)
    return render(request, 'snippets/snippet_detail.html', {'snippet':snippet})
