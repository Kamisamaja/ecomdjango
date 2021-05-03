from django.db import models
from django.contrib.auth.models import User

# the main things models
# the product models
class categories(models.Model):
    category = models.CharField(max_length=30)
    codedyalicon = models.TextField("catagory icon class code from http://www.w3.org/2000/svg")
    slug = models.SlugField(max_length=255)
    def get_absolute_url(self):
        return '/%s/' % (self.slug)

    def __str__(self):
        return self.title

class product(models.Model):
    categories = models.ForeignKey(categories, on_delete=models.CASCADE , blank=True, null=True)
    image = models.ImageField("image of the slide",)
    image = models.ImageField("image of the slide",)
    image = models.ImageField("image of the slide",)
    slug = models.SlugField(max_length=255)
    description = models.TextField(blank=True, null=True)
    price = models.FloatField()
    newproduct = models.BooleanField("is it new should be in home page?",default=False)
    dateadded = models.DateTimeField("date added?",auto_now_add=True)
    class Meta:
        ordering = ('-dateadded',)
        def get_absolute_url(self):
            return '/%s/%s/' % (self.category.slug, self.slug)
        def __str__(self):
            return self.title
        def get_rating(self):
            total = sum(int(review['stars']) for review in self.reviews.values())

            if self.reviews.count() > 0:
                return total / self.reviews.count()
            else:
                return 0


# home page your models here.
class slide(models.Model):
    image = models.ImageField("image of the slide",)
    title = models.TextField("the main title", max_length=50)
    title2 = models.TextField("the second title", max_length=50)
    link = models.TextField("the link to the object")
