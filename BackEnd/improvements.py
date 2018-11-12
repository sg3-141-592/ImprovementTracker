## ----------------------------------------------------------
## Alerts
## ----------------------------------------------------------
alertsData = [{'id': 1, 'message': "Get started and create your first improvement!"},
              {'id': 2, 'message': "You can customise the benefits areas users can modify!"}]

def alerts():
    return alertsData

def dismissAlert(alertnum):
    # Find the matching alert number
    for alert in alertsData:
        if alert['id'] == alertnum:
            alertsData.remove(alert)
    print(alertnum)

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
