# Create your views here.

import datetime
from dateutil.relativedelta import relativedelta

from catalog.models import Texts
from collections import Counter
from numpy import histogram
from rest_framework.views import APIView
from rest_framework.response import Response
import pytz


class ListTexts(APIView):

    def get(self, request, format=None):
        """
        Return :
            Top 10 authors (by number of texts)
            Distribution of text creation in time (last 24 months)
        """
        # authors
        authors = [record.author for record in Texts.objects.all()]
        authors_counter = Counter(authors)
        top_authors = authors_counter.most_common(10)
        authors_output = {author: number_of_texts for author, number_of_texts in top_authors}

        # distribution
        utc = pytz.UTC
        end_date = utc.localize(datetime.datetime.now())
        start_date = end_date - relativedelta(years=2)
        bins = []
        while end_date > start_date:
            bins.append(start_date)
            start_date += relativedelta(months=1)

        dates = [record.date for record in Texts.objects.all()]
        distribution = histogram(dates, bins)
        response = {
            'Top 10 authors (by number of texts)': authors_output,
            'Distribution of text creation in time (last 24 months)': distribution[0]
        }
        return Response(response)
