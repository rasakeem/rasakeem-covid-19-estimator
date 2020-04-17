data = {"region": {
    "name": "Africa",
    'avgAge': 19.7,
    'avgDailyIncomeInUSD': 5,
    'avgDailyIncomePopulation': 0.71
    },
    'periodType': "days",
    'timeToElapse': 58,
    'reportedCases': 674,
    'population': 66622705,
    'totalHospitalBeds': 1380614
}

def normalize(data):

  if data.get('periodType') == 'days':
    return data.get('timeToElapse')
  if data.get('periodType') == 'weeks':
    return data.get('timeToElapse') * 7
  if data.get('periodType') == 'months':
    return data.get('timeToElapse') * 30

def estimator(data):
    display={'data': data, "impact": {}, "severeImpact": {}}
    days=normalize(data)
    display['impact']['currentlyInfected']=data['reportedCases'] * 10
    display['severeImpact']['currentlyInfected']=data['reportedCases'] * 50
    display['impact']['infectionsByRequestedTime']=int(
    display['impact']['currentlyInfected'] * (2 ** int(days / 3)))
    display['severeImpact']['infectionsByRequestedTime']=int(
    display['severeImpact']['currentlyInfected'] * (2 ** int(days / 3)))
    display['impact']['severeCasesByRequestedTime']=int( 
        0.15 * display['impact']['infectionsByRequestedTime'])
    display['severeImpact']['severeCasesByRequestedTime']=int(
    0.15 * display['severeImpact']['infectionsByRequestedTime'])
    display['impact']['hospitalBedsByRequestedTime']=int((0.35 * data['totalHospitalBeds'])
    - display['impact']['severeCasesByRequestedTime'])
    display['severeImpact']['hospitalBedsByRequestedTime']=int((0.35 * data['totalHospitalBeds'])
    - display['severeImpact']['severeCasesByRequestedTime'])
    display['impact']['casesForICUByRequestedTime']=int(
    0.05 * display['impact']['infectionsByRequestedTime'])
    display['severeImpact']['casesForICUByRequestedTime']=int(
    0.05 * display['severeImpact']['infectionsByRequestedTime'])
    display['impact']['casesForVentilatorsByRequestedTime']=int(
    0.02 * display['impact']['infectionsByRequestedTime'])
    display['severeImpact']['casesForVentilatorsByRequestedTime']=int(
    0.02 * display['severeImpact']['infectionsByRequestedTime'])
    display['impact']['dollarsInFlight']=int((display['impact']['infectionsByRequestedTime']
    * data['region']['avgDailyIncomePopulation'] * data['region']['avgDailyIncomeInUSD']) / days)
    display['severeImpact']['dollarsInFlight']=int((display['severeImpact']['infectionsByRequestedTime']
    * data['region']['avgDailyIncomePopulation'] * data['region']['avgDailyIncomeInUSD']) / days)
    return display
print(estimator(data))


