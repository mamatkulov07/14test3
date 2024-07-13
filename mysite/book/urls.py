from django.urls import path
from .views import *

urlpatterns = [
    path('userprofile', UserProfileViewSet.as_view({'get': 'list', 'post': 'create'}),
         name='userprofile_list'),
    path('userprofile/<int:pk>/', UserProfileViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='userprofile_detail'),

    path('book', BookViewSet.as_view({'get': 'list', 'post': 'create'}),
         name='book_list'),
    path('book/<int:pk>/', BookViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='book_detail'),

    path('member', MemberViewSet.as_view({'get': 'list', 'post': 'create'}),
         name='member_list'),
    path('member/<int:pk>/', MemberViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='member_detail'),

    path('loan', LoanViewSet.as_view({'get': 'list', 'post': 'create'}),
         name='Loan_list'),
    path('loan/<int:pk>/', LoanViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='Loan_detail'),

    path('fine', FineViewSet.as_view({'get': 'list', 'post': 'create'}),
         name='file_list'),
    path('fine/<int:pk>/', FineViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='fine_detail'),

    path('reservation', ReservationViewSet.as_view({'get': 'list', 'post': 'create'}),
         name='reservation_list'),
    path('reservation/<int:pk>/', ReservationViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='reservation_detail'),

]