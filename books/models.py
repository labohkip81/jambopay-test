from django.db import models

STOCK_STATUSES = (
    ("Good", "Good"),
    ("Bad", "Bad"),
    ("Critical", "Critical"),
    ("Out of Stock", "Out of Stock"),
)

# Create your models here.
class Author(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField()
    date_of_birth = models.DateField(auto_now=False, auto_now_add=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_date']
    
    def __str__(self):
        return self.first_name + " " + self.last_name


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_date']
        
    def __str__(self):
        return self.title


class Stock(models.Model):
    book = models.OneToOneField(Book, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    status = models.CharField(
        max_length=200, choices=STOCK_STATUSES, default="Out of Stock"
    )
    created_date = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    # Assign status on save based on number of books
    def save(self, *args, **kwargs):
        if self.quantity >= 10:
            self.status = "Good"
        elif self.quantity >= 5 and self.quantity < 10:
            self.status = "Bad"
        elif self.quantity >= 1 and self.quantity < 5:
            self.status = "Critical"
        else:
            self.status = "Out of Stock"
        super().save(*args, **kwargs)
    
    class Meta:
        ordering = ['-created_date']
        
    def __str__(self):
        return self.book.title
