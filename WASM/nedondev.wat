;; Used WASI
;; Execute: wasmtime coffe2code.wat
;; Only change lowercase "Coffee" to "Code"
(module
    ;; Import the required fd_write WASI function which will write the given io vectors to stdout
    ;; The function signature for fd_write is:
    ;; (File Descriptor, *iovs, iovs_len, nwritten) -> Returns number of bytes written
    (import "wasi_unstable" "fd_write" (func $fd_write (param i32 i32 i32 i32) (result i32)))
    (import "wasi_unstable" "fd_read" (func $fd_read (param i32 i32 i32 i32) (result i32)))

    (memory 1)
    (export "memory" (memory 0))
    (data (i32.const 4) "Coffee\n") ;; 4-12
    (data (i32.const 12) "Code\n") ;; 12-20

    (func $check_char (param $offset i32) (param $expect_offset i32) (result i32)
        (local $char i32)
        (local $expect_char i32)

        local.get $expect_offset
        i32.load8_u 
        local.set $expect_char

        local.get $offset
        i32.load8_u 
        local.set $char


        local.get $expect_char
        local.get $char
        i32.ne
        return
    )

    (func $check_coffee (result i32)
        (local $char_index i32)
        (local $expect_index i32)
        (local $limit i32)

        i32.const 28
        local.set $char_index

        i32.const 4
        local.set $expect_index

        i32.const 6
        local.set $limit

        loop
            ;; load and check
            local.get $char_index
            local.get $expect_index
            call $check_char 
            if 
                i32.const 0
                return
            end         

            local.get $limit
            i32.const 1
            i32.sub
            local.set $limit

            local.get $char_index
            i32.const 1
            i32.add
            local.set $char_index

            local.get $expect_index
            i32.const 1
            i32.add
            local.set $expect_index

            local.get $limit
            i32.const 0
            i32.gt_s
            br_if 0

        end

        i32.const 1

    )

    (func $main (export "_start")
        (local $cofee i32)
        (i32.store (i32.const 20) (i32.const 28)) ;; 20 - 28
        (i32.store (i32.const 24) (i32.const 100)) ;; Expect (28 - 128) to store buffer.
        (i32.store (i32.const 128) (i32.const 12)) ;; 128 - 136
        (i32.store (i32.const 132) (i32.const 8)) ;; Use declare space as string length.

        (call $fd_read
            (i32.const 0) ;; 0 for stdin
            (i32.const 20) ;; *iovs
            (i32.const 1) ;; iovs_len
            (i32.const 24) ;; nread
        )
        drop

        call $check_coffee
            
        if
            (call $fd_write
                (i32.const 1) ;; file_descriptor - 1 for stdout
                (i32.const 128) ;; *iovs
                (i32.const 1) ;; iovs_len 
                (i32.const 4) ;; nwritten 
            )
            drop ;; Discard the number of bytes written from the top of the stack
        else
            (call $fd_write
                (i32.const 1) ;; file_descriptor - 1 for stdout
                (i32.const 20) ;; *iovs
                (i32.const 1) ;; iovs_len 
                (i32.const 24) ;; nwritten 
            )
            drop ;; Discard the number of bytes written from the top of the stack
        end
    )
)