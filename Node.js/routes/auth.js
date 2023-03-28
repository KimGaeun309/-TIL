const express = require('express');
const router = express.Router();

const AutoController = require('../controllers/AutoController');

router.post('/register', AutoController.register);
router.post('/login', AutoController.login);
router.post('/refresh-token', AutoController.refreshToken);

module.exports = router;

// created a route for the registration process
