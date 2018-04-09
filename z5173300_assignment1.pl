% Program:  Assignment 1 - Prolog Programming
% Source:   Prolog
%
% Name: Shiwei Sun
% Student Number: z5173300

% Q1 go through each element in the list if the value is less than 0 then compute the square value of it

sumsq_neg([],0).        %base case
sumsq_neg([Head|Tail],Sum) :-   % case where the value < 0 
    sumsq_neg(Tail, Sum1), 
    (Head < 0 ->
    Sum is Sum1 + (Head * Head)).       % sum = sum + value^2
sumsq_neg([Head|Tail],Sum) :-   % case where the value > 0
    sumsq_neg(Tail, Sum1), 
    (Head > 0 ->
    Sum = Sum1).            %do nothing
    
% Q2 given 2 list name list and fruit list, 
% see if each name like all fruit in the fruit list, return false if any case failed

all_like_all([],_).             % An empty list likes anything
all_like_all([FirstPeople|RestPeople],Fruit) :-  % list go through all name in the name list
    forall(member(A,Fruit),likes(FirstPeople,A)),  % compare with the fact that whether the name like all member in Fruit list
    all_like_all(RestPeople,Fruit).     % continue this for the rest of names
    
% Q3 compute a list in form [N, ... ,M] then for each element compute its sqrt in from[Element,sqrt(Element)]

sqrt_table(N,M,Result):-
    N>=M,
    mn_span(M,N,Out),
    maplist(sqrt_of_I, Out, Result).
range(H,_,H).
range(Out,L,H):-
    NewH is H-1,NewH>=L,
    range(Out,L,NewH).
    
mn_span(L,H,Out):-
        findall(X,range(X,L,H),Out).  % compute a list in form [N, ... ,M]
sqrt_of_I(I, [I,Root]):- 
    Root is sqrt(I).

% Q4  Read a list recursively and for each chunk of numbers, remove the number in between and append to the answer, 

% There are 3 cases, 1. the second number is first number + 1, 
                %    2. the second number is greater than first number+1
                %    3. the second number is smaller than first number.
getlast([Last],Last).
getlast([_|Tail],Last):-
    getlast(Tail,Last).
returnfirst_last([],[]).
returnfirst_last([First],First).
returnfirst_last([First,Last],[First,Last]).
returnfirst_last([First|Mid],[First,Last]):-
    getlast(Mid,Last).

chop_up([],_).
chop_up(List,Result):-
    chop_up_case(List,[],[],Result).
    
chop_up_case([First,Second],Temp,ResultTemp,Result):-             % base case       Case 2
    Second > First+1,
    append(Temp,[First],Temp1),
    returnfirst_last(Temp1,Remaining),
    append(ResultTemp,[Remaining,Second],Result).
chop_up_case([First,Second|Tail],Temp,ResultTemp,Result):-           % recursive
    Second > First+1,
    append(Temp,[First],Temp1),
    returnfirst_last(Temp1,Remaining),
    append(ResultTemp,[Remaining],ResultTemp1),
    chop_up_case([Second|Tail],[],ResultTemp1,Result).

chop_up_case([First,Second],Temp,ResultTemp,Result):-             % base case       Case 3
    Second =< First,
    append(Temp,[First],Temp1),
    returnfirst_last(Temp1,Remaining),
    append(ResultTemp,[Remaining,Second],Result).
chop_up_case([First,Second|Tail],Temp,ResultTemp,Result):-           % recursive
    Second =< First,
    append(Temp,[First],Temp1),
    returnfirst_last(Temp1,Remaining),
    append(ResultTemp,[Remaining],ResultTemp1),
    chop_up_case([Second|Tail],[],ResultTemp1,Result).

chop_up_case([First,Second],Temp,ResultTemp,Result):-            % base case        Case 1
    Second is First+1,
    append(Temp,[First,Second],LTO),
    returnfirst_last(LTO,Removed),
    append(ResultTemp,[Removed],Result).
chop_up_case([First,Second|Tail],Temp,ResultTemp,Result):-       % recursive
    Second is First+1,
    append(Temp,[First],LTO),
    chop_up_case([Second|Tail],LTO,ResultTemp,Result).
    

% Q5 define the tree fact, and then define tree_eval,  there are two base case for tree_eval

%   one is single tree leaf with 'z', the Eval for this leaf will be equal to Value
%   the other one is leaf with a number, Eval for this leaf is the number itself.
%   then define recursively tree left and right similar to the one on lecture note, tree_size.
%   4 predicate for 4 different operator. 
tree(_,_,_).
tree(empty, z, empty).
tree(empty, _, empty).
tree_eval(_,empty,0).
tree_eval(Value, tree(empty,Node,empty), Eval) :- 
    Node=z,
    Eval = Value. 
tree_eval(_, tree(empty,Node,empty), Eval) :- 
    number(Node), 
    Eval = Node.
tree_eval(Value, tree(L,Op,R), Eval) :- 
    tree_eval(Value, L, LeftResult), 
    tree_eval(Value, R, RightResult),
    Op = '+',
    Eval is LeftResult + RightResult.
tree_eval(Value, tree(L,Op,R), Eval) :- 
    tree_eval(Value, L, LeftResult), 
    tree_eval(Value, R, RightResult),
    Op = '-',
    Eval is LeftResult - RightResult.
tree_eval(Value, tree(L,Op,R), Eval) :- 
    tree_eval(Value, L, LeftResult), 
    tree_eval(Value, R, RightResult),
    Op = '*',
    Eval is LeftResult * RightResult.
tree_eval(Value, tree(L,Op,R), Eval) :- 
    tree_eval(Value, L, LeftResult), 
    tree_eval(Value, R, RightResult),
    Op = '/',
    Eval is LeftResult / RightResult.
