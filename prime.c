
int main() {
    int i, j;

    // Loop through numbers from 2 to 100
    for (i = 2; i <= 100; i++) {
        j = 2;
        
        // Check if the current number is divisible by any number less than itself
        while (j < i) {
            if (i % j == 0) {
                break; // Not a prime number
            }
            j++;
        }

        // If the loop completes and no divisors are found, j will equal i
        if (j == i) {
            printf("%d ", i); // It's a prime number
        }
    }

    return 0;
}
