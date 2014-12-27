### README ###


### Account Voucher Credit Transfer Payment for Odoo/OpenERP ###

* This module is a technical dependency to Account_Voucher_ Sepa

### Main Improvments ###

* Combines an Electronic Template File transfer to a Bank. 

### Requirements ###

* You need to set up some things before using it:
	- A credit transfer config link a bank with a parser
	- A credit transfer parser link a parser with a template that you can upload

### Exemples ###

* These banks are set to be used with OpenERP / Odoo:

 Nom banque           	| Bic         	| Paramétré OPEN 	|                                                 	|
----------------------	|-------------	|----------------	|-------------------------------------------------	|
 SG PARIS XV          	| SOGEFRPPBLG 	| OK             	| pain 001.001.02 et pain 001.001.03              	|
 CA                   	| AGRIFRPP836 	| OK             	|                                                 	|
 CCM                  	| CMBRFR2BARK 	| OK             	| PAIN.000.001.03.xsd                             	|
 CIC POITIERS         	| CMCIFRPP    	| OK             	| PAIN.000.001.03.xsd                             	|
 Credit coopératif    	| CCOPFRPPXXX 	| OK             	| PAIN.001.001.02.sct.vsc PAIN.001.001.03.sct.vs3 	|
 CIC PARIS            	| CMCIFRPP    	| OK             	| PAIN.001.001.02.sct                             	|
 CE MONTEPELLIER      	| CEPAFRPP348 	| OK             	| pain.001.001.02.sct                             	|
 CE BASSE NORMANDIE   	| CEPAFRPP142 	| OK             	| PAIN.001.001.03.xsd                             	|
 CIC NORD OUEST       	| CMCIFRPP    	| OK             	| PAIN.001.001.02.xsd                             	|
 CREDIT MUTUEL        	| CMCIFR2A    	| OK             	| PAIN.001.001.03.xsd                             	|
 SG REIMS             	| SOGEFRPP    	| OK             	| PAIN.000.001.03.xsd                             	|
 BANQUE MARTIN MAUREL 	| BMMMFR2A    	| OK             	| PAIN.001.001.02.sct                             	|
 SG PARIS XV          	| SOGEFRPP    	| OK             	| pain 001.001.02 et pain 001.001.03              	|
 BFCC TOULOUSE        	| CCOPFRPPXXX 	| ok             	| PAIN.001.001.02.sct.vsc PAIN.001.001.03.sct.vs3 	|
 SG                   	| SOGEFRPP    	| OK             	| pain 001.001.02 et pain 001.001.03              	|
 LCL                  	| CRLYFRPPXXX 	| OK             	| pain 001.001.03                                 	|

