from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseForbidden
from snippets.models import Snippet #Snippetモデルをインポート
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from snippets.forms import SnippetForm

# Create your views here.
def top(request):
    #実践Django Pythonによる本格Webアプリケーション開発
    #return render(request, "snippets/top.html")
    #return HttpResponse(b"Hello World")
    #実践Django Pythonによる本格Webアプリケーション開発(p.93)
    snippets = Snippet.objects.all()
    context = {"snippets": snippets}    #テンプレートエンジンに与えるPythonオブジェクト
    return render(request, "snippets/top.html", context)

#実践Django Pythonによる本格Webアプリケーション開発 1.4.4
@login_required
def snippet_new(request):
    if request.method == 'POST':
        form = SnippetForm(request.POST)
        if form.is_valid():
            snippet = form.save(commit=False)
            snippet.created_by = request.user
            snippet.save()
            return redirect(snippet_detail, snippet_id=snippet.pk)
    else:
        form = SnippetForm()
    return render(request, "snippets/snippet_new.html", {'form': form})

#実践Django Pythonによる本格Webアプリケーション開発 1.4.4
@login_required
def snippet_edit(request, snippet_id):
    snippet = get_object_or_404(Snippet, pk=snippet_id)
    if snippet.created_by_id != request.user.id:
        return HttpResponseForbidden("このスニペットの編集は許可されていません。")
    if request.method == "POST":
        form = SnippetForm(request.POST, instance=snippet)
        if form.is_valid():
            form.save()
            return redirect('snippet_detail', snippet_id=snippet_id)
    else:
        form = SnippetForm(instance=snippet)
    return render(request, 'snippets/snippet_edit.html',{'form': form})


def snippet_detail(request, snippet_id):
    return HttpResponse('スニペットの詳細閲覧')

#実践Django Pythonによる本格Webアプリケーション開発(p.102)
def snippet_detail(request, snippet_id):
    snippet = get_object_or_404(Snippet, pk=snippet_id)
    return render(request, 'snippets/snippet_detail.html', {'snippet':snippet})
