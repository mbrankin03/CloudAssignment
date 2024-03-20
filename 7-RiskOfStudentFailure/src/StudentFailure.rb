class StudentFailure 
    def failure (engagement_score,x)
        if engagement_score&. < x
            return "Student is at risk of failing"
        else
            return "Student is not at risk of failing"
        end
    end
end

