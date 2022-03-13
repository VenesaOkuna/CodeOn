from django.test import TestCase
from . models import Projects, Profile, Rating

# Create your tests here.

# Profile model tests 
      
class ProfileTestClass(TestCase):        
    
        # Set up method
    def setUp(self):
        self.image= Profile(photo = 'img.jpg', bio ='image', email = "ness@gmail.com",phone_number = '0785429922')
        
        # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.image,Profile))     

        # Testing Save Method of Profile model
    def test_save_method(self):
        self.image.save_profile()
        images = Profile.objects.all()
        self.assertTrue(len(images) > 0)   
        
    # Testing  delete method of Profile model     
    def test_delete(self):
        self.image= Profile(photo = 'img.jpg', bio ='image')
        self.image.save_profile()
        image = Profile.objects.filter(photo = 'img.jpg').first()
        delete = Profile.objects.filter(id = image.id).delete()
        images = Profile.objects.all()
        self.assertTrue(len(images) == 0)         

    # Testing  update method of Profile model    
    def test_update(self):
        self.image.save_profile()
        image = Profile.objects.filter(photo = 'img.jpg').first()
        update = Profile.objects.filter(id = image.id).update(photo = 'cake.jpg')
        updated = Profile.objects.filter(photo = 'cake.jpg').first()
        self.assertNotEqual(image.photo, updated.photo) 

# Project model tests  
class ProjectsTestClass(TestCase):        
    
        # Set up method
    def setUp(self):
        self.pizza= Projects(title = 'pizza',image = 'img.jpg', description ='delicious',post_date = '07854222')
        
        # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.pizza,Projects))
        
        # Testing Save Method of Project model
    def test_save_method(self):
        self.pizza.save_projects()
        pizza1 = Projects.objects.all()
        self.assertTrue(len(pizza1) > 0)                    
        
    # Testing  delete method of Project model     
    def test_delete(self):
        self.pizza= Projects(title ='pizza', image = 'img.jpg')
        self.pizza.save_projects()
        pizza = Projects.objects.filter(image = 'img.jpg').first()
        delete = Projects.objects.filter(id = pizza.id).delete()
        pizza1 = Projects.objects.all()
        self.assertTrue(len(pizza1) == 0)          
        
    # Testing  update method of Project model    
    def test_update(self):
        self.pizza.save_projects()
        pizza = Projects.objects.filter(image = 'img.jpg').first()
        update = Projects.objects.filter(id = pizza.id).update(image = 'cake.jpg')
        updated = Projects.objects.filter(image = 'cake.jpg').first()
        self.assertNotEqual(pizza.image, updated.image)          

# Rating model tests
      
class RatingTestClass(TestCase):          
    
        # Set up method
    def setUp(self):
        self.review= Rating(design = '9',usability = '7', content ='8')
        
        # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.review,Rating))   
        
        # Testing Save Method of Rating model
    def test_save_method(self):
        self.review.save_rating()
        rating = Rating.objects.all()
        self.assertTrue(len(rating) > 0)         
        
    # Testing  delete method of Rating model     
    def test_delete(self):
        self.review= Rating(design = '9',usability = '7', content ='8')
        self.review.save_rating()
        review = Rating.objects.filter(design = '9').first()
        delete = Rating.objects.filter(id = review.id).delete()
        rating = Rating.objects.all()
        self.assertTrue(len(rating) == 0) 
        
    # Testing  update method of Rating model    
    def test_update(self):
        self.review.save_rating()
        review = Rating.objects.filter(design = '9').first()
        update = Rating.objects.filter(id = review.id).update(design = '5')
        updated = Rating.objects.filter(design = '5').first()
        self.assertNotEqual(review.design, updated.design)                     