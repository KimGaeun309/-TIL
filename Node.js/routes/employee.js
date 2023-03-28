const express = require('express');
const router = express.Router();

const EmployeeController = require('../controllers/EmployeeController');
const upload = require('../middleware/upload');
const authenticate = require('../middleware/authenticate'); // 코드 추가

router.get('/', authenticate, EmployeeController.index); // 수정
router.post('/show', EmployeeController.show);
router.post('/store', upload.array('avatar[]'), EmployeeController.store);
router.post('/update', EmployeeController.update);
router.post('/delete', EmployeeController.destroy);

module.exports = router;
