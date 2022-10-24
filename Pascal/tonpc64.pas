program CoffeeToCode;

uses
 cthreads,
 Classes, SysUtils;

var
    coffee, code : string;

begin
  coffee := 'coffee';
  code := StringReplace(coffee, 'ffee', 'de', [rfReplaceAll]);
  writeln(code);
end.
