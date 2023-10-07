
import firebase_admin
from firebase_admin import credentials, db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL':"https://attendance-cfeec-default-rtdb.firebaseio.com/"
})


ref = db.reference('Students')

data = {
    "20BCS5804":
        {
            "name": "Chirag Kumar",
            "major": "CSE",
            "SEC": 605,
            "total_attendance": 0,
            "group": "B",
            "year": 3,
            "last_attendance_time": "2023-05-14 00:54:34"
        },
    "22BCS9891":
        {
            "name": "XYZ",
            "major": "CSE",
            "SEC": 601,
            "total_attendance": 0,
            "group": "A",
            "year": 1,
            "last_attendance_time": "2023-05-14 00:54:34"
        }

}

for key, value in data.items():
    ref.child(key).set(value)