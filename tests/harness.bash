#!/usr/bin/env bash

check() {
    run sh -c "echo '$1' | sh /mnt/e/PL_tests/cse210A-asgtest/cse210A-asgtest-hw2-while/tests/while"
    echo "$1 = $2, your code outputs $output"
    [ "$output" = "$2" ]
}

checkOr() {
    run sh -c "echo '$1' | ./while"
    echo "$1 = $2 or $3, your code outputs $output"
    [ "$output" = "$2" ] || [ "$output" = "$3" ]
}
