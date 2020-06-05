# django-user-tracker
A Django application with User and ActivityPeriod models, 
JSON format served by the API is:
```json
{
	"ok": true,
	"members": [{
			"id": "W012A3CDE",
			"real_name": "Egon Spengler",
			"tz": "America/Los_Angeles",
			"activity_periods": [{
					"start_time": "Feb 1 2020  1:33PM",
					"end_time": "Feb 1 2020 1:54PM"
				},
				{
					"start_time": "Mar 1 2020  11:11AM",
					"end_time": "Mar 1 2020 2:00PM"
				},
				{
					"start_time": "Mar 16 2020  5:33PM",
					"end_time": "Mar 16 2020 8:02PM"
				}
			]
		},
		{
			"id": "W07QCRPA4",
			"real_name": "Glinda Southgood",
			"tz": "Asia/Kolkata",
			"activity_periods": [{
					"start_time": "Feb 1 2020  1:33PM",
					"end_time": "Feb 1 2020 1:54PM"
				},
				{
					"start_time": "Mar 1 2020  11:11AM",
					"end_time": "Mar 1 2020 2:00PM"
				},
				{
					"start_time": "Mar 16 2020  5:33PM",
					"end_time": "Mar 16 2020 8:02PM"
				}
			]
		}
	]
}
```
## Features

- Using python3
- REST Api using django REST Framework

## To add Dummy data to the API
A json file has been created under 
- django-user-tracker/mysite/fixtures/dummy_data.json 
- To Run use command "python manage.py loaddata mysite/fixtures/dummy_data.json
