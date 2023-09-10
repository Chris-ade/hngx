from flask import Flask, request, Response, json
import datetime

app = Flask(__name__)

@app.route('/api', methods=['GET'])
def get_info():
    ''' This endpoint takes two GET request query parameters and return specific information in JSON format
    
    Parameters:
        slack_name (str): slack_name passed as a GET request query parameter.
        track (str): track passed as a GET request query parameter.
        
    Returns:
        JSON: A json response that includes the information passed from the GET request query with some other informations.

    Example:
        GET /api?slack_name=example_name&track=backend
    '''
    # Get query parameters from the GET request
    slack_name = request.args.get('slack_name')
    track = request.args.get('track')

    # Get the current day of the week
    current_day = datetime.datetime.utcnow().strftime('%A')

    # Get the current UTC time within a +/-2 minute window
    current_time = datetime.datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ')

    # Construct GitHub URLs
    github_file_url = "https://github.com/Chris-ade/hngx/blob/main/stage_one/app.py"
    github_repo_url = "https://github.com/chris-ade/hngx"

    # Prepare the response JSON
    response_data = {
        "slack_name": slack_name,
        "current_day": current_day,
        "utc_time": current_time,
        "track": track,
        "github_file_url": github_file_url,
        "github_repo_url": github_repo_url,
        "status_code": 200
    }
    
    # convert the dictionary to json
    json_res = json.dumps(response_data, indent=4, sort_keys=False),
    
    # Returns the json response
    return Response(json_res, content_type='application/json; charset=utf-8')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
