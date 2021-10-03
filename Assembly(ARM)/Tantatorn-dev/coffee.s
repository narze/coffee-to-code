//
// Assembler program to convert coffee to code 
// to stdout.
//
//
.global _start             // Provide program starting address to linker
.align 2

// Setup the parameters 

_start: mov x3, #0
	adr x1, coffee // store coffee in a register
	adr x1, code // replace coffee with code

// print out the result
 	mov x0, #1     // 1 = StdOut
        mov x2, #6     // length of our string
        mov X16, #4     // MacOS write system call
        svc 0     // Call to output the string
	cmp x3, #9  //
	add x3, x3, #1   //

// Setup the parameters to exit the program

        mov     X0, #0      // Use 0 return code
        mov     X16, #1     // Service command code 1 terminates this program
        svc     0           // Call MacOS to terminate the program

coffee:      .ascii  "Coffee\n"
code:      .ascii  "Code\n"