from django.urls import path
from snippets import views

urlpatterns = [
    #実践Django Pythonによる本格Webアプリケーション開発(p.65)
    path("new/", views.snippet_new, name="snippet_new"),
    path("<int:snippet_id>/", views.snippet_detail, name="snippet_detail"),
    path("<int:snippet_id>/edit/", views.snippet_edit, name="snippet_edit"),
]