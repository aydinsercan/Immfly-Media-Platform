import csv
from django.core.management import BaseCommand
from core.management.utils.channel_rate import ratingAlgorithm
from core.models import Channel


class Command(BaseCommand):
    help = 'Generate CSV containing all Channel Ratings'

    def add_arguments(self, parser):
        pass

    def handle(self, *args: str, **options: str) -> None:
        channels = Channel.objects.all()
        ratingDict = ratingAlgorithm(channels)
        header = ["Channel Title", "Average Rating"]

        with open('RatingOfChannels.csv', 'w', encoding='utf8', newline='') as channels_csv:
            writer = csv.writer(channels_csv)
            writer.writerow(header)
            for title, averageRating in ratingDict.items():
                self.stdout.write(title+': '+str(averageRating))
                writer.writerow([title, averageRating])