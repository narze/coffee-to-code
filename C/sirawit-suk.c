//Run code on website: https://onlinegdb.com/G56njUUFt

#include <stdio.h>
#include <string.h> //for strlen() and strcmp()

int main(){
	
	
	
	while(1){
		char input[100];
		int i,j;
		printf("Enter word \"Coffee\" : ");
		scanf("%s",input);

		//Check if input equal to "Coffee"
		if(strcmp(input,"Coffee") == 0){ 
			//Create buffer result for display
			char result[100];
			
			// Cut the same character out
			for(i=0; i<strlen(input); i++){
				int found = 0; // renew found state to 0 every new character of input
				
				//Init the first character 
				if(strlen(result) == 0){
					result[0] = input[i];
				}else{
					//Check every character in result
					for(j=0; j<strlen(result); j++){
						//If found the same character.. break
						if(input[i] == result[j]){
							found = 1;
							break;
						}
					}
					//If Check every character and not found the same character
					if(found == 0){
						//Append new character to result
						result[strlen(result)] = input[i];
					}
				}
			}
			// After this will get "Cofe"
			
			// Change 'f' -> 'd' 
			for(i=0; i<strlen(result); i++){
				if(result[i] == 'f'){
					result[i] = 'd';
					//break;
				}
			}
			// After this will get "Code"
			printf("%s\n",result);
			break;
			
		}else{
			printf("Umm... Try Again!\n\n");
		}	
	}
	
	return 0;
}

