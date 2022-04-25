from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from .models import Post


@receiver(post_save, sender=Post)
def notify_category_update(sender: Post, instance: Post, created: bool,
                           **kwargs) -> None:
    if not created:
        return
    users = {}
    categories = instance.category.objects.all()
    for category in categories:
        for user in category.subscribers.all():
            if user not in users:
                users[user] = set()
            users[user].add(category.name)

    print('sending mail', users, categories, kwargs, sender, instance)
    for user, categories in users.items():
        _categories = ', '.join(categories)
        send_mail(subject=f'new article in {_categories}',
                  message='\n'.join((f'hello, {user.name}',
                                    f'new article in {_categories}',
                                     '',
                                     instance.description[:50].split('\n'))),
                  recipient_list=[user.email])
