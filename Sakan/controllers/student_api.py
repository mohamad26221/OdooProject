import json

from odoo import http
from odoo.http import request


class StudentApi(http.Controller):

    @http.route("/api/student",method=["POST"],type='http',auth="none",csrf=False)
    def post_student(self):
        args = request.httprequest.data.decode()
        vals = json.loads(args)

        res = request.env['student'].sudo().create(vals)
        if res:
            return request.make_json_response({
                "message":"Student has been created successfully"
            }, status=200)
