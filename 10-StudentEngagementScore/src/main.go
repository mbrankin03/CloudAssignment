package main

import (
	"encoding/json"
	"math"
	"net/http"
	"strconv"
)

func errorCheck(err error) {
	if err != nil {
		panic(err)
	}
}

func handleError(wr http.ResponseWriter, errorMessage string) {
	wr.Header().Set("Content-Type", "application/json")
	wr.Header().Set("Access-Control-Allow-Origin", "*")
	wr.WriteHeader(http.StatusBadGateway)
	b, err := json.Marshal(CustomResponse{Answer: -1, Error: true, Status: 400, Message: errorMessage})
	if err != nil {
		errorCheck(err)
	}
	wr.Write(b)
}

type CustomResponse struct {
	Answer  float64
	Error   bool
	Status  int
	Message string
}

func main() {
	http.HandleFunc("/", ServeHTTP)
	err := http.ListenAndServe("0.0.0.0:2023", nil)
	errorCheck(err)
}

type Entry struct{}

func ServeHTTP(wr http.ResponseWriter, r *http.Request) {
	w := r.URL.Query().Get("w")
	x := r.URL.Query().Get("x")
	y := r.URL.Query().Get("y")
	z := r.URL.Query().Get("z")
	if w == "" && x == "" && y == "" && z == "" {
		handleError(wr, "w,x,y,z is empty")
		return
	} else {
		wFloat, err := strconv.ParseFloat(w, 64)
		if err != nil || wFloat > 33 || wFloat < 0 {
			handleError(wr, "w is not a valid float - must be less than 33 and a number ")
			return
		}
		xFloat, err := strconv.ParseFloat(x, 64)
		if err != nil || xFloat > 22 || xFloat < 0 {
			handleError(wr, "x is not a valid float - must be less than 22 and a number ")
			return
		}
		yFloat, err := strconv.ParseFloat(y, 64)
		if err != nil || yFloat > 44 || yFloat < 0 {
			handleError(wr, "y is not a valid float - must be less than 44 and a number ")
			return
		}
		zFloat, err := strconv.ParseFloat(z, 64)
		if err != nil || zFloat > 55 || zFloat < 0{
			handleError(wr, "z is not a valid float - must be less than 55 and a number ")
			return
		}
		answer := engagement(wFloat, xFloat, yFloat, zFloat)
		wr.Header().Set("Content-Type", "application/json")
		wr.Header().Set("Access-Control-Allow-Origin", "*")
		wr.WriteHeader(http.StatusOK)
		answer = math.Round(answer * 100)
		str := strconv.FormatFloat(answer, 'f', 0, 64) + " is the student engagement score "
		b, err := json.Marshal(CustomResponse{Answer: answer, Error: false, Status: 200, Message: str})
		if err != nil {
			errorCheck(err)
		}
		wr.Write(b)
		return
	}
}
