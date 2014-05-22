#Import Flask and request (request let's us identify the HTTP verbs.
from flask import Flask, request, jsonify
#Import the SQL alchemy class
from flask.ext.sqlalchemy import SQLAlchemy

#app variable is assigned to a flask instance
app = Flask(__name__)
#db variable references a SQLAlchemy instance containing the flask app instance
db = SQLAlchemy(app)
#Connect to the DB we created containing our data.
#Enter your database login details where 'user' and 'pass' are.
#Change your db name after 'mysql://user:pass@localhost/
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://user:pass@localhost/mikesmotorshops'


#Now we relate the database table to a model that we create.
#This will interface to query the motorshops table.
class Motorshop(db.Model):
  __tablename__ = 'motorshops'
  store_number = db.Column(db.Integer, primary_key = True)
  number_of_employees = db.Column(db.Integer)
  location = db.Column(db.String(100))
  speciality = db.Column(db.String(10))
  average_turnaround = db.Column(db.String(20))
  description = db.Column(db.Text)
  lat = db.Column(db.Float(6))
  lng = db.Column(db.Float(6))

#Now let's set up the URLs for our interface.
#Let's support /motorshops/ and /motorshops/<id>
#This is the GET URL for /motorshops/
@app.route('/motorshops/', methods=['GET'])
def motorshops():
  if request.method == 'GET':
    #We enable optional arguments /motorshops/?limit=20&offset=20 
    lim = request.args.get('limit', 10)
    off = request.args.get('offset', 0)
    #We enable a search close to certain locations longitude latitude.
    #/motorshops/?location=76.43424,111.12331&radius=10&limit=2
    radius = request.args.get('radius', 10)
    location = request.args.get('location', ',')
    lat, lng = location.split(',')

    if lat and lng and radius:
      query = "SELECT id,  location, ( 3959 * acos( cos( radians( %(latitude)s ) ) * cos( radians( lat ) ) * cos( radians( lng ) - radians( %(longitude)s ) ) + sin( radians( %(latitude)s ) ) * sin( radians( lat ) ) ) ) AS distance FROM sightings HAVING distance < %(radius)s ORDER BY distance LIMIT %(limit)s" % {"latitude": lat, "longitude": lng, "radius": radius, "limit": lim}

      results = Sighting.query.from_statement(query).all()

    else:
    results = Motorshop.query.limit(lim).offset(off).all()

    json_results = []
    for result in results:
      d = {'store_number': result.store_number,
           'number_of_employees': result.number_of_employees,
           'location': result.location,
           'speciality': result.speciality,
           'average_turnaround': result.average_turnaround,
           'description': result.description,
           'lat': result.lat,
           'lng': result.lng}
      json_results.append(d)
#returns a json browser response
    return jsonify(items=json_results)

#Now this is the GET URL for /motorshops/<id>
@app.route('/motorshops/<int:motorshop_id>', methods=['GET'])
def motorshops(motorshop_id):
  if request.method == 'GET':
    result = Motorshop.query.filter_by(id=motorshop_id).first()

    json_result = {'store_number': result.store_number,
                   'number_of_employees': result.number_of_employees,
                   'location': result.location,
                   'speciality': result.speciality,
                   'average_turnaround': result.average_turnaround,
                   'description': result.description,
                   'lat': result.lat,
                   'lng': result.lng}

    return jsonify(items=json_result)




#Run app run so we use the server on our localhost
#and set debug to true to it restarts after we make changes to the code
if __name__ == '__main__':
  app.run(debug=True)
  '''
#When you want to move into production specify your information here.
  app.run( 
        host="0.0.0.0",
        port=int("80")
  )
  '''
