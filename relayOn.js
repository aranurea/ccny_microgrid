var b = require('bonescript');

if(process.argv.length != 3)
{
	throw "Invalid number of arguments";
}

relayNumber = process.argv[2];

if(relayNumber < 1 || relayNumber > 4)
{
	throw "Invalid relay number";
}

var relay = "P8_" + (4*relayNumber + 30);

b.pinMode(relay, 'out');
b.digitalWrite(relay, 0);

