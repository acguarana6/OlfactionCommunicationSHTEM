from firebase import firebase
firebase = firebase.FirebaseApplication('https://olfaction-communication-shtem.firebaseio.com/', None)
result = firebase.get('/users', None)
data =  { 'Message': 'Hello from the comm team!',
          'Ethanol': 70.05,
          'Alcohol': 59.22,
          'Propane': 63.76
          }
result2 = firebase.post('/Customer',data)
print(result2)
