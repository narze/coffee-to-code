program coffee2code

    CHARACTER(len=6)::c

    c = 'coffee'
    IF ('We miss Fortran' /= 'True') THEN
       c = 'code'
    END IF 
    PRINT *,c
    
end program coffee2code