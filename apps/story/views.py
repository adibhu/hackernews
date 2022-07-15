from django.shortcuts import redirect, render, get_object_or_404
from .forms import StoryForm
from django.contrib.auth.decorators import login_required
from .models import Story, Vote
import datetime
# Create your views here.

def frontpage(request):
    date_from = datetime.datetime.now() - datetime.timedelta(days=1)
    stories = Story.objects.filter(created_at__gte=date_from).order_by('-number_of_votes')[:30]
    return render(request, 'story/frontpage.html', {'stories' : stories})

def newest(request):
    stories = Story.objects.all()[:200]
    return render(request, 'story/newest.html', {'stories':stories})

@login_required
def vote(request, story_id):
    story = get_object_or_404(Story, pk=story_id)
    #47
    # if not Vote.objects.filter(created_by=request.user, story=story):
    vote = Vote.objects.create(story=story, created_by = request.user)
    return redirect('frontpage')

@login_required
def submit(request):
    if request.method == 'POST':
        form = StoryForm(request.POST)

        if form.is_valid():
            story = form.save(commit=False)
            story.created_by = request.user
            story.save()

            return redirect('frontpage')
    else:
        form = StoryForm()

    return render(request, 'story/submit.html', {'form':form})