import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
while True:
    city= input('Please pick a city from chicago, new york city, washington: ').lower()
    if city not in CITY_DATA:
        print('please choose one of the following cities: chicago, new york, washington')
        
    else:
        break

    # TO DO: get user input for month (all, january, february, ... , june)
while True:
    month= input('please enter a month from january to june, or type "all" for all months: ').lower()
    months = ['january', 'february', 'march', 'april', 'may', 'june']
    if month != 'all' and month not in months:
        print('please enter a full valid month name')

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
while True:
    day= input('please enter a day of the week, or type "all" to display all days: ').lower.()
    days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    if day != 'all' and day not in days:
        print('please enter one day name')
    else:
        break

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
  common_month= df['month].mode()[0] 
    print('Most Common Month:', calendar.month_name[common_month]) #Get month name from number
                 
    # TO DO: display the most common day of week
   common_day= df['day_of_week'].mode()[0]
    print('Most Common Day:', common_day)

    # TO DO: display the most common start hour
   df['hour] = df['Start Time'].dt.hour
   common_hour = df['hour'].mode()[0]
   print('Most common start hour: ', common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
  common_start = df['Start Station'].mode()[0]

    # TO DO: display most commonly used end station
  common_end = df['End Station'].mode()[]
      print('Most common used End Station:', common_end)

    # TO DO: display most frequent combination of start station and end station trip
   common_start_end = (df['Start Station'] + ' - ' + df['End Station']).mode()[0]
      print('Most frequent combination of start and end Stations:', common_start_end)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_time = df['Trip Duration'].sum()
      print('Total travel time:', total_time, ' seconds, or ', total_time/3600, ' hours ')
      

    # TO DO: display mean travel time
    avg_time = df['Trip duration'].mean()
      print('Average Travel Time:', avg_time, ' seconds, or ', avg_time/3600, ' hours ')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
      print('Counts of User types:\n', df['User Type'].value_counts())
    

    # TO DO: Display counts of gender
      if 'Gender' in df:
      print('\n Counts of Gender:\n', df['Gender'].value_counts())


    # TO DO: Display earliest, most recent, and most common year of birth
      if 'Birth Year' in df:
      earliest_byear = int(df['Birth Year'].min())
      print('\n Earliest year of Birth:\n', earliest_byear)
      recent_byear = int(df['Birth Year'].max())
      print('\n Most recent year of Birth:\n', recent_byear)
      common_byear = int(df['Birth Year'].mode()[0])
      print('\n Most common year of Birth:\n', common_byear)
    


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
