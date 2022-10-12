from django.urls import path,include

from moviesapp import views

app_name = 'moviesapp'

urlpatterns = [
    path('',views.index,name='index'),
    path('movie/<int:movie_id>/',views.details,name='details'),
    path('add/',views.add_movie,name='add_movies'),
    path('update/<int:id>/',views.update,name='update'),
    path('delete/<int:id>/',views.delete,name='delete')

]
