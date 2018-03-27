// Videos //
const cricket = '<iframe width="560" height="315" src="https://www.youtube.com/embed/vUQPLAlU0Sw?rel=0&amp;showinfo=0" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>';
const tennis = '<iframe width="560" height="315" src="https://www.youtube.com/embed/3IzdGNeD6j0?rel=0&amp;showinfo=0" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>';
const badminton = '<iframe width="560" height="315" src="https://www.youtube.com/embed/BDFafqskt7k?rel=0&amp;showinfo=0" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>';
const baseball = '<iframe width="560" height="315" src="https://www.youtube.com/embed/a585G2ls_KU?rel=0&amp;showinfo=0" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>';
const basketball = '<iframe width="560" height="315" src="https://www.youtube.com/embed/Yi3CrReo-S0?rel=0&amp;showinfo=0" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>';

var express = require('express');
var router = express.Router();

/* GET home page. */
router.get('/', function(req, res, next) {
  res.render('index', { title: 'Express' });
});

// routes will go here
router.get('/api/test', function(req, res) {

  var user_id = req.param('id');
  var token = req.param('token');
  var geo = req.param('geo');

  res.send(user_id + ' ' + token + ' ' + geo);
});

router.post('/test2', function(req, res) {
  var name = req.body.name;
  var color = req.body.color;
  var RFID = req.body.rfid;
  console.log("RFID: " +RFID);
  res.send("Hello: " +name +" " +color +" " +RFID);
});


router.post('/changeVideo', function(req, res) {

  var rfid = req.body.rfid;
  console.log("RFID: " +rfid);

  var message = getVideoForRFID(rfid);
  io.emit('rfidEvent',message );

  res.send("Success");
});

function getVideoForRFID(rfid) {
  if ( rfid === "100,127,55,170" )
    return cricket;
  else if ( rfid === "180,9,94,170" )
    return tennis;
  else if ( rfid === "68,59,90,170" )
      return badminton;
  else if ( rfid === "100,4,66,170" )
      return baseball;
  else if ( rfid === "36,233,222,109" )
      return basketball;
}
module.exports = router;
