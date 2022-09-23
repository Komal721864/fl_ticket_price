import pickle
import numpy as np
import json
import config as config


class ticket_price():


    def __init__(self, airline, flight_name,source_city,departure_time,stops,arrival_time,destination_city,flight_class,duration,days_left):
          self.airline = airline
          self.flight_name = flight_name
          self.source_city = source_city
          self.departure_time = departure_time
          self.stops = stops 
          self.arrival_time = arrival_time
          self.destination_city = destination_city
          self.flight_class = flight_class
          self.duration = duration
          self.days_left = days_left


    def load_model(self):
      with open(config.MODEL_FILE_PATH,'rb') as file:
        self.model = pickle.load(file)

      with open(config.COLUMN_LIST_PATH,'r') as file:
        self.columns_dict =json.load(file)
   
   
   
    def predict_price(self):
      self.load_model()

      array = np.zeros(len(self.columns_dict['columns']))


      
      array[0] = self.stops 
      array[1] = self.flight_class
      array[2] = self.duration
      array[3]= self.days_left

    
      airline_value = 'airline_' + self.airline
      airline_index = self.columns_dict['columns'].index(airline_value)
      array[airline_index] = 1

      flight_name_value = 'flight_name_' + self.flight_name
      flight_name_index = self.columns_dict['columns'].index(flight_name_value)
      array[flight_name_index] = 1

      source_city_value = 'source_city_' + self.source_city
      source_city_index = self.columns_dict['columns'].index(source_city_value)
      array[source_city_index] = 1

      departure_time_value = 'departure_time_' + self.departure_time
      departure_time_index =self.columns_dict['columns'].index(departure_time_value)
      array[departure_time_index] = 1

      arrival_time_value = 'arrival_time_' + self.arrival_time
      arrival_time_index = self.columns_dict['columns'].index(arrival_time_value)
      array[arrival_time_index] = 1

      destination_city_value = 'destination_city_' + self.destination_city
      destination_city_index = self.columns_dict['columns'].index(destination_city_value)
      array[destination_city_index] = 1
                              

      result = self.model.predict([array])

      return result[0]


if __name__ == '__main__':
  airline='SpiceJet'
  flight_name= 'SG'
  source_city='Delhi'
  departure_time='Evening'
  stops= 0
  arrival_time= 'Night'
  destination_city='Mumbai'
  flight_class=0
  duration=2.17
  days_left=1


  ticket_price_obj = ticket_price(airline,flight_name,source_city,departure_time,stops,arrival_time,destination_city,flight_class,duration,days_left)

  ticket_price_obj.predict_price()