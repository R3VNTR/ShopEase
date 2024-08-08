from django.contrib.auth.decorators import login_required
from .models import ConversationMessage, Conversation

def unread_messages(request):
    if request.user.is_authenticated:
        conversations = Conversation.objects.filter(members=request.user)

        unread_count = ConversationMessage.objects.filter(
            conversation__in=conversations,
            conversation__item__user=request.user,
            is_read=False
        ).count()
        return {'unread_count': unread_count}
    return {'unread_count': 0}