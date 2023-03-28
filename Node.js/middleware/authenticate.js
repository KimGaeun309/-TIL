const jwt = require('jsonwebtoken');

const authenticate = (req, res, next) => {
  try {
    // our user should send their token to req.headers.authorization
    const token = req.headers.authorization.split(' ')[1];
    const decode = jwt.verify(token, process.env.ACCESS_TOKEN_SECRET); // this secretValue is given while login.
    // this two values should be same or your token will be rejected
    // you should keep it complex to increase your application security
    // so change from 'secretValue' to 'Asd3e0)38'
    // never share it!!

    req.user = decode;
    next();
  } catch (error) {
    if (error.name == 'TokenExpiredError') {
      res.status(401).json({
        message: 'Token Expired!',
      });
    } else {
      res.json({
        message: 'Authentication Failed!',
      });
    }
    res.json({
      message: 'Authentication Failed!',
    });
  }
};

module.exports = authenticate;
