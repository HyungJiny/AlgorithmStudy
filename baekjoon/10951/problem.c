#include <stdio.h>

int main(){
	int input1, input2, result;
	while(scanf("%d %d", &input1, &input2) == 2){
		result = input1 + input2;
		printf("%d\n", result);
	}
	return 0;
}
