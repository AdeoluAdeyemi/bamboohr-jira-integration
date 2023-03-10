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
jira_url = 'https://hostvisionng.atlassian.net/rest/servicedeskapi/request'
jira_customer_id = 'qm:d94bc636-9699-4551-9935-f8cfc8bbd23d:3be83321-de1a-4a86-9eef-87bd708a8803' # ID of the Jira Service Desk customer who should be added to the request
serviceDeskId = 2

params = {'projectKey': 'EX', 'requestTypeId': 30, 'serviceDeskId': 2}
headers = {'Accept': 'application/json', 'Content-Type': 'application/json', 'Authorization': 'Basic ZGU0ZDE4YzhjMTEyMmJiZDY4YzdkNmMwMDA0ZWFmODM4Mjg4YmRmYzpBZGVvbHUyOCQ='}

#query_params = {'since': '2021-01-01', type: 'inserted'}

# Make API request to retrieve data for all new employees

def fetch_all_new_employees(since):
    date_since_last_sync = since
    url = endpoint + f'employees/changed?since={date_since_last_sync}T00%3A00%3A00-07%3A00&type=inserted'
    response = requests.get(url, headers=headers)

    data = response.json()

    employees = json.loads(response.content)['employees']

    # Loop through employee directory for newly created employees 
    for key, value in employees.items():
        employee_id = key
        employee_details_url = endpoint + f"employees/{employee_id}/?fields=firstName%2ClastName%2CjobTitle%2CbestEmail%2ChireDate%2CjobTitle%2Csupervisor%2CterminationDate%2Cstatus%2Clocation%2Cdepartment&onlyCurrent=true"

        # Fetch Employee Details
        employee_details_response = requests.get(employee_details_url, headers=headers)

        # Parse the response to json.          
        employee_details_data = employee_details_response.json()
        
        create_jira_onboarding_request(employee_details_data)

        #return(employee_details_data)

# Loop through employee data and create Jira Service Desk customer requests
def create_jira_onboarding_request(employee_details_data):

    #for key, value in employee_details_data.items():
    # Construct Jira Service Desk API request payload
    payload = {
        'serviceDeskId': params['serviceDeskId'],
        'requestTypeId': params['requestTypeId'],
        'requestFieldValues': {'summary': f'Onboard New Employee: {employee_details_data["firstName"]} {employee_details_data["lastName"]}',
            'description': f'Job Title: {employee_details_data["jobTitle"]}\nEmail: {employee_details_data["bestEmail"]}\nDepartment: {employee_details_data["department"]}\nJob Title: {employee_details_data["jobTitle"]}\nStart Date: {employee_details_data["hireDate"]}\nManager: {employee_details_data["supervisor"]}\nLocation: {employee_details_data["location"]}'
        }
        #'requestParticipants': [{'id': jira_customer_id}] 
    }

    # Send Jira Service Desk API request to create new customer request
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json', 'Authorization': 'Basic aGVsbG9AaG9zdHZpc2lvbi5uZzpBVEFUVDN4RmZHRjBCVUhobHh2a0d4c1VhUzlEVWhpNllKRm92TkwyanpnUW5QaXNBbkpoM1FPX1Qwb2k1UTlDVDY1Y25VTEVfUkdMaWw2R200Mkw0aWNnSHFPRXZVWDFKYmhlQU1vMHppZ2RraDVLbmJuOVlueUpvUVB1NmtlYzdZaERjdnRhYjFocFBPN1FoVjdxV19adllrR0FwWHVvS3F3U3l1T2gyanN1Sk54YVo3TnFFTWM9MTAxODFBQ0I='}
    
    print(f'final jira url = {jira_url}')
    print(f'headers are:  {headers}')

    response = requests.post(f'{jira_url}', headers=headers, json=payload)
    if response.status_code == 201:
        print(f'Customer request created for {employee_details_data["firstName"]} {employee_details_data["lastName"]}')
    else:
        print(f'Error creating customer request for {employee_details_data["firstName"]} {employee_details_data["lastName"]}: {response.content}')


# Call the fetch_all_new_employees method passing in a last since sync date.
get_new_employees = fetch_all_new_employees('2023-01-01')
