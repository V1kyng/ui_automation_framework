import base64
import json
import os
import requests

# This directory is where you have all your results locally, generally named as `allure-results`
#from settings import ALLURE_SERVICE_HOST, ANDROID_RESULTS_DIR

# This url is where the Allure container is deployed. We are using localhost as example

# Project ID according to existent projects in your Allure container - Check endpoint for project creation >> `[POST]/projects`
ANDROID_ID = 'android'
IOS_ID = 'android'
#project_id = 'my-project-id'

def generate_latest_report(platform):
    """
    :param platform: ios|android
    :return: report url
    """
    if platform == 'android':
        res_dir = ANDROID_RESULTS_DIR

    elif platform == 'ios':
        res_dir = ANDROID_RESULTS_DIR
    else:
        raise Exception("Invalid platform name")
    files = os.listdir(res_dir)
    results = []
    for filename in files:
        result = {}
        file_path = os.path.join(res_dir, filename)
        if os.path.isfile(file_path):
            try:
                with open(file_path, "rb") as f:
                    content = f.read()
                    if content.strip():
                        b64_content = base64.b64encode(content)
                        result['file_name'] = filename
                        result['content_base64'] = b64_content.decode('UTF-8')
                        results.append(result)
                    else:
                        print('Empty File skipped: ' + file_path)
            finally:
                f.close()
        else:
            print('Directory skipped: ' + file_path)

    headers = {'Content-type': 'application/json'}
    request_body = {
        "results": results
    }
    json_request_body = json.dumps(request_body)

    ssl_verification = True

    print("------------------SEND-RESULTS------------------")
    response = requests.post(ALLURE_SERVICE_HOST + '/allure-docker-service/send-results?project_id=' + platform,
                             headers=headers, data=json_request_body, verify=ssl_verification)
    print("STATUS CODE:")
    print(response.status_code)
    print("RESPONSE:")
    json_response_body = json.loads(response.content)
    json_prettier_response_body = json.dumps(json_response_body, indent=4, sort_keys=True)
    print(json_prettier_response_body)
    print("------------------GENERATE-REPORT------------------")
    execution_name = 'execution from my script'
    execution_from = 'http://google.com'
    execution_type = 'teamcity'
    response = requests.get(
        ALLURE_SERVICE_HOST + '/allure-docker-service/generate-report?project_id=' + platform + '&execution_name=' +
        execution_name + '&execution_from=' + execution_from + '&execution_type=' + execution_type,
        headers=headers, verify=ssl_verification)
    print("STATUS CODE:")
    print(response.status_code)
    print("RESPONSE:")
    json_response_body = json.loads(response.content)
    json_prettier_response_body = json.dumps(json_response_body, indent=4, sort_keys=True)
    print(json_prettier_response_body)
    print('ALLURE REPORT URL:')
    print(json_response_body['data']['report_url'])

# If you want to generate reports on demand use the endpoint `GET /generate-report` and disable the Automatic Execution >> `CHECK_RESULTS_EVERY_SECONDS: NONE`
"""

"""