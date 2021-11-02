# после заполнения моделей и миграций выполняем команду "py manage.py shell" для входа в shell

from newapp.models import *
#создаем пользователей
user1 = User.objects.create(username='Mike', first_name='Frank')
user2 = User.objects.create(username='Jerry', first_name='Mouse')
#создаем авторов из пользователей
Author.objects.create(authorUser=user1)
<Author: Author object (1)>
Author.objects.create(authorUser=user2)
<Author: Author object (2)>
#создаем категории
Category.objects.create(name='IT')
<Category: Category object (1)>
Category.objects.create(name='Education')
<Category: Category object (2)>
Category.objects.create(name='News')
<Category: Category object (3)>
#пишем посты от авторов
Post.objects.create(author=Author.objects.get(authorUser=User.objects.get(username='Mike')), categoryType='NW', title='smt title', text='smth text')
<Post: Post object (1)>
Post.objects.create(author=Author.objects.get(authorUser=User.objects.get(username='Mike')), categoryType='AR', title='smth title123', text='smth text123')
<Post: Post object (2)>
Post.objects.create(author=Author.objects.get(authorUser=User.objects.get(username='Jerry')), categoryType='NW', title='smth title123!!!', text='smth text123!!!')
<Post: Post object (3)>
Post.objects.create(author=Author.objects.get(authorUser=User.objects.get(username='Jerry')), categoryType='AR', title='smth title123!!!2222', text='smth text123!!!2222')
<Post: Post object (4)>
#связываем посты с категориями
p1 = Post.objects.get(pk=1)
p2 = Post.objects.get(pk=2)
p3 = Post.objects.get(pk=3)
p4 = Post.objects.get(pk=4)
c1 = Category.objects.get(name='IT')
c2 = Category.objects.get(name='Education')
c3 = Category.objects.get(name='News')
p1.postCategory.add(c1)
p2.postCategory.add(c3)
p3.postCategory.add(c1, c2)
p4.postCategory.add(c1, c3)
#пишем комменты
Comment.objects.create(commentUser=User.objects.get(username='Mike'), commentPost=Post.objects.get(pk=1), text='comment text1')
<Comment: Mike>
Comment.objects.create(commentUser=User.objects.get(username='Jerry'), commentPost=Post.objects.get(pk=2), text='comment text2')
<Comment: Mike>
Comment.objects.create(commentUser=User.objects.get(username='Jerry'), commentPost=Post.objects.get(pk=3), text='comment text3')
<Comment: Jerry>
Comment.objects.create(commentUser=User.objects.get(username='Mike'), commentPost=Post.objects.get(pk=4), text='comment text4')
<Comment: Jerry>
#ставим лайки постам
Post.objects.get(pk=1).like()
Post.objects.get(pk=1).like()
Post.objects.get(pk=1).like()
Post.objects.get(pk=2).dislike()
Post.objects.get(pk=2).dislike()
Post.objects.get(pk=3).dislike()
Post.objects.get(pk=3).like()
Post.objects.get(pk=4).like()
#ставим лайки комментам
Comment.objects.get(pk=1).like()
Comment.objects.get(pk=1).like()
Comment.objects.get(pk=2).like()
Comment.objects.get(pk=2).like()
Comment.objects.get(pk=3).dislike()
Comment.objects.get(pk=3).dislike()
Comment.objects.get(pk=4).dislike()
Comment.objects.get(pk=4).dislike()
#обновляем рейтинг авторов
Author.objects.get(authorUser=User.objects.get(username='Mike')).update_rating()
Author.objects.get(authorUser=User.objects.get(username='Jerry')).update_rating()
#выводим их рейтинг
a = Author.objects.get(authorUser=User.objects.get(username='Mike'))
b = Author.objects.get(authorUser=User.objects.get(username='Jerry'))
a.ratingAuthor
3
b.ratingAuthor
0
#рейтинг лучшего автора
best = Author.objects.all().order_by('-ratingAuthor').values('authorUser', 'ratingAuthor')[0]
print(best)
{'authorUser': 1, 'ratingAuthor': 3}
#рейтинг лучшего поста
best_post = Post.objects.all().order_by('-rating')[0]
print(best_post)
Post object (1)
best_comment = Comment.objects.all().order_by('-rating').values('created', 'id_user', 'rating', 'text')[0]



