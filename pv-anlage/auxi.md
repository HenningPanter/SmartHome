5010	MPPT 1 Voltage	MPPT1 Spannung	        V	uint16be	1	0.1
5011	MPPT 1 Current	MPPT1 Strom	            A	uint16be	1	0.1
5012	MPPT 2 Voltage	MPPT2 Spannung	        V	uint16be	1	0.1
5013	MPPT 2 Current	MPPT2 Strom	            A	uint16be	1	0.1
5016	Total DC Power	PV-Leistung aktuell	    W	uint32sw	2	1
5018	Spannung Ph A	Spannung Phase A	    V	uint16be	1	0.1
5019	Spannung Ph B	Spannung Phase C	    V	uint16be	1	0.1
5020	Spannung Ph C	Spannung Phase C	    V	uint16be	1	0.1


12999	System State	Systemstatus		                                            uint16be	1	1	
13000	Running State	Betriebsstatus		                                            uint16be	1	1	

13001	Daily PV Generation	PV-Stromerzeugung heute	                                Kwh	uint16be	1	0.1	


13007	Load power	Wirkleistung gesamt	                                            W	int32sw	    2	1	

13009	Export power	Aktuelle Leistung am Übergabepunkt des Versorgungsnetzes	W	int32sw	    2	1	

13011	Daily battery charge energy from PV	Energie in Speicher heute	            Kwh	uint16be	1	0.1
13016	Daily direct Energy Consumption	Direkter Eigenverbrauch aus PV heute	    Kwh	uint16be	1	0.1	
13017	Total direct Energy Consumption	Direkter Eigenverbrauch aus PV gesamt	    Kwh	uint32sw	2	0.1	

13019	Battery voltage	Batteriespannung	                                        V	uint16be	1	0.1	
13020	Battery current	Batteriestrom	                                            A	uint16be	1	0.1	
13021	Battery power	Batterieladeleistung	                                    W	uint16be	1	1	
13022	Battery level	Batteriekapazität	                                        %	uint16be	1	0.1	
13023	Battery state of health	Gesundheit der Batterie	                            %	uint16be	1	0.1	
13024	Battery Temperature	Batterietemperatur	                                    °C	int16be	    1	0.1	
13025	Daily battery discharge Energy	Tägliche Entladungsenergie der Batterie	    Kwh	uint16be	1	0.1	
13026	Total battery discharge Energy	Gesamte Entladungsenergie der Batterie	    Kwh	uint32sw	2	0.1	
13028	Self-consumption of today	Heutiger Anteil des Eigenverbrauches	        %	uint16be	1	0.1	
13029	Grid state	Netzstatus		                                                    int16be	    1	0.1	
13030	Phase A current	Strom Phase A aktuell	                                    A	uint16be	1	0.1	
13031	Phase B current	Strom Phase B aktuell	                                    A	uint16be	1	0.1	
13032	Phase C current	Strom Phase C aktuell	                                    A	uint16be	1	0.1	
13033	Total active power	Eigenverbrauch aktuell	                                W	int32sw	    2	1	


13038	Battery Capacity	Batterie-Kapazität	                                    Kwh	uint16be	1	0.1
13039	Daily Charge Energy	Batterie-Ladeenergie heute	                            Kwh	uint16be	1	0.1

13044	Daily export energy	Energie Netzeinspeisung heute	                        Kwh	uint16be	1	0.1


Fehler:

13049	Inverter alarm	Inverter alarm		uint32sw	2	1	0		value		false	false
13051	Grid-side fault	Netzfehler		uint32sw	2	1	0		value		false	false
13053	System fault 1	System Fehler 1		uint32sw	2	1	0		value		false	false
13055	System fault 2	System Fehler 2		uint32sw	2	1	0		value		false	false
13057	DC-side fault	Fehler DC-Seitig		uint32sw	2	1	0		value		false	false
13059	Permanent fault	Permanenter Fehler		uint32sw	2	1	0		value		false	false
13061	BDC-side fault	BDC-side fault		uint32sw	2	1	0		value		false	false
13063	BDC-side permanent fault	BDC-side permanent fault		uint32sw	2	1	0		value		false	false
13065	Battery fault	Batterie Fehler		uint32sw	2	1	0		value		false	false
13067	Battery alarm	Battery Alarm		uint32sw	2	1	0		value		false	false
13069	BMS alarm	BMS Alarm		uint32sw	2	1	0		value		false	false
13071	BMS protection	BMS protection		uint32sw	2	1	0		value		false	false
13073	BMS fault 1	BMS fault 1		uint32sw	2	1	0		value		false	false
13075	BMS fault 2	BMS fault 2		uint32sw	2	1	0		value		false	false
13077	BMS alarm 2	BMS alarm 2		uint32sw	2	1	0		value		false	false