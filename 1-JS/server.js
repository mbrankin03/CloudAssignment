'use strict';

const express = require('express');

const PORT = 60;
const HOST = '0.0.0.0';

var activityIntensity = require('./activityIntensity');

const app = express();
app.get('/', (req,res) => {

    var output = {
        'error': false,
        'string': '',
        'status': 0,
        'answer': 0
    };

    res.setHeader('Content-Type', 'application/json');
    res.setHeader('Access-Control-Allow-Origin', '*')
    var x = req.query.x;
    
    if (x !== undefined && !isNaN(x)) {
        x = parseFloat(x);
        
        if (x <= 55 && x >= 0) {
            var answer = activityIntensity.intensity(x);

            output.string = 'Activity Intensity: ' + answer;
            output.status = 200;
            output.answer = answer;
        
            res.end(JSON.stringify(output));
        } else {
            output.error = true;
            output.string = 'Please provide a valid input between 0 and 55';
            output.status = 400;
        
            res.end(JSON.stringify(output));
        }
    } else {
        output.error = true;
        output.string = 'Please provide a valid numeric input';
        output.status = 400;
    
        res.end(JSON.stringify(output));
    }
    
});

app.listen(PORT, HOST);
