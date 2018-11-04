int pwm[] = {5, 9}; 
int dir_a = 4;  //direction control for motor outputs 1 and 2 
int dir_b = 8;  //direction control for motor outputs 3 and 4 
int ir_in_a = 2;  //IR input to calculate the speed
int ir_in_b = 3;  //IR input to calculate the speed
int up_btn[] = {6, 7};  //IR input to calculate the speed
int down_btn[] = {10,12};  //IR input to calculate the speed


int compteurTour[] = {0,0};
int minSpeed[] = {25,25};
int maxSpeed[] = {255,255};
int coefCorection[] = {1,1};
bool up[] = {false, false};
bool down[] = {false, false};
float corectionPiste[] = {1.0, 0.9};
float previousSpeed[] = {0.0, 0.0};

void countTacho(int index) {
  compteurTour[index] = compteurTour[index] + 1;
  Serial.println(compteurTour[index]);
}

void countTachoA() {
  countTacho(0);
}

void countTachoB() {
  countTacho(1);
}


void setup()
{
  pinMode(pwm[0], OUTPUT);  //Set control pins to be outputs
  pinMode(pwm[1], OUTPUT);
  pinMode(dir_a, OUTPUT);
  pinMode(dir_b, OUTPUT);

  
  pinMode(ir_in_a, INPUT);
  pinMode(ir_in_b, INPUT);
  
  pinMode(up_btn[0], INPUT);
  pinMode(up_btn[1], INPUT);
  pinMode(down_btn[0], INPUT);
  pinMode(down_btn[1], INPUT);
  
  analogWrite(pwm[0], 0);  //set both motors to run at (0/255 = 0)% duty cycle (slow)
  analogWrite(pwm[1], 0);

  attachInterrupt(digitalPinToInterrupt(ir_in_a), countTachoA, RISING);
  attachInterrupt(digitalPinToInterrupt(ir_in_b), countTachoB, RISING);

  Serial.begin(9600);
  
}

int getCompteur(int index) {
  int result = compteurTour[index];
  if (compteurTour[index] < 0) {
    result = result * -1 ;
  }
  if (result > maxSpeed[index]) {
    result = maxSpeed[index];
  }
  
  //Serial.println("getCompteur >>");
  //Serial.println(result);
  return result;
}


void runMotor(int index, int value) {
  
  //Serial.println("runMotor >>");
  //Serial.println("val : " + value);
  float actualSpeed = 0.0;
  
  if (value != 0) {

    int range = maxSpeed[index] - minSpeed[index];
    float maxCount;
    if (coefCorection[index] < 0) {
      maxCount = range * coefCorection[index] * -1;
    } else if (coefCorection[index] > 0) {
      maxCount = range / coefCorection[index];
    } else {
      maxCount = 0;
    }
    
    actualSpeed = corectionPiste[index] * value * range / maxCount ;
    if (previousSpeed[index] == 0) {
      actualSpeed = actualSpeed * 2;
    }
    //Serial.println(actualSpeed);
    
  } else {
    if (previousSpeed[index] > minSpeed[index]) {
      actualSpeed = max(previousSpeed[index] / 2, minSpeed[index]);
    }
  }
  analogWrite(pwm[index], (int) actualSpeed);
  previousSpeed[index] = actualSpeed;

}

void manageButton(int button, int index, bool isUp) {
  
  int state = digitalRead(button);
  
  if(digitalRead(button) == HIGH) {
    int val = coefCorection[index];
    if (isUp) {
      if (!up[index]) {
        val = val + 1;
        Serial.println("button up " + index);
        Serial.println(index);
        Serial.println(val);
        up[index] = true;
      }
    } else {
      if (!down[index]) {
        val = val - 1;
        Serial.println("button down " + index);
        Serial.println(index);
        Serial.println(val);
        down[index] = true;
      }
    }
    coefCorection[index] = val;
  } else {
    if (isUp) {
      up[index] = false;
    } else {
      down[index] = false;
    }
  }
}

void loop()
{
  digitalWrite(dir_a, LOW);
  digitalWrite(dir_b, LOW);
  
  compteurTour[0] = 0;
  Serial.println("A-" + compteurTour[0]);
  compteurTour[1] = 0;
  Serial.println("B-" + compteurTour[1]);
  
  for (int i = 0; i < 100; i++) {
    manageButton(up_btn[0], 0, true);
    manageButton(up_btn[1], 1, true);
    manageButton(down_btn[0], 0, false);
    manageButton(down_btn[1], 1, false);
    delay(10);
  }
  

  runMotor(0, getCompteur(0));
  runMotor(1, getCompteur(1));

 
}
