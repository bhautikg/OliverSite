from flask import Flask, request
from processing import do_processing


app = Flask(__name__)
app.config["DEBUG"] = True

@app.route('/',methods=["GET", "POST"])
def main():
    errors = ""
    if request.method == "POST":
        street1 = None
        street2 = None
        locationdetail = None
        email = None
        phone = None
        try:
            street1 = str(request.form["street1"])
        except:
            errors += "<p>{!r} is not a valid street name.</p>\n".format(request.form["street1"])
        try:
            street2 = str(request.form["street2"])
        except:
            errors += "<p>{!r} is not a valid street name.</p>\n".format(request.form["street2"])
        try:
            locationdetail = str(request.form["locationdetail"])
        except:
            errors += "<p>{!r} is not a valid location detail.</p>\n".format(request.form["locationdetail"])
        try:
            email = str(request.form["email"])
        except:
            errors += "<p>{!r} is not a valid email.</p>\n".format(request.form["email"])
        try:
            phone = int(request.form["phone"])
        except:
            errors += "<p>{!r} is not a phone number.</p>\n".format(request.form["phone"])

        if street1 is not None and street2 is not None and locationdetail is not None and email is not None and phone is not None:
            result = do_processing(street1, street2, locationdetail, email, phone)
            return '''
                <html>
                    <body>
                        <p>The form is submitted</p>
                        <p><a href="/">Click here to submit another request</a>
                    </body>
                </html>
            '''.format(result=result)

    return '''
        <html>
            <body>
                {errors}
                <p>Enter your details:</p>
                <form method="post" action=".">
                    <p>Street 1: <input name="street1" /></p>
                    <p>Street 2: <input name="street2" /></p>
                    <p>Location detail: <input name="locationdetail" /></p>
                    <p>email: <input name="email" /></p>
                    <p>phone: <input name="phone" /></p>
                    <p><input type="submit" value="Submit form" /></p>
                </form>
            </body>
        </html>
    '''.format(errors=errors)

if __name__ == '__main__':
    app.run()

