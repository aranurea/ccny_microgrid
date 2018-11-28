var b = require('bonescript');
var relay = "P8_13";

b.pinMode(relay,'out');
b.digitalWrite(relay,0);
console.log('Relay initialized.');
