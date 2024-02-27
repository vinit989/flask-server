from flask import Flask, make_response

app = Flask(__name__)

@app.route('/api')
def home():
    filename = 'hacky.yaml'
    response = make_response(open(filename).read())
    response.headers["Content-Disposition"] = "attachment; filename={}".format(filename)
    return response

# This function is required for Vercel serverless function
def handler(request, context):
    from werkzeug.wrappers import Request, Response
    with app.request_context(request):
        response = app.full_dispatch_request()
    return Response(response.data, status=response.status_code, headers=dict(response.headers))

# This block allows running Flask app locally
if __name__ == '__main__':
    app.run(debug=True)
