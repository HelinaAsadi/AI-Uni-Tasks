% DATA BASE
%
% tyre( 5 types)
%
% weather( dry , wet)
%
% rain( light , heavy).
%
% temperature( cool , hot)
%
% grip( good , bad).


% HELPERS

dry_tyre( hard ).
dry_tyre( medium ).
dry_tyre( soft ).
medium_tyre( medium ).


light_rain( light ).
heavy_rain( heavy ).

cool_temp(cool).
hot_temp(hot).

zero_pits(zero).
one_pits(one).
two_pits(two).



% KNOWLEDGE BASE

% % % % %  for wet weather
weather(wet) :-
    write('Is it light or heavy rain? '),
    read(RAIN),
    write('Current tyre?'),
    read(TYRE),
    (
        dry_tyre(TYRE) ->

        (
            light_rain(RAIN) -> write('BOX and change to INTERMEDIATE')
            ;
            heavy_rain(RAIN) -> write('BOX and change to FULLWET')
            ;
            fail
        )

        ;

        (
            (light_rain(RAIN), TYRE==intermediate) -> write('DONT BOX, you have the correct tyre')
            ;
            (heavy_rain(RAIN), TYRE==fullwet) -> write('DONT BOX, you have the correct tyre')
        )

        ;

        write('How many laps to go?'),
        read(LAPS),
        (
            LAPS=<5 -> write('DONT BOX, push till end')
        )
    ).




% % % % %  for bad grip
grip(bad) :-
    write('How many pits so far? zero or one or two?'),
    read(PITS),
    write('Current tyre?'),
    read(TYRE),
    write('Temperature cool ot hot?'),
    read(TEMP),
    (
       zero_pits(PITS) ->
        (
           medium_tyre(TYRE) ->

           (
               cool_temp(TEMP) -> write('BOX and change to SOFT')
               ;
               hot_temp(TEMP) -> write('BOX and change to HARD')
           )

           ;

           write('BOX and change to MEDIUM')
        )

        ;

        one_pits(PITS) ->
        (
            write('BOX and change to a nes set of the current tyre,'), write(TYRE)
        )

        ;

        two_pits(PITS) ->
        (
            write('Pitstops have reached maximum, CAN NOT BOX')
        )
    ).

