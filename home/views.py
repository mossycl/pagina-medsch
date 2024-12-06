from django.shortcuts import render
from django_user_agents.utils import get_user_agent

# Create your views here.
def index(request):
    user_agent = get_user_agent(request)
    context = {
        "mobile_user" : user_agent.is_mobile,
        "pc_user" : user_agent.is_pc,
        "tablet_user" : user_agent.is_tablet,
        "os" : user_agent.os.family
        }
    return render(request, 'index.html', context)