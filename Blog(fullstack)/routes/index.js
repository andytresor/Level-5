var express = require('express');
var router = express.Router();
const model = require('../models/user')

/* GET home page. */
router.get('/', function(req, res, next) {
  res.render('index', { 
    title: 'Express',
    description: "Hello Seven Ecademy",
    
   });
});

router.get('/about', function(req, res, next) {
  res.render('about', { title: 'About Page' });
});

router.post('/about',async function(req, res, next) {
  const body = req.body;
  const storeUser = new model ( body );
  await storeUser.save()
  console.log(body);
  res.redirect('/?name=' + body.name)
});

module.exports = router;
