from django.db import models


class Employee(models.Model):
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    middle_name = models.CharField(max_length=255)
    birthdate = models.DateField()
    photo = models.ImageField()
    phone_number = models.CharField(max_length=255)
    email = models.EmailField()
    address = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Education(models.Model):
    education = models.CharField('Образование', max_length=255)
    institution = models.CharField('Учебное заведение', max_length=255)
    city = models.CharField('Город', max_length=255)
    starting_date = models.DateField('Дата начало')
    ending_date = models.DateField('Дата окончания')
    description = models.TextField(blank=True, null=True)
    employee_id = models.ForeignKey(Employee, on_delete=models.CASCADE)


class Jobs(models.Model):
    position = models.CharField('Должность', max_length=255)
    company = models.CharField('Работодатель', max_length=255)
    starting_date = models.DateField()
    ending_date = models.DateField()
    description = models.TextField(blank=True, null=True)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)


class Skills(models.Model):
    name = models.CharField('Навык', max_length=255)
    BEGINNER = 'E'
    MODERATE = 'D'
    GOOD = 'C'
    VERYGOOD = 'B'
    EXCELLENT = 'A'
    DEGREE_CHOICES = [
        (BEGINNER, 'Beginner'),
        (MODERATE, 'Moderate'),
        (GOOD, 'Good'),
        (VERYGOOD, 'Very good'),
        (EXCELLENT, 'Excellent'),
    ]
    level = models.CharField(
        max_length=1,
        choices=DEGREE_CHOICES,
        default=BEGINNER,
    )
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)


class Languages(models.Model):
    name = models.CharField('Язык', max_length=255)
    BEGINNER = 'A0'
    ELEMENTARY = 'A1'
    PRE_INTERMEDIATE = 'A2'
    INTERMEDIATE = 'B1'
    UPPER_INTERMEDIATE = 'B2'
    ADVANCED = 'C1'
    PROFICIENT = 'C2'
    DEGREE_CHOICES = [
        (BEGINNER, 'Beginner'),
        (ELEMENTARY, 'Elementary'),
        (PRE_INTERMEDIATE, 'Pre Intermediate'),
        (INTERMEDIATE, 'Intermediate'),
        (UPPER_INTERMEDIATE, 'Upper intermediate'),
        (ADVANCED, 'Advanced'),
        (PROFICIENT, 'Proficient'),
    ]
    level = models.CharField(
        max_length=2,
        choices=DEGREE_CHOICES,
        default=BEGINNER,
    )
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)

