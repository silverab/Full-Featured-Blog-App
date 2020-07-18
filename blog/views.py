from django.shortcuts import render
# from django.http import HttpResponse

posts = [
	{
		'author': 'Hassan',
		'title': 'Blog Post 1',
		'content': 'First post content',
		'date_posted': 'July 17, 2020'
	},
	{
		'author': 'Hassan',
		'title': 'Blog Post 2',
		'content': 'First post content',
		'date_posted': 'July 16, 2020'
	},
]


def home(request):
	template = 'blog/home.html'
	context = {'title': 'Home', 'posts': posts}
	return render(request, template, context)

def about(request):
	template = 'blog/about.html'
	context = {'title': 'About'}
	return render(request, template, context)
