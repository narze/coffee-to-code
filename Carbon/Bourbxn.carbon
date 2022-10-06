//--------------------//
//   Coffee to Code   //
//--------------------//

package ExplorerTest api;

fn Coffee_To_Code(my_favorite_things: String) -> String {
  if(my_favorite_things=="Coffee"){
    return "Code";
  }
  else{
    return my_favorite_things;
  }
}

fn Main() -> i32 {
  var my_favorite_things: String = "Coffee";
  Print(Coffee_To_Code(my_favorite_things));
  return 0;
}

//-----------------------------------------------//
//   My favorite things is coffee with code :)   //
//               Made by Bourbxn                 //
//-----------------------------------------------//
