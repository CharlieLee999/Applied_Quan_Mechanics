#include <stdio.h>
#include <stdlib.h>

int main()
{
    int i, j, n;
    printf("Please input the number of terms of Hermite polynomials (n>2):\n");
	scanf("%d",&n);
    // Static size of 2d array
    
    // Initialize the coeff matrix
    int coeff[20][20] = {{0}};
    coeff[0][0] = 1;
    coeff[1][1] = 2;
/*    printf("Coeff [] is %d\n", coeff[1][1]);*/
    
    // Calculate other coeffs
    for(i = 2; i<n; i++)
    {
        coeff[i][0] = -2 * (i-1) * coeff[i-2][0];
        for (j = 1; j<n; j++)
        {
            coeff[i][j] = 2 * coeff[i-1][j-1] - 2 * (i-1) * coeff[i-2][j];
        }
    }
    
    // Print all coeffs out, the lower order term is in front to higher one
    for (i = 0; i<n; i++)
    {
        printf("Coeff[");
        printf("%d", i);
        printf("][:] is \n");
        for(j = 0; j<n; j++)
        {
            printf("%d \t", coeff[i][j]);
        }
        printf("\n");
    }
}
