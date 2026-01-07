from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from django.utils import timezone

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Clear existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Create Teams
        marvel = Team.objects.create(name='marvel', description='Marvel superheroes')
        dc = Team.objects.create(name='dc', description='DC superheroes')

        # Create Users
        tony = User.objects.create(email='tony@stark.com', name='Tony Stark', team=marvel.name)
        steve = User.objects.create(email='steve@rogers.com', name='Steve Rogers', team=marvel.name)
        bruce = User.objects.create(email='bruce@wayne.com', name='Bruce Wayne', team=dc.name)
        clark = User.objects.create(email='clark@kent.com', name='Clark Kent', team=dc.name)

        # Create Activities
        Activity.objects.create(user=tony, type='run', duration=30, date=timezone.now().date())
        Activity.objects.create(user=steve, type='cycle', duration=45, date=timezone.now().date())
        Activity.objects.create(user=bruce, type='swim', duration=60, date=timezone.now().date())
        Activity.objects.create(user=clark, type='yoga', duration=20, date=timezone.now().date())

        # Create Leaderboard
        Leaderboard.objects.create(user=tony, score=120)
        Leaderboard.objects.create(user=steve, score=110)
        Leaderboard.objects.create(user=bruce, score=130)
        Leaderboard.objects.create(user=clark, score=125)

        # Create Workouts
        Workout.objects.create(name='Pushups', description='Do 20 pushups', difficulty='easy')
        Workout.objects.create(name='Plank', description='Hold plank for 1 min', difficulty='medium')
        Workout.objects.create(name='Burpees', description='Do 15 burpees', difficulty='hard')

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))
