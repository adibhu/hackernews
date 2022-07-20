from django.shortcuts import redirect, render, get_object_or_404
from .forms import StoryForm, CommentForm
from django.contrib.auth.decorators import login_required
from .models import Story, Vote, Comment
import datetime
from django.contrib.auth.models import User

# Create your views here.


def frontpage(request):
    date_from = datetime.datetime.now() - datetime.timedelta(days=1)
    stories = Story.objects.filter(
        created_at__gte=date_from).order_by('-number_of_votes')[:30]
    return render(request, 'story/frontpage.html', {'stories': stories})


def story(request, story_id):
    story = get_object_or_404(Story, pk=story_id)

    # return render(request, 'story/detail.html', {'story':story})

    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.story = story
            comment.created_by = request.user
            comment.save()

            return redirect('story', story_id=story_id)
    else:
        form = CommentForm()

    return render(request, 'story/detail.html', {'story': story, 'form': form})


def newest(request):
    stories = Story.objects.all()[:200]
    return render(request, 'story/newest.html', {'stories': stories})


@login_required
def vote(request, story_id):
    story = get_object_or_404(Story, pk=story_id)
    next_page = request.GET.get('next_page', '')
    # 47
    # if not Vote.objects.filter(created_by=request.user, story=story):
    vote = Vote.objects.create(story=story, created_by=request.user)

    if next_page == 'story':
        return redirect('story', story_id=story_id)
    else:
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

    return render(request, 'story/submit.html', {'form': form})

def ask(request):
    stories = Story.objects.all()[:200]
    return render(request, 'story/ask.html', {'stories': stories})

def show(request):
    stories = []
    for story in Story.objects.all():
        if str(story)[:7] == 'Show HN':
            stories.append(story)
    return render(request, 'story/show.html', {'stories': stories})

def comments(request):
    stories = Comment.objects.all()[:200]
    return render(request, 'story/comments.html', {'stories': stories})

def search(request):
    query = request.GET.get('query', '')

    if len(query) > 0:
        stories = Story.objects.filter(title__icontains=query)
    else:
        stories =[]

    return render(request, 'story/search.html', {'stories': stories, 'query': query})

def threads(request, username):
    user = get_object_or_404(User, username=username)
    threads = user.stories.all()

    return render(request, 'story/threads.html', {'user':user, 'threads':threads})
