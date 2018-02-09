from django.db import models

# this will include choices sections
Year_Choices = (
    ('1','1st Year'),
    ('2', '2nd Year'),
    ('3','3rd Year'),
    ('4','4th Year'),
)


Branch_Choices = (
	('CSE' , 'Computer Science And Engineering'),
	('IT' , 'Information Technology'),
	('EC' , 'Electronics Engineering'),
	('EEE' , 'Electrical And Electronics Engineering'),
	('CE','Civil Engineering'),
	('ME' , 'Mechanical Engineering'),
	('EE' , 'Electrical Engineering'),
	('IC' , 'Instrumentation and Control'),
	)
# this ends here

class names(models.Model):
	name = models.CharField(max_length=100,help_text='Enter the name of the person')
	branch = models.CharField(max_length=100,choices=Branch_Choices,help_text="Enter Person's Branch Here")
	year = models.CharField(max_length=10,choices=Year_Choices,help_text='Enter the year of study of person')
	num_posts = models.IntegerField(default=0)

	def __str__(self):
		return self.name

class posts(models.Model):
	name = models.ForeignKey(names,on_delete=models.CASCADE)
	post = models.CharField(max_length=450)
	dat = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.post