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
objectivesData = None

# Convert the objectives data into json for webpage
def getObjectives():
        # Get latest from database
        objectivesData = manageDb.getObjectives()

        jsonObjectives = []
        for objective in objectivesData:
                jsonObjectives.append(manageDb.as_dict(objective))
        return jsonObjectives

# Add a new objective based on JSON object
def addObjective(NewObjective):
        newItem = manageDb.Objectives(name=NewObjective['name'],
                                      description=NewObjective['description'])
        
        # Add the item to the database
        manageDb.dbSession.add(newItem)
        manageDb.dbSession.commit()

        return 200


## ----------------------------------------------------------
## Benefits
## ----------------------------------------------------------
benefitsData = manageDb.getBenefitTypes()

def getBenefits():
        jsonBenefits = []
        for benefit in benefitsData:
                jsonBenefits.append(manageDb.as_dict(benefit))
        return jsonBenefits

## ----------------------------------------------------------
## Improvements
## ----------------------------------------------------------
improvementsData = manageDb.getImprovements()

def getImprovements():
        # Refresh the improvements data
        improvementsData = manageDb.getImprovements()

        jsonImprovements = []
        for improvement in improvementsData:
                item = manageDb.as_dict(improvement)
                item['benefits'] = []
                for a in improvement.benefits:
                        item['benefits'].append(manageDb.as_dict(a))
                jsonImprovements.append(item)
        return jsonImprovements

# Need to look at removing unused "NAME" field
def addImprovement(NewImprovement):
        # Create the new improvement object
        newItem = manageDb.Improvement(name=NewImprovement['name'],
                                       description=NewImprovement['description'])
        
        benefits = []
        # Create the benefits objects
        for benefit in NewImprovement['benefits']:
                newBenefit = manageDb.Benefit(description=benefit['description'],
                                              benefit_type=benefit['id'])
                benefits.append(newBenefit)

        newItem.benefits = benefits
        
        manageDb.dbSession.add(newItem)
        manageDb.dbSession.commit()

        return 200