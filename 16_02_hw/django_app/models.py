from django.db import models

class Book(models.Model):
    author = models.ForeignKey(
        editable=True,
        blank=True,
        null=True,
        default=None,
        verbose_name='Автор',
        help_text='<small class="text-muted">ForeignKey</small><hr><br>',
        to=User,
        on_delete=models.CASCADE,
    )

    title = models.CharField(
        validators=[MinLengthValidator(0), MaxLengthValidator(300), ],
        unique=False,
        editable=True,
        blank=True,
        null=True,
        default='',
        verbose_name='Название',
        help_text='<small class="text-muted">CharField [0, 300]</small><hr><br>',
        max_length=300,
    )

    description = models.TextField(
        validators=[MinLengthValidator(0), MaxLengthValidator(3000), ],
        editable=True,
        blank=True,
        null=True,
        default="",
        verbose_name='Краткое описание',
        help_text='<small class="text-muted">TextField [0, 3000]</small><hr><br>',

        max_length=3000,
    )

    price = models.DecimalField(
        max_digits=10,
        decimal_places=0,
        verbose_name='Цена',
    )

    published = models.DateTimeField(
        editable=True,
        blank=True,
        null=True,
        default=timezone.now,
        verbose_name='Дата написания',
        help_text='<small class="text-muted">DateTimeField</small><hr><br>',
        auto_now=False,
        auto_now_add=False,
    )
    image = models.ImageField(
        upload_to='media/ads/%Y/%m/%d/',
        blank=True)

    class Meta:
        app_label = 'django_app'
        ordering = ('title')
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'
        db_table = 'django_app_post_model_table'

    def __str__(self):
        return f"{self.title}({self.id}) | {self.description[0:30]}... | {self.updated}"