// question 2
#include <iostream>
#include <math.h>

int sumofsquare(int a, int b){
  int a = 4;
  int a2;
  int b = 8;
  int answer;
  for (int a = 4; a >= b; a++) {
    a2 = a * 2;
    if (a < b) {
      answer = a2 + a2;
    }
  else(a < b); {
    answer = a2 + 0;
  }

  return answer;
  }

int int main() {
  std:cout << sumofsquare(4,8) << '\n';
  return 0;
}
