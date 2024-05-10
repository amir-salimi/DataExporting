from django.shortcuts import render
from django.views.generic import DetailView

from django.core.exceptions import ObjectDoesNotExist

from django.http import HttpResponse

from .models import Product, AnswerAndQuestion, About, ProductPhoto, ProductPlanMap, Category, Status


class GetData(DetailView):
    def get(self, request):
        question = request.GET.get("question", None)
        answer = request.GET.get("answer", None)
        q_a_link = request.GET.get("link", None)
        if question and q_a_link is not None:
            AnswerAndQuestion.objects.create(link=q_a_link, question=question, answer=answer)
        
        about = request.GET.get("about", None)
        about_link = request.GET.get("link", None)

        if about and about_link:
            About.objects.create(link=about_link, about=about)

        img = request.GET.get("img", None)
        img_link = request.GET.get("link", None)
        if img and img_link:
            ProductPhoto.objects.create(link=img_link, image=img)

        plan = request.GET.get("plan", None)
        plan_link = request.GET.get("link", None)
        if plan_link and plan:
            ProductPlanMap.objects.create(link=plan_link, plan_map=plan)

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
        link = request.GET.get("link") 
        
        if name and area and bed_room and category :
            try:
                cat = Category.objects.get(category=category)
            except ObjectDoesNotExist:
                cat = Category.objects.create(category=category)
            
            try:
                stat = Status.objects.get(status=status)
            except ObjectDoesNotExist:
                stat = Status.objects.create(status=status)

            

            map = ProductPlanMap.objects.filter(link=link)
            photo = ProductPhoto.objects.filter(link=link)


            frequntly_questions = AnswerAndQuestion.objects.filter(link=link)

            about = About.objects.filter(link=link)


            
            p = Product.objects.create(
                name=name,
                location=location, 
                developer=developer, 
                link=link, 
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


        return HttpResponse("ok")

