var expect  = require('chai').expect;
const request = require('request');
var activityIntensity = require('./activityIntensity');

describe('activityIntensity', function() {
    it('should return "Low intensity activity" for activityHours less than or equal to 5', function() {
        const result = activityIntensity.intensity(5);
        expect(result).to.equal('Low intensity activity');
    });

    it('should return "Medium intensity activity" for activityHours less than or equal to 10', function() {
        const result = activityIntensity.intensity(10);
        expect(result).to.equal('Medium intensity activity');
    });

    it('should return "High intensity activity" for activityHours less than or equal to 15', function() {
        const result = activityIntensity.intensity(15);
        expect(result).to.equal('High intensity activity');
    });

    it('should return "Very High Intensity activity" for activityHours greater than 15 and less than or equal to 55', function() {
        const result = activityIntensity.intensity(20);
        expect(result).to.equal('Very High Intensity activity');
    });

    it('should return "Invalid input" for activityHours greater than 55', function() {
        const result = activityIntensity.intensity(60);
        expect(result).to.equal('Invalid input');
    });
});

describe("ActivityIntensity API", function() {

        let j;

        describe("No parameter to count", function() {
                var url = "http://localhost:60/";

                it("returns status 400", function(done) {
                        request(url, function(error, response, body) {
                                console.log(body);
                                j = JSON.parse(body);
                        expect(j.status).to.equal(400);
                        done();
                        });
                });
                it("returns error as true", function(done) {
                        request(url, function(error, response, body) {
                                console.log(body);
                                j = JSON.parse(body);
                        expect(j.error).to.equal(true);
                        done();
                        });
                });
                it("returns error message", function(done) {
                        request(url, function(error, response, body) {
                                console.log(body);
                                j = JSON.parse(body);
                        expect(j.string).to.equal('Please provide a valid numeric input');
                        done();
                        });
                });
        });
        describe("successful test", function() {

                var url = "http://localhost:60/?x=10";

                it("returns status 200", function(done) {
                        request(url, function(error, response, body) {
                                console.log(body);
                                j = JSON.parse(body);
                        expect(j.status).to.equal(200);
                        done();
                        });
                });
                it("returns error as false", function(done) {
                        request(url, function(error, response, body) {
                                console.log(body);
                                j = JSON.parse(body);
                        expect(j.error).to.equal(false);
                        done();
                        });
                });
                it("returns correct message", function(done) {
                        request(url, function(error, response, body) {
                                console.log(body);
                                j = JSON.parse(body);
                        expect(j.string).to.equal('Activity Intensity: Medium intensity activity');
                        done();
                        });
                });
        });
});