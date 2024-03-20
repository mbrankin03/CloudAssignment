require 'test-unit'
require 'net/http'
require 'json'
require 'webrick'
require_relative 'StudentFailure'

class TestStudentFailure < Test::Unit::TestCase
    def test_failure
        assert_equal("Student is not at risk of failing", StudentFailure.new.failure(50,50))
        assert_equal("Student is at risk of failing", StudentFailure.new.failure(50,60))
        assert_equal("Student is not at risk of failing", StudentFailure.new.failure(50,40))
        assert_equal("Student is not at risk of failing", StudentFailure.new.failure(50,49))
        assert_equal("Student is at risk of failing", StudentFailure.new.failure(50,51))
    end
end

# do web test for app.rb
class TestWebTest < Test::Unit::TestCase
    def test_do_GET_with_cutoff
        uri = URI.parse("http://localhost:8001/?w=12&x=21&y=20&z=23&a=50")
        response = Net::HTTP.get_response(uri)
        assert_equal(200, response.code.to_i)
        assert_equal("application/json", response.content_type)
        body = JSON.parse(response.body)
        assert_equal("Student Engagement score is 62 and the cut off is 50", body["string"])
        assert_equal("Student is not at risk of failing", body["answer"])
        assert_equal(200, body["status"])
    end

    def test_do_GET_without_cutoff
        uri = URI.parse("http://localhost:8001/?w=12&x=21&y=20&z=23")
        response = Net::HTTP.get_response(uri)
        assert_equal(400, response.code.to_i)
        assert_equal("application/json", response.content_type)
        body = JSON.parse(response.body)
        assert_equal("Please provide a cut off score value", body["string"])
        assert_equal("N/A", body["answer"])
        assert_equal(400, body["status"])
    end
end
