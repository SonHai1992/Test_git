from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Question, Choice, Customer
from django.utils import timezone
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

#Send mail
from django.conf import settings
from django.core.mail import send_mail


def send_mail_view(request):
    if request.method == 'POST':
        email = request.POST.get('email', '')
        data = """
                Hello! I am Phuc.
            """
        send_mail('Welcome!', data, "PLC", [email,], fail_silently=False)
    return render(request,'home/send_mail.html')


# Create your views here.


def index(request):
    # List ra toan bộ data trong bảng Question
    list_questions = Question.objects.filter(delete=False)
    # Chia data trong bảng Quetsion thành 4 trang (pages)
    paginator = Paginator(list_questions, 4)
    # Lấy cái trang mà user đang trỏ đến (Lấy từ URL, Không có thì mặc định là 1)
    page = request.GET.get('page')
    # Từ cái trang lấy đc từ URL, lấy dữ liệu tương ứng với trang đó
    customers = paginator.get_page(page)
    return render(request, 'home/index.html', {'customers': customers})



def AddQuestion(request):
    if request.method == 'POST':
        question_new = request.POST.get('add')
        if question_new:
            a = Question(question_text=question_new, date_time=timezone.now())
            a.save()

    return redirect('/')


def EditQuestion(request, id_input):
    question = Question.objects.get(id=id_input)
    if request.method == 'POST':
        question_edit = request.POST.get('edit')
        if question.question_text != question_edit:
            question.question_text = question_edit
            question.save()
        return redirect('/')

    return render(request,'home/edit.html',{'question':question})



def DeleteQuestion(request, id_input):
    question = Question.objects.get(id=id_input)
    if request.method == 'POST':
        question.delete = True
        question.save()
    return redirect('/')



def Error(request):
    return redirect(request,'home/error.html')


def list(request):
    customer_list = Customer.objects.all()
    paginator = Paginator(customer_list,2)
    pageNumber = request.GET.get('pa')

    customers = paginator.get_page(pageNumber)

    return render(request, 'home/list.html', {'customers': customers})
