from django.db import models

class RationCard(models.Model):
    holder_name = models.CharField(max_length=100)
    card_number = models.CharField(max_length=20, unique=True)
    card_type = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.holder_name} ({self.card_number})"

class RationCenter(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()
    contact_number = models.CharField(max_length=15)

class RationDistribution(models.Model):
    ration_card = models.ForeignKey(RationCard, on_delete=models.CASCADE) 
    center = models.ForeignKey(RationCenter, on_delete=models.CASCADE)
    distributed_items = models.TextField()
    distribution_date = models.DateField()

class Member(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    mobile_no = models.CharField(max_length=15)
    address = models.TextField()  # ✅ Ensure this exists
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

