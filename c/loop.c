#include <unistd.h>

int main(void) {
    long int i = 1000000000;
    for (int j = 0; j < i; j++) {
        i--;
    }
    return 0;
}