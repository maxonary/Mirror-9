package main

import (
	"fmt"
	"net/http"
)

// Install Mercurial DVCS build tools
// sudo apt-get install gcc libc6-dev mercurial

// Install Go 1.18 for MacOS ARM64
// https://go.dev/dl/go1.18.darwin-arm64.pkg


// variables have to be declared
var api_key = "87b984ab68a0c5ba314b0b1148ad540e"

var city = "Berlin"

var url = "http://api.openweathermap.org/data/2.5/weather?q=" + city + "&APPID=" + api_key

// http response for testing at http://localhost:8081
func main() {
	http.HandleFunc("/", handler) 
	http.HandleFunc("/json", jsonHandler) 
	http.ListenAndServe(":8081", nil) 
}

func handler(w http.ResponseWriter, r *http.Request) {                               
    fmt.Fprintf(w, "Hello Linus") 
}

type User struct { 
	Id    int     `json:"id"` 
	Name  string  `json:"name"` 
	Email string  `json:"email"` 
	Phone string  `json:"phone"` 
}


func jsonHandler(w http.ResponseWriter, r *http.Request) {     
      
	w.Header().Set("Content-Type", "application/json") 
	user := User {
				  Id: 1, 
				  Name: "John Doe", 
				  Email: "johndoe@gmail.com", 
				  Phone: "000099999"} 
				  
   json.NewEncoder(w).Encode(user) 
}

// dinge die Linus nicht sehen soll, weil Max Schabernack macht, btw alle comments sind von mir und auf einmal schreibe ich auf Deutsch statt Englisch
/*
func weather_data() {
	var data = url.json()
	
	var city_data = (
        "city": data["name"],
        "sunrise": datetime.fromtimestamp(data["sys"]["sunrise"]),
        "sunset": datetime.fromtimestamp(data["sys"]["sunset"])
	)

    var weather_data = (
        "city": data["name"],
        "weather": data["weather"][0]["description"],
        "temperature": round(kelvin_to_celsius(data["main"]["feels_like"]), 1)
	)

    return {"city_data":city_data, "weather_data":weather_data}
} 

func kelvin_to_celsius(kelvin) {
    return kelvin - 273.15
}*/