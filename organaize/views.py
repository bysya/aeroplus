from django.http import HttpResponse, FileResponse
from django.shortcuts import render, redirect
from .models import Customer, Object
import io
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter

def spdf(request):
    buf = io.BytesIO()
    c = canvas.Canvas(buf, pagesize=letter, bottomup=0)
    texttob = c.beginText()
    texttob.setTextOrigin(inch, inch)
    texttob.setFont("Times-Roman", 18)

    objects = Object.objects.all()
    #c.drawImage("object.foto.url", 10, 10)
    lines = []

    for object in objects:
        lines.append(str(object.name))
        lines.append(str(object.data))
        lines.append(str(object.adres))

    for line in lines:
        texttob.textLine(line)

    c.drawText(texttob)
    c.showPage()
    c.save()
    buf.seek(0)
    return FileResponse(buf, as_attachment=True, filename="{name}.pdf")


def index(request):
    return render(request, "organaize/index.html", {
        "customers": Customer.objects.all(),
        "objects": Object.objects.all()
    })

def create(request):
    if request.method == 'POST':
        customer = Customer()
        customer.name = request.POST['name']
        customer.phone = request.POST['phone']
        customer.save()
        return redirect('index')
    return render(request, "organaize/create.html")

def customer(request, customer_id):
    customer = Customer.objects.get(id=customer_id)
    return render(request, "organaize/customer.html", {
        "customer": customer
    })


def object(request, customer_id, object_name):
    customer = Customer.objects.get(id=customer_id)
    object = Object.objects.get(name=object_name)
    return render(request, "organaize/object.html", {
        "objects": Object.objects.all(),
        "object": object,
        "customer": customer
    })