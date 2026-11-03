Bekreftelse på nådd posissjon

Sende steg for steg

Implimentere punkt over målet



Drive mode sette opp 10



Profile velocity 112

***Velocity-based Profile		Values		Description***

Unit				0.229		\[rev/min]	Sets velocity of the Profile

Range				0 \~ 32767	'0' represents an infinite velocity





profile Acceleration 108

***Velocity-based Profile		Values			Description***

Unit				214.577 \[rev/min2]	Sets acceleration of the Profile

Range				0 \~ 32767		'0' represents an infinitte Acceleration





***Condition				Types of Profile***

VPRFL(112) = 0				Profile not used(Step Instruction)

(VPRFL(112) ≠ 0) \& (APRF(108) = 0)	Rectangular Profile

(VPRFL(112) ≠ 0) \& (APRF(108) ≠ 0)	Trapezoidal Profile



&#x20;

***Lytt:*** Present Current(126) <? 2.1A 

&#x09;2.69mA per steg, kansje noe 16 bit konvertering for netativ retning

