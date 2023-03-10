import requests
import json

# Set up BambooHR API request parameters
bamboo_api_key = 'de4d18c8c1122bbd68c7d6c0004eaf838288bdfc'
bamboo_subdomain = 'hostvisioncloudservices'
#bamboo_url = f'https://{bamboo_subdomain}.bamboohr.com/api/gateway.php'
bamboo_url = f'https://api.bamboohr.com/api/gateway.php/hostvisioncloudservices/v1/employees/directory'
headers = {'Accept': 'application/json', 'Content-Type': 'application/json', 'Authorization': 'Basic ZGU0ZDE4YzhjMTEyMmJiZDY4YzdkNmMwMDA0ZWFmODM4Mjg4YmRmYzpBZGVvbHUyOCQ='}
#params = {'type': 'employees', 'fields': 'firstName,lastName,jobTitle,bestEmail,hireDate,jobTitle,supervisor,terminationDate,status,location,department'}

# Send BambooHR API request and retrieve employee data

#response = requests.get(bamboo_url, auth=(bamboo_api_key, ''), headers=headers, params=params)

response = requests.get(bamboo_url, headers=headers)
data = response.json()

#print(response.content)

employees = json.loads(response.content)['employees']

# Set up Jira Service Desk API request parameters
jira_api_token = 'ATATT3xFfGF0BUHhlxvkGxsUaS9DUhi6YJFovNL2jzgQnPisAnJh3QO_T0oi5Q9CT65cnULE_RGLil6Gm42L4icgHqOEvUX1JbheAMo0zigdkh5Knbn9YnyJoQPu6kec7YhDcvtab1hpPO7QhV7qW_ZvYkGApXuoKqwSyuOh2jsuJNxaZ7NqEMc=10181ACB'
jira_url = 'https://hostvisionng.atlassian.net/rest/api/3'

headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
params = {'projectKey': 'EX', 'requestTypeId': 11}

# # Store data in a database, file, or data structure as needed
# # e.g., write data to a file
# with open('new_employees_details.json', 'w') as fp:
#     json.dump(data, fp, indent=4, sort_keys=True)
#     #fp.write(json.dump(result, indent=4, sort_keys=True))

# Loop through employee data and create Jira Service Desk customer requests
for employee in employees:
    # Construct Jira Service Desk API request payload
    payload = {
        'serviceDeskId': 2,
        'requestTypeId': params['requestTypeId'],
        'requestFieldValues': {'summary': f'New Employee: {employee["firstName"]} {employee["lastName"]}',
            'description': f'Job Title: {employee["jobTitle"]}\nEmail: {employee["email"]}'
        },
        'requestParticipants': [{'id': 'your_jira_customer_id'}] # ID of the Jira Service Desk customer who should be added to the request
    }

    # Send Jira Service Desk API request to create new customer request
    response = requests.post(f'{jira_url}/servicedesk/{params["serviceDeskId"]}/request', auth=('', jira_api_token), headers=headers, json=payload)
    if response.status_code == 201:
        print(f'Customer request created for {employee["firstName"]} {employee["lastName"]}')
    else:
        print(f'Error creating customer request for {employee["firstName"]} {employee["lastName"]}: {response.content}')
