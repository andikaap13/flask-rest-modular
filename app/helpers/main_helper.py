from flask import jsonify

def send_response(message, data, code):
    status = False

    if code in [200, 201]:
        status = True

    return jsonify({'status' : status, 'message' : message, 'data' : data}), code