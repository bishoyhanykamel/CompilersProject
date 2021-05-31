import scanner as sc
code = """int x; 
if x > 0 then {don’t compute if x <= 0 }
fact := 1;
repeat 
fact:= fact * x;
x := x –1; 
until x = 0 write fact; end"""
my_scanner = sc.Scanner()

my_scanner.scan(code)
my_scanner.output()
my_scanner.print_output()