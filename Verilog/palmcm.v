module main;
  reg [47:0] coffee = "Coffee";
  initial 
    begin
      coffee[8] = 0;
      coffee = {coffee[47:32], coffee[15:0]};
      $display("%s", coffee);
      $finish ;
    end
endmodule