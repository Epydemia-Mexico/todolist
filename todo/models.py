from django.db import models
from django.contrib.auth.models import User

# uno a uno = OneToOne
# uno a muchos = ForeignKey
# muchos a muchos = ManyToMany


class Todo(models.Model):
    title = models.CharField(max_length=100, blank=False, null=True)
    done = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='tudus',
        blank=False,
        null=False,
    )

    def __str__(self):
        return self.title

# Todo.objects.all()  # traeria todas las tareas de todos lo usuarios
# Todo.objects.filter(user=user)  # equivalnte a user.tudus.all()
# user.tudus.all()  # traera todas las tareas del usuario.
#
# todo = Todo()
# todo.title
# todo.done
# todo.created_date
# todo.user
# todo.user.email
# user.mistareas.get()
# user.mistareas.all()
# user.mistareas.filter()
# user.mistareas.first()
# user.mistareas.last()

