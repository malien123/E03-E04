from django.db import models
from django.db.models.fields.json import JSONField



class Book(models.Model):
    """All the variables used"""
    name = models.CharField(max_length=500, default = '') #making the default plank
    authors = models.JSONField('List of authors')
    year_published = models.IntegerField('year published')
    date_added = models.DateField(auto_now_add=True)
    date_modified = models.DateField(auto_now_add=True)


    def __str__(self):
        """Formating variables so that they are strings and can be outputted correctly"""
        return '{} {} {} {} {}' .format(self.authors, self.name, self.year_published, self.date_added, self.date_modified)
    




class Review(models.Model):


    my_review = models.TextField(max_length=500, default = '') # max length of 500 characters for the review
    stars = models.IntegerField('How many stars would you give this book? 0-5', max_length=1) 
    unfinished = models.BooleanField(default=False) # is the review unfinished, False or True
    date_added = models.DateField(auto_now_add=True)
    date_modified = models.DateField(auto_now_add=True)
    book = models.ForeignKey(Book, on_delete = models.CASCADE, null=True)

   
    class Meta:
        verbose_name_plural = 'reviews'


    def __str__(self):
        """Formating variables so that they are strings and can be outputted correctly"""
        return '{} {} {} {} {}' .format( f"{self.my_review[:25]}", self.stars, self.unfinished, self.date_added, self.date_modified, self.book)

    
class Entry(models.Model):
    #users can type their own books and reviews
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    review = models.ForeignKey(Review, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        #return string of the model

        return f"{self.text[:25]}" #only outputs 25 characters   
   
    