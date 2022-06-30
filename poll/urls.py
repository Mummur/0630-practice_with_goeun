from django.urls import path

from poll import views
# home_work 에서 views.py를 가져온다


urlpatterns = [
    path("index/", views.index),
    path("survey/", views.survey),
]

# home_work(app)안에(경로주의!!) urls.py 라는 파일을 생성하여 위와 같이 작성한다.
# views.py와 urls.py를 연결하는 과정이다.
# views.landing == views.py에 존재하는 landing 함수를 의미한다.