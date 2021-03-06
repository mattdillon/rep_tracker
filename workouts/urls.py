from django.urls import path

from . import views

urlpatterns =[ 
    path('',views.index, name='index'),
    path('userExercises', views.exerciseList, name='exercises'),
    path('exercise', views.apiExercise, name='apiExercise'),
    path('home',views.index, name = 'home'),
    path('session', views.session, name='workoutSession'),
    path('api/set', views.apiSet, name='apiSet'),
    path('api/session',views.apiSession, name='apiSession'),
    path('session_summary/<int:session_id>', views.sessionSummary, name='sessionSummary'),
    path('api/individual', views.apiIndiv, name='apiIndiv'),
    path('api/signOut', views.signOut, name='apiSignOut'),
    path('history', views.historySummary, name='historySummary'),
    path('add_exercise', views.addExercise, name='addExercisePage'),
    path('api/exercise', views.apiExercise, name='apiExercise'),
    path('profile', views.profilePage, name='profilePage'),
    path('newProgram', views.planView, name ='planView'),
    path('api/program', views.apiProgram, name='apiProgram'),
    path('api/plannedSets', views.apiPlannedSets, name='apiPlannedSets'),
    path('userPrograms', views.programList, name='programList'),
    path('startProgram', views.startProgram, name='startProgram'),
]
