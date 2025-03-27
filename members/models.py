from django.db import models

class Member(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    address = models.TextField()
    joined_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name
    
class RationCard(models.Model):
    card_number = models.CharField(max_length=20, unique=True)
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    issue_date = models.DateField()
    valid_until = models.DateField()
    ration_type = models.CharField(max_length=50, choices=[
        ('APL', 'Above Poverty Line'),
        ('BPL', 'Below Poverty Line'),
        ('AAY', 'Antyodaya Anna Yojana')
    ])

    def __str__(self):
        return f"{self.card_number} - {self.member.name}"