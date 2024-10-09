// g++ -o werkstatt_gpio_steuerung werkstatt.cpp -lwiringPi

#include <iostream>
#include <wiringPi.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <arpa/inet.h>
#include <netinet/in.h>

using namespace std;

#define PORT 5556
#define BufferSize 10u

void a_an(void)
{
    digitalWrite(21, 0);
}

void a_aus(void)
{
    digitalWrite(21, 1);
}

void b_an(void)
{
    digitalWrite(22, 0);
}

void b_aus(void)
{
    digitalWrite(22, 1);
}

void c_an(void)
{
    digitalWrite(23, 0);
}

void c_aus(void)
{
    digitalWrite(23, 1);
}

void d_an(void)
{
    digitalWrite(27, 0);
}

void d_aus(void)
{
    digitalWrite(27, 1);
}

void e_an(void)
{
    digitalWrite(24, 0);
}

void e_aus(void)
{
    digitalWrite(24, 1);
}

void f_an(void)
{
    digitalWrite(28, 0);
}

void f_aus(void)
{
    digitalWrite(28, 1);
}

void g_an(void)
{
    digitalWrite(29, 0);
}

void g_aus(void)
{
    digitalWrite(29, 1);
}

void h_an(void)
{
    digitalWrite(25, 0);
}

void h_aus(void)
{
    digitalWrite(25, 1);
}

void auswerten(char inhalt[])
{
    printf("%s\n", inhalt);

    if (strcmp(inhalt, "a_an") == 0)
    {
        digitalWrite(21, 0);
    }

    if (strcmp(inhalt, "a_aus") == 0)
    {
        digitalWrite(21, 1);
    }

    if (strcmp(inhalt, "b_an") == 0)
    {
        digitalWrite(22, 0);
    }

    if (strcmp(inhalt, "b_aus") == 0)
    {
        digitalWrite(22, 1);
    }

    if (strcmp(inhalt, "c_an") == 0)
    {
        digitalWrite(23, 0);
    }

    if (strcmp(inhalt, "c_aus") == 0)
    {
        digitalWrite(23, 1);
    }

    if (strcmp(inhalt, "d_an") == 0)
    {
        digitalWrite(27, 0);
    }

    if (strcmp(inhalt, "d_aus") == 0)
    {
        digitalWrite(27, 1);
    }

    if (strcmp(inhalt, "e_an") == 0)
    {
        digitalWrite(24, 0);
    }

    if (strcmp(inhalt, "e_aus") == 0)
    {
        digitalWrite(24, 1);
    }

    if (strcmp(inhalt, "f_an") == 0)
    {
        digitalWrite(28, 0);
    }

    if (strcmp(inhalt, "f_aus") == 0)
    {
        digitalWrite(28, 1);
    }

    if (strcmp(inhalt, "g_an") == 0)
    {
        digitalWrite(29, 0);
    }

    if (strcmp(inhalt, "g_aus") == 0)
    {
        digitalWrite(29, 1);
    }

    if (strcmp(inhalt, "h_an") == 0)
    {
        digitalWrite(25, 0);
    }

    if (strcmp(inhalt, "h_aus") == 0)
    {
        digitalWrite(25, 1);
    }
}

int main()
{
    int rcvSocket;
    char buffer[BufferSize];
    struct sockaddr_in servaddr, cliaddr;

    wiringPiSetup();     // Setup the library
    pinMode(21, OUTPUT); // Channel A
    pinMode(22, OUTPUT); // Channel B
    pinMode(23, OUTPUT); // Channel C
    pinMode(27, OUTPUT); // Channel D
    pinMode(24, OUTPUT); // Channel E
    pinMode(28, OUTPUT); // Channel F
    pinMode(29, OUTPUT); // Channel G
    pinMode(25, OUTPUT); // Channel H

    if ((rcvSocket = socket(AF_INET, SOCK_DGRAM, 0)) < 0)
    {
        perror("socket creation failed");
        exit(EXIT_FAILURE);
    }

    memset(&servaddr, 0, sizeof(servaddr));
    memset(&cliaddr, 0, sizeof(cliaddr));

    servaddr.sin_family = AF_INET; // IPv4
    servaddr.sin_addr.s_addr = INADDR_ANY;
    servaddr.sin_port = htons(PORT);

    if (bind(rcvSocket, (const struct sockaddr *)&servaddr,
             sizeof(servaddr)) < 0)
    {
        perror("bind failed");
        exit(EXIT_FAILURE);
    }

    int len, n;

    len = sizeof(cliaddr);

    //	n = recvfrom(rcvSocket, (char *)buffer, BufferSize, MSG_WAITALL, ( struct sockaddr *) (socklen_t*)&cliaddr, (socklen_t*)&len);

    while (1)
    {
        n = recv(rcvSocket, buffer, BufferSize, MSG_WAITALL);
        buffer[n] = '\0';

        auswerten(buffer);
    }

    return 0;
}

//	sendto(rcvSocket, (const char *)hello, strlen(hello), MSG_CONFIRM, (const struct sockaddr *) &cliaddr, len);
//	printf("Hello message sent.\n");
