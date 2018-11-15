## ----------------------------------------------------------
## Alerts
## ----------------------------------------------------------
alertsData = [{'id': 1, 'message': "Get started and create your first improvement!"},
              {'id': 2, 'message': "You can customise the benefits areas users can modify!"},
              {'id': 3, 'message': "Add some organisational objectives!"}]

def initAlerts():
    print("Loading user alerts")

def getAlerts():
    return alertsData

def dismissAlert(DismissAlertContent):
    # Find the matching alert number
    for alert in alertsData:
        if alert['id'] == DismissAlertContent['alertNum']:
            alertsData.remove(alert)

## ----------------------------------------------------------
## Objectives
## ----------------------------------------------------------
objectivesData = [{'name': "Great Place to Work",
                   'description': "Improve the business for the employees"},
                  {'name': "Lead Time Reduction",
                   'description': "Get out products out the door quicker"},
                  {'name': "Reduce Cost",
                   'description': "Bring down the cost of our products"}]

def objectives():
        return objectivesData

def addObjective(NewObjective):
        objectivesData.append({'name': NewObjective['name'],
                               'description': NewObjective['description']})
        return 200
