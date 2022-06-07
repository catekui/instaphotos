from django.shortcuts import render,redirect,get_object_or_404
from django.http  import HttpResponse,Http404,HttpResponseRedirect
from .models import Image,Comment, Like
from users.models import Profile
from django.contrib.auth.decorators import login_required
from .forms import CommentForm, AddPostForm
from django.contrib.auth import login, authenticate

# Create your views here.
@login_required(login_url='login/')
def home(request):
    posts = Image.objects.all().order_by('-id')
    users = Profile.objects.all()
    form = CommentForm()
    if request.method == 'POST':  
        form = CommentForm(request.POST, request.FILES)
        if form.is_valid():
            commentt = form.save(commit=False)
            commentt.user = request.POST.user
            commentt.save()
            return redirect('home')
            
    return render(request, 'instagram/home.html', {"posts":posts,  "form":form, 'users':users})

# def user_profile(request,user_id):
#     user_profile = Profile.objects.filter(user_id = user_id).first()
#     images = Image.objects.filter(user_id = user_id)

#     return render(request, 'userprofile.html', {'user_profile':user_profile, 'images':images})    

def search_results(request):
    
    if 'posts' in request.GET and request.GET["posts"]:
        search_term = request.GET.get("posts")
        searched_posts = Image.search_by_name(search_term)
        message = search_term

        return render(request, 'instagram/search.html',{"message":message,"posts": searched_posts})

    else:
        message = "You have not searched for any term"
        return render(request, 'instagram/search.html',{"message":message})
    
@login_required
def comments(request,image_id):
  form = CommentForm()
  image = Image.objects.filter(pk = image_id).first()
  if request.method == 'POST':
    form = CommentForm(request.POST)
    if form.is_valid():
      comment = form.save(commit = False)
      comment.user = request.user
      comment.image = image
      comment.save() 
  return redirect('home') 

def like_post(request):
    current_user = request.user
    
    if request.method == 'POST':
        image_id = request.POST.get('image_id')
        image = Image.objects.get(id=image_id)
        
        if current_user in image.liked.all():
            image.liked.add(current_user)
        else:
            image.liked.add(current_user)
            
        like,created = Like.objects.get_or_create(user=current_user,image_id=image_id)  
        
        if not created:
            if like.response == 'Like':
                like.response = 'Unlike'
                
        else:
                like.response = 'Like' 
                
        like.save()
    return redirect('home')

@login_required()
def upload(request):
    if request.method == 'POST' and request.FILES['image']:
        form = AddPostForm(request.POST, request.FILES)

        if form.is_valid():
            image = form.save(commit=False)
            image.user = request.user
            image.save()

            return redirect(request.META.get('HTTP_REFERER'), {'success': 'Image Uploaded Successfully'})

    return redirect(request.META.get('HTTP_REFERER'), {'error': 'Image Uploaded Successfully'})