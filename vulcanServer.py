from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

todos = {}
vulcan_detector_status = {}

class VulcanServer(Resource):
    def detector_id_exists(self, detector_id):
        return detector_id in vulcan_detector_status.keys()

    def get(self, detector_id):
        if self.detector_id_exists(detector_id):
            return vulcan_detector_status[detector_id]
        else:
            return {}

    # def get(self):
    #     return vulcan_detector_status

    def put(self, detector_id):
        coordinates = {}
        coordinates['longitude'] = request.form['longitude']
        coordinates['latitude'] = request.form['latitude']
        vulcan_detector_status[detector_id] = coordinates
        return {detector_id: vulcan_detector_status[detector_id]}


class TodoSimple(Resource):
    def get(self, todo_id):
        return {todo_id: todos[todo_id]}

    def put(self, todo_id):
        todos[todo_id] = request.form['data']
        return {todo_id: todos[todo_id]}

api.add_resource(TodoSimple, '/example/<string:todo_id>')
api.add_resource(VulcanServer, '/<string:detector_id>')

if __name__ == '__main__':
    # app.run(debug=True)
    app.run()
