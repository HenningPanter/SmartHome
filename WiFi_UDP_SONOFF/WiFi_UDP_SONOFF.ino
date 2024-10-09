#include <ESP8266WiFi.h>
#include <WiFiUdp.h>

const char* ssid     = "Panter_1";
const char* password = "26968748840208120998";

WiFiUDP Udp;
unsigned int localUdpPort = 5555;  // local port to listen on
char IncomingPacket[255];  // buffer for incoming packets
char Error[1];
int len = 0;

void setup()
{
  Serial.begin(115200);
  delay(10);

  
  // Connect to WiFi network
  Serial.println();
  Serial.println();
  Serial.print("Connecting to ");
  Serial.println(ssid);
  WiFi.hostname("ESP8266_SONOFF_1");
  WiFi.mode(WIFI_STA);


  //IPAddress staticIP(192, 168, 0, 111); //ESP static ip : Modula A
  //IPAddress staticIP(192, 168, 0, 112); //ESP static ip : Modula B
  //IPAddress staticIP(192, 168, 0, 113); //ESP static ip : Modula C
  //IPAddress staticIP(192, 168, 0, 114); //ESP static ip : Modula D
  //IPAddress staticIP(192, 168, 0, 115); //ESP static ip : Modula E
  IPAddress staticIP(192, 168, 0, 116); //ESP static ip : Modula F
  
  IPAddress gateway(192, 168, 0, 1);   //IP Address of your WiFi Router (Gateway)
  IPAddress subnet(255, 255, 255, 0);  //Subnet mask
  IPAddress dns(8, 8, 8, 8);  //DNS

  WiFi.config(staticIP, subnet, gateway, dns);
  
  WiFi.begin(ssid, password);
  
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("");
  Serial.println("WiFi connected");
  
  Udp.begin(localUdpPort);
  Serial.printf("Now listening at IP %s, UDP port %d\n", WiFi.localIP().toString().c_str(), localUdpPort);

  // Print the IP address
  Serial.println(WiFi.localIP());


  // prepare GPI12 : Relais
  pinMode(12, OUTPUT);
  digitalWrite(12, 0);

  // prepare GPI13 : LED
  pinMode(13, OUTPUT);
  digitalWrite(13, 1);
  
}

void loop()
{ 
  int packetSize = Udp.parsePacket();

  if(packetSize)
  {

      // receive incoming UDP packets
      Serial.printf("Received %d bytes from %s, port %d\n", packetSize, Udp.remoteIP().toString().c_str(), Udp.remotePort());
      int len = Udp.read(IncomingPacket, 255);

//      Serial.printf("UDP packet contents: %s\n", IncomingPacket);
      
      if(strcmp(IncomingPacket, "an") == 0)
      {
        Serial.printf("an\n");
        digitalWrite(12, 1);
        digitalWrite(13, 0);
        
      }
      if(strcmp(IncomingPacket, "aus") == 0)
      {
        Serial.printf("aus\n");
          digitalWrite(12, 0);
          digitalWrite(13, 1);
      }

      memset(IncomingPacket, 0, 255);

  }
}
