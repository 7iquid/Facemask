#include <ESP8266WiFi.h> 
const char* ssid = "Covid19"; //replace with your own wifi ssid 
const char* password = "123456789"; //replace with your own //wifi ssid password 
const char* host = "192.168.1.44";
const int httpPort = 8000;


void setup() { 
  Serial.begin(115200); 
  delay(10); // We start by connecting to a WiFi network Serial.println();
  Serial.println(); Serial.print("Connecting to ");
  Serial.println(ssid);
  /* Explicitly set the ESP8266 to be a WiFi-client, otherwise, it by default, would try to act as both a client and an access-point and could cause network-issues with your other WiFi-devices on your WiFi-network. */
  WiFi.mode(WIFI_STA);
  WiFi.begin(ssid, password);
  
  while (WiFi.status() != WL_CONNECTED)
    {
    delay(500);
    Serial.print(".");
    }
  Serial.println("");
  Serial.println("WiFi connected"); 
  Serial.println("IP address: "); 
  Serial.println(WiFi.localIP());
   } 

int value = 0; 
WiFiClient client;
String url = "api/machine/323/";
unsigned long timeout = millis();

void loop() {
	delay(5000);
	++value; 
	Serial.print("connecting to ");
	Serial.println(host); // Use WiFiClient class to create TCP connections
	

	if (!client.connect(host, httpPort)) {
		Serial.println("connection failed");
		return;
		}
	client.print(String("GET /") + " HTTP/1.1\r\n" +
		"Host: " + host + "\r\n" +
		"Connection: close\r\n" +
		"\r\n"
		);
	
	while (client.available() == 0) {
		if (millis() - timeout > 5000) { 
			Serial.println(">>> Client Timeout !");
			client.stop(); return; } } // Read all the lines of the reply from server and print them to Serial
	
	while (client.available()) { 
		String line = client.readStringUntil('\r'); Serial.print(line);
    }

	}

