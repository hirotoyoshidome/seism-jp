#include<stdio.h>
#include <stdlib.h>

#define N 256

// gcc -o index index.c

int main(void) {
  printf("HelloWorld!\n");

  FILE *fp;
  char filename[] = "./sample.txt";
//   int chr;
  char str[N];

  fp = fopen(filename, "r");
  if (fp == NULL) {
    printf("%s is opening error.\n", filename);
	return -1;
  } else {
    printf("%s is opened\n", filename);
  }

//   while((chr = fgetc(fp)) != EOF) {
//     putchar(chr);
//   }

  while(fgets(str, N, fp) != NULL) {
      printf("%s", str);
  }

  printf("%d\n", N);


  fclose(fp);

  return 0;
}
