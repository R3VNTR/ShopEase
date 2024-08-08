from django.urls import path
from . import views

urlpatterns = [
    path('new/<int:item_pk>', views.new_conversation, name = 'new-message'),
    path('inbox/', views.inbox, name = 'inbox-message'),
    path('message_details/<int:conversation_id>', views.conversation_details, name = 'message-details')
]
