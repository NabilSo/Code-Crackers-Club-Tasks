#include <stdio.h>
#include <stdlib.h>


int main()
{
	int x,n,j = 0;
	int test;
	int inserted = 0;
	int money_available[5][2]={{1,5},{2,7},{5,10},{10,41},{20,10}};
	int *coins = (int *)malloc(1 * sizeof(int));
	int pos=0;
	
	int size = sizeof(money_available)/sizeof(money_available[0]);
	printf("available money : ");
	for (int i = 0; i < 5; i++) {
        printf("[%d, %d] ", money_available[i][0], money_available[i][1]);
    }
	printf("\n");
	printf("Number of Tram tickets : ");
	scanf("%d",&n);
	
	int price = n*6;
	
	printf("Insert %d dirhams : ", price);
	
	while(inserted < price){
		scanf("%d",&x);
		test = 0;
		for(int i=0; i < size ;i+=1){
			if(x == money_available[i][0]){
				money_available[i][1]++;
				inserted += x;
				test = 1;
				coins = (int *)realloc(coins, (pos + 1) * sizeof(int));
				coins[pos]=x;
				pos++;
				break;
			}
		}
		if(!test){
			printf("Invalid money inserted ");
		}
	}

	int change = inserted - price;
	j = change;
	
	pos = 0;

	for(int i=size-1;i>=0;i--){
		while(j>=money_available[i][0] && money_available[i][1] > 0){
			coins = (int *)realloc(coins, (pos + 1) * sizeof(int));
			coins[pos]=money_available[i][0];
			pos++;
			j -=money_available[i][0];
			money_available[i][1]--;
		}
	}

	if(j!=0){
		printf("Not enough change to give");
	}else{
		printf("change to give : ");
		for(int i=0;i<pos;i++){
			printf("%d DH ",coins[i]);
		}
	}

	printf("\n");
	printf("Updated money in machine: ");
    for (int i = 0; i < 5; i++) {
        printf("[%d, %d] ", money_available[i][0], money_available[i][1]);
    }
	free(coins);
	return 0;
}