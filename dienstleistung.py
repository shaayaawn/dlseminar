
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st
from datetime import datetime, timedelta


def generate_location_data():
    locations = {
        'A': (2, 3), 'B': (5, 4), 'C': (7, 2), 'D': (3, 7),
        'E': (6, 6), 'F': (8, 5), 'G': (1, 2), 'H': (4, 9),
        'I': (9, 1), 'J': (7, 8),
    }
    return locations


def calculate_distance(point1, point2):
    return np.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)


def create_distance_matrix(locations):
    distance_df = pd.DataFrame(index=locations.keys(), columns=locations.keys())
    for loc1, coord1 in locations.items():
        for loc2, coord2 in locations.items():
            distance_df.loc[loc1, loc2] = calculate_distance(coord1, coord2)
    return distance_df.astype(float)


def plot_locations(locations):
    plt.figure(figsize=(8, 6))
    for loc, (x, y) in locations.items():
        plt.plot(x, y, 'o', label=loc)
        plt.text(x, y, loc)
    plt.title('Graphical Representation of Locations')
    plt.xlabel('X Coordinate')
    plt.ylabel('Y Coordinate')
    plt.grid(True)
    plt.legend()
    plt.show()

def generate_time_slots(start, end, interval):
    """Generates time slots from start to end with given interval in minutes."""
    start_time = datetime.strptime(start, '%H:%M')
    end_time = datetime.strptime(end, '%H:%M')
    times = []
    while start_time <= end_time:
        times.append(start_time.strftime('%H:%M'))
        start_time += timedelta(minutes=interval)
    return times

def generate_bus_timetable():
    

   
    locations = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
    bus_routes = {
        'GA': generate_time_slots('08:00', '18:00', 20),
        'AB': generate_time_slots('08:00', '18:00', 30),
        'BE': generate_time_slots('08:00', '18:00', 15),
        'JE': generate_time_slots('08:00', '18:00', 20),
        'DB': generate_time_slots('08:00', '18:00', 60),
        'HE': generate_time_slots('08:00', '18:00', 60),
        'CB': generate_time_slots('08:00', '18:00', 60),
        'FE': generate_time_slots('08:00', '18:00', 60),
        'GH': generate_time_slots('08:00', '18:00', 75),
        'GJ': generate_time_slots('08:00', '18:00', 130),
        'GI': generate_time_slots('08:00', '18:00', 100),
        'FA': generate_time_slots('08:00', '18:00', 90),
        'IJ': generate_time_slots('08:00', '18:00', 80),
        'AH': generate_time_slots('08:00', '18:00', 140),
        'CG': generate_time_slots('08:00', '18:00', 40),
        'DF': generate_time_slots('08:00', '18:00', 65),
        'HC': generate_time_slots('08:00', '18:00', 105),
    }

    
    for route in list(bus_routes.keys()):
        reverse_route = route[::-1]
        bus_routes[reverse_route] = bus_routes[route]

 
    bus_time_table_df = pd.DataFrame(index=locations, columns=locations)

    
    for loc1 in locations:
        for loc2 in locations:
            if loc1 != loc2:  # No self routes
                key = loc1 + loc2
                if key in bus_routes:
                    bus_time_table_df.loc[loc1, loc2] = [bus_routes[key]]

    return bus_time_table_df
def generate_tram_timetable():
    


    locations = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
    tram_routes = {
        'DB': generate_time_slots('08:45', '22:45', 60),
        'BC': generate_time_slots('08:00', '18:00', 65),
        'CI': generate_time_slots('06:00', '23:00', 45),
        'FI': generate_time_slots('08:00', '18:00', 100),
        'FE': generate_time_slots('08:15', '18:00', 30),
        'HE': generate_time_slots('08:35', '18:00', 25),
        'ID': generate_time_slots('06:00', '23:00', 130),
        'IH': generate_time_slots('08:00', '18:00', 140),
        'CH': generate_time_slots('08:15', '18:00', 80),
        'FD': generate_time_slots('08:35', '18:00', 75),
    }

    
    for route in list(tram_routes.keys()):
        reverse_route = route[::-1]
        tram_routes[reverse_route] = tram_routes[route]

   
    tram_time_table_df = pd.DataFrame(index=locations, columns=locations)

   
    for loc1 in locations:
        for loc2 in locations:
            if loc1 != loc2:  # No self routes
                key = loc1 + loc2
                if key in tram_routes:
                    tram_time_table_df.loc[loc1, loc2] = [tram_routes[key]]

    return tram_time_table_df


def calculate_min_max_intervals(origin,destination):
    
    
    
    
    return None







if __name__ == "__main__":
   
    locations = generate_location_data()
    distance_matrix = create_distance_matrix(locations)
    locs = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
    preferences = ["Nachhaltig", "schnellste", "günstigste", "am wenigsten umsteigen"]

    
    origin = st.selectbox("Choose your origin:", locs)
    destination = st.selectbox("Choose your destination:", locs)
    departure_time = st.time_input("Choose your departure time:")
    preference = st.selectbox("Select your preference:", preferences)
    
    st.header("Locations Distance Dataframe")
    st.write(distance_matrix)
    
    
    st.header("Locations on the Map")
    st.pyplot(plot_locations(locations))
    st.set_option('deprecation.showPyplotGlobalUse', False)
    st.header("Bus TimeTable")
    st.write(generate_bus_timetable())
    st.header("Tram TimeTable")
    st.write(generate_tram_timetable())
    
    
    
    
    
    