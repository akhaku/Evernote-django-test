from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from evernote_auth import EvernoteAPI

def landing(request):
    return render_to_response('home.html', {},
            context_instance=RequestContext(request))

def run_evernote_auth(request):
    """ Starts the OAuth token obtaining process by obtaining the token we use
        to request the user's token
    """
    callback_url = request.build_absolute_uri(reverse(
        'basic.views.get_evernote_token', args=[]))
            
    everAuth = EvernoteAPI()
    return everAuth.get_token(request, callback_url)

def get_evernote_token(request):
    """ View that handles the callback from the Evernote OAuth call and
        stores the OAuth token for the user
    """
    everAuth = EvernoteAPI()
    credentials = everAuth.get_user_token(request)
    # credentials here contain OAuth token, save it!
    return HttpResponseRedirect(reverse('basic.views.post_evernote_token',
        args=[]))
 
def post_evernote_token(request):
    return render_to_response('evernote_resp.html', {},
            context_instance=RequestContext(request))
