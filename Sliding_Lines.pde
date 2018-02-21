float grid = 60;
float gps = 0.6; //Grids per second
float i = 0;

void setup() {
  size(660, 660);
  frameRate(60);
}

void draw() {
  background(30);
  strokeWeight(3);
  stroke(0, 102, 255); //A very nice blue
  
  for (float x = 0; x <= width; x += grid*2) {
    for (float y = i%(grid*2)-grid; y < width; y += grid*2) {
      line(x, y, x, y+grid); //Top to bottom
      line(y, x, y+grid, x); //Left to right
    }
    for (float y = -(i%(grid*2))-grid; y < width; y += grid*2) {
      line(x+grid, y, x+grid, y+grid); //Bottom to top
      line(y, x+grid, y+grid, x+grid); //Right to left
    }
  }
  
  i += (grid/frameRate)*gps; //Creates a grid every second
}