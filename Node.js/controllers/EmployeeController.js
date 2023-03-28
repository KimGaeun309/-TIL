const Employee = require('../models/Employee');

// Show the list of Employees from the DB
const index = (req, res, next) => {
  if (req.query.page && req.query.limit) {
    Employee.paginate({}, { page: req.query.page, limit: req.query.limit })
      .then((response) => {
        res.json({
          response,
        });
      })
      .catch((error) => {
        res.json({
          message: 'An error Occured: ' + error,
        });
      });
  } else {
    Employee.find()
      .then((response) => {
        res.json({
          response,
        });
      })
      .catch((error) => {
        res.json({
          message: 'An error Occured: ' + error,
        });
      });
  }
};

// Show single employee
const show = (req, res, next) => {
  let employeeID = req.body.employeeID;
  Employee.findById(employeeID)
    .then((response) => {
      res.json({
        response,
      });
    })
    .catch((error) => {
      console.log(error); // add this line to log the error
      res.json({
        message: 'An error Occured!',
      });
    });
};

//  add new employee
const store = (req, res, next) => {
  let employee = new Employee({
    name: req.body.name,
    designation: req.body.designation,
    email: req.body.email,
    phone: req.body.phone,
    age: req.body.age,
  });

  // if (req.file) {
  //   // 코드 추가
  //   employee.avatar = req.file.path;
  // }

  if (req.files) {
    let path = '';
    req.files.forEach(function (files, index, arr) {
      path = path + files.path + ',';
    });
    path = path.substring(0, path.lastIndexOf(','));
    employee.avatar = path;
  }

  employee
    .save()
    .then((response) => {
      res.json({
        message: 'Employee Added Successfully!',
      });
    })
    .catch((error) => {
      console.log(error); // add this line to log the error
      res.json({
        message: 'An error Occured!',
      });
    });
};

// update an employee
const update = (req, res, next) => {
  let employeeID = req.body.employeeID;

  let updatedData = {
    name: req.body.name,
    designation: req.body.designation,
    email: req.body.email,
    phone: req.body.phone,
    age: req.body.age,
  };
  Employee.findByIdAndUpdate(employeeID, { $set: updatedData })
    .then(() => {
      res.json({
        message: 'Employee updated Successfully!',
      });
    })
    .catch((error) => {
      console.log(error); // add this line to log the error
      res.json({
        message: 'An error Occured!',
      });
    });
};

// delete an employee
const destroy = (req, res, next) => {
  let employeeID = req.body.employeeID;
  Employee.findByIdAndRemove(employeeID)
    .then(() => {
      req.json({
        message: 'Employee deleted successfully!',
      });
    })
    .catch((error) => {
      console.log(error); // add this line to log the error
      req.json({
        message: 'An error Occured!',
      });
    });
};

module.exports = {
  index,
  show,
  store,
  update,
  destroy,
};
