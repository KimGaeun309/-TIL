// import the user model
const User = require('../models/User');
// import the packages
const bcrypt = require('bcryptjs');
const jwt = require('jsonwebtoken');

// write a function for the registration process
const register = (req, res, next) => {
  // encrypt the password we submitted
  bcrypt.hash(req.body.password, 10, function (err, hashedPass) {
    // and if any error occur, it will return the error.
    if (err) {
      res.json({
        error: err,
      });
    }

    let user = new User({
      name: req.body.name,
      email: req.body.email,
      phone: req.body.phone,
      password: hashedPass,
    });
    user
      .save()
      .then((user) => {
        res.json({
          message: 'User Added Successfully!',
        });
      })
      .catch((error) => {
        res.json({
          message: 'An error occured!',
        });
      });
  });
};

const login = (req, res, next) => {
  var username = req.body.username;
  var password = req.body.password;

  // if user submit email or phone as username
  // it will search the database if it exists
  User.findOne({ $or: [{ email: username }, { phone: username }] }).then(
    (user) => {
      // if it exists, it will campare the submitted password
      // with the encrypted password
      if (user) {
        bcrypt.compare(password, user.password, function (err, result) {
          if (err) {
            res.json({
              error: err,
            });
          }
          // if it matches, message is 'Login Successful'
          if (result) {
            let token = jwt.sign(
              { name: user.name },
              process.env.ACCESS_TOKEN_SECRET,
              {
                expiresIn: process.env.ACCESS_TOKEN_EXPIRE_TIME,
              }
            );
            let refreshtoken = jwt.sign(
              { name: user.name },
              process.env.REFRESH_TOKEN_SECRET,
              {
                expiresIn: process.env.REFRESH_TOKEN_EXPIRE_TIME,
              }
            );

            // send the user name with the token
            // we don't have to run any extra query
            // this user has to login again in 1 hour
            // identity of the token is verySecretValue
            // it shows whether token is original or not
            res.status(200).json({
              message: 'Login Succesful!',
              token,
              refreshtoken, // token: token 과 같은 뜻.
            });
          } else {
            // if it doesn't match, message is 'pw does not matched'
            res.status(200).json({
              message: 'Password does not matched!',
            });
          }
        });
      } else {
        // if it does not exist in db,
        res.json({
          // return message 'No user found'
          message: 'No user found!',
        });
      }
    }
  );
};

const refreshToken = (req, res, next) => {
  const refreshToken = req.body.refreshToken;
  jwt.verify(refreshToken, 'refreshtokensecret', function (err, decode) {
    if (err) {
      res.status(400).json({
        err,
      });
    } else {
      let token = jwt.sign({ name: decode.name }, 'Asd3e0)38', {
        expiresIn: '60s',
      });
      let refreshToken = req.body.refreshToken;
      res.status(200).json({
        message: 'Token refreshed successfully!',
        token,
        refreshToken,
      });
    }
  });
};

module.exports = {
  register,
  login,
  refreshToken,
};
