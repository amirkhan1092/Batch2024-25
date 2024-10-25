#include <stdio.h>

int main() {
    int C, N, D;
    
    // Reading the values of C, N, and D
    scanf("%d %d %d", &C, &N, &D);
    
    // Calculate total chocolates at the end of N days
    int total_chocolates = C + (D * N) - N;
    
    // Output the result
    printf("%d\n", total_chocolates);
    
    return 0;
}
