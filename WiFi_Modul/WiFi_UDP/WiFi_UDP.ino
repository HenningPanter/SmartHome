#include <ESP8266WiFi.h>
#include <WiFiUdp.h>
//test
const char* ssid     = "Panter_1";
const char* password = "xxxx";

WiFiUDP Udp;
unsigned int localUdpPort = 5555;  // local port to listen on
char IncomingPacket[255];  // buffer for incoming packets
char  replyPacekt[] = "Hi there! Got the message :-)";  // a reply string to send back
char Error[1];
int len = 0;

char OutFrame[21];


void setup()
{
  Serial.begin(115200);
  delay(10);

  // prepare GPIO2
  pinMode(2, OUTPUT);
  digitalWrite(2, 0);
  
  // Connect to WiFi network
  Serial.println();
  Serial.println();
  Serial.print("Connecting to ");
  Serial.println(ssid);
  
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

  // prepare GPIO2 as output
  pinMode(2, OUTPUT);
  digitalWrite(2, 0);

  // prepare GPIO0 as input
  pinMode(0, INPUT);

  strcpy(OutFrame, "0123456789");
  
}

void loop()
{

  bool RelaisState = digitalRead(0); //GPIO 0
  
  int packetSize = Udp.parsePacket();

  if(packetSize)
  {
    if (packetSize == 11)
    {
      // receive incoming UDP packets
//      Serial.printf("Received %d bytes from %s, port %d\n", packetSize, Udp.remoteIP().toString().c_str(), Udp.remotePort());
      int len = Udp.read(IncomingPacket, 255);

      
      
      if(IncomingPacket[0] == 0)  // Read data
      {
      
        if(RelaisState)
        {
          Udp.beginPacket(Udp.remoteIP(), Udp.remotePort());
          Udp.write("AN", 2);
          Udp.endPacket();
        }
        else
        {
          Udp.beginPacket(Udp.remoteIP(), Udp.remotePort());
          Udp.write("AUS", 3);
          Udp.endPacket();
        }
        
      }
      else  // Write data
      {
        Udp.beginPacket(Udp.remoteIP(), Udp.remotePort());
        Udp.write("WriteData", 9);
        Udp.endPacket();

        OutFrame[10] = IncomingPacket[1];
        OutFrame[11] = IncomingPacket[2];
        OutFrame[12] = IncomingPacket[3];
        OutFrame[13] = IncomingPacket[4];
        OutFrame[14] = IncomingPacket[5];
        OutFrame[15] = IncomingPacket[6];
        OutFrame[16] = IncomingPacket[7];
        OutFrame[17] = IncomingPacket[8];
        OutFrame[18] = IncomingPacket[9];
        OutFrame[19] = IncomingPacket[10];
        OutFrame[20] = 0;

        Serial.write(OutFrame, 20);
//        Serial.printf("UDP packet contents: %s\n", IncomingPacket);
      }
    }
    else
    {
      Udp.read(IncomingPacket, 255);
      Error[0] = 1;
      Udp.beginPacket(Udp.remoteIP(), Udp.remotePort());
      Udp.write(Error, 1);
      Udp.endPacket();
    }
  }
}
