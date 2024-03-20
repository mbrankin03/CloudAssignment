package main

import (
	"net/http"
	"net/http/httptest"
	"testing"
)

func TestEngagementValidRequest(t *testing.T) {
	req, err := http.NewRequest("GET", "/?w=33&&x=22&y=44&z=55", nil)
	if err != nil {
		t.Fatal(err)
	}
	rr := httptest.NewRecorder()
	handler := http.HandlerFunc(ServeHTTP)
	handler.ServeHTTP(rr, req)

	if status := rr.Code; status != http.StatusOK {
		t.Errorf("handler returned wrong status code: got %v want %v",
			status, http.StatusOK)
	}

	expected := `{"Answer":100,"Error":false,"Status":200,"Message":"100 is the student engagement score "}`
	if rr.Body.String() != expected {
		t.Errorf("handler returned unexpected body: got %v want %v",
			rr.Body.String(), expected)
	}
}

func TestEngagement(t *testing.T) {
	score := engagement(33, 22, 44, 55)
	if score != 1 {
		t.Error("Expected 1, got ", score)
	}
}
