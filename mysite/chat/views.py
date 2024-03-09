from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.contrib import messages
from .models import Conversation,Message
from mainPage.models import Product
from .forms import MessageForm

@login_required
def inbox(request):
    conversations = Conversation.objects.filter(members__in=[request.user.id])

    return render(request, 'chat/inbox.html', {
        'conversations': conversations
    })

@login_required
def new_chat(request, pk): #pk is the item id 
    item = get_object_or_404(Product, pk=pk)

    conversations = Conversation.objects.filter(item=item).filter(members__in=[request.user.id])

    if conversations:
        return redirect('chat:chat', pk=conversations.first().id)

    if request.method == 'POST':
        form = MessageForm(request.POST)

        if form.is_valid():
            conversation = Conversation.objects.create(item=item)
            conversation.members.add(request.user)
            conversation.members.add(item.created_by)
            conversation.save()

            conversation_message = form.save(commit=False)
            conversation_message.conversation = conversation
            conversation_message.created_by = request.user
            conversation_message.save()
            messages.success(request, "Conversation saved!")
            return redirect('chat:inbox')
    else:
        form = MessageForm()
    
    return render(request, 'chat/chat.html', {
        'form': form
    })

@login_required
def chat(request, pk): #pk is the converstaion id 
    conversation = Conversation.objects.filter(members__in=[request.user.id]).get(pk=pk)
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
                conversation_message = form.save(commit=False)
                conversation_message.conversation = conversation
                conversation_message.created_by = request.user
                conversation_message.save()

                conversation.save()

                return redirect('chat:inbox', pk=pk)
        else:
            form = MessageForm()
    return render(request, 'conversation/chat.html', {
        'conversation': conversation,
        'form': form
    })

#In the template, using this method to set interval and display all the messages real time, without refreshing
def getMessages(request, pk):
    the_chat = Conversation.objects.get(pk=pk)

    messages = Message.objects.filter(conversation=the_chat)
    return JsonResponse({"messages":list(messages.content)})
