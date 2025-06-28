from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    result = None
    if request.method == 'POST':
        dob_str = request.form['dob']
        try:
            dob = datetime.strptime(dob_str, '%Y-%m-%d')
            today = datetime.today()

            age_years = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
            days_alive = (today - dob).days

            next_birthday = dob.replace(year=today.year)
            if next_birthday < today:
                next_birthday = next_birthday.replace(year=today.year + 1)
            days_to_birthday = (next_birthday - today).days

            result = {
                'age': age_years,
                'days_alive': days_alive,
                'days_to_birthday': days_to_birthday
            }

        except:
            result = 'Invalid date format. Please try again.'

    return render_template('index.html', result=result)

if __name__ == "__main__":
    app.run()
    print(" Triggering Railway deploy...")
