from flask import Flask
from flask_restful import Api,Resource
from flask_restful import fields, marshal
from flask_restful import reqparse

app = Flask(__name__)
api = Api(app)

parking_spot = []

vehicle = {'title': fields.String}


class ParkListAPI(Resource):

    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('title', type=str, required=True,
                                   help='No vehicle title provided', location='json')
        super(ParkListAPI, self).__init__()

    def get (self):
        parking = 100
        if len(parking_spot) == 0:
            return {"Available parking": parking}
        else:
            length = len(parking_spot)
            count = 0

            while count < length:

                if parking_spot[count] == "Car":
                    parking = parking - 1

                elif parking_spot[count] == "Motorbike":
                    parking = parking - 0.2

                elif parking_spot[count] == "Bus":
                    parking = parking - 3

                else:
                    parking = parking -5

                count += 1

            return {"Available parking": parking}

    def post(self):
        value = 100
        args = self.reqparse.parse_args()
        vehicle = args['title']
        parking = 100
        if not vehicle.replace(" ", ""):
            return {"message": "not vehicle added"}
        if len(parking_spot) == 0:
            parking_spot.append(vehicle)
            print(parking_spot)
            return {"message": "vehicle Succesfully parked"}

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
                    return {"message": "vehicle Succesfully parked"}
                elif vehicle == 'bus' and (parking - 3) >= 0:
                    parking_spot.append(vehicle)
                    return {"message": "vehicle Succesfully parked"}
                elif vehicle == 'motorbike' and (parking - 0.2) >= 0:
                    parking_spot.append(vehicle)
                    return {"message": "vehicle Succesfully parked"}
                elif vehicle == 'trailer' and (parking - 5) >= 0:
                    parking_spot.append(vehicle)
                    return {"message": "vehicle Succesfully parked"}
                else:
                    return {"message": "no available space for parking"}


class ParkAPI(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('title', type=str, required=True,
                                   help='No vehicle title provided', location='json')
        super(ParkAPI, self).__init__()

    def get(self, vehicle):
        parking = 100
        value = 100
        if len(parking_spot) == 0:
            parking = parking - value
            return {"Next parking space": parking}
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
                return {"next parking": parking + 1}
            else:
                return {"next parking":"The is no any slots in parking"}

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
            while count < length:

                if vehicle == "car":
                    print(parking_spot)
                    parking = parking + 1
                    return {"parking spot remaining": parking_spot}

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

api.add_resource(ParkListAPI, '/api/all', endpoint='tasks')

api.add_resource(ParkAPI, '/api/<string:vehicle>', endpoint='task')