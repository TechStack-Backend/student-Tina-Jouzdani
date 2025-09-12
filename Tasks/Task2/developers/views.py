from django.shortcuts import render

developers_list = [
    {
        'first_name': 'Tina',
        'last_name': 'Jouzdani',
        'username': 'tinatuo',
        'skills': ['Python', 'Django', 'httml']
    },
    {
        'first_name': 'Ali',
        'last_name': 'Rezaei',
        'username': 'ali123',
        'skills': ['Python', 'Django', 'JavaScript']
    },
    {
        'first_name': 'Sara',
        'last_name': 'Ahmadi',
        'username': 'sara456',
        'skills': ['Java', 'Spring', 'SQL']
    },
]

def developers_list_view(request):
    return render(request, 'developers/developers_list.html', {'developers': developers_list})



def developer_cv_view(request, username):
    developer = next((dev for dev in developers_list if dev['username'] == username), None)
    if not developer:
        from django.http import Http404
        raise Http404("Developer not found")
    return render(request, 'developers/developers_cv.html', {'developer': developer})
