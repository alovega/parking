from flask import Flask
from flask_restful import Api, Resource, abort
from flask_restful import fields
from flask_restful import reqparse

app = Flask(__name__)
api = Api(app)

parking_spot = []

vehicle = {'title': fields.String}


class ParkListAPI(Resource):
    #a constructor for the class
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('title', type=str, required=True,
                                   help='No vehicle title provided', location='json')
        super(ParkListAPI, self).__init__()
    #<Get:all> create a get method that returns all available parking spaces
    def get (self):
        parking = 10
        if len(parking_spot) == 0:
            return {"Available parking": parking}
        else:
            length = len(parking_spot)
            count = 0

            while count < length:

                if parking_spot[count] == "car":
                    parking = parking - 1

                elif parking_spot[count] == "motorbike":
                    parking = parking - 0.2

                elif parking_spot[count] == "bus":
                    parking = parking - 3

                elif parking_spot[count] == "trailer":
                    parking = parking -5

                else:
                    return abort(404)
                print(parking)
                count += 1

            message = [{"Available parking": parking},{"vehicle in park": parking_spot}]
            return {"message": message}
    #<POST> method for posting or parking a vehicle
    def post(self):
        value = 100
        args = self.reqparse.parse_args()
        vehicle = args['title']
        parking = 10
        if not vehicle.replace(" ", ""):
            return {"message": "not vehicle added"}
        if len(parking_spot) == 0:
            parking_spot.append(vehicle)
            print(parking_spot)
            message = [{"message": "vehicle Succesfully parked"},{"cars in park":parking_spot}]
            return {"message":message}

        else:
            length = len(parking_spot)
            count = 0
            while count < length:
                if parking_spot[count] == "car":
                    parking = parking - 1

                elif parking_spot[count] == "motorbike":
                    parking = parking - 0.2

                elif parking_spot[count] == "bus":
                    parking = parking - 3

                elif parking_spot[count] == "trailer" :
                    parking = parking - 5

                else:
                    return {"message": "error"}

                count += 1

            if parking < 100:
                if vehicle == 'car' and (parking - 1) >= 0:
                    parking_spot.append(vehicle)
                    message = [{"message": "vehicle Succesfully parked"}, {"cars in park": parking_spot}]
                    return {"message": message}

                elif vehicle == 'bus' and (parking - 3) >= 0:
                    parking_spot.append(vehicle)
                    message = [{"message": "vehicle Succesfully parked"}, {"cars in park": parking_spot}]
                    return {"message": message}
                elif vehicle == 'motorbike' and (parking - 0.2) >= 0:
                    parking_spot.append(vehicle)
                    message = [{"message": "vehicle Succesfully parked"}, {"cars in park": parking_spot}]
                    return {"message": message}
                elif vehicle == 'trailer' and (parking - 5) >= 0:
                    parking_spot.append(vehicle)
                    message = [{"message": "vehicle Succesfully parked"}, {"cars in park": parking_spot}]
                    return {"message": message}
                else:
                    return {"message": "no available space for parking"}


class ParkAPI(Resource):
    #a constructor for the class
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('title', type=str, required=True,
                                   help='No vehicle title provided', location='json')
        super(ParkAPI, self).__init__()

    #<GET:ID> implements a method for getting the next available parking space
    def get(self, vehicle):
        #variable parking instatiate parking space to be automatically 100
        parking = 100
        #variable  value used for obtaining the next parking space
        value = 100
        if len(parking_spot) == 0:
            parking = parking - value
            message = [{"Next parking space": parking + 1}, {"vehicles in parking": parking_spot}]
            return {"message":message}
        else:
            length = len(parking_spot)
            count = 0

            while count < length:
                if parking_spot[count] == "car":
                    parking = parking - 1

                elif parking_spot[count] == "motorbike":
                    parking = parking - 0.2

                elif parking_spot[count] == "bus":
                    parking = parking - 3

                else:
                    parking = parking - 5

                count += 1
            parking = value - parking
            if parking < 100:
                message = [{"Next parking space": parking + 1}, {"vehicles in parking": parking_spot}]
                return {"message": message}
            else:
                return {"next parking":"The is no any slots in parking"}

    #<DELETE:> endpoint for deleting items in the list
    def delete(self,vehicle):
        args = self.reqparse.parse_args()
        vehicle = args['title']
        parking = 100
        if not vehicle.replace(" ", ""):
            return {"message": "no vehicle given"}
        if len(parking_spot) == 0:
            return {"message": "the park is empty"}
        else:
            length = len(parking_spot)
            count = 0

            while count < length:
                if parking_spot[count] == "car":
                    parking = parking - 1

                elif parking_spot[count] == "motorbike":
                    parking = parking - 0.2

                elif parking_spot[count] == "bus":
                    parking = parking - 3

                else:
                    parking = parking - 5

                count += 1
            if vehicle == "car":
                print(parking_spot)
                parking = parking + 1
                return {"parking spot remaining": parking}

            elif vehicle == "motorbike":
                parking = parking + 0.2
                return {"parking spot remaining": parking}

            elif vehicle == "bus":
                parking = parking + 3
                return {"parking spot remaining": parking}
            else:
                parking = parking + 5
                return {"parking spot remaining": parking}
            return {"parking spot remaining": parking}
            count +=1

#<resource:Endpoint>
api.add_resource(ParkListAPI, '/parking_app/api/all', endpoint='tasks')
#<resource:Endpoint>
api.add_resource(ParkAPI, 'parking_app/api/<string:vehicle>', endpoint='task')