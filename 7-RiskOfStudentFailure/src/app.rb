#!/usr/bin/env ruby

require "webrick"
require 'json'
require_relative 'StudentFailure'
require 'net/http'

# Make a request to the qubengage-studentEngagementScore service
# to get the student engagement score so that we can parse it
# and use it in the studentFailure service - current issue
def get_student_engagement_score(w_value, x_value, y_value, z_value)
    # Build the URI using the values passed in from the request
    uri = URI.parse("http://studentengagementscore.40297935.qpc.hal.davecutting.uk/")
    uri.query = URI.encode_www_form({ w: w_value, x: x_value, y: y_value, z: z_value })
    puts "URI: #{uri}\n"
    res = Net::HTTP.get_response(uri)

    # Check if the response is successful (HTTP 200 OK)
    if res.is_a?(Net::HTTPSuccess)
        engagement_score = JSON.parse(res.body)["Answer"]
        return engagement_score
    else
        # Handle the case where the Go server response is not successful
        puts "Error: Unable to get student engagement score from Go server"
        return -1
    end
end

class MyServlet < WEBrick::HTTPServlet::AbstractServlet
    def do_GET(request, response)
        response.content_type = "application/json"
        response.header['Access-Control-Allow-Origin'] = '*'

        w = request.query["w"].to_i
        x = request.query["x"].to_i
        y = request.query["y"].to_i
        z = request.query["z"].to_i

        engagement_score = get_student_engagement_score(w, x, y, z)

        if engagement_score == -1
            response.status = 500
            error_response = {
                "string" => "Unable to get student engagement score from Go server - W must be between 0 and 33, X must be between 0 and 22, Y must be between 0 and 44, Z must be between 0 and 55",
                "answer" => "N/A",
                "status" => 500
            }
            response.body = JSON.generate(error_response)
            elsif request.query["a"]
            a = request.query["a"]
            if a.to_i.to_s == a && a.to_i <= 100 && a.to_i >= 0
                response.status = 200
                result = StudentFailure.new.failure(engagement_score.to_i, a.to_i)
                raw_response = {
                    "string" => "Student Engagement score is #{engagement_score} and the cut off is #{a}",
                    "answer" => result,
                    "status" => 200
                }
                response.body = JSON.generate(raw_response)
            elsif a.to_i > 100 || a.to_i < 0
                response.status = 400
                error_response = {
                    "string" => "Invalid cut off score value. The cut off score cannot be higher than 100 or lower than 0",
                    "answer" => "N/A",
                    "status" => 400
                }
                response.body = JSON.generate(error_response)
            else
                response.status = 400
                error_response = {
                    "string" => "Invalid cut off score value. Please provide a numeric value",
                    "answer" => "N/A",
                    "status" => 400
                }
                response.body = JSON.generate(error_response)
            end
        else
            response.status = 400
            error_response = {
                "string" => "Please provide a cut off score value",
                "answer" => "N/A",
                "status" => 400
            }
            response.body = JSON.generate(error_response)
        end
    end
end 

server = WEBrick::HTTPServer.new(:Port => 8001)

server.mount "/", MyServlet

trap("INT") {
    server.shutdown
}

server.start