#include<stdio.h>
#include<string.h>
char* coffee2Code(char* sentence);
int main(){
	/* Enter "Coffee" then see the Miracle! */
	char oldS[255];
	printf("Enter String : ");
	
	// get string from stdin (keyboard)
	fgets(oldS, 255, stdin); 
	
	// convert "Coffee" to "Code" !!
	char* newS = coffee2Code(oldS);
  
  	// print result
	printf("Result : ");
	puts(newS);
	return 0;
}
char* coffee2Code(char* sentence){
	char* result;
	int i = 0;
	while (*sentence) {
		
		// find word "Coffee"
        if (strstr(sentence, "Coffee") == sentence) {
            strcpy(&result[i], "Code"); // add "Code" instead of "Coffee"
            i += 4; // skip "Code"
            sentence += 6; // skip "Coffee"
        }
        else
            result[i++] = *sentence++;
    }
    result[i] = '\0';
	
	return result;
}
