from flask import Flask, render_template, url_for, request, redirect

app = Flask(__name__)

available_seat=4
passenger_list = {}


@app.route('/')
def home_page():
    return render_template('home.html')

@app.route('/booking', methods= ['POST','GET'])
def booking_ticket():
    seat = available_seat
    id = 0 if not len(passenger_list) else len(passenger_list)
    if request.method == 'POST':
        #passenger_num=3&passenger_name=Raji&Age=&Email=&gender=male
        input_seat = int(request.form.get('passenger_num'))
        input_name = request.form.get('passenger_name')
        input_age = int(request.form.get('age'))
        input_email = request.form.get('email')
        input_gender = request.form.get('gender')
        seat_fixed = seat - input_seat
        if seat_fixed < 0:
            return render_template('404.html', message=f"Sorry! Available seats are {seat}")
        else:
            passenger_list[id] = {"id":id,
                              "name" : input_name, 
                              "seat" : input_seat,
                              "age" : input_age,
                              "email" : input_email,
                              "gender" : input_gender}
            #return render_template('booking_confirmation.html', message = f"Booking confirmed for {passenger_list[id]['name']}!")
            return redirect(url_for('booking_confirmation', pass_id=id))
    return render_template('booking.html', seat=seat)


@app.route('/booking/confirmation/<int:pass_id>', methods = ['GET','POST'])
def booking_confirmation(pass_id):
    #passenger = pass_passenger_list[pass_id]
    total_amount = passenger_list[pass_id]['seat'] * 350
    if request.method == 'POST':
        input_amount = int(request.form.get('amount'))
        if total_amount == input_amount:
            return render_template('booking_confirmation.html', message = f"Booking confirmed for {passenger_list[pass_id]['name']}!")
        else:
            return render_template('insufficient-amt.html', message=f"Total amount to be paid {total_amount}, \
                                user paid {input_amount}. Insufficient amount. Booking failed!" )
        
    return render_template('booking_progress.html', amount = f'Total amount payable: {total_amount}')

@app.route('/booking/cancel', methods=['POST','GET'])
def cancellation():
    id = len(passenger_list)-1
    if id < 0:
        message = "No Passengers added"
        return render_template('booking_confirmation.html', message=message)
    message = f"Are you sure you want to cancel the ticket of {passenger_list[id]['name']}?"
    if request.method == 'POST':
        option = request.form.get('option')
        if option == 'yes':
            passenger_list.pop(id)
        return redirect(url_for('home_page'))
    return render_template('cancellation.html', message=message)

@app.route('/passenger_list')
def display_passenger():
    id = len(passenger_list)-1
    if id < 0:
        message = "No Passengers added"
        return render_template('booking_confirmation.html', message=message)
    return render_template('passenger-list.html', id=id, passenger_list=passenger_list)


if __name__ == '__main__':
    app.run(debug=True)
