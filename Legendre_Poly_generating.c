// Legendre polynomials calculating function
// Author: Charlie 

#include <stdio.h>
#include <stdlib.h>

int main(int argc, char* argv[])
{
    int max_poly = atoi(argv[1]);
    int i, j;
    int num_coeff = (max_poly + 1) * max_poly;
    double *poly = (double *) malloc(num_coeff * sizeof(double));
    
    //**** Initialization ****
    poly[0] = 1.0;
    poly[1] = 0.0;
    poly[2] = 1.0;
    
    for(i = 3; i < num_coeff; i++)
    {
        poly[i] = 0;
    }
    
    
    //****  Calculate each coefficient with given iteration relationship
    
    for (i = 2; i< max_poly; i++)
    {
        //Add coefficients of the last polynomial
        for(j = i*(i+1)/2+1; j < (i+1)*(i+2)/2; j++)
        {
            poly[j] = (2 * i - 1) * poly[j-i-1] / i; 
/*            printf("poly[%d] is %g\n", j, poly[j]);*/
        }
        
        // Add coefficients of the second last polynomials
        // To get the real current coefficients
        for(j = i*(i+1)/2; j<(i+1)*(i+2)/2 - 2; j++)
        {
            poly[j] = -(i - 1) * poly[j-2*i + 1] /i + poly[j]; 
/*            printf("poly[%d] is %g\n", j, poly[j]);   */
        }
    } 
    
    //****   Print all coefficients   ***
    for(i = 0; i < max_poly; i++)
    {
        printf("P[%d] is : \n", i);
        for(j = i*(i+1)/2; j <= (i+1)*(i+2)/2-1; j++)
        {
            printf("%g \t", poly[j]);
        }
        printf("\n\n");
    }
}
