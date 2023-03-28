const express = require('express'); // node.js의 framework
const mongoose = require('mongoose'); // work with mongodb
const morgan = require('morgan'); // log in console
const bodyParser = require('body-parser'); // parse the request incoming bodies

const dotenv = require('dotenv');
dotenv.config(); // if you add or change in .env file,
// you have to restart your npm or server.

const EmployeeRoute = require('./routes/employee');
const AuthRoute = require('./routes/auth');

mongoose.connect('mongodb://localhost:27017/testdb', {
  useNewUrlParser: true,
  useUnifiedTopology: true,
}); // testdb is the name of the database
const db = mongoose.connection;

// error during connection -> log error
db.on('error', (err) => {
  console.log(err);
});

// no error during connection -> log connection established
db.once('open', () => {
  console.log('Database Connection Established!');
});

// declare express
const app = express();
// we have to use morgan and body parser in express
// we both used URL envoded and JSON for body parser
// -> request가 url로 오든 json으로 오든 처리 가능
app.use(morgan('dev'));
app.use(bodyParser.urlencoded({ extended: true }));
app.use(bodyParser.json());

app.use('/uploads', express.static('uploads')); // 코드 추가

// declare a port for our node.js application
const PORT = process.env.PORT || 3000;
// env file에 저장된 PORT 가 있으면 그 PORT를 사용
// 없으면 3000을 PORT로 사용

app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});

app.use('/api/employee', EmployeeRoute);

// localhost:3000/api/employee -> EmployeeController.index
// localhost:3000/api/employee/show -> EmployeeController.show

app.use('/api', AuthRoute);

// localhost:3000/api/register -> registerController!
