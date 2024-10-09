/* empfängt Frames über UDP und setzt sie auf UART um und umgekehrt
 * 
 * Frameaufbau UDP:
 * Länge: 11 Bytes
 * Byte 1 bis 10 enthalten die umzusetzenden Nutzdaten
 * Byte 0 enthält den Steuerbefehl
 * 
 * Steuerbefehle:
 * 0: Daten lesen
 * 1: Daten schreiben
 * 
 * 
 * Frameaufbau UART:
 * Länge 21 Bytes
 * Byte 0 bis 9 enthalten eine preambel: "0123456789"
 * Byte 10 bis 19 enthalten die Nutzdaten
 * Byte 20 enthält den Steuerbefehl
 * 
 * Steuerbefehle:
 * 0: Daten lesen
 * 1: Daten schreiben
 * 
 * 
 */

#include <ESP8266WiFi.h>
#include <WiFiUdp.h>
#include "defines.h"

const char *ssid = "Panter_1";
const char *password = pw;

WiFiUDP Udp;
unsigned int localUdpPort = 5555;                     // local port to listen on
char IncomingPacket[255];                             // buffer for incoming packets

int len = 0;

char SerialOutFrame[21];
char SerialInFrame[21];

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

  WiFi.mode(WIFI_STA);

  WiFi.begin(ssid, password);

  while (WiFi.status() != WL_CONNECTED)
  {
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

  strcpy(SerialOutFrame, "0123456789");
}

void loop()
{

  //  bool RelaisState = digitalRead(0); //GPIO 0

  int packetSize = Udp.parsePacket();

  if (packetSize)
  {
    if (packetSize == 11)
    {
      // receive incoming UDP packets
      //      Serial.printf("Received %d bytes from %s, port %d\n", packetSize, Udp.remoteIP().toString().c_str(), Udp.remotePort());
      int len = Udp.read(IncomingPacket, 255);

      switch (IncomingPacket[0])
      {
      case 0:
      {
        SerialOutFrame[10] = 0;
        SerialOutFrame[11] = 0;
        SerialOutFrame[12] = 0;
        SerialOutFrame[13] = 0;
        SerialOutFrame[14] = 0;
        SerialOutFrame[15] = 0;
        SerialOutFrame[16] = 0;
        SerialOutFrame[17] = 0;
        SerialOutFrame[18] = 0;
        SerialOutFrame[19] = 0;
        SerialOutFrame[20] = 0; // Steuerbefehl Daten lesen

        Serial.write(SerialOutFrame, 21);
        break;
      }
      case 1:
      {
        //        Udp.beginPacket(Udp.remoteIP(), Udp.remotePort());
        //        Udp.write("WriteData", 9);
        //        Udp.endPacket();

        SerialOutFrame[10] = IncomingPacket[1]; // Weiß
        SerialOutFrame[11] = IncomingPacket[2]; // Rot
        SerialOutFrame[12] = IncomingPacket[3]; // Grün
        SerialOutFrame[13] = IncomingPacket[4]; // Blau
        SerialOutFrame[14] = 0;
        SerialOutFrame[15] = 0;
        SerialOutFrame[16] = 0;
        SerialOutFrame[17] = 0;
        SerialOutFrame[18] = 0;
        SerialOutFrame[19] = 0;
        SerialOutFrame[20] = 1; // Steuerbefehl daten schreiben

        Serial.write(SerialOutFrame, 21);
        //        Serial.printf("UDP packet contents: %s\n", IncomingPacket);
        break;
      }
      case 2:
      {
        /*
        if (RelaisState)
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
        */
        break;
      }
      }
    }
    else
    {
      Udp.read(IncomingPacket, 255);
      //      Udp.beginPacket(Udp.remoteIP(), Udp.remotePort());
      //      Udp.write(Error, 1);
      //      Udp.endPacket();
    }
  }

  //Read Serial:

  if (Serial.available() > 20)
  {
    for(int i = 0; i < 21; i++)
    {
      SerialInFrame[i] = Serial.read();
    }

  }
}
