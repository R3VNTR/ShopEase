from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Conversation, ConversationMessage
from store.models import Product
from .forms import ConversationMessageForm
from django.utils import timezone 


@login_required
def new_conversation(request, item_pk):
    item = get_object_or_404(Product, pk=item_pk)
    cat_slug = item.category.slug
    itm_vendor = item.user.username

    if item.user == request.user:
        return redirect('frontpage')

    coversations = Conversation.objects.filter(
        item=item).filter(members__in=[request.user.id])

    if coversations:
        return redirect('message-details',conversation_id=coversations.first().id)

    if request.method == 'POST':
        form = ConversationMessageForm(request.POST)

        if form.is_valid():
            conversation = Conversation.objects.create(item=item)
            conversation.members.add(request.user)
            conversation.members.add(item.user)
            conversation.save()

            conversation_message = form.save(commit=False)
            conversation_message.conversation = conversation
            conversation_message.created_by = request.user
            conversation_message.save()

            return redirect('product_detail', slug=item.slug, category_slug=cat_slug)

    else:
        form = ConversationMessageForm()

    return render(request, 'coversation/new.html', {'form': form, 'itm_vendor':itm_vendor ,'item_slug':item.slug, 'cat_slug':cat_slug})

@login_required
def inbox(request):
    coversations = Conversation.objects.filter(members__in=[request.user.id])
    conversation_data = [
        {
            'conversation': conversation,
            'members': conversation.members.all()
        }
        for conversation in coversations
    ]
    return render(request, 'coversation/inbox.html', {'conversations':coversations,'conversation_data': conversation_data})


@login_required
def conversation_details(request,conversation_id):
    conversation = get_object_or_404(Conversation, id=conversation_id, members=request.user)
    latest_message = conversation.get_latest_message()

    if request.method == 'POST':

        form = ConversationMessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.conversation = conversation
            message.created_by = request.user
            message.save()
            conversation.modified_at = timezone.now()
            conversation.save()
            return redirect('message-details', conversation_id=conversation.id)
    else:

        if latest_message.created_by !=request.user:
            ConversationMessage.objects.filter(
            conversation=conversation,
            id=latest_message.id
            ).update(is_read=True)
            
        form = ConversationMessageForm()

    return render(request, 'coversation/conversation_details.html', {
        'conversation': conversation,
        'form': form
    })