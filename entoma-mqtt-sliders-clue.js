  var sensor;
  var value;
   
   // Accelerometer X
    var xccelerometer = document.getElementById("X-Accelerometer");
    var xvalue = document.getElementById("X-Accelerometervalue");
    xvalue.innerHTML = xccelerometer.value;
    
    xccelerometer.oninput = function() {
        xvalue.innerHTML = this.value;
        sensor = "slider/xaccelerometer";
        value = xccelerometer.value;
    }

    // 



    // Accelometer Y
    var yccelerometer = document.getElementById("Y-Accelerometer");
    var yvalue = document.getElementById("Y-Accelerometervalue");
    yvalue.innerHTML = yccelerometer.value;
    
    yccelerometer.oninput = function() {
        yvalue.innerHTML = this.value;
        sensor = "slider/yaccelerometer";
        value = yccelerometer.value;
    }

    // Accelometer Z

    var zccelerometer = document.getElementById("Z-Accelerometer");
    var zvalue = document.getElementById("Z-Accelerometervalue");
    zvalue.innerHTML = zccelerometer.value;
    
    zccelerometer.oninput = function() {
        zvalue.innerHTML = this.value;
        sensor = "slider/zccelerometer";
        value = zccelerometer.value;
    }

      //Gyroscope X
   var xgyroscope = document.getElementById("X-Gyroscope");
    var xgyroscopevalue = document.getElementById("X-Gyroscopevalue");
    xgyroscopevalue.innerHTML = xgyroscope.value;
    
    xgyroscope.oninput = function() {
        xgyroscopevalue.innerHTML = this.value;
        sensor = "slider/xgyroscope";
        value = xgyroscope.value;
    }

    // Gyroscope Y
    var ygyroscope = document.getElementById("Y-Gyroscope");
    var ygyroscopevalue = document.getElementById("Y-Gyroscopevalue");
    ygyroscopevalue.innerHTML = ygyroscope.value;
    
    ygyroscope.oninput = function() {
        ygyroscopevalue.innerHTML = this.value;
        sensor = "slider/ygyroscope";
        value = ygyroscope.value;
    }

    // Gyroscope Z

    var zgyroscope = document.getElementById("Z-Gyroscope");
    var zgyroscopevalue = document.getElementById("Z-Gyroscopevalue");
    zgyroscopevalue.innerHTML = zgyroscope.value;
    
    zgyroscope.oninput = function() {
        zgyroscopevalue.innerHTML = this.value;
        sensor = "slider/zgyroscope";
        value = zgyroscope.value;
    }

     //magnetic X
   var xmagnetic = document.getElementById("X-Magnetic");
    var xmagneticvalue = document.getElementById("X-Magneticvalue");
    xmagneticvalue.innerHTML = xmagnetic.value;
    
    xmagnetic.oninput = function() {
        xmagneticvalue.innerHTML = this.value;
        sensor = "slider/xmagnetic";
        value = xmagnetic.value;
    }

    // magnetic Y
    var ymagnetic = document.getElementById("Y-Magnetic");
    var ymagneticvalue = document.getElementById("Y-Magneticvalue");
    ymagneticvalue.innerHTML = ymagnetic.value;
    
    ymagnetic.oninput = function() {
        ymagneticvalue.innerHTML = this.value;
        sensor = "slider/ymagnetic";
        value = ymagnetic.value;
    }

    // magnetic Z

    var zmagnetic = document.getElementById("Z-Magnetic");
    var zmagneticvalue = document.getElementById("Z-Magneticvalue");
    zmagneticvalue.innerHTML = zmagnetic.value;
    
    zmagnetic.oninput = function() {
        zmagneticvalue.innerHTML = this.value;
        sensor = "slider/zmagnetic";
        value = zmagnetic.value;
    }

     // Pressure
   var pressure = document.getElementById("Pressure");
    var pressurevalue = document.getElementById("Pressurevalue");
    pressurevalue.innerHTML = pressure.value;
    
    pressure.oninput = function() {
        pressurevalue.innerHTML = this.value;
        sensor = "slider/pressure";
        value = pressure.value;
    }

     // Temperature
   var temperature = document.getElementById("Temperature");
    var temperaturevalue = document.getElementById("Temperaturevalue");
    temperaturevalue.innerHTML = temperature.value;
    
    temperature.oninput = function() {
        temperaturevalue.innerHTML = this.value;
        sensor = "slider/temperature";
        value = temperature.value;
    }

    // Humidity
    var humidity = document.getElementById("Humidity");
    var humidityvalue = document.getElementById("Humidityvalue");
    humidityvalue.innerHTML = humidity.value;
    
    humidity.oninput = function() {
        humidityvalue.innerHTML = this.value;
        sensor = "slider/humidity";
        value = humidity.value;
    }

    // red
    var red = document.getElementById("red");
    var redvalue = document.getElementById("redvalue");
    redvalue.innerHTML = red.value;
    
    red.oninput = function() {
        redvalue.innerHTML = this.value;
        sensor = "slider/red";
        value = red.value;
    }
    // green
    var green = document.getElementById("green");
    var greenvalue = document.getElementById("greenvalue");
    greenvalue.innerHTML = green.value;
    
    green.oninput = function() {
        greenvalue.innerHTML = this.value;
        sensor = "slider/green";
        value = green.value;
    }
    // blue
    var blue = document.getElementById("blue");
    var bluevalue = document.getElementById("bluevalue");
    bluevalue.innerHTML = blue.value;
    
    blue.oninput = function() {
        bluevalue.innerHTML = this.value;
        sensor = "slider/blue";
        value = blue.value;
    }

    // Proximity
    var proximity = document.getElementById("proximity");
    var proximityvalue = document.getElementById("proximityvalue");
    proximityvalue.innerHTML = proximity.value;
    
    proximity.oninput = function() {
        proximityvalue.innerHTML = this.value;
        sensor = "slider/proximity";
        value = proximity.value;
    }

    // Light Intensity
    var light = document.getElementById("light");
    var lightvalue = document.getElementById("lightvalue");
    lightvalue.innerHTML = light.value;
    
    light.oninput = function() {
        lightvalue.innerHTML = this.value;
        sensor = "slider/light";
        value = light.value;
    }


    function publishFunction() {
        console.log(sensor)
        console.log(value);
        client.publish(sensor, value)
    }