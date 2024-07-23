from flask import Flask, jsonify, request, render_template
from flask_cors import CORS 
import mysql.connector

app = Flask(__name__)
CORS(app, origins=['http://localhost:3000'])

# create a MySQL database connection
conn = mysql.connector.connect(
  host="localhost",
  user="root",
  password="password",
  database="flight_management"
)


@app.route('/', methods=['GET'])
def index():
  return render_template('index.html')

@app.route('/add_airplane', methods=['GET','POST'])
def add_airplane():
  if ( request.method == 'GET' ):
    return render_template('add_airplane.html')

  data = request.form.to_dict()
  print("hello")
  for key in data:
    if data[key] == "":
      data[key] = None

  print(data)

  cursor = conn.cursor()
  cursor.callproc('add_airplane', [data['airline_id'], data['tail_num'], data['seat_capacity'], data['speed'], data['location_id'], data['plane_type'], data['skids'], data['propellers'], data['jet_engines']])
  # print("yes!")
  conn.commit()

  cursor.close()

  return "Airplane Added"

@app.route('/add_airport', methods=['GET','POST'])
def add_airport():
  if ( request.method == 'GET' ):
    return render_template('add_airport.html')

  data = request.form.to_dict()
  print("hello")
  for key in data:
    if data[key] == "":
      data[key] = None

  print(data)

  cursor = conn.cursor()
  cursor.callproc('add_airport', [data['airport_id'], data['airport_name'], data['city'], data['state'], data['location_id']])
  # print("yes!")
  conn.commit()

  cursor.close()

  return "Airport Added"


# define a route to handle POST requests
@app.route('/add_person', methods=['GET','POST'])
def add_person():
  if ( request.method == 'GET' ):
    return render_template('add_person.html')

  data = request.form.to_dict()

  for key in data:
    if data[key] == "":
      data[key] = None
  
  cursor = conn.cursor()
  cursor.callproc('add_person', [data['person_id'], data['first_name'], data['last_name'], data['location_id'], data['tax_id'], data['experience'], data['flying_airline'], data['flying_tail'], data['flying_miles']])

  conn.commit()

  cursor.close()

  return "Person Added"

@app.route('/grant_pilot_license', methods=['GET','POST'])
def grant_pilot_license():
  if ( request.method == 'GET' ):
    return render_template('grant_pilot_license.html')

  data = request.form.to_dict()

  for key in data:
    if data[key] == "":
      data[key] = None

  print(data)
  
  cursor = conn.cursor()
  cursor.callproc('grant_pilot_license', [data['person_id'], data['ip_license']])

  conn.commit()

  cursor.close()

  return "License Granted"

@app.route('/offer_flight', methods=['GET','POST'])
def offer_flight():
  if ( request.method == 'GET' ):
    return render_template('offer_flight.html')

  data = request.form.to_dict()

  for key in data:
    if data[key] == "":
      data[key] = None
  
  cursor = conn.cursor()
  cursor.callproc('offer_flight', [data[key] for key in data])

  conn.commit()

  cursor.close()

  return "Flight Offered"

@app.route('/purchase_ticket_and_seat', methods=['GET','POST'])
def purchase_ticket_and_seat():
  if ( request.method == 'GET' ):
    return render_template('purchase_ticket_and_seat.html')

  data = request.form.to_dict()

  for key in data:
    if data[key] == "":
      data[key] = None
  
  cursor = conn.cursor()
  cursor.callproc('purchase_ticket_and_seat', [data[key] for key in data])

  conn.commit()


  return "Ticket Purchased"

@app.route('/add_update_leg', methods=['GET','POST'])
def add_update_leg():
  if ( request.method == 'GET' ):
    return render_template('add_update_leg.html')

  data = request.form.to_dict()

  for key in data:
    if data[key] == "":
      data[key] = None
  
  cursor = conn.cursor()
  cursor.callproc('add_update_leg', [data[key] for key in data])

  conn.commit()

  cursor.close()

  return "Leg Updated"

@app.route('/start_route', methods=['GET','POST'])
def start_route():
  if ( request.method == 'GET' ):
    return render_template('start_route.html')

  data = request.form.to_dict()

  for key in data:
    if data[key] == "":
      data[key] = None
  
  cursor = conn.cursor()
  cursor.callproc('start_route', [data[key] for key in data])

  conn.commit()

  cursor.close()

  return "Route Started"

@app.route('/extend_route', methods=['GET','POST'])
def extend_route():
  if ( request.method == 'GET' ):
    return render_template('extend_route.html')

  data = request.form.to_dict()

  for key in data:
    if data[key] == "":
      data[key] = None
  
  cursor = conn.cursor()
  cursor.callproc('extend_route', [data[key] for key in data])

  conn.commit()

  cursor.close()

  return "Route Extended"

@app.route('/flight_landing', methods=['GET','POST'])
def flight_landing():
  if ( request.method == 'GET' ):
    return render_template('flight_id.html')

  data = request.form.to_dict()

  for key in data:
    if data[key] == "":
      data[key] = None
  
  cursor = conn.cursor()
  cursor.callproc('flight_landing', [data[key] for key in data])

  conn.commit()

  cursor.close()

  return "Flight Landed"

@app.route('/flight_takeoff', methods=['GET','POST'])
def flight_takeoff():
  if ( request.method == 'GET' ):
    return render_template('flight_id.html')

  data = request.form.to_dict()

  for key in data:
    if data[key] == "":
      data[key] = None
  print(data)
  cursor = conn.cursor()
  cursor.callproc('flight_takeoff', [data[key] for key in data])

  conn.commit()

  cursor.close()

  return "Flight Taken Off"

@app.route('/passengers_board', methods=['GET','POST'])
def passengers_board():
  if ( request.method == 'GET' ):
    return render_template('flight_id.html')

  data = request.form.to_dict()

  for key in data:
    if data[key] == "":
      data[key] = None
  print(data)
  cursor = conn.cursor()
  cursor.callproc('passengers_board', [data[key] for key in data])

  conn.commit()

  cursor.close()

  return "Passengers Boarded"

@app.route('/passengers_disembark', methods=['GET','POST'])
def passengers_disembark():
  if ( request.method == 'GET' ):
    return render_template('flight_id.html')

  data = request.form.to_dict()

  for key in data:
    if data[key] == "":
      data[key] = None
  print(data)
  cursor = conn.cursor()
  cursor.callproc('passengers_disembark', [data[key] for key in data])

  conn.commit()

  cursor.close()

  return "Passengers Disembarked"

@app.route('/assign_pilot', methods=['GET','POST'])
def assign_pilot():
  if ( request.method == 'GET' ):
    return render_template('assign_pilot.html')

  data = request.form.to_dict()

  for key in data:
    if data[key] == "":
      data[key] = None
  print(data)
  cursor = conn.cursor()
  cursor.callproc('assign_pilot', [data[key] for key in data])

  conn.commit()

  cursor.close()

  return "Pilot Assigned"

@app.route('/recycle_crew', methods=['GET','POST'])
def recycle_crew():
  if ( request.method == 'GET' ):
    return render_template('flight_id.html')

  data = request.form.to_dict()

  for key in data:
    if data[key] == "":
      data[key] = None
  print(data)
  cursor = conn.cursor()
  cursor.callproc('recycle_crew', [data[key] for key in data])

  conn.commit()

  cursor.close()

  return "Crew Recycled"

@app.route('/retire_flight', methods=['GET','POST'])
def retire_flight():
  if ( request.method == 'GET' ):
    return render_template('flight_id.html')

  data = request.form.to_dict()

  for key in data:
    if data[key] == "":
      data[key] = None
  print(data)
  cursor = conn.cursor()
  cursor.callproc('retire_flight', [data[key] for key in data])

  conn.commit()

  cursor.close()

  return "Flight Retired"

@app.route('/remove_passenger_role', methods=['GET','POST'])
def remove_passenger_role():
  if ( request.method == 'GET' ):
    return render_template('remove_people_role.html')

  data = request.form.to_dict()

  for key in data:
    if data[key] == "":
      data[key] = None
  print(data)
  cursor = conn.cursor()
  cursor.callproc('remove_passenger_role', [data[key] for key in data])

  conn.commit()

  cursor.close()

  return "Passenger Role Removed"

@app.route('/remove_pilot_role', methods=['GET','POST'])
def remove_pilot_role():
  if ( request.method == 'GET' ):
    return render_template('remove_people_role.html')
  print("submitting")
  data = request.form.to_dict()

  for key in data:
    if data[key] == "":
      data[key] = None
  print(data)
  cursor = conn.cursor()
  cursor.callproc('remove_pilot_role', [data[key] for key in data])

  conn.commit()

  cursor.close()

  return "Pilot Role Removed"

@app.route('/simulation_cycle', methods=['GET','POST'])
def simulation_cycle():
  if ( request.method == 'GET' ):
    return render_template('simulation_cycle.html')
  
  cursor = conn.cursor()
  cursor.callproc('simulation_cycle')

  conn.commit()

  cursor.close()

  return "Simulation Ran"

@app.route('/flights_in_the_air', methods=['GET'])
def flights_in_the_air():
  cursor = conn.cursor()
  cursor.execute('SELECT * FROM flights_in_the_air')
  table = cursor.fetchall()
  return render_template('flights_in_the_air.html', table=table)

@app.route('/flights_on_the_ground', methods=['GET'])
def flights_on_the_ground():
  cursor = conn.cursor()
  cursor.execute('SELECT * FROM flights_on_the_ground')
  table = cursor.fetchall()
  return render_template('flights_on_the_ground.html', table=table)

@app.route('/people_in_the_air', methods=['GET'])
def people_in_the_air():
  cursor = conn.cursor()
  cursor.execute('SELECT * FROM people_in_the_air')
  table = cursor.fetchall()
  return render_template('people_in_the_air.html', table=table)

@app.route('/people_on_the_ground', methods=['GET'])
def people_on_the_ground():
  cursor = conn.cursor()
  cursor.execute('SELECT * FROM people_on_the_ground')
  table = cursor.fetchall()
  return render_template('people_on_the_ground.html', table=table)

@app.route('/route_summary', methods=['GET'])
def route_summary():
  cursor = conn.cursor()
  cursor.execute('SELECT * FROM route_summary')
  table = cursor.fetchall()
  return render_template('route_summary.html', table=table)

@app.route('/alternative_airports', methods=['GET'])
def alternative_airports():
  cursor = conn.cursor()
  cursor.execute('SELECT * FROM alternative_airports')
  table = cursor.fetchall()
  return render_template('alternative_airports.html', table=table)

if __name__ == '__main__':
  app.run(port=5000)
