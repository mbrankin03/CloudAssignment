package main

func engagement(w, x, y, z float64) float64 {

	lecture := (w * 0.3) / 33
	lab := (x * 0.4) / 22
	supportSessions := (y * 0.15) / 44
	canvasActivities := (z * 0.15) / 55

	total := lecture + lab + supportSessions + canvasActivities
	return total
}
