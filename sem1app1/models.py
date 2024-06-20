from django.db import models


class CoinFlip(models.Model):
    FLIP_CHOICES = [
        ('T', 'решка'),
        ('H', 'орёл'),
    ]

    result = models.CharField(max_length=1, choices=FLIP_CHOICES)
    flip_time = models.DateTimeField(auto_now_add=True)

    @staticmethod
    def statistic(n):
        flips = CoinFlip.objects.order_by('-flip_time')[:n]
        stats = {'орёл': 0, 'решка': 0}
        for flip in flips:
            if flip.result == 'орёл':
                stats['орёл'] += 1
            else:
                stats['решка'] += 1
        return stats

    def __str__(self):
        return f"{self.result} flipped at {self.flip_time}"


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    bio = models.TextField()
    birthday = models.DateField()

    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    def __str__(self):
        return f'Name: {self.full_name()}, email: {self.email}'

    def __repr__(self):
        return f'Author("{self.first_name}", "{self.last_name}", "{self.email}", "{self.bio}", "{self.birthday}")'

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'


class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    date = models.DateField(auto_now_add=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    category = models.CharField(max_length=100)
    views = models.PositiveIntegerField(default=0)
    is_published = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def __str__(self):
        return f'Title is {self.title}, author: {self.author}'

    def add_view(self):
        self.views += 1


class Comment(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment = models.TextField
    publication_date = models.DateField(auto_now_add=True)
    update_date = models.DateField(auto_now_add=True)
