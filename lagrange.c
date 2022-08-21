#include <stdio.h>
#define n 3                         // Lagrange,数字为输入点个数
main()                               
{
    float x, x_[n], y_[n]; int k, j; float t, y;
    printf("\nPlease enter x_: ");     
    for(k=0;k<=n-1;k++)              
    scanf_s("%f",&x_[k]);
        printf("\nPlease enter y_:");
        for (k = 0; k <= n-1; k++)
            scanf_s("%f", &y_[k]);
          printf("\nPlease enter x");
          scanf_s("%f", &x);
        for (k = 0,y=0; k <= n-1; k++)
        {
            for (j = 0,t=1; j <= n-1; j++)
            {
                if (j == k) continue;
                t = t * (x - x_[j]) / (x_[k] - x_[j]); 
            y = y + t * y_[k];
        }    
    printf("x为%f时，y为%f",x,y);
} 