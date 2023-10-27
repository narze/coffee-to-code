" pinpongTp.vim

function! Translate(text)
    let str = a:text
    if a:text ==# "coffee"
       let str = "code"
    endif
    echo "input: " .. a:text
    echo "output: " .. str
endfunction
