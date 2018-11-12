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
