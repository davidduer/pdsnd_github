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
    city = input("Enter the city name you would like to see data for (Chicago, New York City, or Washington): ")
    city = city.casefold()
    while city not in CITY_DATA:
        city = input("City not listed. Enter a valid city name: ")
        city = city.casefold()

    # TO DO: get user input for month (all, january, february, ... , june)
    months = ['all', 'january', 'febrary', 'march', 'april', 'may', 'june']
    month = input("Enter the Month you would like to see data for (January to June). Type all to see data for all months: ")
    month = month.casefold()
    while month not in months:
        month = input("Month not listed. Enter a valid month or type all for all months: ")
        month = month.casefold()

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    days = ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    day = input("Enter the Day you would like to see data for. Type 'all' to see all days: ")
    day = day.casefold()
    while day not in days:
        day = input("Day not listed. Enter a valid day or type all for all days: ")
        day = day.casefold()

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
    df['day_of_week'] = df['Start Time'].dt.day_name()
    df['hour'] = df['Start Time'].dt.hour
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]

    if day != 'all':
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    most_common_month = df['month'].value_counts().idxmax()
    print("The most common month is: ", most_common_month)

    # TO DO: display the most common day of week
    most_common_day = df['day_of_week'].value_counts().idxmax()
    print("The most common day is: ", most_common_day)

    # TO DO: display the most common start hour
    most_common_hour = df['hour'].value_counts().idxmax()
    print("The most common start hour is: ", most_common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)



def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_common_start = df['Start Station'].value_counts().idxmax()
    print("The most commonly used start station is: ", most_common_start)

    # TO DO: display most commonly used end station
    most_common_end = df['End Station'].value_counts().idxmax()
    print("The most commonly used end station is: ", most_common_end)

    # TO DO: display most frequent combination of start station and end station trip
    df['Start to End'] = df['Start Station'] + " to " + df['End Station']
    print("The most commonly used combination of start station and end station is: ", df['Start to End'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)



def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('The total travel time is: ', total_travel_time, ' seconds')

    # TO DO: display mean travel time
    total_travel_average = df['Trip Duration'].mean()
    print('The average travel time is: ', total_travel_average, ' seconds')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)



def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print("\nThese are the counts of the user types:\n",user_types)

    # TO DO: Display counts of gender
    if 'Gender' in df.columns:
        gender_types = df['Gender'].value_counts()
        print("\nThese are the counts of the genders:",'\n',gender_types)

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        earlist_birth = df['Birth Year'].min()
        recent_birth = df['Birth Year'].max()
        common_birth = df['Birth Year'].value_counts().idxmax()
        print("\nThe  earlist birth is in: ", int(earlist_birth))
        print("The  most recent birth is in: ", int(recent_birth))
        print("The  most common birth is in: ", int(common_birth))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)



def raw_data(df):
    """Displays raw data upon request of the users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()
    x = 0

    raw_list = ['yes', 'no']
    raw = input("Do you want to see raw data? (yes or no) ")
    raw.casefold()
    while raw not in raw_list:
        raw = input("Invalid input. Do you want to see raw data? (yes or no) ")
        raw.casefold

    while raw == 'yes':
        print(df.iloc[x : x + 5])
        x += 5
        raw = input("Do you want to see more raw data? (yes or no) ")
        raw.casefold()
        while raw not in raw_list:
            raw = input("Invalid input. Do you want to see raw data? (yes or no) ")
            raw.casefold

    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
