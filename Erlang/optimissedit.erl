-module(optimissedit).
-export([coffee_to_code/0]).

% Initial Function to create the Coffee str
coffee_to_code() ->
	Coffee = "Coffee",
	io:format("~n~p ->", [Coffee]),
	coffee_to_code(Coffee).
	
% Split	coffee into substrings
coffee_to_code(C) ->
	Head = string:substr(C,1,2),
	Len = string:length(C),
	Tail = string:substr(C, Len - 1, 1),
	coffee_to_code(Head, Tail).
	
% Recombine substrings with a new character in the middle
coffee_to_code(H, T) ->
	Half = string:concat(H, "d"),
	Full = string:concat(Half, T),
	io:format("~n~p\n", [Full]).
	