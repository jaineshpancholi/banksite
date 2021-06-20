from django.db.models.fields import DateTimeField
from django.shortcuts import render, redirect
from Bank.models import *
from datetime import date

# Create your views here.

def Home(request):
    return render(request, 'index.html')

def users(request):
    allusers = user.objects.all()
    d = {"allusers":allusers}
    return render(request, 'AllUsers.html', d)

def MakeTransaction(request):
    users = user.objects.all()

    d = {"users":users}
    return render(request, 'MakeTransaction.html', d)

def TransferTo(request, uid):
    error = False
    users = user.objects.get(id = uid)
    allusers = user.objects.filter()
    
    # notone = alluser.objects.filter(Name = users.Name)[0]
    # print(notone)
    
    if request.method == "POST":
        datadict = request.POST
        
        sender = user.objects.get(Name = users.Name)
        # print(sender)
        uid = datadict['uid']
        receiver = user.objects.get(id = uid)
        # print(receiver)
        amount = datadict['amount']
        # print(amount)
        tdate = date.today()
        balance = users.Balance
        if balance < (int(amount)):
            error = True
        else:
            users.Balance -= (int(amount))
            users.save()

            receiver.Balance += (int(amount))
            receiver.save()
            
            TransactionHistory.objects.create(SenderName = sender, ReceiverName = receiver, Amount = amount, Date = tdate)
            return redirect("mtransaction")

    d = {"users":users, "allusers":allusers, "error":error}
    return render(request, 'TransferTo.html', d)


def history(request):
    history = TransactionHistory.objects.filter()
    
    d = {"history":history}
    return render(request, 'History.html', d)

