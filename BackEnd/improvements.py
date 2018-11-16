import manageDb

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
objectivesData = manageDb.getObjectives()

# Convert the objectives data into json for webpage
def getObjectives():
        jsonObjectives = []
        for objective in objectivesData:
                jsonObjectives.append(manageDb.as_dict(objective))
        return jsonObjectives

# Add a new objective based on JSON object
# UNTESTED ---------
def addObjective(NewObjective):
        newItem = manageDb.Objectives(name=NewObjective['name'],
                                      description=NewObjective['description'])
        objectivesData.append(newItem)
        # Add the item to the database
        manageDb.dbSession.add(objectivesData)
        return 200


## ----------------------------------------------------------
## Benefits
## ----------------------------------------------------------
benefitsData = manageDb.getBenefits()

def getBenefits():
        jsonBenefits = []
        for benefit in benefitsData:
                jsonBenefits.append(manageDb.as_dict(benefit))
        return jsonBenefits
