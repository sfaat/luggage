from django.db import models

# Create your models here.

class Price(models.Model):
    flying_from = models.CharField(max_length=225, null=True)
    postcode = models.CharField(max_length=50,null=True)
    no_of_bags = models.CharField(max_length=25,null=True)
    updated_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.flying_from

class Customer(models.Model):
    name = models.CharField(max_length=225)
    address = models.CharField(max_length=225)
    mobile = models.IntegerField( blank=True, null=True)
    emailid = models.EmailField(max_length=225)
    postcode = models.CharField(max_length=225)
    password = models.CharField(max_length=225)
    logo = models.ImageField(upload_to="productimg")
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Notification(models.Model):
    date = models.DateField(auto_now_add=True)
    email = models.EmailField(max_length=225)

    def __str__(self):
        return str(self.date)

# class State(models.Model):
#     state_name = models.CharField(max_length=100,null=True)
#     state_flag = models.BooleanField(default=True)
#     created_on = models.DateTimeField(auto_now_add=True)
#     update_on = models.DateTimeField(auto_now_add=True)


#     def __str__(self):
#         return self.flying_from

# class City(models.Model):
#     city_name = models.CharField(max_length=100,null=True)
#     city_flag = models.BooleanField(default=True)
#     created_on = models.DateTimeField(auto_now_add=True)
#     update_on = models.DateTimeField(auto_now_add=True)


#     def __str__(self):
#         return self.flying_from

# class Location_Map(models.Model):
#     state_id = models.ForeignKey(State, on_delete=models.CASCADE)
#     city_id = models.ForeignKey(City,on_delete=models.CASCADE)
#     pin_code_id = models.ForeignKey(City,on_delete=models.CASCADE)
#     created_on = models.DateTimeField(auto_now_add=True)
#     update_on = models.DateTimeField(auto_now_add=True)


#     def __str__(self):
#         return self.flying_from

# class Pincode(models.Model):
#     pin_code = models.IntegerField()
#     pincode_flag = models.BooleanField(default=True)
#     location_map_id = models.ForeignKey(City,on_delete=models.CASCADE)
#     created_on = models.DateTimeField(auto_now_add=True)
#     update_on = models.DateTimeField(auto_now_add=True)


#     def __str__(self):
#         return self.flying_from

# class User_From_Data(models.Model):
#     address1 = models.CharField(max_length=100)
#     location_map_id = models.ForeignKey(City,on_delete=models.CASCADE)
#     created_on = models.DateTimeField(auto_now_add=True)
#     update_on = models.DateTimeField(auto_now_add=True)


#     def __str__(self):
#         return self.flying_from




class FormField(models.Model):
    tripe_type=models.CharField(max_length=200)
    laguage_type=models.CharField(max_length=200)
    From=models.CharField(max_length=200)
    To=models.CharField(max_length=200)
    arrival=models.CharField(max_length=200,null=True,blank=True)
    Return=models.CharField(max_length=200,null=True,blank=True)
    user=models.ForeignKey(Customer,on_delete= models.CASCADE)

    def __str__(self) -> str:
        return self.tripe_type



