from MusicPost.models import User
from MusicPost.models import post



def storePost(text, user):
   
    p = post(poster = user, submission = text)
    p.save()

def getEntries():
    
    all_entries = post.objects.all()
    
    return all_entries
