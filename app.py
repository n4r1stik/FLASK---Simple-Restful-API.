from flask import Flask, request
from flask_restful import Resource, Api
from flask_cors import CORS


app = Flask(__name__)

api = Api(app)

CORS(app)

#Untuk di isi dengan data nama/umur
identitas = {}

class ControlResource(Resource):

    def get(self):
        return identitas

    def post(self):
        nama = request.form['nama']
        umur = request.form['umur']
        identitas['nama'] = nama
        identitas['umur'] = umur
        response = f'Data berhasil dimasukan'
        return response


api.add_resource(ControlResource,"/api", methods=['GET','POST'])

if __name__ == '__main__':
    app.run(debug=True, port=5050)