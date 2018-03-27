var express = require('express');
var router = express.Router();

/* GET home page. */
router.get('/', function(req, res, next) {
  res.render('index', { title: 'Express' });
});

// routes will go here
router.post('/changeState', function(req, res) {

  var state = req.body.state;
  console.log("state: " +state);

  io.emit('stateChangeEvent',state);

  res.send("Success");
});

module.exports = router;
