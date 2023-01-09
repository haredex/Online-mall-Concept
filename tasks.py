import google.auth
from google.auth.transport.requests import AuthorizedSession
from google.oauth2.credentials import Credentials
from celery.decorators import periodic_task
from django.models import Shop

@periodic_task(run_every=crontab(hour=0, minute=0, day_of_month='1'))

def update_rating():
    credentials = Credentials.from_authorized_user_info(client_id='CLIENT_ID', client_secret='CLIENT_SECRET')

    # Set up the Google Analytics API client
    client = google.auth.transport.requests.AuthorizedSession(credentials)

    # Set the view ID for the Google Analytics view you want to access
    view_id = 'YOUR_VIEW_ID'

    # Set the date range for the data you want to retrieve
    start_date = '2020-01-01'
    end_date = '2020-12-31'

    # Query the Google Analytics API to get the number of sessions and sales for the specified view and date range
    response = client.get(f'https://analyticsreporting.googleapis.com/v4/reports:batchGet', params={
    'reportRequests': [{
        'viewId': view_id,
        'dateRanges': [{'startDate': start_date, 'endDate': end_date}],
        'metrics': [{'expression': 'ga:sessions'}, {'expression': 'ga:transactions'}]
    }]
    })

    # Parse the API response to get the number of sessions and sales
    response_json = response.json()
    sessions = response_json['reports'][0]['data']['totals'][0]['values'][0]
    sales = response_json['reports'][0]['data']['totals'][0]['values'][1]

    # Calculate the conversion rate as the number of sales divided by the number of sessions
    conversion_rate = sales / sessions

    # Set the number of points to assign for each data point
    points_per_session = 0.1
    points_per_sale = 1

    # Calculate the total score for the shop based on the conversion rate and number of sales
    total_score = conversion_rate * points_per_session + sales * points_per_sale

    # Save the total score to the database
    shop = Shop.objects.get(id=1)
    shop.rating = total_score
    shop.save()

    pass