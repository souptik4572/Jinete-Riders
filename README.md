[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)
# Jinete
Ride booking app for traveling within the city made using Python and Django.

The backend part is made using Python and using the versatile Django framework and uses JWT authentication along with auto email password reset functionality implemented using SendGrid API.

It also features a payment gateway which is implemented using Razorpay API.

The backend is hosted using Heroku and can be accessed from [here](https://jinete-riders.herokuapp.com/).

The complete Postman documentation can be accessed from [here](https://documenter.getpostman.com/view/14121536/UV5f6t9J).

## Environment Variables

To run this project, you will need to add the following environment variables to your .env file

`SECRET_KEY - The default secret key auto generated by django while creating new project`

`ACCESS_SECRET_TOKEN - The secret used for creating all Json Web Tokens for Authorization and Authentication`

`BCRYPT_SALT - Sale value for encrypting the password`

`SENDGRID_API_KEY - Sendgrid API key for enabling sendgrid email sending system`

`PASSWORD_RESET_EMAIL_TEMPLATE_ID - Sendgrid password reset template id`

`FROM_EMAIL - Email is from where password reset email should be sent`

`DATABASE_URL - PostgreSQL url to be used as database for production`

`RAZOR_KEY_ID - Unique Razorpay Key ID to make secure payments using the Razorpay API`

`RAZOR_KEY_SECRET - Razorpay secret key which is used alongside RAZOR_KEY_ID`
