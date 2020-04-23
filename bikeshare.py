import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to ananlyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    allowed_city = ['chicago', 'new york city', 'washington']
    city = input('Input city that you wantt to explore(chicago, new york city, washington):')
    while city not in allowed_city:
        print('Wrong city name, please try again!')
        city = input('Input city you want to explore(chicago, new york city, washington):')
           
      
    # TO DO: get user input for month (all, january, february, ... , june)
    month = input('Input month name you want to explore ( all, january, february, ..., june):')
    

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday
    day = input('Input day of week you want to explore(all, monday, tuesday, ... sunday:')

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
    df = pd.read_csv(CITY_DATA[city])
  
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour
    
    if city == 'washington':
        NaN = np.nan
        df['Gender'] = NaN
        df['Birth Year'] = NaN
    
    if month != 'all':
        months = ['janurary', 'februrary', 'march', 'april', 'may', 'june']
        month = months.index(month) +1
        df = df[df['month'] == month]
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]
    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""
    import datetime as dt
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
   
                   
    # TO DO: display the most common month
    popular_month = df['month'].mode()[0]
    print('Most popular month:', popular_month)
     

    popular_day = df['day_of_week'].mode()[0]
    print('Most popular day:', popular_day) 
    

    # TO DO: display the most common start hour
    popular_hour = df['hour'].mode()[0]
    print('Most popular start hour:', popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start = df['Start Station'].mode()[0]
    print('Most popular start station:', popular_start)

    # TO DO: display most commonly used end station
    popular_end = df['End Station'].mode()[0]
    print('Most popular end station:', popular_end)

    # TO DO: display most frequent combination of start station and end station trip
    df['combination trip'] = df['Start Station'] + ':' + df['End Station']
    station_combination = df['combination trip'].mode()[0]
    print('Most popular combination station:', station_combination)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    
    total_time = df['Trip Duration'].sum()
    print('Total trip duration in seconds:', total_time)
    # TO DO: display mean travel time
    avg_time = df['Trip Duration'].mean()
    print('Average trip duration in seconds:', avg_time)

    print("\nThis took %syues seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_type_count = df.groupby('User Type')['User Type'].count()
    for (name, value) in zip(user_type_count.index, user_type_count.values):
        print("%-20s %20d" % (name, value))
    #print('User type count:\n', user_type_count)
    # TO DO: Display counts of gender
    
    if df['Gender'].count() == 0:
          print('No gender data')
    else:
        gender_count = df.groupby('Gender')['Gender'].count()
        print('\n Gender count:', gender_count)

    # TO DO: Display earliest, most recent, and most common year of birth
    
    if df['Birth Year'].count() == 0:
        print('No Birth Year Data')
    else:
        earliest_birth = df['Birth Year'].min()
        recent_birth = df['Birth Year'].max()
        most_common_year = df['Birth Year'].mode()[0]
        print('Earliest birth year: %s  most recent birth year: %s most common year of birth year: %s' % (earliest_birth, recent_birth, most_common_year))
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
