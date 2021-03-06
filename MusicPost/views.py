from django.template import RequestContext
from django.shortcuts import render_to_response
from django.shortcuts import redirect
from MusicPost import MusicPost_Functions
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
from MusicPost.forms import UserForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout


def user_logout(request):
    context = RequestContext(request)
    logout(request)
    return render_to_response('MusicPost/logout.html',context) 


# Create your views here.

def index(request):
    
    context = RequestContext(request)
    text = MusicPost_Functions.getEntries()
    context_dict = {'list': text}
    
        
        
    if request.method == 'POST':
        submitPost(request)
             
    return render_to_response('MusicPost/index.html', context_dict, context)
    
        
    return redirect('login')




def welcome(request):
    context = RequestContext(request)
    
         
    return render_to_response('MusicPost/welcome.html',context)
  

        
def about(request):
    context = RequestContext(request)
    context_dict = {'boldmessage': "I am bold font from the context"}
    return render_to_response('MusicPost/about.html', context_dict, context)

"""def login(request):
    context = RequestContext(request)
    context_dict = {'boldmessage': "I am bold font from the context"}
    return render_to_response('MusicPost/login.html', context_dict, context)"""

def register(request):
    
        
    # Like before, get the request's context.
    context = RequestContext(request)

    # A boolean value for telling the template whether the registration was successful.
    # Set to False initially. Code changes value to True when registration succeeds.
    registered = False

    # If it's a HTTP POST, we're interested in processing form data.
    if request.method == 'POST':
        # Attempt to grab information from the raw form information.
        # Note that we make use of both UserForm and UserProfileForm.
        user_form = UserForm(data=request.POST)
        

        # If the two forms are valid...
        if user_form.is_valid():
            # Save the user's form data to the database.
            user = user_form.save()

            # Now we hash the password with the set_password method.
            # Once hashed, we can update the user object.
            user.set_password(user.password)
            user.save()

            # Update our variable to tell the template registration was successful.
            registered = True

            return render_to_response(
            'MusicPost/register.html',
            {'user_form': user_form,'registered': registered},
            context)



        # Invalid form or forms - mistakes or something else?
        # Print problems to the terminal.
        # They'll also be shown to the user.
        else:
            
            print (user_form.errors)

    # Not a HTTP POST, so we render our form using two ModelForm instances.
    # These forms will be blank, ready for user input.
    else:
        user_form = UserForm()
        

    # Render the template depending on the context.
    return render_to_response(
            'MusicPost/register.html',
            {'user_form': user_form},
            context)



def user_login(request):
    print("Entering login")
    # Like before, obtain the context for the user's request.
    context = RequestContext(request)

    # If the request is a HTTP POST, try to pull out the relevant information.
    if request.method == 'POST':
        # Gather the username and password provided by the user.
        # This information is obtained from the login form.
        username = request.POST['username']
        password = request.POST['password']

        

        # Use Django's machinery to attempt to see if the username/password
        # combination is valid - a User object is returned if it is.
        user = authenticate(username=username, password=password)

        # If we have a User object, the details are correct.
        # If None (Python's way of representing the absence of a value), no user
        # with matching credentials was found.
        if user is not None:
            # Is the account active? It could have been disabled.
            if user.is_active:
                # If the account is valid and active, we can log the user in.
                # We'll send the user back to the homepage.
                login(request, user)
               
                print("Should go to home page")
                return redirect('index')
            else:
                # An inactive account was used - no logging in!
                return HttpResponse("Your MusicPost account is disabled.")
        else:
            # Bad login details were provided. So we can't log the user in.
            print ("Invalid login details: {0}, {1}".format(username, password))
            return HttpResponse("Invalid login details supplied.")

    # The request is not a HTTP POST, so display the login form.
    # This scenario would most likely be a HTTP GET.
    else:
        # No context variables to pass to the template system, hence the
        # blank dictionary object...
        return render_to_response('MusicPost/login.html', {}, context)



def submitPost(request):
    text = request.POST['mytextbox']
    user = request.user.username
    print("before calling storepost")
    MusicPost_Functions.storePost(text, user)
    print("after calling storepost")
         
