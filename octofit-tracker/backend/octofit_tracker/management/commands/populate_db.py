from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from djongo import models

class Team(models.Model):
    name = models.CharField(max_length=100, unique=True)
    class Meta:
        app_label = 'octofit_tracker'

class Activity(models.Model):
    user = models.CharField(max_length=100)
    activity_type = models.CharField(max_length=100)
    duration = models.IntegerField()
    team = models.CharField(max_length=100)
    class Meta:
        app_label = 'octofit_tracker'

class Leaderboard(models.Model):
    team = models.CharField(max_length=100)
    points = models.IntegerField()
    class Meta:
        app_label = 'octofit_tracker'

class Workout(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    suggested_for = models.CharField(max_length=100)
    class Meta:
        app_label = 'octofit_tracker'

User = get_user_model()

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Clear collections
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Teams
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')

        # Users
        users = [
            User.objects.create_user(username='superman', email='superman@dc.com', password='pass', first_name='Clark', last_name='Kent'),
            User.objects.create_user(username='batman', email='batman@dc.com', password='pass', first_name='Bruce', last_name='Wayne'),
            User.objects.create_user(username='ironman', email='ironman@marvel.com', password='pass', first_name='Tony', last_name='Stark'),
            User.objects.create_user(username='spiderman', email='spiderman@marvel.com', password='pass', first_name='Peter', last_name='Parker'),
        ]

        # Activities
        Activity.objects.create(user='superman', activity_type='Flight', duration=120, team='DC')
        Activity.objects.create(user='batman', activity_type='Martial Arts', duration=90, team='DC')
        Activity.objects.create(user='ironman', activity_type='Tech Training', duration=100, team='Marvel')
        Activity.objects.create(user='spiderman', activity_type='Wall Climbing', duration=80, team='Marvel')

        # Leaderboard
        Leaderboard.objects.create(team='Marvel', points=180)
        Leaderboard.objects.create(team='DC', points=210)

        # Workouts
        Workout.objects.create(name='Super Strength', description='Heavy lifting and endurance', suggested_for='DC')
        Workout.objects.create(name='Web Swing', description='Agility and flexibility', suggested_for='Marvel')

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))
