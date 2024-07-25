from typing import Any
from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpRequest, HttpResponse

from django.views.generic import DetailView

from django.core.exceptions import ObjectDoesNotExist

from django.http import HttpResponse

from .models import Product, AnswerAndQuestion, About, ProductPhoto, ProductPlanMap, Category, Status

class HttpResponseOk(HttpResponse):
    status_code = 200

def clean_data(data):
    data = data.replace("W", "")
    data = data.replace("H", "")
    data = data.replace(" ", "")
    data = data.replace("cm", "")
    data = data.replace(",", "")
    data = data.replace("AED", "")
    return data
        


class EasyMapScraping(DetailView):
    def get(self, request):
        area = None
        city = request.GET.get("city", None)
        size = request.GET.get("size", None)
        finish = request.GET.get("finish", None)
        type = request.GET.get("type", None)
        price = request.GET.get("price", None)
        about = request.GET.get("description", None)
        prj_link = request.GET.get("link", None)
        img_link = request.GET.get("img", None)

        if prj_link and img_link :
            ProductPhoto.objects.get_or_create(link=prj_link, image=img_link)

        try:
            About.objects.get_or_create(link=prj_link, about=about)
        except:
            pass


        try:
            size_list = []
            size = size.split("x")
            for s in size:
                data = clean_data(s)
                size_list.append(data)

            area = float(size_list[0])*float(size_list[1])
        except:
            pass

        if prj_link and city and area and price is not None:
            try:
                ab = About.objects.filter(link=prj_link)
                image = ProductPhoto.objects.filter(link=prj_link)

                p = Product.objects.create(
                    name=city, 
                    location=city, 
                    link=prj_link, 
                    city=city, 
                    area=area, 
                    price=float(clean_data(price)), 
                    type=type, 
                    finish=finish
                )
                p.about.set(ab)
                p.photo.set(image)
            except:
                pass        
        
        return HttpResponseOk()



class OprScrapingData(DetailView):
    def get(self, request):
        link_prj = request.GET.get("link", None)

        question = request.GET.get("question", None)
        answer = request.GET.get("answer", None)
        if question and link_prj is not None:
            AnswerAndQuestion.objects.create(link=link_prj, question=question, answer=answer)
        
        about = request.GET.get("about", None)
        if about and link_prj:
            About.objects.create(link=link_prj, about=about)

        img = request.GET.get("img", None)
        if img and link_prj:
            ProductPhoto.objects.create(link=link_prj, image=img)

        plan = request.GET.get("plan", None)
        if link_prj and plan:
            ProductPlanMap.objects.create(link=link_prj, plan_map=plan)

        bed_room = request.GET.get("bed_room", None)
        area = request.GET.get("area", None)
        handover = request.GET.get("handover", None)
        name = request.GET.get("name", None)
        location = request.GET.get("location", None)
        developer = request.GET.get("developer", None)
        category = request.GET.get("category", None)
        price = request.GET.get("price", None)
        payment_plan = request.GET.get("payment_plan", None)
        status = request.GET.get("status", None)
        approximate_location = request.GET.get("approximate_location") 

        if name and area and bed_room and category :
            try:
                if price.isdigit():
                    pass
                else:
                    price = None
                cat, cat_created = Category.objects.get_or_create(category=category)
                stat, stat_created = Status.objects.get_or_create(status=status)
                map = ProductPlanMap.objects.filter(link=link_prj)
                photo = ProductPhoto.objects.filter(link=link_prj)
                frequntly_questions = AnswerAndQuestion.objects.filter(link=link_prj)
                about = About.objects.filter(link=link_prj)
                p = Product.objects.create(
                    name=name,
                    location=location, 
                    developer=developer, 
                    link=link_prj, 
                    category = cat,
                    status = stat,
                    price=price, 
                    area=area, 
                    payment_plan=payment_plan, 
                    bed_room=bed_room, 
                    handover=handover, 
                    approximate_location=approximate_location
                    )
                p.frequntly_question.set(frequntly_questions)
                p.about.set(about)
                p.photo.set(photo)
                p.plan_map.set(map)
            except:
                pass
        return HttpResponseOk()



class DxbScrapingData(DetailView):
    def get(self, request):
        name = request.GET.get("name", None)
        development = request.GET.get("development", None)
        city = request.GET.get("city", None)
        img = request.GET.get("img", None)
        price = request.GET.get("price", None)
        price_per_meter = request.GET.get("price_per_meter", None)
        area = request.GET.get("area", None)
        category = request.GET.get("category", None)
        bed_room = request.GET.get("bed_room", None)
        views = request.GET.get("views", None)
        handover = request.GET.get("handover", None)
        developer_project_number = request.GET.get("developer_project_number", None)
        developer = request.GET.get("developer", None)
        location = request.GET.get("location", None)
        link = request.GET.get("link", None)

        try:
            if name and category and bed_room and area and link :
                area = area.replace("مترمربع", "")
                cat, cat_created = Category.objects.get_or_create(category=category)
                photo, photo_created = ProductPhoto.objects.get_or_create(link=link, image=img)
                p = Product.objects.create(
                    name=name,
                    location=location, 
                    developer=developer, 
                    link=link, 
                    category = cat,
                    price=price, 
                    area=area, 
                    bed_room=bed_room, 
                    handover=handover,
                    developer_project_number = developer_project_number,
                    viwes = int(views),
                    per_meter_price = price_per_meter,
                    city = city,
                    development = development,
                    )
                p.photo.add(photo)
                p.save()
        except:
            pass
        
        return HttpResponseOk()