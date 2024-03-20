module.exports = {
    intensity: function (activityHours) {

        
        var lowIntensity = 5;
        var mediumIntensity = 10;
        var highIntensity = 15;

        if (activityHours > 55){
            return "Invalid input"
        } else if (activityHours <= lowIntensity) {
            return "Low intensity activity"
        } else if (activityHours <= mediumIntensity) {
            return "Medium intensity activity"
        }
        else if (activityHours <= highIntensity) {
            return "High intensity activity"
        }
        else {
            return "Very High Intensity activity"
        }
}
}
