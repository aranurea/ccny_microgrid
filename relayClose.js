var b = require('bonescript');

var relay;

for (var i = 2; i < process.argv.length; i++)
{
	relayNumber = process.argv[i];

	if(relayNumber < 1 || relayNumber > 4)
	{
		throw "Invalid relay number";
	}

	relay = "P8_" + (4*relayNumber + 30);

	b.pinMode(relay, 'out');
	b.digitalWrite(relay, 1);
}
