
def profile(request):
    from django.contrib.auth.models import User, Group
    from Profile.models import  ProfilePic
    current_user = request.user
    user_id = current_user.id
    profile_pic = ProfilePic.objects.filter(user_id=user_id)

    return {
        'profile_pic': profile_pic  # Add 'latest_song' to the context
    }