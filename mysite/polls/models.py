from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField(blank=True)

    def __str__(self):
        return self.name

# One to Many

class Book(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')
    title = models.CharField(max_length=200)
    publication_date = models.DateField()

    def __str__(self):
        return self.title


# One to One

class Profile(models.Model):
    author = models.OneToOneField(Author, on_delete=models.CASCADE,related_name='profile')
    desc = models.TextField()
    
    
# Many to Many

class Student(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} {self.id}"

class Course(models.Model):
    title = models.CharField(max_length=200)
    students = models.ManyToManyField(Student, related_name='courses')

    def __str__(self):
        return self.title