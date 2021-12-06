from django.urls import path
from measurement import views

urlpatterns = [
    path('sensors/', views.CreateSensor.as_view()),
    path('sensors/<pk>/', views.UpdateSensor.as_view()),
    path('measurements/', views.MakeMeasurement.as_view()),
    path('sensors/<pk>', views.SensorListView.as_view())
    # TODO: зарегистрируйте необходимые маршруты
]
