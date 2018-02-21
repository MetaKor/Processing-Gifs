color light = color(66, 157, 255, 127);
color mid = color(0, 123, 255, 127);
color dark = color(30);
float big = 25;
float i = 0;

void setup() {
  size(400, 400);
  frameRate(60);
};

void draw() {
    background(30);
    setSetSet((200%(big*2*sqrt(3)))-big*2*sqrt(3), sin(i));
    i += 0.03;
};

void cube(float X, float Y) {
    fill(light);
    stroke(light);
    noStroke(); //Remove this is removing transparency
    quad(X, Y, X-(big*sqrt(3)/2), Y-(big/2), X, Y-big, X+(big*sqrt(3)/2), Y-(big/2));
    fill(mid);
    stroke(mid);
    noStroke(); //Same deal
    quad(X, Y, X, Y+big, X-(big*sqrt(3)/2), Y+(big/2), X-(big*sqrt(3)/2), Y-(big/2));
    fill(dark);
    noStroke();
    quad(X, Y, X, Y+big, X+(big*sqrt(3)/2), Y+(big/2), X+(big*sqrt(3)/2), Y-(big/2));
};

void cubeSet(float X, float Y, float len) {
    cube(X-((len*big)*sqrt(3)/2), Y-(big/2));
    cube(X-(big*sqrt(3)/2), Y+((len*big)/2));
    cube(X+(big*sqrt(3)/2), Y-((len*big)/2));
    cube(X+((len*big)*sqrt(3)/2), Y+(big/2));
};

void setSet(float X, float len) {
    for (float f = ((width/2)%big)-big*3/2; f < width+(big*2); f += big*2) {
        cubeSet(X, f, len);
    }
};

void setSetSet(float X, float len) {
    for (float e = X; e < width+(big*2*sqrt(3)); e += big*2*sqrt(3)) {
        setSet(e, len);
    }
};