import requests
import json

# Set up BambooHR API request parameters
bamboo_api_key = 'de4d18c8c1122bbd68c7d6c0004eaf838288bdfc'
bamboo_subdomain = 'hostvisioncloudservices'

# Set up API endpoint and API key
endpoint = f'https://api.bamboohr.com/api/gateway.php/{bamboo_subdomain}/v1/'

# Set up query parameters to retrieve data for new employees added since a certain date
# Replace "YYYY-MM-DD" with actual date
since = '2023-01-01'

# Set up Jira Service Desk API request parameters
jira_api_token = 'ATATT3xFfGF0BUHhlxvkGxsUaS9DUhi6YJFovNL2jzgQnPisAnJh3QO_T0oi5Q9CT65cnULE_RGLil6Gm42L4icgHqOEvUX1JbheAMo0zigdkh5Knbn9YnyJoQPu6kec7YhDcvtab1hpPO7QhV7qW_ZvYkGApXuoKqwSyuOh2jsuJNxaZ7NqEMc=10181ACB'
jira_url = 'https://hostvisionng.atlassian.net/rest/api/3'
params = {'projectKey': 'EX', 'requestTypeId': 11}
headers = {'Accept': 'application/json', 'Content-Type': 'application/json', 'Authorization': 'Basic ZGU0ZDE4YzhjMTEyMmJiZDY4YzdkNmMwMDA0ZWFmODM4Mjg4YmRmYzpBZGVvbHUyOCQ='}

#query_params = {'since': '2021-01-01', type: 'inserted'}

# Make API request to retrieve data for all new employees

def fetch_all_new_employees():
    url = endpoint + f'employees/changed?since={since}T00%3A00%3A00-07%3A00&type=inserted'
    response = requests.get(url, headers=headers)
    data = response.json()

employees = json.loads(response.content)['employees']

def fetch_new_employees_data:

for key, value in employees.items():
    employee_id = key
    employee_details_url = endpoint + f"employees/{employee_id}/?fields=firstName%2ClastName%2CjobTitle%2CbestEmail%2ChireDate%2CjobTitle%2Csupervisor%2CterminationDate%2Cstatus%2Clocation%2Cdepartment&onlyCurrent=true"

    # Fetch Employee Details
    employee_details_response = requests.get(employee_details_url, headers=headers)
    print(f'url is: {employee_details_url}')
    
    employee_details_data = employee_details_response.json()
    print(employee_details_data)

#Loop through employee data and create Jira Service Desk customer requests
def create_jira_onboarding_request():

    for key, value in employees.items():
    
    # # Construct Jira Service Desk API request payload
    # payload = {
    #     'serviceDeskId': 2,
    #     'requestTypeId': params['requestTypeId'],
    #     'requestFieldValues': {'summary': f'New Employee: {employee["firstName"]} {employee["lastName"]}',
    #         'description': f'Job Title: {employee["jobTitle"]}\nEmail: {employee["email"]}'
    #     },
    #     'requestParticipants': [{'id': 'your_jira_customer_id'}] # ID of the Jira Service Desk customer who should be added to the request
    # }

# Parse response and extract relevant data for each new employee
# data = response.json()
# new_employee_data = []
# for employee_data in data:
#     new_employee_data.append({
#         'id': employee_data['id'],
#         'name': employee_data['displayName'],
#         'department': employee_data['department'],
#         'jobTitle': employee_data['department'],
#         'bestEmail': employee_data['department'],
#         'hireDate': employee_data['department'],
#         'supervisor': employee_data['department'],
#         'status': employee_data['department'],
#         'location': employee_data['department'],
#         # add more fields as needed
#     })

# # Store data in a database, file, or data structure as needed
# # e.g., write data to a file
# with open('new_employees_data.json', 'w') as fp:
#     json.dump(data, fp, indent=4, sort_keys=True)
#     #fp.write(json.dump(result, indent=4, sort_keys=True))


