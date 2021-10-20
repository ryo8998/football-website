from django.shortcuts import get_object_or_404, render
from django.views import View
from django.template.response import TemplateResponse
from django.views.generic import TemplateView
import random
from .models import Player

index_pics = [
    "https://thehill.com/sites/default/files/styles/thumb_small_article/public/istock-soccer-sports-lgbt-2019.jpg?itok=RUuuRhwc",
    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRgZagkLwjqzSp-bUJo6rWAKKJ-drPf7EgV1nl2yhiX0MIqklI2U26Ox8vMBoXNehIzEXM&usqp=CAU",
    "https://www.worldfirst.com/app/uploads/2018/06/FIFA_World_Cup_2006_-_GER_vs_SWE-759x500.jpg",
    "https://www.soccer-king.jp/wp-content/uploads/2018/06/GettyImages-1001036088.jpg",
    "https://www.visitbritain.com/sites/default/files/styles/wysiwyg_image/public/consumer/northamerica/arsenal_omgb.jpg?itok=_NYhKwhV",
    "https://www.aljazeera.com/wp-content/uploads/2021/05/2021-05-29T211724Z_127224441_UP1EH5T1N4ZMU_RTRMADP_3_SOCCER-CHAMPIONS-MCI-CHE-REPORT.jpg?resize=770%2C513"
]

rule_pics = [
    "https://thumbs.dreamstime.com/b/football-judge-cards-8653673.jpg",
    "https://lh3.googleusercontent.com/proxy/H65vYsRHrkfbHEEgIYzf1Q_V31Qh54nuWpmX1WLyP0qC-qCxDeZ8fmvpzXVywdT4F857tjbyTkkxVwolcqxxzZxn5cyFQ0CPdKaiZnnri1879skVU_aN67l0M8JkSzjWDjHv_d-9BmY4",
    "https://media.istockphoto.com/vectors/soccer-referee-character-set-vector-id636887192?k=20&m=636887192&s=612x612&w=0&h=1vepq78CuUqJYKqBmBNNoppX0WgIDwpanOIvyO3FQYY="
]


links_url = {
    "Wikipedia": "https://en.wikipedia.org/wiki/Association_football",
    "Top Players":"https://www.theguardian.com/football/ng-interactive/2020/dec/21/the-100-best-male-footballers-in-the-world-2020",
    "Recursion":"https://recursionist.io/"
}
   
# Create your views here.
def index(request):
   pics = random.sample(index_pics,3)
   return render(request,'website/index.html',{
       "pics":pics
   })

def rule(request):
    context = {
        "pic_main":rule_pics[0],
        "pic_sub": rule_pics[1]
    }
    return render(request,"website/rule.html",context)

def star_players(request):
    players = Player.objects.all()
    context = {
        "players":players
    }
    return render(request,"website/star_players.html",context)

def player_detail(request,id):
    player = get_object_or_404(Player,id=id)
    print(player)
    print(player.name)

    context = {
        "player":player
    }
    return render(request,"website/player_detail.html",context)

def links(request):
    context = {
        "links":links_url
    }
    return render(request,"website/link.html", context)