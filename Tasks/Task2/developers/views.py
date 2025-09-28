from django.shortcuts import render
from django.http import Http404
developers_dict = {
    "tinatou": {
        'first_name': 'Tina',
        'last_name': 'Jouzdani',
        'skills': ['Python', 'Django', 'HTML']
    },
    "ali123": {
        'first_name': 'Ali',
        'last_name': 'Rezaei',
        'skills': ['Python', 'Django', 'JavaScript']
    },
    "sara456": {
        'first_name': 'Sara',
        'last_name': 'Ahmadi',
        'skills': ['Java', 'Spring', 'SQL']
    }
}


def developers_list_view(request):
    return render(request, 'developers/developers_list.html', {'developers': developers_dict})



def developer_cv_view(request, username):
    developer = developers_dict.get(username)
    if not developer:
        raise Http404("Developer not found")
    return render(request, 'developers/developers_cv.html', {'developer': developer})
