from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import Conversation,Message
from .forms import MessageForm

@login_required
def inbox(request):
    conversations = Conversation.objects.filter(members__in=[request.user.id])

    return render(request, 'chat/inbox.html', {
        'conversations': conversations
    })

@login_required
def chat(request, pk): #pk is the converstaion id 
    conversation = Conversation.objects.filter(members__in=[request.user.id]).get(pk=pk)
    #if there is an existing conversation
    if conversation: 
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
    #if there isn't an existing conversation, create a new one
    else: 


    return render(request, 'conversation/chat.html', {
        'conversation': conversation,
        'form': form
    })

#In the template, using this method to set interval and display all the messages real time, without refreshing
def getMessages(request, pk):
    the_chat = Conversation.objects.get(pk=pk)

    messages = Message.objects.filter(conversation=the_chat)
    return JsonResponse({"messages":list(messages.values())})
