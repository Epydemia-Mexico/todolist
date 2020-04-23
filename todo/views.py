from django.shortcuts import render, redirect
from .forms import TodoForm
from django.views import View


class TodoCreateView(View):
    template_name = 'todo-create.html'

    def get(self, request):
        if request.user.is_authenticated:
            form = TodoForm(initial={'user': request.user})
            return render(request, self.template_name, dict(form=form))
        else:
            return redirect('user-login')
