var b = require('bonescript');

var load1 = "P8_34";
var load2 = "P8_38";
var load3 = "P8_42";
var load4 = "P8_46";


b.pinMode(load1,'out');
b.pinMode(load2,'out');
b.pinMode(load3,'out');
b.pinMode(load4,'out');

b.digitalWrite(load1,0);
b.digitalWrite(load2,0);
b.digitalWrite(load3,0);
b.digitalWrite(load4,0);

console.log('Relays initialized.');
