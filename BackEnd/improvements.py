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

def initObjectives():
        print("Loading objectives data")

def getObjectives():
        return objectivesData

def addObjective(NewObjective):
        objectivesData.append({'name': NewObjective['name'],
                               'description': NewObjective['description']})
        return 200


## ----------------------------------------------------------
## Benefits
## ----------------------------------------------------------
benefitsData = [{
                    'id': 1,
                    'name': "Time",
                    'description': "Users reduce the amount of time they need to spend reviewing work"
                },
                {
                    'id': 2,
                    'name': "Great Place to Work",
                    'description': "Users have access to best in class tooling, and feel listened to"
                },
                {
                    'id': 3,
                    'name': "Automation",
                    'description': "Increase quality through automation, and reduce effort"
                }]

def initBenefits():
        print("Loading Benefits Data")

def getBenefits():
        return benefitsData

