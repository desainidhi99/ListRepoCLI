# ListRepoCLI
These tool helps to Lists the number of repositories based on their popularity i.e No of stars/forks/PR
It is a command line tool which takes 2 parameters. First Parameter is "Organization Name " and Second is "No of records" needed to display in o/p console window.


For Eg :- 
Command - ListRepoCLI twitter 10 ---> should give user statistics for Top 10 repositories based on below criteria :-
1. No of Fork Counts
2. No of Stars
3. No of Pull Requests
4. PR contribution i.e PRCount/ForkCount

Tool also considers pagination and hence "all the records" are requested.
